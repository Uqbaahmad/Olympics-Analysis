import streamlit as st
import pandas as pd
import plotly.express as px
import preprocessor, Streamlit.add as add
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff



df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv') 

df = preprocessor.preprocess(df, region_df)
st.sidebar.title("Olympics Analysis")

user_menu = st.sidebar.radio('Select An Option', ('Medal Tally', 'Overall Analysis'))

#st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years, country = add.country_year_list(df)

    selected_year= st.sidebar.selectbox("Select Year", years)
    selected_country= st.sidebar.selectbox("Select Country", country)

    medal_tally = add.fetch_medal_tally(df, selected_year, selected_country)
    if selected_year == "Overall" and selected_country == "Overall":
        st.title("Overall Tally")
    if selected_year != "Overall" and selected_country == "Overall":
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year == "Overall" and selected_country != "Overall":
        st.title(selected_country + " overall performance")
    
    if selected_year != "Overall" and selected_country != "Overall":
        st.title(selected_country + " performance in " + str(selected_year) + " Olympics")

    st.table(medal_tally)

if user_menu == "Overall Analysis":
    editions = df['Year'].unique().shape[0] -1
    cities = df['City'].unique().shape[0]    
    sports = df['Sport'].unique().shape[0]    
    events = df['Event'].unique().shape[0]    
    athletes = df['City'].unique().shape[0]    
    nations = df['region'].unique().shape[0] 
    st.title("Top Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions") 
        st.header(editions)
    with col2:
        st.header("Hosts") 
        st.header(cities) 
    with col3:
        st.header("Sports") 
        st.header(sports)

    col4, col5, col6 = st.columns(3)
    with col4:
        st.header("Events") 
        st.header(events)
    with col5:
        st.header("Nations") 
        st.header(nations)                       
    with col6:
        st.header("Athletes") 
        st.header(athletes) 


