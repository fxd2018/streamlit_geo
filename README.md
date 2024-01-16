# ローカル環境で実行するための手順書
## STEP1: 作業用フォルダ作成、使用ファイルをダウンロード
- 「Win」＋「R」でコマンドプロンプトを起動、以下のコードを実行
~~~
C:\Users\username>cd c:/
c:\>mkdir work
c:\>cd c:/work
c:\work>git clone https://github.com/fxd2018/streamlit_geo.git
~~~
## STEP2: 環境配置
- 仮想環境作成
~~~
詳細略
~~~
- 仮想環境を起動し、使用のライブラリをインストール
~~~
# ダウンロードしたフォルダの中にあるequirements.txtを使用
(env_st) C:\my_envs\env_st\Scripts>pip install -r C:\work2\streamlit_geo\requirements.txt
(env_st) C:\my_envs\env_st\Scripts>cd C:\work2\streamlit_geo
(env_st) C:\work2\streamlit_geo>streamlit run st_home.py
~~~
## STEP3:

