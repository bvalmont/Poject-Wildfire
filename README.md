# **Analysis of Wild Fires in the United States (Full Stack-Project)**
## Background
The purpose of this project is to analyze historical records of wildfires in the United States.
To accomplish this analysis, data was extracted from a kaggle dataset containing 1.88 million US wildfires; 24 years of geo-referenced wildfire records.
The data publication contains a spatial database of wildfires that occurred in the US from 1992 to 2015. The wildfire records were acquired from the reporting systems of federal, state, and local fire organizations. The following core data elements were required for records to be included in this data publication: discovery date, final fire size, and a point location. Tools used for this project include Python, Pandas, Plotly.js, Leaflet.js, Flask, PostgreSQL, SQLAlcemy, HTML5, CSS, and Javascript among others.
# Extract
# ![Alt Text](https://www.bing.com/th?id=OIP.Fw4E9H7ZRyhHzWK7xk6jUQHaFB&w=233&h=160&c=7&o=5&dpr=1.5&pid=1.7)
## Original Data Source:
   * https://www.kaggle.com/rtatman/188-million-us-wildfires  
The data was stored as a SQLite file where it was then exported to a .csv file holding over 1.8 million rows of data.  Once in .csv format, the file was read into a Pandas dataframe using Python, Jupyter Notebooks, and Pandas.
# Transform: (Data Cleaning Process)  
##  ![Alt Text](https://www.bing.com/th?id=OIP.l8MinJm6s4scX7EmLp_hvAAAAA&w=179&h=178&c=7&o=5&dpr=1.5&pid=1.7)


Factors analyzed includes: wildfire geographic location, acreage burned, causes of wildfire, and number of wildfires.  This page provides the source data and visualizations created as part of the analysis, as well as explanations and descriptions of any trends and correlations witnessed.
# Analysis and Insights
# Pie Chart
- Clearly shows that the top causes of wildfires is due to human action. - Debris and
# Line Chart
- Indicates an increasingly upwards trend in the total number of fires across all States in the USA.
# Bar Chart
- Highlights the top States with the largest acres burned - California, Georgia, Texas, North Carolina,Florida.
# Heat Map
- Most of the fires are concentrated in the urban areas lending further credence to the fact that Humans are the largest causes of wildfires.
# The trend analysis shows that areas that were not previously subjected to wildfires in the early 90's now have a high propensity to fires as the human population expands into these areas.
