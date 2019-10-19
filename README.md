![Alt Text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgvTvbL44_iA2eJPy30599Hc1duyJhttBEU0qAWjILr4c1a3tK)
# **Analysis of Wild Fires in the United States (Full Stack-Project)**
# Background:
The purpose of this project is to analyze historical records of wildfires in the United States.
To accomplish this analysis, data was extracted from a kaggle dataset containing 1.88 million US wildfires; 24 years of geo-referenced wildfire records.
The data publication contains a spatial database of wildfires that occurred in the US from 1992 to 2015. The wildfire records were acquired from the reporting systems of federal, state, and local fire organizations. The following core data elements were required for records to be included in this data publication: discovery date, final fire size, and a point location. Tools used for this project include Python, Pandas, Plotly.js, Leaflet.js, Flask, PostgreSQL, SQLAlcemy, HTML5, CSS, Javascript and D3 among others.
# Extract
# ![Alt Text](https://www.bing.com/th?id=OIP.Fw4E9H7ZRyhHzWK7xk6jUQHaFB&w=233&h=160&c=7&o=5&dpr=1.5&pid=1.7)
## Original Data Source:
   * https://www.kaggle.com/rtatman/188-million-us-wildfires  
The data was stored as a SQLite file where it was then exported to a .csv file holding over 1.8 million rows of data.  Once in .csv format, the file was read into a Pandas dataframe using Python, Jupyter Notebooks, and Pandas.
# Transform: (Data Cleaning Process)  
##  ![Alt Text](https://www.bing.com/th?id=OIP.l8MinJm6s4scX7EmLp_hvAAAAA&w=179&h=178&c=7&o=5&dpr=1.5&pid=1.7)

As part of the transformation of the data, the columns of the dataframe were evaluated and columns that were relevant to the project was selected from the dataframes.  Next, some columns were renamed to give them more descriptive labeling.  After manipulating columns, each dataframe was evaluated to find what type of data was included in the database, the shape of the data meaning the number of rows and columns in the database, missing data, and duplicate data. Factors considered for analysis include: wildfire geographic location, acreage burned, causes of wildfire, and number of wildfires.  

# Load the Data
# ![Alt Text](https://www.bing.com/th?id=OIP.EKlqoGs8WygAu7Nq5-gKFgHaHa&w=208&h=206&c=7&o=5&pid=1.7)
After the data cleaning process was completed using Python and Pandas, a .csv was written where it was then uploaded to a PostgreSQL database which was connected to the Heroku web app hosting platform where the data could be queried.  

# Pre-Analysis
# ![Alt Text](https://www.bing.com/th?id=OIP.FBRjqFe8yZnS5oI7N2I_lwHaEL&w=299&h=169&c=7&o=5&pid=1.7)
## Several steps were taken before producing charts, interactive charts, and a heatmap:
  * Python was used to run SQLAlchemy where queries from the PostgreSQL database could be run
  * Pandas was used along with Python to read the query into a Pandas data frame
  * Selected data from Pandas was held in a variable where it was converted into a list and then jsonified
  * Flask returned the data as a route
  * D3 and Javascript selected a route to plot data using Plotly and Leaflet for the heatmap
  * Several Flask routes were used in conjunction wit Javascript to make the line chart and bar chart interactive.
  * A simple HTML file was used to present the inital analysis


# Analysis 
# ![Alt Text](https://www.bing.com/th?id=OIP.gOyn3l39bzwcepBMx2NYYQHaF7&w=265&h=206&c=7&o=5&pid=1.7)
## Pie Chart
The pie chart created with Plotly.js visualized the top 10 causes of wildfire and their respective percentages for the dataset. 
## Interactive Line Chart
The interactive line chart created with Plotly.js visualized a twenty year trend for total wildfires in the United States and a twenty year trend for wildfires in the top ten states for most number of wildfires.
## Interactive Bar Chart
The interactive bar chart created with Plotly.js displayed the total acres of land burned for the top ten states in the dataset and also displayed the top ten states for wildfire acreage burned during the last 5 years in the dataset.
## Heat Map
The heatmap created wit Leaflet.js displayed a heatmap which geolocated over 1.8 million areas of the United States where a wildfire was reported and also used terminator.js plugin to visualize which part of the map is in day or night.
## HTML5 
Bootstrap and CSS was used in conjunction with the plots to make an attractive visualizaton of the data, purpose of the project, and to display facts about the dataset.

# Post Analysis & Conclusion
# ![Alt Text](https://www.bing.com/th?id=OIP.3Y9U4Q0qs-ileWqR9F_GsAHaEc&w=300&h=179&c=7&o=5&pid=1.7)
There were no particular trends discovered in the line chart or bar chart based on the dataset used in this project. It seems that there are several factors that determines the number of wildfires and acreage burned due to wildfires that goes beyond the scope of this project. One could form a solid theory that when wildfires do occur humans are the culprit the vast majorty of the time based on the statistics captured in the pie chart and by observing the heat map which shows most of the fires occuring in near populated areas of the United States.  The only top 10 cause of fire that was of natural occurance is lightning according to this dataset which came in at 15% of causes of wildfire.

#Link to Project
# ![Alt Text](https://www.bing.com/th?id=OIP.b7j37FCv7hO196UEw_gSkwHaFj&w=273&h=205&c=7&o=5&pid=1.7)
**https://smokejumpers.herokuapp.com**




