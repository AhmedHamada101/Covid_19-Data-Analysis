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

# some plots
st.subheader('1. Overview of Cases and Deaths in Top Countries')

top_countries_cases = px.bar(data.groupby('Country')['New_cases'].sum().nlargest(10).sort_values(ascending = True), 
                       title = 'The Top 10 Countries have Cases', orientation='h')
top_countries_cases.update(layout_showlegend = False)
top_countries_cases.update_layout(xaxis_title = 'Regions', yaxis_title = 'Totle Cases')
st.plotly_chart(top_countries_cases)

top_countries_deaths = px.bar(data.groupby('Country')['New_deaths'].sum().nlargest(10).sort_values(ascending = True), 
                       title = 'The Top 10 Countries have Deaths', orientation='h')
top_countries_deaths.update_traces(marker_color = 'red')
top_countries_deaths.update(layout_showlegend = False)
top_countries_deaths.update_layout(xaxis_title = 'Regions', yaxis_title = 'Total Deaths')
st.plotly_chart(top_countries_deaths)

# add subheader
st.subheader('2. More details about Cases and Deaths')
st.header(' ')
st.markdown('##### Select Country and Date')


# filter by countries
def countries_total_cases_hist(countries, start_date = data.Date_reported.min(), end_date = data.Date_reported.max()):
    if countries != 'All Countries':
        data_temp = data[(data['Country'].isin(countries))]
    else:
        data_temp = data
    fig = px.histogram(data_temp, x = 'Month_year', y = 'New_cases', color = 'Year', 
                       title='Total Cases', range_x = [start_date, end_date], nbins = 50)
    return fig


def countries_total_deaths_hist(countries, start_date = data.Date_reported.min(), end_date = data.Date_reported.max()):
    if countries != 'All Countries':
        data_temp = data[(data['Country'].isin(countries))]
    else:
        data_temp = data
    fig = px.histogram(data_temp, x = 'Month_year', y = 'New_deaths', color = 'Year', 
                       title = 'Total Deaths', range_x=[start_date, end_date], nbins = 50)
    return fig


# Country selection
country_options = st.selectbox('Select Country', ['All Countries', 'Select Countries'])
if country_options == 'All Countries':
    countries = 'All Countries'
else:
    countries = st.multiselect('Select', data['Country'].unique())

# Date selection
start_date = st.date_input('Start date', datetime(2020, 1, 1))
start_date = pd.to_datetime(start_date)
end_date = st.date_input('End date', datetime(2023, 1, 1))
end_date = pd.to_datetime(end_date)


# Display Total Cases
st.header('Total Cases')
total_cases = countries_total_cases_hist(countries, start_date, end_date)
st.plotly_chart(total_cases)

# Display Total Deaths
st.header('Total Deaths')
total_deaths = countries_total_deaths_hist(countries, start_date, end_date)
st.plotly_chart(total_deaths)
