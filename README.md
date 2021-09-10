# procon32_Lets_AIdea_python

## 開発環境
- Python 3.9.6
- Python 3.8.10(開発サーバー)
  - pip3 20.0.2
## クローンから環境構築

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
python3 -m venv venv
direnv allow
mkdir $HOME/tmp
export TMPDIR=$HOME/tmp
pip3 install wheel
pip3 install -r requirements.txt
```

## 実行準備

1. procon32_Lets_AIdea_python\catrにconfig.jsonを追加  
1. 中身のコードをPython班に聞く  
1. コードをconfig.jsonに記述  

## 実行方法

- ローカル

```
python3 catr/start.py
```

- 開発サーバー(Ubuntu)

```
python3 catr/start.py
```

## API 実行方法

- ローカル

1. VS Codeの拡張機能である[REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)をインストールする
1. 下のコマンドを実行した後、`test.http` ファイルの `Send Request` をクリックする
1. `text.http`ファイルの中で、キーの名前が`url`である値を、自分が保存したい写真のURLに変えることで写真を保存することができ、NGワードと日本語文がjson形式で返される
```
cd API
python connect.py
```

- 開発サーバー(Ubuntu)

1. VS Codeの拡張機能である[REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)をインストールする
1. 下のコマンドを実行した後、`test.http` ファイルの `Send Request` をクリックする
1. `text.http`ファイルの中で、キーの名前が`url`である値を、自分が保存したい写真のURLに変えることで写真を保存することができ、NGワードと日本語文がjson形式で返される
```
cd API
python3 connect.py
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
