import nltk
from janome.analyzer import Analyzer
from janome.tokenfilter import CompoundNounFilter, POSKeepFilter

from src import translate


def NGword(text, lang):
    words = {}

<<<<<<< HEAD
	words["sentence"] = sentence
=======
    # Run only the first time
    # nltk.download('all')
>>>>>>> main

    if lang == 0:
        morph = nltk.word_tokenize(text)
        pos = nltk.pos_tag(morph)
        i = 0
        for j in range(len(pos)):
            if (pos[j][1] == "NN") or (pos[j][1] == "NNS") or (pos[j][1] == "JJ"):
                if pos[j][0] not in words:
                    i = i + 1
                    number = "NGword" + (str)(i)
                    words[number] = pos[j][0]
    else:
        sentence = translate.translate(text)
        a = Analyzer(token_filters=[CompoundNounFilter(), POSKeepFilter(["名詞", "形容詞"])])
        i = 0
        for token in a.analyze(sentence):
            word = (token.base_form).replace(".", "")
            if word not in words.values():
                i = i + 1
                number = "NGword" + (str)(i)
                words[number] = word

    return words
