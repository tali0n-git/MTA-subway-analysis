# MTA Subway Data Analysis

To explore trends in the MTA subway system in New York City, we performed a different sets of analysis. The goal of this analysis is to evaluate subway performance to understand commuter experience, service reliability and train delay trends. We will be downloading subway consumer metrics csv files from 2015-2019, and in certain cases comparing them to metrics data from 2020-2024. We have also integrated weather datasets to explore these trends.

## Overview
The goal of this analysis is to:

* Download relevant datasets from the MTA website and other sources.
* Structure the data into manageable Pandas DataFrames for further analysis.
* Potentially explore trends, or visualize subway activity.

## Files in this Project
* `data` (csv files): The CSV files where DataFrames will be generated from.
* notebooks: Jupyter notebooks (5) for data exploration and analysis.
* `mta-att-apipy`: The access point of our MTA api, JSON data. Was not implemented in the analysis but is available for future use.
* 'README.md': This file, which provides an overview of the project and answers to analytical questions.

## Dataset Dictionary

* `month`: The month in which the metrics are being calculated (yyyy-mm-dd).
* `division`: The A Division (numbered subway lines and S 42nd) and B Division (lettered subway lines).
* `line`: Each subway line (1, 2, 3, 4, 5, 6, 7, A, C, E, B, D, F, M, G, JZ, L, N, Q, R, W, S 42nd, S Rock, S Fkln).
* `period`: Represents both the peak and off-peak service periods.
* `num_passengers`: Total number of estimated passengers reported each month and on each line.
* `additional platform time`: The average estimated additional time in minutes (above scheduled time) customers wait for their train, reported each month and on each line.
* `additional train time`: The average estimated additional time in minutes (above scheduled time) customers spend onboard a train, reported each month and on each line.
* `total_apt`: The total number of estimated additional time in minutes (above scheduled time) customers wait for their train, reported each month and on each line.
* `total_att`: The total number of average additional time in minutes (above scheduled time) customers spend onboard a train, reported each month and on each line
* `over_five_mins`: The estimated total number of customers whose journeys are not completed within 5 minutes of the scheduled time, reported each month and on each line.
* `over_five_mins_perc`: The estimated percentage of customers whose journeys are not completed within 5 minutes of the scheduled time, reported each month and on each line.
* `customer journey time performance` : The estimated percentage of customers whose journeys are completed within 5 minutes of the scheduled time, reported each month and on each line.


## Analytical questions and responses

### 1. How punctual/consistent are the trains in each division from 2020-2024? (Jahaira-notebook)

* After running various analyses we can conclude that train lines in Division A (numbered lines) are the most punctual and consistent across the years from 2020-2024. We can observe this trend in our box plot where we observed a higher median in the average additional platform times in Division B (lettered lines) in comparison to Division A. Additionally, the plot depicts more extreme outliers in Division B which suggests that overall this division experiences longer delays in comparison to Division A. This finding is also consistent with our standard deviation values. We learned that Division A had a lower deviation of average additional platform times of 33 minutes in comparison to Division B with an average additional platform time of about 48 minutes. This indicates, once again, that Division A experiences more consistency in arrival time in comparison to Division B. 

### 2. How punctual/consistent are the trains in each divisions from 2015-2019? (Jahaira-notebook)

* After running various analyses we can conclude that train lines in Division A (numbered lines) are the most punctual and consistent across the years from 2015-2019. We can observe this trend in our box plot where we observed a higher median in the average additional platform times in Division B (lettered lines) in comparison to Division A. Additionally, the plot depicts more extreme outliers in Division B which suggests that overall this division experiences longer delays in comparison to Division A. This finding is also consistent with our standard deviation values. We learned that Division A had a lower deviation of average additional platform times of 31 minutes in comparison to Division B with an average additional platform time of about 42 minutes. This indicates, once again, that Division A experiences more consistency in arrival time in comparison to Division B which is similar to the findings for delays between divisions from 2020-2024.

### 3. How punctual/consistent are the trains in each divisions from 2015-2024? (Jahaira-notebook)

* For our final analysis, to determine train line consistencies and punctuality, we combined data from 2015-2019 and 2020-2024 to perform various analyses based on divisions A and B. Based on our findings, we can conclude that train lines in Division A (numbered lines) are the most punctual and consistent across the years. This finding is consistent with our standard deviation values. We learned that Division A had a lower deviation of average additional platform times of 32 minutes in comparison to Division B with an average additional platform time of about 46 minutes. This indicates, once again, that Division A experiences more consistency in arrival time in comparison to Division B. 

