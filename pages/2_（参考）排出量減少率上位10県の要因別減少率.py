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

def year_selectbox():
    year_list = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
    year = st.sidebar.selectbox('年度', year_list, len(year_list)-1)
    return year

def display_plot1(df, year, ken):
    st.header(ken)
    #df['年度'] = df['年度'].astype(int)
    data = df.loc[(df['都道府県']==ken)&(df['年度']<=year), ['年度', 'CO2排出原単位要因_変化率', 'エネルギー消費効率要因_変化率', '一人当たり総生産要因_変化率', '人口要因_変化率']]
    data.columns = ['年度', 'CO2排出原単位要因', 'エネルギー消費効率要因', '一人当たり総生産要因', '人口要因']
    data_melt = data.melt(id_vars=['年度'])
    data_melt.columns = ['年度', '指標', '変化率']
    st.bar_chart(data_melt, x="年度", y="変化率", color="指標")

def main():
    st.set_page_config(page_title='CO2排出量増減要因分析', page_icon='🗾', layout='wide')
    # selectbox
    year = year_selectbox()
    st.title('要因別CO2排出量増減分析（2011年度比）')
    st.header('年度別要因別排出量減少率上位10県')
    #Load Data
    df = load_data('./data/都道府県年度別CO2排出量_最終報告用.csv')
    ken_list = df[df['年度']==year].sort_values(by='排出量増減率')['都道府県'].to_list()
    #
    col1, col2 = st.columns(2)
    with col1:
        display_plot1(df, year, ken_list[0])
    with col2:
        display_plot1(df, year, ken_list[1])
    #
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        display_plot1(df, year, ken_list[2])
    with col2:
        display_plot1(df, year, ken_list[3])
    with col3:
        display_plot1(df, year, ken_list[4])
    with col4:
        display_plot1(df, year, ken_list[5])
    #
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        display_plot1(df, year, ken_list[6])
    with col2:
        display_plot1(df, year, ken_list[7])
    with col3:
        display_plot1(df, year, ken_list[8])
    with col4:
        display_plot1(df, year, ken_list[9])

if __name__ == "__main__":
    main()
