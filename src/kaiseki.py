import pykakasi

ng = "熊"
kakasi = pykakasi.kakasi()
kakasi.setMode("J", "H")  # 漢字からひらがなに変換
conv = kakasi.getConverter()
print(conv.do(ng))
kakasi.setMode("J", "K")  # 漢字からカタカナに変換
conv1 = kakasi.getConverter()

print(conv1.do(ng))
