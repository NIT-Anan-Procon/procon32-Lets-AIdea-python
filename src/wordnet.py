# -*- coding: utf-8 -*-
# Wordnet via Python3
#
# ref:
#   WordList_JP: http://compling.hss.ntu.edu.sg/wnja/
#   python3: http://sucrose.hatenablog.com/entry/20120305/p1
import sqlite3
import sys
from collections import namedtuple
from pprint import pprint

conn = sqlite3.connect("./wnjpn.db")

Word = namedtuple("Word", "wordid lang lemma pron pos")


def get_words(lemma):
    cur = conn.execute("select * from word where lemma=?", (lemma,))
    return [Word(*row) for row in cur]


Sense = namedtuple("Sense", "synset wordid lang rank lexid freq src")


def get_senses(word):
    cur = conn.execute("select * from sense where wordid=?", (word.wordid,))
    return [Sense(*row) for row in cur]


Synset = namedtuple("Synset", "synset pos name src")


def get_synset(synset):
    cur = conn.execute("select * from synset where synset=?", (synset,))
    return Synset(*cur.fetchone())


def get_words_from_synset(synset, lang):
    cur = conn.execute(
        "select word.* from sense, word where synset=? and word.lang=? and sense.wordid = word.wordid;",  # noqa: E501
        (synset, lang),
    )
    return [Word(*row) for row in cur]


def get_words_from_senses(sense, lang="jpn"):
    synonym = {}
    for s in sense:
        lemmas = []
        syns = get_words_from_synset(s.synset, lang)
        for sy in syns:
            lemmas.append(sy.lemma)
            synonym[get_synset(s.synset).name] = lemmas
    return synonym


def get_synonym(word):
    synonym = {}
    words = get_words(word)
    if words:
        for w in words:
            sense = get_senses(w)
            s = get_words_from_senses(sense)
            synonym = dict(list(synonym.items()) + list(s.items()))
    return synonym


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        synonym = get_synonym(sys.argv[1])
        pprint(synonym)
    else:
        print(
            "You need at least 1 argument as a word like below.\nExample:\n  $ python3 wordnet 楽しい"  # noqa: E501
        )
