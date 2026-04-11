# Climate Data Analysis Indonesia
This project analyzes daily climate data in Indonesia (2010–2022) using Python and Pandas.

# Objective
- Clean the dataset (handle missing values & duplicates)
- Analyze rainfall (RR) and average temperature (Tavg)
- Identify climate patterns across stations

# Tools & Libraries
- Python
- Pandas

# Dataset
Indonesia Daily Climate Data (2010–2022)
Source:
https://www.kaggle.com/datasets/greegtitan/indonesia-climate 
This dataset contains daily climate observations including temperature, rainfall, humidity, and wind parameters across multiple stations in Indonesia.

# Data Processing
- Handling missing values using:
  - Median (numerical data)
  - Mode (categorical data)
- Removing duplicate data
- Grouping data by station_id
- Calculating mean rainfall and temperature

# Analysis
- Aggregation using groupby
- Sorting to identify extreme values

# Key Insights
- The highest average rainfall is observed at station 97796 (~16.93 mm)
- Rainfall varies significantly across stations, indicating different local climate conditions  
- The highest average temperature is around 28.9°C
- Most stations have temperatures ranging between 25–28°C
- Rainfall variation is more extreme compared to temperature variation  

# Author
Dwi Widyaningsih
