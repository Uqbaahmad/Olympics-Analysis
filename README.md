# Data Analysis of Olympics
Data Analysis or sometimes referred to as Exploratory Data Analysis (EDA) is one of the core components of data science. It is also the part on which data scientists, data engineers and data analysts spend their majority of the time which makes it extremely important in the field of data science.

This repository demonstrates some common EDA methods and techniques using Python. For purpose of illustration the 120 Years of Olympic Analysis history dataset has been taken from [kaggle](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results) since it is one of the ideal dataset for performing EDA and taking a step towards the most amazing and interesting field of data science. <br/>


The modern Olympic Games are the most important international sporting events, with summer and winter sports tournaments involving thousands of competitors from all over the world.
With over 200 nations competing, the Olympic Games are regarded as the world's premier sporting event. The Olympic Games are generally held every four years, and since 1994, the Summer and Winter Olympics have alternated every two years throughout the four-year period.

This file contains analysis performed upon used car dataset - [Olympic.ipynb](https://github.com/Uqbaahmad/Olympics-Analysis/tree/main/Analysis)

# Column Description 
This dataset contains information about the Olympic games from 1896–2016. The dataset contains two files; the athletes and the region file.
There are 271116 rows and 15 columns in the Athletes file. Each row represents an individual athlete competing in an Olympic event (athlete events). The columns are as follows:
* ID — Unique number for each athlete
* Name — Athlete’s name
* Sex — M or F
* Age — Integer
* Height — In centimeters
* Weight — In kilograms
* Team — Team name
* NOC — National Olympic Committee 3-letter code
* Games — Year and season
* Year — Integer
* Season — Summer or Winter
* City — Host city
* Sport — Sport
* Event — Event
* Medal — Gold, Silver, Bronze, or NA.

The Region file contains 230 rows and 3 columns. The columns are;

* NOC — National Olympic Committee 3-letter code
* Region — Name of countries
* Notes — Notes

### Issue in Dataset :
**Region Column**
* There are 206 country participate the olympics but there are some historical issue.<br/>
**For example** - At that time east germany and west germany were different, but now they have become one.<br/>
                  In 1991 Russia has disintegrated into 16 country.<br/>
   Samoa and American Samoa are same region.<br/>
   Individual Olympics Athletes is not a region. <br/>
   There are 2 Virgin Islands.
    

### Data analysis is about answering questions. Let's define some questions :
1. How many country participated in Olympics?
2. How many Olympics games have been held?
3. Top 10 participating countries to the Olympics? in both summer and winter

2. Mention the total number of nations who participated in each Olympics game?

3. Which year saw the highest and lowest no of countries participating in the Olympics?

4. Which nation has participated in all of the Olympic games?

5. Identify the sport which was played in all summer Olympics.

6. Which Sports were just played only once in the Olympics?

7. Fetch the total number of sports played in each Olympic game.

8. Fetch details of the oldest athletes to win a gold medal.

9. Find the Ratio of male and female athletes who participated in all Olympic games.

15. Identify which country won the most medals in each Olympic game.

17. Which countries have never won medals?

-- [olympic.ipynb](https://github.com/Uqbaahmad/Olympics-Analysis/blob/main/Analysis/olympics.ipynb)


### Insights : 
* There have been a total of 51 Olympic games from 1896–2016
* France, Italy, Switzerland, and UK have participated in all Olympic games from 1896–2016
* The Oldest Athletes to win a gold medal are Charles Jacobus and Oscar Gomer Swahn at the age of 64
* Michael Fred Phelps has won the most medals in Olympic history
* The most successful country in the Olympics is the USA with a total of 5637 medals
* Nigeria won its highest Olympic medal in football with 50 medals.

# Streamlit
I have used streamlit because in this I can show all the graph in web page. In Jupyter notebooks, we used to do a lot of coding for every graph, which caused space problems.

[Streamlit Visulization](https://github.com/Uqbaahmad/Olympics-Analysis/tree/main/Streamlit)

To run this web page: <br/>

* **cd Streamlit** <br/>
* **streamlit run app.py** <br/>
  **Local URL: http://localhost:8501  <br/>
  Network URL: http://192.168.0.101:8501**
