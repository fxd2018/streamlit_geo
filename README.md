![画像 (1)](https://github.com/fxd2018/streamlit_geo/assets/156732003/b5c45373-c93c-4b9b-b346-25346622bb81)
![画像](https://github.com/fxd2018/streamlit_geo/assets/156732003/f27763c2-c67b-4043-a0b0-f1c4d30bdc48)
# ローカル環境で実行するための手順書
## STEP1: 使用のファイルをダウンロードし、作業用フォルダに格納する
### ＞　やり方①：手動でダウンロードする
- ｃドライブの直下に「my_envs」というフォルダを作成
- 本画面の「Clone」の緑のボタンより、「Download Zip」をクリックしダウロードする
- Zipファイルを解凍し、先ほど作成した「my_envs」フォルダに格納する

### ＞　やり方②：gitを使い、ダウンロードする

- gitをインストール（ダウンロード先：https://git-scm.com/downloads ）
- 「Win」＋「R」でコマンドプロンプトを起動する。
  - できたら、コマンドプロンプトは下のような状態になるはず

    | ディレクトリ              | コマンド                                             |
    |---------------------------|----------------------------------------------------|
    | C:\Users\username         | 

- 下のコマンドをコピーして、コマンドプロンプトに貼り付けて実行する                
~~~
git clone https://github.com/fxd2018/streamlit_geo.git c:\my_envs\streamlit_geo
~~~

  | ディレクトリ              | コマンド                                             |
  |---------------------------|----------------------------------------------------|
  | C:\Users\username         | git clone https://github.com/fxd2018/streamlit_geo.git c:\my_envs\streamlit_geo |

  -実行ができたら、先ほど作成した「my_envs」フォルダに「streamlit_geo」フォルダが格納され、その中に本画面にあるファイルも確認できるはず

## STEP2: 環境配置
- pythonのインストール（Microsoft Store経由でインストールするか、このリンク https://www.python.org/downloads/ よりダウロードしインストールする）
- 「Win」＋「R」でコマンドプロンプトを起動
- 下のコードをコピーして、コマンドプロンプトに貼り付けて実行 （仮想環境を作成するため）。実行が終了次第、「my_envs」フォルダの中に、「env_st」というフォルダが確認できるはず
~~~
python -m venv c:/my_envs/env_st
~~~

  | ディレクトリ              | コマンド                                             |
  |---------------------------|----------------------------------------------------|
  | C:\Users\username         | python -m venv c:/my_envs/env_st |

- 下のコードをコピーして、コマンドプロンプトに貼り付けて実行。仮想環境を起動する
~~~
C:\my_envs\env_st\Scripts\Activate
~~~

  | ディレクトリ              | コマンド                                             |
  |---------------------------|----------------------------------------------------|
  | C:\Users\username         | C:\my_envs\env_st\Scripts\Activate |

- 起動できたら、コマンドプロンプトのディレクトリは下のようになるはず

  | ディレクトリ              | コマンド                                            |
  |---------------------------|----------------------------------------------------|
  |(env_st) C:\Users\username |  |

- 必要なライブラリをインストール（ダウンロードしたフォルダの中にあるrequirements.txtを使用）
~~~
pip install -r C:\my_envs\streamlit_geo\requirements.txt
~~~
  | ディレクトリ              | コマンド                                            |
  |---------------------------|----------------------------------------------------|
  |(env_st) C:\Users\username | pip install -r C:\my_envs\streamlit_geo\requirements.txt |

## STEP3: アプリ起動
- コマンドプロンプトのディレクトリを「streamlit_geo」に変更する。下のコードをコピーして、コマンドプロンプトに貼り付けて実行。
  -      cd C:\my_envs\streamlit_geo
  - （参考）
    | ディレクトリ              | コマンド                                            |
    |---------------------------|----------------------------------------------------|
    |(env_st) C:\Users\username | cd C:\my_envs\streamlit_geo |

- 変更できたら、ディレクトリは下のようになるはず
    | ディレクトリ              | コマンド                                            |
    |---------------------------|----------------------------------------------------|
    |(env_st) C:\my_envs\streamlit_geo |   |
    
- 下のコードをコピーして、コマンドプロンプトに貼り付けて実行
  -     streamlit run st_home.py
  - （参考）
    | ディレクトリ              | コマンド                                            |
    |---------------------------|----------------------------------------------------|
    |(env_st) C:\my_envs\streamlit_geo | streamlit run st_home.py |

  

