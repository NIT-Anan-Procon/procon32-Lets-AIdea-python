import argparse
import sys
from functools import lru_cache

import torch
from PIL import Image
from transformers import BertTokenizer

sys.path.append("../catr")
import os

from configuration import Config
from datasets import coco
from models import caption

sys.path.append("../src")
import ng_word


@lru_cache(maxsize=None)
def pre(subject, synonym, image_name):
    global model
    global config
    global image
    global cap_mask
    global caption

    image_path = image_name

    config = Config()

    model = torch.hub.load("saahiluppal/catr", "v3", pretrained=True)

    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

    start_token = tokenizer.convert_tokens_to_ids(tokenizer._cls_token)
    end_token = tokenizer.convert_tokens_to_ids(tokenizer._sep_token)

    image = Image.open(image_path)
    image = coco.val_transform(image)
    image = image.unsqueeze(0)

    caption, cap_mask = create_caption_and_mask(
        start_token, config.max_position_embeddings
    )

    output = evaluate()
    result = tokenizer.decode(output[0].tolist(), skip_special_tokens=True)
    # result = tokenizer.decode(output[0], skip_special_tokens=True)
    os.remove(image_name)
    return ng_word.ng_word(result.capitalize(), subject, synonym)


def create_caption_and_mask(start_token, max_length):
    caption_template = torch.zeros((1, max_length), dtype=torch.long)
    mask_template = torch.ones((1, max_length), dtype=torch.bool)

    caption_template[:, 0] = start_token
    mask_template[:, 0] = False

    return caption_template, mask_template


@torch.no_grad()
def evaluate():
    model.eval()
    for i in range(config.max_position_embeddings - 1):
        predictions = model(image, caption, cap_mask)
        predictions = predictions[:, i, :]
        predicted_id = torch.argmax(predictions, axis=-1)

        if predicted_id[0] == 102:
            return caption

        caption[:, i + 1] = predicted_id[0]
        cap_mask[:, i + 1] = False

    return caption
