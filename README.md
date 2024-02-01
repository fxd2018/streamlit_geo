# ローカル環境で実行するための手順書
## STEP1: 使用のファイルをダウンロードし、作業用フォルダに格納する
### ＞　やり方①：手動でダウンロードする
- ｃドライブの直下に「my_envs」というフォルダを作成
- 本画面の「Clone or Download」の緑のボタンより、「Download Zip」をクリックし、先ほど作成した「my_envs」フォルダに格納する

### ＞　やり方②：gitを使い、ダウンロードする

- gitをインストール（ダウンロード先：https://git-scm.com/downloads ）
- 「Win」＋「R」でコマンドプロンプトを起動、以下のコードを実行                                        
~~~
git clone https://github.com/fxd2018/streamlit_geo.git c:\my_envs\streamlit_geo
~~~                                      
- 実行ができたら、先ほど作成した「my_envs」フォルダに「streamlit_geo」フォルダがあり、その中に本画面にあるファイルを確認できるはず
- git clone の文法について

| パス                      | コード                                             |
|---------------------------|----------------------------------------------------|
| C:\Users\username>        | git clone [ダウロード元] [ダウロード先] |   
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
(env_st) C:\my_envs\env_st\Scripts>cd C:\work\streamlit_geo
(env_st) C:\work\streamlit_geo>streamlit run st_home.py
~~~
