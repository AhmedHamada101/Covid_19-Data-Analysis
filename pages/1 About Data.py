# import libraries
import streamlit as st 
import pandas as pd

# load data
@st.cache
def load_data():
    data = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')
    data['Date_reported'] = pd.to_datetime(data['Date_reported'])
    return data

data = load_data()

# add title
st.markdown('<h1 style = "text-align:center;">Covid_19 Data Analysis</h1>', unsafe_allow_html = True)
st.header(' ')
st.header(' ')

# about data
st.header('Data Link')
st.markdown('You can get data from WHO : https://covid19.who.int/data')

# display data
st.header(' ')
st.header(' ')
st.header(' ')

st.header('Display Data')
if st.checkbox('Show Data'):
    st.dataframe(data)