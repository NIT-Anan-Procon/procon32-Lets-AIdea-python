import wordnet

<<<<<<< HEAD

def syno():
    global list
    word = "白"
=======
def syno(word):
    global list
>>>>>>> a1dee8436ce5b0758a0e2ce493666bd6069f45f2
    synonym = wordnet.getSynonym(word)
    list = list(synonym.values())
    try:
<<<<<<< HEAD
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
=======
        #NGワードが含まれていない類義語を配列で返す
        l=list[0]
        l_in_not = [s for s in l if word not in s]
        return l_in_not
    except IndexError:
        return
>>>>>>> a1dee8436ce5b0758a0e2ce493666bd6069f45f2
