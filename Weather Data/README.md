# Scraping Weather Data

* In this case study you have to scrape weather data from the website <b>"http://www.estesparkweather.net/archive_reports.php?date=200901"</b>
* Scrape all the available attributes of weather data for each day from 2009-01-01 to 2018-10-28
* Ignore records for missing days
* Represent the scraped data as pandas dataframe object.

## Dataframe specific deatails

### Expected column names (order dose not matter):

* Average temperature (°F)
* Average humidity (%)
* Average dewpoint (°F)
* Average barometer (in)
* Average windspeed (mph)
* Average gustspeed (mph)
* Average direction (°deg)
* Rainfall for month (in)'
* Rainfall for year (in)
* Maximum rain per minute
* Maximum temperature (°F)
* Minimum temperature (°F)
* Maximum humidity (%)
* Minimum humidity (%)
* Maximum pressure
* Minimum pressure
* Maximum windspeed (mph)
* Maximum gust speed (mph)
* Maximum heat index (°F)

### More details:

* Each record in the dataframe corresponds to weather deatils of a given day
* Make sure the index column is date-time format (yyyy-mm-dd)
* Perform necessary data cleaning and type cast each attributes to relevent data type
