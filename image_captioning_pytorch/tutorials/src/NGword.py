from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import CompoundNounFilter
from janome.tokenfilter import POSKeepFilter
from src import translate

def NGword(text):
	words=[]
	sentence = translate.translate(text)

	tokenizer = Tokenizer()
	a = Analyzer(token_filters=[CompoundNounFilter(), POSKeepFilter(["名詞","形容詞"])])

	for token in a.analyze(sentence):
		if token.base_form not in words:
			print(token.base_form)
			words.append(token.base_form)