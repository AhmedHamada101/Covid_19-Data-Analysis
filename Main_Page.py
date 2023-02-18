# import libraries
import streamlit as st

# add title
st.markdown('<h1 style = "text-align:center;">Covid_19 Data Analysis</h1>', unsafe_allow_html = True)

# add image
st.image('image.jpeg')

# add description
st.info('### Description: ')
st.markdown('* ##### This app was created to analyze Covid-19 data.')

# about project
st.info('### About Project: ')
st.markdown('* ##### You can get data from WHO:                      [Dataset](https://covid19.who.int/data)', unsafe_allow_html = True)
st.markdown('* ##### You can see the notebook on Google Colab:       [Notebook](https://colab.research.google.com/drive/1KDRbXtzv9jxob0_3fdCQ3WqDDTRlghjA?authuser=1)', unsafe_allow_html = True)
st.markdown('* ##### You can check the project repository on GitHub: [Project Repository](https://github.com/AhmedHamada101/Covid_19-Data-Analysis)', unsafe_allow_html = True)

# add space
st.title(' ')

# about me
st.info('### About Me: ')
st.markdown('* ##### You can view my LinkedIn Profile: [LinkedIn Profile](https://www.linkedin.com/in/ahmed-mohammed-hamada/)', unsafe_allow_html = True)
st.markdown('* ##### You can view my Kaggle Profile:   [Kaggle Profile](https://www.kaggle.com/ahmedmohammedhamada)', unsafe_allow_html = True)
st.markdown('* ##### You can view my GitHub Profile:   [GitHub Profile](https://github.com/AhmedHamada101?tab=repositories)', unsafe_allow_html = True)
