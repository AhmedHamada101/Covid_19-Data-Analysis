# import libraries
import streamlit as st

# add title
st.markdown('<h1 style = "text-align:center;">Covid_19 Data Analysis</h1>', unsafe_allow_html = True)

# add image
st.image('image.jpeg')

# add description
st.header('Description')
st.markdown(
            '''
            ###### This app was created to analyze Covid-19 data for the last four years (2020, 2021, 2022, 2023).
            '''
            )
