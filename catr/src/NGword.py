import nltk
from janome.analyzer import Analyzer
from janome.tokenizer import Tokenizer
from janome.tokenfilter import CompoundNounFilter, POSKeepFilter

from src import translate
from src.subject import parse_document


def NGword(text):
    words = {}
    l = list()

    # Run only the first time
    # nltk.download('all')

    #英語のNGワードを返す
    """
    if lang == 0:
        morph = nltk.word_tokenize(text)
        pos = nltk.pos_tag(morph)
        # i = 0
        for j in range(len(pos)):
            if (pos[j][1] == "NN") or (pos[j][1] == "NNS") or (pos[j][1] == "JJ"):
                if pos[j][0] not in words:
                    l.append(poss[j][0])
                    # number = "NGword" + (str)(i)
                    # words[number] = pos[j][0]
    """

    sentence = translate.translate(text)
    tokenizer = Tokenizer()
    a = Analyzer(token_filters=[CompoundNounFilter(), POSKeepFilter(["名詞", "形容詞"])])
    # i = 0
    for token in a.analyze(sentence):
        word = (token.base_form).replace(".", "")
        if word not in words.values():
            l.append(word)
            #i = i + 1
            #number = "NGword" + (str)(i)
            #words[number] = word
    words["sentence"] = sentence
    words["NGword"] = l
    print(parse_document(sentence))

    return words