### 4. How did passenger experience (measured by delays and journey time performance) change over subway lines and time? (Mina-notebook)

* Passenger experience, measured by Customer Journey Time Performance and delay metrics, improved from the years 2015 to 2024. Customer Journey Time Performance is the percentage of trips that are completed within five minutes of their scheduling, reported each month for each line. During the 2020 COVID-pandemic, MTA activity dropped significantly, which was reflected in a temporary decline in delays. However, when comparing the pre-COVID and post-COVID periods, improvements in service quality is revealed.

* Subway lines varied in performance, with some lines consistently underperforming, while others, such as the L line, maintained high performance, with CJTP values of around 90%. The Pearson's correlation coefficient between the total additional platform wait time and Customer Journey Time Perfromace was -0.5, indicating a moderate negative correlation. This implies that the more a person waits on the platform for the train, the lower the CJTP. Reducing these delays would greatly improve rider experience across the train system.

### 5. How do average platform and train delays change over time, and what months experience the worst performance in 2020-2024? (Jessica-notebook)

* In 2020, the delays for platform and train delays were very low, it was close to zero delays from March to June. This was probably due to COVID and low number of customers using MTA services.

* Delays started to increase in 2021, with platform delays peaking 1.62 by the end of the year. 

* In 2022-2024, delays remained higher than 2020. Especially during the fall and winter months, many months exceded 1.3 of platform delay and 0.4 + of train delay. 

* There is a moderate positive correlation 0.50 between platform and train delays which means most of the time When platform delays go up, train delays tend to go up too.

* The top worst 5 months (Sep 2021,Oct 2022, Dec 2023, Nov 2024, Jan 2024) can suggest delays occur the most during the fall and winter months. From 2020 to 2024, average platform and train delays are higher in colder months. This insight can help transit authorities target months that need more improvements such as increasing staffing and planning more scheduled MTA services for less wait time. 

### 6. Does weather have an influence on train time? (Thalyann-notebook)

* Ultimately, the correlation between weather (precipitation, snow, and temperature) and total train time for underground trains is weak (0.06, 0.03, and 0.003 respectively).

* However, the correlation between precipitation and total train time for above ground trains is slightly stronger (0.08 vs 0.06). This suggests that rain has a minor impact on above ground when compared to the service of all trains. For snow and temperature, the correlation is even weaker (0.03 and 0.003 respectively). This suggests that snow and temperature have a negligible impact on above ground trains when compared to underground trains.

* This could be an incorrect assessment, as the trains were divided into above ground and underground based on the station location. This means that the train could be above ground for part of the trip and underground for the rest. This could lead to an underestimation of the impact of weather on total train time for above ground trains.

* A future analysis could include a more detailed breakdown of the train routes and their locations to get a better understanding of the impact of weather on total train time. This could include breaking down the train routes into percentages of their being above ground and underground, and then using that information to calculate a more accurate correlation between weather and total train time.

### 7. Is there a difference in service time between off-peak and peak service periods? (Rosania-notebook)

* There is no difference in service time between offpeak and peak service. From the graphs below, the average customer journey time for offpeak and peak service was evenly split for both. Peak service is slight more than 3.0 compared to offpeak service in comparing with number of passengers. Besides that, nothing influences the service time between offpeak and peak service.

* According to Pearson's correlation coefficient for Number of Passengers and Customer Journey Time, there is no correlation. Customer Journey Time was -0.31 which is closer to -1 than 0. Hence, it's a very weak negative correlation. It looks that there's no influence on the number of passengers and train punctuality.


### 8. What influence does the number of passengers have with train punctuality? (Rosania-notebook)
* There is no difference in service time between offpeak and peak service. From the graphs below, the average customer journey time for offpeak and peak service was evenly split for both. Peak service is slight more than 3.0 compared to offpeak service in comparing with number of passengers. Besides that, nothing influences the service time between offpeak and peak service.

* According to Pearson's correlation coefficient for Number of Passengers and Customer Journey Time, there is no correlation. Customer Journey Time was -0.31 which is closer to -1 than 0. Hence, it's a very weak negative correlation. It looks that there's no influence on the number of passengers and train punctuality.