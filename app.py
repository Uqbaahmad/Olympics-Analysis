import streamlit as st
import pandas as pd
import preprocessor, add



df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv') 

df = preprocessor.preprocess(df, region_df)
st.sidebar.title("Olympics Analysis")

user_menu = st.sidebar.radio('Select An Option', ('Medal Tally', 'Overall Analysis', 'Country-Wise Analysis', 'Athele Wise Analysis'))

st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years, country = add.country_year_list(df)
    selected_year= st.sidebar.selectbox("Select Year", years)
    selected_country= st.sidebar.selectbox("Select Country", country)
    medal_tally = add.medal_tally(df)
    st.dataframe(medal_tally)