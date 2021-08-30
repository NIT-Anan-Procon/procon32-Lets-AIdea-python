# procon32_Lets_AIdea_python

## 開発環境
- Python 3.9.6
- Python 3.8.10(開発サーバー)
  - pip3 20.0.2
## 使い方

- ローカル

```
git clone https://github.com/NIT-Anan-Procon/procon32_Lets_AIdea_python.git
cd procon32_Lets_AIdea_python
python3 -m venv venv
source venv/bin/activate
```

- 開発サーバー

```
git clone https://github.com/NIT-Anan-Procon/procon32_Lets_AIdea_python.git
cd procon32_Lets_AIdea_python
make setup
```

## 実行準備
1. 以下のサイトから `decoder-5-3000.pkl` , `encoder-5-3000.pkl` が入ったzipファイルと `vocab.pkl` が入ったzipファイルをダウンロードして展開する。
  - https://www.dropbox.com/s/ne0ixz5d58ccbbz/pretrained_model.zip?dl=0
  - https://www.dropbox.com/s/26adb7y9m98uisa/vocap.zip?dl=0
2. `decoder-5-3000.pkl` , `encoder-5-3000.pkl` を `image_captioning_pytorch\tutorials\models` に移動させる。
3. `vocab.pkl` を `image_captioning_pytorch\tutorials\data` に移動させる。

## 実行方法

- ローカル

```
cd image_captioning_pytorch/tutorials
python image_captioning.py --image=png/example.png 
```

- 開発サーバー(Ubuntu)

```
cd image_captioning_pytorch/tutorials
python3 image_captioning.py --image=png/example.png 
```

## エラー対処  

- pipコマンド実行時に、 `error: Microsoft Visual C++ 14.0 is required.` エラーが出た場合は、[ここ](https://visualstudio.microsoft.com/ja/downloads/)からVisual Studioをダウンロード
  - 途中で出てくるワードロードタブから以下をインストーラーに追加する  
    - デスクトップとモバイル：C++ Build Tools  
    - インストールの詳細：MSVC v140(さらにエラーが出るようならこれも追加)  

- pipコマンド実行時に `WARNING：HTTPS Connection. `が出て失敗した場合は、 以下に変更する 
```
set HTTP_PROXY=プロキシのホスト名:ポート
set HTTPS_PROXY=プロキシのホスト名:ポート
pip install -r requirements.txt --proxy プロキシのホスト名:ポート
```
