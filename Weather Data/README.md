# Scraping Weather Data

* In this case study you have to scrape weather data from the website <b>"http://www.estesparkweather.net/archive_reports.php?date=200901"</b>
* Scrape all the available attributes of weather data for each day from 2009-01-01 to 2018-10-28
* Ignore records for missing days
* Represent the scraped data as pandas dataframe object.

## Dataframe specific details

### Expected column names (order dose not matter):

<table><tr><td>
<ul>
<li>Average temperature (°F)</li>
<li>Average humidity (%)</li>
<li>Average dewpoint (°F)</li>
<li>Average barometer (in)</li>
<li>Average windspeed (mph)</li>
<li>Average gustspeed (mph)</li>
<li>Average direction (°deg)</li>
<li>Rainfall for month (in)</li>
<li>Rainfall for year (in)</li>
<li>Maximum rain per minute</li>
</ul></td><td><ul>
<li>Maximum temperature (°F)</li>
<li>Minimum temperature (°F)</li>
<li>Maximum humidity (%)</li>
<li>Minimum humidity (%)</li>
<li>Maximum pressure</li>
<li>Minimum pressure</li>
<li>Maximum windspeed (mph)</li>
<li>Maximum gust speed (mph)</li>
<li>Maximum heat index (°F)</li>
</ul>
</td></tr></table>


### More details:

* Each record in the dataframe corresponds to weather deatils of a given day
* Make sure the index column is date-time format (yyyy-mm-dd)
* Perform necessary data cleaning and type cast each attributes to relevent data type
