import json
import numpy as np
import pandas as pd
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

@st.cache_data
def load_geodata(data_path):
    with open (data_path, 'r',encoding="utf-8_sig") as jsonFile:
        geo_data = json.load(jsonFile)
    return geo_data

def year_selectbox():
    year_list = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
    year = st.sidebar.selectbox('年度', year_list, len(year_list)-1)
    return year

def display_co2(df, geo_data, year):
    st.header('CO2排出量増減率')
    df = df[df['年度']==year]
    map = folium.Map(location=[35.689, 139.692], zoom_start=6, scrollWheelZoom=False)
    choropleth = folium.Choropleth(
        geo_data=geo_data,
        data=df,
        columns=['都道府県', '排出量増減率'],
        key_on='feature.properties.nam_ja',
        #fill_color='YlGn',  # 色を変更する
        fill_color='RdBu',
        fill_opacity=0.8,
        nan_fill_color='black', # 欠損値の色
        nan_fill_opacity=0.8,
        line_opacity=0.2,
        legend_name='CO₂排出量増減率',  # カラーバーのタイトル
    )
    choropleth.geojson.add_to(map)
    df_indexed = df.set_index('都道府県')
    for feature in choropleth.geojson.data['features']:
        state_name = feature['properties']['nam_ja']
        feature['properties']['排出量増減率'] = '排出量増減率: ' + '{:,}'.format(df_indexed.loc[state_name, '排出量増減率']) if state_name in list(df_indexed.index) else ''
        
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['nam_ja', '排出量増減率'], labels=False)
    )
    # カラーバーを追加
    choropleth.add_to(map)
    st_folium(map, width=1000, height=800)

def display_plot1(df, year):
    col_to_plot = '排出量増減率'
    st.header('CO2排出量増減率')
    data = df.loc[df['年度']==year, ['都道府県', col_to_plot]]
    st.write(alt.Chart(data).mark_bar().encode(
        x=alt.X('都道府県', sort=None),
        y=col_to_plot,
    ))

def display_plot2(df, year):
    col_to_plot = '排出量合計'
    st.header('CO2排出量（千トン）')
    data = df.loc[df['年度']==year, ['都道府県', col_to_plot]]
    st.write(alt.Chart(data).mark_bar().encode(
        x=alt.X('都道府県', sort=None),
        y=col_to_plot,
    ))
def display_plot3(df):
    col_to_plot = '排出量合計'
    st.header('2011年度（初年度）CO2排出量（千トン）')
    data = df.loc[df['年度']==2011, ['都道府県', col_to_plot]]
    st.write(alt.Chart(data).mark_bar().encode(
        x=alt.X('都道府県', sort=None),
        y=col_to_plot,
    ))

def main():
    st.set_page_config(page_title='CO2排出量増減要因分析', page_icon='🗾', layout='wide')
    # selectbox
    year = year_selectbox()
    st.title('CO2排出量増減分析（2011年度比）')
    #Load Data
    df = load_data('./data/都道府県年度別CO2排出量_最終報告用.csv')
    geo_data = load_geodata('./data/japan.geojson')
    # # #Display Filters and Map
    col1, col2 = st.columns(2)
    with col1:
    # 地図で排出量増減率
        display_co2(df, geo_data, year)
    with col2:
        display_plot2(df, year)
        display_plot3(df)
    display_plot1(df, year)
if __name__ == "__main__":
    main()