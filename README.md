# procon32_Lets_AIdea_python
## 開発環境
Python==3.9.6

## 実行準備
1.以下のサイトから「decoder-5-3000.pkl」「encoder-5-3000.pkl」が入ったzipファイルと「vocab.pkl」が入ったzipファイルをダウンロードして展開する。
https://www.dropbox.com/s/ne0ixz5d58ccbbz/pretrained_model.zip?dl=0
https://www.dropbox.com/s/26adb7y9m98uisa/vocap.zip?dl=0

2．「decoder-5-3000.pkl」「encoder-5-3000.pkl」をimage_captioning_pytorch\tutorials\modelsに移動させる。

3．「vocab.pkl」をimage_captioning_pytorch\tutorials\dataに移動させる。

## 実行方法

```
cd image_captioning_pytorch/tutorials  
python image_captioning.py --image=png/example.png 
```
