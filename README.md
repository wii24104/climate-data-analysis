# Climate Data Analysis Indonesia
This project analyzes daily climate data in Indonesia (2010–2022) using Python to explore rainfall patterns and temperature trends across multiple weather stations.

# Objective
- Clean the dataset (handle missing values & duplicates)
- Analyze rainfall (RR) and average temperature (Tavg)
- Identify climate patterns and trends across stations

# Tools & Libraries
- Python
- Pandas
- Matplotlib
- Seaborn

# Dataset
Indonesia Daily Climate Data (2010–2022)
Source:
https://www.kaggle.com/datasets/greegtitan/indonesia-climate 
This dataset contains daily observations including:
- Temperature (Tn, Tx, Tavg)
- Rainfall (RR)
- Humidity (RH_avg)
- Wind parameters

# Data Processing
- Handling missing values:
  - Median → numerical data (robust to outliers)
  - Mode → categorical data
- Removing duplicate data
- Grouping data by station_id
- Aggregating:
  - Mean rainfall
  - Mean temperature

# Analysis
- Aggregation using groupby
- Sorting to identify extreme values

# Visualizations
1. Top 5 Rainfall Stations
Shows stations with the highest average rainfall.
2. Rainfall Distribution
Displays distribution of daily rainfall (<50 mm) to reduce outlier dominance.
3. Temperature Trend
Shows yearly average temperature trends across Indonesia.

# Key Insights
1. Temperature Trend (Climate Signal)
- There is a gradual increase in average temperature from 2011 to 2020
- Lowest temperature: 2011 (~26.48°C)
- Highest temperature: 2016 (>27.2°C)
- The spike in 2016 is likely influenced by a strong El Niño event
2. Rainfall Distribution
- Rainfall distribution is positively skewed
- Most daily rainfall values are in the 0–5 mm range
- Indicates that light rain or no rain occurs more frequently than heavy rain
3. Station-Based Rainfall Characteristics
- Station 97796 has the highest average rainfall (~16.93 mm)
- Rainfall varies significantly across stations
- Temperature remains relatively stable (25–27°C) even in high rainfall areas
4. Data Insight (Processing Perspective)
- Using median for missing values is appropriate due to:
  - presence of extreme rainfall values
  - non-normal distribution
- Temperature shows low variability, consistent with tropical climate behavior

# Conclusion
This analysis suggests that:
- Indonesia shows a gradual warming trend over the observed decade
- Daily climate is dominated by low rainfall events, with occasional extremes
- Climate characteristics vary spatially across stations, especially for rainfall

# Author
Dwi Widyaningsih

⭐Notes
This project is part of a data science learning journey focusing on real-world climate data analysis.
