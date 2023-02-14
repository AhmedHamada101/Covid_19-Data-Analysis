# import libraries
import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.express as px

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

# some plots
st.subheader('1. Overview of Cases and Deaths in every Region')

bar_plot1 = px.bar(data.groupby('WHO_region')['New_cases'].sum().astype(float).sort_values(ascending = False),
                   title = 'Total Cases for every Region')
bar_plot1.update(layout_showlegend = False)
bar_plot1.update_layout(xaxis_title = 'Regions', yaxis_title = 'Totle Cases')
st.plotly_chart(bar_plot1)

bar_plot2 = px.bar(data.groupby('WHO_region')['New_deaths'].sum().astype(float).sort_values(ascending = False),
                   title = 'Total Deaths for every Region')
bar_plot2.update_traces(marker_color = 'red')
bar_plot2.update(layout_showlegend = False)
bar_plot2.update_layout(xaxis_title = 'Regions', yaxis_title = 'Total Deaths')
st.plotly_chart(bar_plot2)

# add subheader
st.subheader('2. More details about Cases and Deaths')
st.header(' ')
st.markdown('##### Select Region and Date')


# filter by regions
def regions_total_cases_hist(regions, start_date = data.Date_reported.min(), end_date = data.Date_reported.max()):
    if regions != 'All Regions':
        data_temp = data[(data['WHO_region'].isin(regions))]
    else:
        data_temp = data
    fig = px.histogram(data_temp, x = 'Month_year', y = 'New_cases', color = 'Year', 
                       title = 'Total Cases', range_x = [start_date, end_date], nbins = 50)
    return fig


def regions_total_deaths_hist(regions, start_date = data.Date_reported.min(), end_date = data.Date_reported.max()):
    if regions != 'All Regions':
        data_temp = data[(data['WHO_region'].isin(regions))]
    else:
        data_temp = data
    fig = px.histogram(data_temp, x = 'Month_year', y = 'New_deaths', color = 'Year', 
                       title = 'Total Deaths', range_x = [start_date, end_date], nbins = 50)
    return fig


# Region selection
region_options = st.selectbox('Select Region', ['All Regions', 'Select Region'])
if region_options == 'All Regions':
    regions = 'All Regions'
else:
    regions = st.multiselect('Select', data['WHO_region'].unique())

# Date selection
start_date = st.date_input('Strat Data', datetime(2020,1,1))
start_date = pd.to_datetime(start_date)
end_date = st.date_input('End date', datetime(2023, 1, 1))
end_date = pd.to_datetime(end_date)

# Display Total Cases
st.header('Total Cases')
total_cases = regions_total_cases_hist(regions, start_date, end_date)
st.plotly_chart(total_cases)

# Display Total Deaths
st.header('Total Deaths')
total_deaths = regions_total_deaths_hist(regions, start_date, end_date)
st.plotly_chart(total_deaths)
