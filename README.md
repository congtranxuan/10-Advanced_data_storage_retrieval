# This work is about Reflect Tables into SQLAlchemy ORM #
## I. Climate Analysis and Exploration ##
1. Using automap_base() in SQLAlchemy to create table columns, then save the references into tables.
2. Connect the database to pandas using SQLAlchemy through create_engine(), session.
## II. Exploration Data and Analysis ##
1. Find the last date in Measurement table data and calculate the one year date before that to query the data.

![](Reflect_table_SQLAlchemy.png)

2. Query precipitation data into panda and drop NAN values of precipitation then set index equal 'date'.

![](Exploratory_analysis.png)

3. Plot the bar chart of one year data of precipitation.

![](precipitation.png)
 
4. The summary statistics for the precipitation data

![](describe.png)

5. Get the station list of temperature observations.

6. Find the station with highest number of temperature observations and query the temperature in one year for this station.
7. Plot the historam for the temperature dataset.

![](tobs_ayear.png)

8. Use the calc_temps(start, end) to calculate the temperature min, avg, max for the trip period. The trip was from 2016-07-01 to 2016-07-18

9. Plot the bar chart of average temperature for the trip and yerr for the difference of max and min.

![](Trip_avg_temp.png)

10. Calculate the total amount of precipitation for stations during the trip.
### III. Optional Challenge Assignment ###
1. Calculate the temperature of min, max, avg through function daily_normals for dates of trip throughout years.
2. Plot the area chart for tmax, tavg, tmin for days of trip.

![](Temp_trip_normals.png)






