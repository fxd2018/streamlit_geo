# ローカル環境で実行するための手順書
## STEP1: 作業用フォルダ作成、使用のファイルをダウンロード
### やり方①：gitを使ってダウンロードする
- gitをインストール（ダウンロード先：https://git-scm.com/downloads）
- 「Win」＋「R」でコマンドプロンプトを起動、以下のコードを実行
- 実行ができたら、「work」フォルダの中に「streamlit_geo」フォルダが確認できるはず
~~~
C:\Users\username>cd c:/
c:\>mkdir work
c:\>cd c:/work
c:\work>git clone https://github.com/fxd2018/streamlit_geo.git
~~~
### やり方②：手動でダウンロードする
- ｃドライブの直下に「work」というフォルダを作成
- 本画面の「Clone or Download」の緑のボタンより、「Download Zip」をクリックし、先ほど作成した「work」フォルダに格納する
## STEP2: 環境配置
- 仮想環境作成し、起動
~~~
C:\Users\username>cd c:/
c:\>mkdir my_envs
c:\>cd c:/my_envs
c:\my_envs>python -m venv env_st
c:\>cd c:/my_envs/env_st/Scripts
c:\my_envs\env_st\Scripts>activate
~~~
- 必要なライブラリをインストール  
（ダウンロードしたフォルダの中にあるequirements.txtを使用）
~~~
(env_st) C:\my_envs\env_st\Scripts>pip install -r C:\work\streamlit_geo\requirements.txt
~~~
## STEP3: アプリ起動
~~~
(env_st) C:\my_envs\env_st\Scripts>cd C:\work2\streamlit_geo
(env_st) C:\work\streamlit_geo>streamlit run st_home.py
~~~
