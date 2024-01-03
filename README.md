# sqlalchemy-challenge

# Background
You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. 
 ### To help with your trip planning, you decide to do a climate analysis about the area. 

 # Part 1: Analyze and Explore the Climate Data
 This focuses on utlizing SQLalchemy ORM queres, pandas, and matplotlib in order to develop climate analysis from the database.
1. Use the SQLAlchemy create_engine() function to connect to your SQLite database.
2. Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.
3. Link Python to the database by creating a SQLAlchemy session
     - *Remember to close your session at the end of your notebook.*

## Precipitation Analysis
1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data
3. Select only the "date" and "prcp" values.
4. Load the query results into a Pandas DataFrame. Explicitly set the column names.
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame plot method
     ![image](https://github.com/ruqayyahnur/sqlalchemy-challenge/assets/136443525/3b83352d-0e84-439a-b9d6-c4fa9d0d4012)
7. Use Pandas to print the summary statistics for the precipitation data.

## Station Analysis
1. Design a query to calculate the total number of stations in the dataset.
2. Design a query to find the most-active stations
     - List the stations and observation counts in descending order.
     - Answer the following question: which station id has the greatest number of observations?
3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
4. Design a query to get the previous 12 months of temperature observation (TOBS) data.
     - Filter by the station that has the greatest number of observations.
     - Query the previous 12 months of TOBS data for that station.
     - Plot the results as a histogram with *bins=12*
   ![image](https://github.com/ruqayyahnur/sqlalchemy-challenge/assets/136443525/fea74eae-917b-4a9e-8c8b-f8e8e113e866)

# Part 2: Design Your Climate App
Design the Flask API
1. /
   - start at the homepage
   - list all the available routes
2. /api/v1.0/precipitation
   - Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
   - Return the JSON representation of your dictionary.
3. /api/v1.0/stations
   - return a JSON list of stations from the dataset
4. /api/v1.0/tobs
   - Query the dates and temperature observations of the most-active station for the previous year of data.
   - Return a JSON list of temperature observations for the previous year.
5. /api/v1.0/<start> and /api/v1.0/<start>/<end>
   - Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
   - For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
   - For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
