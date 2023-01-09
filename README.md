# Data Analysis of Olympics
Data Analysis or sometimes referred to as Exploratory Data Analysis (EDA) is one of the core components of data science. It is also the part on which data scientists, data engineers and data analysts spend their majority of the time which makes it extremely important in the field of data science.

This repository demonstrates some common EDA methods and techniques using Python. For purpose of illustration the 120 Years of Olympic Analysis history dataset has been taken from [kaggle](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results) since it is one of the ideal dataset for performing EDA and taking a step towards the most amazing and interesting field of data science. <br/>


The modern Olympic Games are the most important international sporting events, with summer and winter sports tournaments involving thousands of competitors from all over the world.
With over 200 nations competing, the Olympic Games are regarded as the world's premier sporting event. The Olympic Games are generally held every four years, and since 1994, the Summer and Winter Olympics have alternated every two years throughout the four-year period.

This file contains analysis performed upon olympic dataset - [Olympic.ipynb](https://github.com/Uqbaahmad/Olympics-Analysis/blob/main/Analysis/olympics.ipynb)

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
**Region**
* There are 206 country participate the olympics but there are some historical issue.<br/>
**For example** - At that time east germany and west germany were different, but now they have become one.<br/>
                  In 1991 Russia has disintegrated into 16 country.<br/>
   Samoa and American Samoa are same region.<br/>
   Individual Olympics Athletes is not a region. <br/>
   There are 2 Virgin Islands.
 
**Sport**
* Earlier, many games used to played in the Olympics, cricket was also one of them but at present cricket is not considered an Olympic game.
* In 120 years of Olympics, many games have been added and many games have also been removed.

   
**Year**
* The cycle of Olympic is 4 year but in year 1904, 1906, 1908 the olympic has been held. <br/>
*The 1906 Summer Olympics, also called the 1906 Intercalated Games, were held in Athens, Greece.
These games are not awarded the title of Olympiad because they were held between the III and IV Olympiads. Medals were given to the participants during these games, but the medals are not officially recognised by the International Olympic Committee.* 
    

### Data analysis is about answering questions. Let's define some questions :
1. How many country participated in Olympics?
2. How many Olympics games have been held?
3. The total number of nations who participated in each Olympics game?
4. Top 5 countries in which most medals were won?
5. How many medals did India win?
6. Identify each country and years record.
7. How many no of editions were there?
8. How many no of cities in Olympics?
9. How many no of sports participated?
10. How many no of events have been held?
11. How many no of athletes participated?
12. How many no of nations participated?
13. Over the years how many participating nations have appeared in each Olympics?
14. Over the years how many no of events have been held in Olympics?
15. Over the years how many athletes have been played in Olympics?
16. Fetch the top 10athletes who have won the most medals
17. Identify most successful athletes all times in Olympics?
18. Identify in which year India has won how many medals?
19. Mention probability density function of athletes age who have participated in olympics and medalist age distribution.
20. Identify the distribution of age respect to sports(Gold Medalist)
21. Identify the distribution of age respect to sports(Silver Medalist)
22. Identify the Weight and height of athletes and who won medals or not.
23. Participation of male and female in Olympics.

link - [Answers](https://medium.com/@uqba2199/olympic-data-analysis-62c4ba87783a)

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
