# Comment out = https://note.nkmk.me/python-comment/
# フォルダ内のファイル一覧を取得 = https://weblabo.oscasierra.net/python/python3-beginning-file-list.html
# Pythonで文字列を連結・結合 = https://note.nkmk.me/python-string-concat/
# サブディレクトリまで再帰的に含める = https://qiita.com/amowwee/items/e63b3610ea750f7dba1b

"""

・持出しファイル名一覧を記載したテキストファイルのファイル名→変数(exportListFile)
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
import os
import sys
import glob
import datetime

# 今の時間→フォーマットに変換
runtime_start = datetime.datetime.now()
runtime_start = runtime_start.strftime('%Y-%m-%dT%H-%M-%S')

# 持出しファイルリストを記載するファイル名定義
from socket import gethostname
listname = '【承認依頼】データ持出し' + '_' + os.getlogin() + '_' + gethostname() + '_' + str( runtime_start ) + '.txt'

# 持出しフォルダパス定義
# デフォルト：実行フォルダ
dirpath = os.getcwd()

# ファイル一覧取得
files = glob.glob(dirpath + '/**', recursive=True)

# .で始まるファイルをリストに追加
files.extend( glob.glob(dirpath + '/**/.**', recursive=True) )

# 重複排除
files = set(files)

# 並び替え
files = list(files)
files.sort()

# ファイルアクセスハンドラー
with open(dirpath + '/' + listname, encoding='utf_8', mode='w') as fileAccessHundler:

    # ルートディレクトリパス取得
    fileAccessHundler.write( '###' + ' ' + dirpath + ' ' + '###' + '\n' )

    # すべての ファイル に対し
    for file in files:
        # ファイル名
        file_name = file.replace(dirpath, '')

        # ファイルサイズ 取得→ KB 形式
        file_size = os.path.getsize(file) / 1000

        # ファイルサイズ 取得→ 少数第2位まで
        file_size = int( file_size * 100 ) / 100

        # 0 正規化 / 0.00 → 0
        if ( int(file_size) == 0 ):
            file_size = 0

        # 0.01KB 未満 だけど 0 byte 以上のときは 0.01KB にする
        if ( int(file_size)==0 ) and ( os.path.getsize(file) > 0 ):
            file_size = 0.01

        # ディレクトリ の時は ファイルサイズ を取得しない / 0 にする
        if os.path.isdir(file):
            file_size = 0

        # KB 表記
        file_size = str( file_size ) + 'KB'

        # 取得した ファイル名 一覧 を テキストファイル に 書き出し
        fileAccessHundler.write( file_name + "\t" + file_size + '\n' )


print( "File count: " + str( len(files) - 1 ) )
