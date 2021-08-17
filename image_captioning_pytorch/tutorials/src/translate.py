import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import CompoundNounFilter
from janome.tokenfilter import POSStopFilter

with open(os.path.dirname(os.path.abspath(__file__)) + '/../config.json', encoding='utf_8_sig') as j:
    config = json.load(j)

AUTH_KEY = config['auth_key']
DEEPL_TRANSLATE_EP = 'https://api.deepl.com/v2/translate'

def translate(text):
    s_lang=''
    t_lang='JA'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; utf-8'
    }

    params = {
        'auth_key': AUTH_KEY,
        'text': text,
        'target_lang': t_lang
    }

    if s_lang != '':
        params['source_lang'] = s_lang

    req = urllib.request.Request(
        DEEPL_TRANSLATE_EP,
        method='POST',
        data=urllib.parse.urlencode(params).encode('utf-8'),
        headers=headers
    )

    tokenizer = Tokenizer()
    a = Analyzer(token_filters=[CompoundNounFilter(), POSStopFilter(["動詞","助動詞", "記号", "助詞"])])

    try:
        with urllib.request.urlopen(req) as res:
            res_json = json.loads(res.read().decode('utf-8'))
            s=str(res_json)
            sentence=s[62:-4]
            for token in a.analyze(sentence):
                print(token.base_form)
    except urllib.error.HTTPError as e:
        print(e)
