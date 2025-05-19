# MTA Subway Data Analysis

This project analyzes real-time data from the Metropolitan Transportation Authority (MTA) subway system in New York City. It fetches live feed data for the A, C, E lines and potentially others, processes it using the `protobuf` and `pandas` libraries, and organizes the information into Pandas DataFrames.

## Overview

The goal of this analysis is to:

* Download real-time subway feed data from the MTA API.
* Parse the Protocol Buffer encoded data.
* Structure the data into manageable Pandas DataFrames for further analysis.
* Potentially explore trends, predict arrivals, or visualize subway activity (depending on future development).

## Files in this Project

* `mta-feed.py`: The script used to download the MTA feed, parse the data, and create the Pandas DataFrames.
* `gtfs_realtime_pb2.py`: Python classes generated from the `gtfs-realtime.proto` file (required for parsing the feed).
* `gtfs-realtime.proto`: The Protocol Buffer schema definition for GTFS Realtime data.
* `data` (csv files): The CSV files where DataFrames will be exported.

## Usage

To view the analysis, open:

analysis.ipynb