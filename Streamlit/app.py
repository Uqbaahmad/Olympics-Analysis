import streamlit as st
import pandas as pd
import plotly.express as px
import preprocessor, add
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff



df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv') 

df = preprocessor.preprocess(df, region_df)
st.sidebar.title("Olympics Analysis")

user_menu = st.sidebar.radio('Select An Option', ('Medal Tally', 'Overall Analysis'))



if user_menu == 'Medal Tally':
    st.dataframe(df)
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

    nations_over_time = add.data_over_time(df, 'region')
    fig = px.line(nations_over_time, x="Edition", y = "region")
    st.header( "Participating nations over the years")
    st.plotly_chart(fig)

    event_over_time = add.data_over_time(df, 'Event')
    fig = px.line(event_over_time, x="Edition", y = "Event")
    st.header( "Event over the years")
    st.plotly_chart(fig)

    athlete_over_time = add.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x="Edition", y = "Name")
    st.header("Athletes over the years")
    st.plotly_chart(fig)

    st.title("No. of Events over time (Every Sport)")
    fig,ax = plt.subplots(figsize = (25, 25))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns = 'Year', values= 'Event', aggfunc='count').fillna(0).astype('int'), annot=True)
    st.pyplot(fig)

    st.title("Most Successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    selected_sport=st.selectbox("Select a Sport", sport_list)
    x = add.most_successful(df, selected_sport)
    st.table(x)

