import wordnet


def syno(word):
    global list
    synonym = wordnet.get_synonym(word)
    l_origin = list(synonym.values())
    try:
        # NGワードが含まれていない類義語を配列で返す
        ng_word_list = l_origin[0]
        l_in_not = [s for s in ng_word_list if word not in s]
        return l_in_not
    except IndexError:
        return
