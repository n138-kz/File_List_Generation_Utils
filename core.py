import os
import sys
import glob

# Comment out = https://note.nkmk.me/python-comment/
# フォルダ内のファイル一覧を取得 = https://weblabo.oscasierra.net/python/python3-beginning-file-list.html
# Pythonで文字列を連結・結合 = https://note.nkmk.me/python-string-concat/
# サブディレクトリまで再帰的に含める = https://qiita.com/amowwee/items/e63b3610ea750f7dba1b

"""

・持出しファイル名一覧を記載したテキストファイルのファイル名(【承認依頼】データ持出し_ユーザ名_AT_ホスト名.txt)→変数(exportListFile)
・現在のフォルダのパスを取得→変数(dirpath)

▲ コマンド引数[1] に値がある とき
｜
｜▲ フォルダパスではない とき
｜｜
｜｜・エラー出力
｜｜・終了
｜｜
｜＋ーーーーーーーーーーーーーーーーーーーーーーーー
｜｜
｜｜・指定されたフォルダパス→変数(dirpath)
｜｜
｜▼
｜
▼

・ファイル一覧 を取得→変数(files)
・DotName(［.］で始まるファイル名、サブフォルダ名) の ファイル一覧 を取得→→変数(files)
・重複してリストに登録されているファイル名を排除

■ 変数(files) すべてに対し → 変数(file)
｜
｜・変数(fileSize) を 初期値 0 にする
｜
｜▲ ファイルである
｜｜
｜｜・ファイルサイズ を 取得→変数(fileSize)
｜｜
｜▼
｜・テキストファイル(exportListFile)に ［ ファイル名(or フォルダ名) + 変数(fileSize) ］ を 1行づつ 記載
｜
■

"""

# 持出しフォルダパス定義
# デフォルト：実行フォルダ
dirpath = os.getcwd()




# ファイル一覧取得
files = glob.glob(dirpath + "/**", recursive=True)

# .で始まるファイルをリストに追加
files.extend( glob.glob(dirpath + "/*.*", recursive=True) )

# 重複排除
files = set(files)

for file in files:
    print(file)

print(len(files))
