# MTA Subway Data Analysis

This project analyzes real-time data from the Metropolitan Transportation Authority (MTA) subway system in New York City. It fetches live feed data for all train lines, processes it using the `protobuf` and `pandas` libraries, and organizes the information into Pandas DataFrames.

## Overview

The goal of this analysis is to:

* Download real-time subway feed data from the MTA API.
* Parse the Protocol Buffer encoded data.
* Structure the data into manageable Pandas DataFrames for further analysis.
* Potentially explore trends, predict arrivals, or visualize subway activity (depending on future development).

## Files in this Project

* `mta-att-apipy`: The access point of our MTA api, JSON data
* `gtfs_realtime_pb2.py`: Python classes generated from the `gtfs-realtime.proto` file (required for parsing the feed).
* `gtfs-realtime.proto`: The Protocol Buffer schema definition for GTFS Realtime data.
* `data` (csv files): The CSV files where DataFrames will be exported.

## Usage

To view the analysis, open:

analysis.ipynb

## Dataset Dictionary 
- `month`: The month in which the metrics are being calculated (yyyy-mm-dd).
- `division`: The A Division (numbered subway lines and S 42nd) and B Division (lettered subway lines).
- `line`: Each subway line (1, 2, 3, 4, 5, 6, 7, A, C, E, B, D, F, M, G, JZ, L, N, Q, R, W, S 42nd, S Rock, S Fkln).
- `period`: Represents both the peak and off-peak service periods.
- `num_passengers`: Total number of estimated passengers reported each month and on each line.
- `additional platform time`: The average estimated additional time in minutes (above scheduled time) customers wait for their train, reported each month and on each line.
- `additional train time`: The average estimated additional time in minutes (above scheduled time) customers spend onboard a train, reported each month and on each line.
- `total_apt`: The total number of estimated additional time in minutes (above scheduled time) customers wait for their train, reported each month and on each line.
- `total_att`: The total number of average additional time in minutes (above scheduled time) customers spend onboard a train, reported each month and on each line
-`over_five_mins`: The estimated total number of customers whose journeys are not completed within 5 minutes of the scheduled time, reported each month and on each line.
- `over_five_mins_perc`: The estimated percentage of customers whose journeys are not completed within 5 minutes of the scheduled time, reported each month and on each line.
- `customer journey time performance` : The estimated percentage of customers whose journeys are completed within 5 minutes of the scheduled time, reported each month and on each line.


## Analytical questions and responses:


### How punctual/consistent are the trains in each division from 2020-2024? 
* After running various analyses we can conclude that train lines in Division A (numbered lines) are the most punctual and consistent across the years from 2020-2024. We can observe this trend in our box plot where we observed a higher median in the average additional platform times in Division B (lettered lines) in comparison to Division A. Additionally, the plot depicts more extreme outliers in Division B which suggests that overall this division experiences longer delays in comparison to Division A. This finding is also consistent with our standard deviation values. We learned that Division A had a lower deviation of average additional platform times of 33 minutes in comparison to Division B with an average additional platform time of about 48 minutes. This indicates, once again, that Division A experiences more consistency in arrival time in comparison to Division B. 

### How punctual/consistent are the trains in each divisions from 2015-2019?
* After running various analyses we can conclude that train lines in Division A (numbered lines) are the most punctual and consistent across the years from 2015-2019. We can observe this trend in our box plot where we observed a higher median in the average additional platform times in Division B (lettered lines) in comparison to Division A. Additionally, the plot depicts more extreme outliers in Division B which suggests that overall this division experiences longer delays in comparison to Division A. This finding is also consistent with our standard deviation values. We learned that Division A had a lower deviation of average additional platform times of 31 minutes in comparison to Division B with an average additional platform time of about 42 minutes. This indicates, once again, that Division A experiences more consistency in arrival time in comparison to Division B which is similar to the findings for delays between divisions from 2020-2024.

### How punctual/consistent are the trains in each divisions from 2015-2024?
* For our final analysis, to determine train line consistencies and punctuality, we combined data from 2015-2019 and 2020-2024 to perform various analyses based on divisions A and B. Based on our findings, we can conclude that train lines in Division A (numbered lines) are the most punctual and consistent across the years. This finding is consistent with our standard deviation values. We learned that Division A had a lower deviation of average additional platform times of 32 minutes in comparison to Division B with an average additional platform time of about 46 minutes. This indicates, once again, that Division A experiences more consistency in arrival time in comparison to Division B. 

### How did passenger experience (measured by delays and journey time performance) change over subway lines and time?
* Passenger experience, measured by Customer Journey Time Performance and delay metrics, improved from the years 2015 to 2024. Customer Journey Time Performance is the percentage of trips that are completed within five minutes of their scheduling, reported each month for each line. During the 2020 COVID-pandemic, MTA activity dropped significantly, which was reflected in a temporary decline in delays. However, when comparing the pre-COVID and post-COVID periods, improvements in service quality is revealed.

* Subway lines varied in performance, with some lines consistently underperforming, while others, such as the L line, maintained high performance, with CJTP values of around 90%. The Pearson's correlation coefficient between the total additional platform wait time and Customer Journey Time Perfromace was -0.5, indicating a moderate negative correlation. This implies that the more a person waits on the platform for the train, the lower the CJTP. Reducing these delays would greatly improve rider experience across the train system.

### How do average platform and train delays change over time, and what months experience the worst performance in 2020-2024?
* In 2020, the delays for platform and train delays were very low, it was close to zero delays from March to June. This was probably due to COVID and low number of customers using MTA services.

* Delays started to increase in 2021, with platform delays peaking 1.62 by the end of the year. 

* In 2022-2024, delays remained higher than 2020. Especially during the fall and winter months, many months exceded 1.3 of platform delay and 0.4 + of train delay. 

* There is a moderate positive correlation 0.50 between platform and train delays which means most of the time When platform delays go up, train delays tend to go up too.

* The top worst 5 months (Sep 2021,Oct 2022, Dec 2023, Nov 2024, Jan 2024) can suggest delays occur the most during the fall and winter months. From 2020 to 2024, average platform and train delays are higher in colder months. This insight can help transit authorities target months that need more improvements such as increasing staffing and planning more scheduled MTA services for less wait time. 







2. Does weather have an influence on train time? -Thalyann
3. Is there a difference in service time between off-peak and peak service periods? -Rosania
    a. What influence does the number of passengers have with train punctuality?
