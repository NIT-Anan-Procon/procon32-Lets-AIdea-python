from janome.analyzer import Analyzer
from janome.tokenfilter import CompoundNounFilter, POSKeepFilter

import translate
from subject import parse_document
from synonym import syno


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
        if word not in ng_word_list:
            ng_word_list.append(word)

    if subject == 1:
        words["subject"] = subject_preparation(sentence, ng_word_list)

    if synonym == 1:
        words["synonym"] = synonym_preparation(ng_word_list)

    words["AI"] = sentence
    words["NGword"] = ng_word_list
    return words


def subject_preparation(sentence, ng_word_list):
    s = (
        translate.word(parse_document(sentence))
        if parse_document(sentence) is not None
        else translate.word(ng_word_list[-1])
    )
    return s


def synonym_preparation(ng_word_list):
    l_syno = list()
    for word2 in ng_word_list:
        l_syno.append(syno(word2))
    return l_syno
