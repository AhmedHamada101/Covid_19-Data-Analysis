# import libraries
import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# load data
@st.cache
def load_data():
    data = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')
    data['Date_reported'] = pd.to_datetime(data['Date_reported'])
    data['Month_year'] = data['Date_reported'].dt.to_period('M').astype(str)
    data['Year'] = data['Date_reported'].dt.year
    data['Month'] = data['Date_reported'].dt.month
    return data

data = load_data()

# add title
st.markdown('<h1 style = "text-align:center;">Covid_19 Data Analysis</h1>', unsafe_allow_html = True)
st.header(' ')
st.header(' ')
st.header(' ')
st.header('Cases Map')


# Map Function
def plot_map(data, column):
    data2 = dict(type = 'choropleth',
                locations = data.index,
                locationmode = 'country names',
                z = data[column],
                text = data.index,
                colorscale = 'agsunset',
                reversescale = False,
                marker = dict(line = dict(color = 'white', width = 1)),
               colorbar = {'title': column })
    
    layout = dict(title = 'Covid 19 Cases Map', geo = dict(showframe = False, projection = {'type': 'natural earth'}))

    choromap = go.Figure(data = [data2], layout = layout)
    choromap.update_layout(margin = {"r":0, "t":40, "l":0, "b":0})
    return(choromap)


# Case selection
feature_options = st.selectbox('Select Case', ['Total Cases', 'Total Deaths'])
if feature_options == 'Total Cases':
    feature = 'New_cases'
else:
    feature = 'New_deaths'

# Date selection
start_date = st.date_input('Strat Data', datetime(2020,1,1))
start_date = pd.to_datetime(start_date)
end_date = st.date_input('End date', datetime(2023, 1, 1))
end_date = pd.to_datetime(end_date)

# Display Map
map_data = data[(data.Date_reported >= start_date) & (data.Date_reported <= end_date)].groupby('Country').sum()
map = plot_map(map_data, feature)
st.plotly_chart(map)
