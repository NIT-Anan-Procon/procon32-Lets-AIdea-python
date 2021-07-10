# procon32_Lets_AIdea_python
・ローカルでのimage captioning実行方法
1. このリポジトリをクローン
2. pytorch-tutorial/tutorials/03-advanced/image_captioning/に移動
3. pip install -r requirements.txtを実行
4. python sample.py --image=png/example.pngを実行(example.pngは好きな画像を入れる)

エラーが出た場合は以下のようなサイトをチェックする  
pycocoapi ビルド                  ：https://qiita.com/funatsufumiya/items/049fc600f13b24ea8633  
pycocotools/_mask.c が見つからない：https://cocoinit23.com/no-such-file-or-directory-pycocotools-_mask-c/  
pipでproxy                        ：https://qiita.com/samunohito/items/40a03e1464899225e698  
import torchエラー                ：https://trend-tracer.com/pytorch/  
