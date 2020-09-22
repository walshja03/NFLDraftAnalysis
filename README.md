# NFLDraftAnalysis

High Level Overview
1) scraped combine information and individual player url's from sports-reference.com using Python along with Pandas, and Beautiful Soup Libraries
2) visited the url of each player and scraped their college stats by year for receiving, rushing, and yards from scrimmage (combo of both)
3) reorganized and standardized the player data to accomodate all players and have a single attribute per column to run through machine learning
4) gathered data manually on Fantasy Points Scored over the last 11 years and read them all into a single dataframe
5) Created a function to get each players sum of fantasy points scored in their first 3 years in the NFL
6) Created a function to standardize names to merge the dataframes together
7) merged all the data frames and wrote a function to run the data through machine learning
8) After seeing initial results with all data created several Tableau dashboards to visualize the data and decide on most relevant data to run into the model
9) Created a web page utilizing HTML, JavaScript, Bootstrap, and D3 to show the results of the model and display the Tableau Dashboards
10) Reworked the model into a function in which you could pass n number of variables
11) created a front end where a user can select the variables to run through the model that connects to the model and returns the appropriate output based on the model


Deeper Dive

  For this project I wanted to project the success of the WR's that were taken in the NFL draft.  In order to attempt to answer this question I web scraped the combine and college statistics of the wide recievers for which the data was available on sports-reference.com. For my analysis I only gathered information on players that were drafted and had college statistics available.  Unfortunately, this limited my data to D2 players. The combine data was by year and easy to get, but the individual player today was more challenging as each individual had their own site.  I ended up scraping the urls of each player from the combine page if they had been drafted.  Then I wrote a programe to visit each players page and get their receiving and rushing statistics.  I collecting the names of those that I couldn't successfully scrape and realized there were 2 populations that didn't follow the typical html format which included players that were primarily rushers at the college level and those that attended multiple schools throughout their career.  I made adjustments to gather their information.  After doing so I had the challenge of getting a players college statistics in a useable format to run through machine learning.  I wrote a function to transform the data so that it had a column per statistic per year/career. Furthermore, I appended  0's for players that didn't have statistics for corresponding years due to injury or not getting playing time.  
