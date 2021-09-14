from src import wordnet


def syno(word):
    global list
    synonym = wordnet.getSynonym(word)
    list = list(synonym.values())
    try:
        # NGワードが含まれていない類義語を配列で返す
        l = list[0]
        l_in_not = [s for s in l if word not in s]
        return l_in_not
    except IndexError:
        return
