# procon32_Lets_AIdea_python
## 開発環境
- Python 3.9.6

## ローカルでのimage captioning実行方法

```
pip install -r requirements.txt  
cd image_captioning_pytorch/tutorials  
python sample.py --image=png/example.png  
```

## エラー対処  
- pipコマンド実行時に、error: Microsoft Visual C++ 14.0 is required.エラーが出た場合は、  
https://visualstudio.microsoft.com/ja/downloads/  
ここからVisual Studioをダウンロード  
途中で出てくるワードロードタブから以下をインストーラーに追加する  
・デスクトップとモバイル：C++ Build Tools  
・インストールの詳細：MSVC v140(さらにエラーが出るようならこれも追加)  
- pipコマンド実行時に、WARNING：HTTPSConnection.が出て失敗した場合は、  
    ```
    set HTTP_PROXY=http://proxy.anan-nct.ac.jp:8080
    set HTTPS_PROXY=http://proxy.anan-nct.ac.jp:8080
    pip install -r requirements.txt --proxy http://proxy.anan-nct.ac.jp:8080
    ```
    に変更する。