import nltk
from janome.analyzer import Analyzer
from janome.tokenfilter import CompoundNounFilter, POSKeepFilter
from janome.tokenizer import Tokenizer

from src import translate
from src.subject import parse_document
from src.synonym import syno


def NGword(text, subject, synonym):
    words = {}
    l = list()

    # Run only the first time
    # nltk.download('all')

    # 英語のNGワードを返す
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

    sentence = translate.sentence(text)
    tokenizer = Tokenizer()
    a = Analyzer(token_filters=[CompoundNounFilter(), POSKeepFilter(["名詞", "形容詞"])])
    # i = 0
    for token in a.analyze(sentence):
        word = (token.base_form).replace(".", "")
        if word not in words.values():
            l.append(word)
            # i = i + 1
            # number = "NGword" + (str)(i)
            # words[number] = word

    if subject == 1:
        if parse_document(sentence) is not None:
            s = translate.word(parse_document(sentence))
        else:
            s = translate.word(l[-1])
        # print(parse_document(sentence))
        words["subject"] = s

    l2 = list()
    if synonym == 1:
        for word2 in l:
            l2  = syno(word2)
        words["synonym"] = l2

    words["AI"] = sentence
    words["NGword"] = l

    return words
