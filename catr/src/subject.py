import spacy


def parse_document(sentence):
    nlp = spacy.load("ja_ginza")
    doc = nlp(sentence)
    tokens = []

    # 参照しやすいようにトークンのリストを作る
    for sent in doc.sents:
        for token in sent:
            tokens.append(token)

    subject_list = []

    for token in tokens:
        # 依存関係ラベルがnsubj or iobjであれば「＜見出し語＞:＜係り先の見出し語＞」をリストに追加する。
        if token.dep_ in ["nsubj", "iobj"]:
            subject_list.append(f"{token.lemma_}")

        #複数の主語となった場合DeepLだと、あとの主語の方が求めている言葉となりやすいのでここでは配列の最後の主語を返している
        subject_last = "主語は検出できませんでした"
        for subject in subject_list:
            subject_last = subject

    return subject_last