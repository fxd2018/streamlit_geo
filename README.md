# ローカル環境で実行するための手順書
## STEP1: 使用のファイルをダウンロードし、作業用フォルダに格納する
### ＞　やり方①：手動でダウンロードする
- ｃドライブの直下に「my_envs」というフォルダを作成
- 本画面の「Clone or Download」の緑のボタンより、「Download Zip」をクリックしダウロードする
- ファイルを解凍し、先ほど作成した「my_envs」フォルダに格納する

### ＞　やり方②：gitを使い、ダウンロードする

- gitをインストール（ダウンロード先：https://git-scm.com/downloads ）
- 「Win」＋「R」でコマンドプロンプトを起動、以下のコードを実行                                        
~~~
git clone https://github.com/fxd2018/streamlit_geo.git c:\my_envs\streamlit_geo
~~~

| ディレクトリ              | コマンド                                             |
|---------------------------|----------------------------------------------------|
| C:\Users\username>        | git clone [ダウロード元] [ダウロード先] |

- 実行ができたら、先ほど作成した「my_envs」フォルダに「streamlit_geo」フォルダが格納でき、その中に本画面にあるファイルも確認できるはず



## STEP2: 環境配置
- pythonのインストール（Microsoft Store経由でインストールするか、このリンク https://www.python.org/downloads/ よりダウロードしインストールする）
- 「Win」＋「R」でコマンドプロンプトを起動、以下のコードを実行 （仮想環境を作成するため）
~~~
python -m venv c:/my_envs/env_st
~~~
- 以下のコードを実行し、仮想環境を起動する
~~~
C:\my_envs\env_st\Scripts\Activate
~~~
- 起動できたら、コマンドプロンプトのディレクトリは下のようになるはず

| ディレクトリ              | コマンド                                            |
|---------------------------|----------------------------------------------------|
|(env_st) C:\Users\username>       |  |

- 必要なライブラリをインストール（ダウンロードしたフォルダの中にあるrequirements.txtを使用）
~~~
pip install -r C:\my_envs\streamlit_geo\requirements.txt
~~~
| ディレクトリ              | コマンド                                            |
|---------------------------|----------------------------------------------------|
|(env_st) C:\Users\username>       | pip install -r C:\my_envs\streamlit_geo\requirements.txt |

## STEP3: アプリ起動
- 下のコードをコピーして、コマンドプロンプトに貼り付けて実行
~~~
C:\work\streamlit_geo>streamlit run C:\work\streamlit_geo\st_home.py
~~~
| ディレクトリ              | コマンド                                            |
|---------------------------|----------------------------------------------------|
|(env_st) C:\Users\username>       | streamlit run C:\work\streamlit_geo\st_home.py |
