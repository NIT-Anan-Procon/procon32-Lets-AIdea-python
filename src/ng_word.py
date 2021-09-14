from janome.analyzer import Analyzer
from janome.tokenfilter import CompoundNounFilter, POSKeepFilter

import translate
from subject import parse_document


def ng_word(text, subject, synonym):
    words = {}
    ng_word_list = list()

    # 英語のNGワードを返す
    """
    if lang == 0:
        morph = nltk.word_tokenize(text)
        pos = nltk.pos_tag(morph)
        for j in range(len(pos)):
            if (pos[j][1] == "NN") or (pos[j][1] == "NNS") or (pos[j][1] == "JJ"):
                if pos[j][0] not in words:
                    l.append(poss[j][0])
    """

    sentence = translate.sentence(text)
    a = Analyzer(token_filters=[CompoundNounFilter(), POSKeepFilter(["名詞", "形容詞"])])
    for token in a.analyze(sentence):
        word = (token.base_form).replace(".", "")
        if word not in words.values():
            ng_word_list.append(word)

    if subject == 1:
        if parse_document(sentence) is not None:
            s = translate.word(parse_document(sentence))
        else:
            s = translate.word(ng_word_list[-1])
        words["subject"] = s

    """
    以下のコードはまだ使用できない ここから
    l2 = list()
    if synonym == 1:
        for word2 in ng_word_list:
            l2.append(syno(word2))
        words["synonym"] = l2
    ここまで
    """

    words["AI"] = sentence
    words["NGword"] = ng_word_list

    return words
