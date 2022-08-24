import streamlit as st 
import numpy as np 
import pandas as pd
import plotly.express as px

# @st.cache 

df = pd.read_json('kenyan cities.json')

st.title('KENYAN CITIES POPULATION DISTRIBUTION') #main title

st.markdown('A map of major Kenyan cities.')

st.header('______________________________________________________________________') # For section titles use st.subheader

# Data at a glance

cols = ['country','city','admin_name','population']
st_ms = list(st.multiselect('Select Columns to view', df.columns.tolist(), default=cols))

st.subheader('City Population.')


sieved_data = df[st_ms]

sieved_data = sieved_data.rename(columns={'admin_name':'Headquaters'})

if st.checkbox('View Full Dataset'):
    st.dataframe(sieved_data.style)
else:
    st.dataframe(sieved_data.head())


# Mapping the cities

st.subheader('City Map')

api_token = 'pk.eyJ1IjoiaGFpbC1yYWluZXIiLCJhIjoiY2w3MjNjYTYwMDB4azNubncxeHUxY2xhYyJ9.0vOPVZT84m7ZfBNJ4vNJRA'

fig = px.scatter_mapbox(df, lat="lat", lon="lng", hover_name="admin_name", hover_data=["city", "population"],
                        zoom=5.5, height=600, width = 800, color_continuous_scale=["black", "purple", "red" ], 
                        color='admin_name', size_max=70)
fig.update_layout(mapbox_accesstoken=api_token, mapbox_style="mapbox://styles/hail-rainer/cl77fst1t003k15rvd70xbfb1")
fig.update_traces(marker=dict(size=6))
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.write(fig)


# Distribution of Population

df['population'] = pd.to_numeric(df['population'])

f = px.histogram(df.population, nbins = 10, title='Population Distribution')
st.plotly_chart(f)