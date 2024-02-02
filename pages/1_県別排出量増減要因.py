import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium
import streamlit as st
import altair as alt
from streamlit_folium import st_folium
import geopandas as gpd

@st.cache_data
def load_data(data_path):
    df = pd.read_csv(data_path)
    df['排出量増減率'] = round(df['排出量増減率'], 4)
    return df

ken_list = ['北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県', '茨城県', '栃木県', 
            '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県', '新潟県', '富山県', '石川県', '福井県', 
            '山梨県', '長野県', '岐阜県', '静岡県', '愛知県', '三重県', '滋賀県', '京都府', '大阪府', 
            '兵庫県', '奈良県', '和歌山県', '鳥取県', '島根県', '岡山県', '広島県', '山口県', '徳島県', 
            '香川県', '愛媛県', '高知県', '福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県']
def year_selectbox():
    year_list = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
    year = st.sidebar.selectbox('年度', year_list, len(year_list)-1)
    return year
ken_list = ken_list
def ken1_selectbox():
    ken = st.sidebar.selectbox('指定都道府県１', ken_list, 0, key='ken1_selectbox')
    return ken
def ken2_selectbox():
    ken = st.sidebar.selectbox('指定都道府県２', ken_list, 1, key='ken2_selectbox')
    return ken
def ken3_selectbox():
    ken = st.sidebar.selectbox('指定都道府県３', ken_list, 2, key='ken3_selectbox')
    return ken
def ken4_selectbox():
    ken = st.sidebar.selectbox('指定都道府県４', ken_list, 3, key='ken4_selectbox')
    return ken
def ken5_selectbox():
    ken = st.sidebar.selectbox('指定都道府県５', ken_list, 4, key='ken5_selectbox')
    return ken
def ken6_selectbox():
    ken = st.sidebar.selectbox('指定都道府県６', ken_list, 5, key='ken6_selectbox')
    return ken
def ken7_selectbox():
    ken = st.sidebar.selectbox('指定都道府県７', ken_list, 6, key='ken7_selectbox')
    return ken
def ken8_selectbox():
    ken = st.sidebar.selectbox('指定都道府県８', ken_list, 7, key='ken8_selectbox')
    return ken

def display_plot1(df, year, ken):
    st.header(ken)
    data = df.loc[df['都道府県']==ken, ['年度', 'CO2排出原単位要因_変化率', 'エネルギー消費効率要因_変化率', '一人当たり総生産要因_変化率', '人口要因_変化率']]
    data.columns = ['年度', 'CO2排出原単位要因', 'エネルギー消費効率要因', '一人当たり総生産要因', '人口要因']
    data_melt = data.melt(id_vars=['年度'])
    data_melt.columns = ['年度', '指標', '変化率']
    st.bar_chart(data_melt, x="年度", y="変化率", color="指標")

def main():
    st.set_page_config(page_title='CO2排出量増減要因分析', page_icon='🗾', layout='wide')
    # selectbox
    year = year_selectbox()
    st.title('要因別CO2排出量増減分析（2011年度比）')
    st.header('年度別指定県の要因別排出量増減率')
    #Load Data
    df = load_data('./data/都道府県年度別CO2排出量_最終報告用.csv')
    ken_list = df[df['年度']==year].sort_values(by='排出量増減率')['都道府県'].to_list()
    #   
    col1, col2 = st.columns(2)
    with col1:
        display_plot1(df, year, ken1_selectbox())
    with col2:
        display_plot1(df, year, ken2_selectbox())
    #
    col1, col2 = st.columns(2)
    with col1:
        display_plot1(df, year, ken3_selectbox())
    with col2:
        display_plot1(df, year, ken4_selectbox())
    #   
    col1, col2 = st.columns(2)
    with col1:
        display_plot1(df, year, ken5_selectbox())
    with col2:
        display_plot1(df, year, ken6_selectbox())
    #
    col1, col2 = st.columns(2)
    with col1:
        display_plot1(df, year, ken7_selectbox())
    with col2:
        display_plot1(df, year, ken8_selectbox())

if __name__ == "__main__":
    main()
