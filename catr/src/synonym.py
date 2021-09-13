import wordnet


def syno():
    global list
    word = "白"
    synonym = wordnet.getSynonym(word)
    list = list(synonym.values())
    try:
        # 類義語を配列で返す
        l = list[0]
        l.remove(word)
        print(l)

        # 類義語を一語だけ返す
        i = 0
        for w in l:
            if word in l[i]:
                i += 1

        print(l[i])
    except IndexError:
        print("None")
