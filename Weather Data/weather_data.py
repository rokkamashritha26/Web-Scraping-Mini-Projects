from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

## PARAMETERS SET ##
FROM_YEAR = 2009
TO_YEAR = 2018
FROM_MONTH = 1
TO_MONTH = 12
END_DATE = 28

## Dataframe with column names ##
df = pd.DataFrame(columns=['Average temperature (°F)', 'Average humidity (%)',
                           'Average dewpoint (°F)', 'Average barometer (in)',
                           'Average windspeed (mph)', 'Average gustspeed (mph)',
                           'Average direction (°deg)', 'Rainfall for month (in)',
                           'Rainfall for year (in)', 'Maximum rain per minute',
                           'Maximum temperature (°F)', 'Minimum temperature (°F)',
                           'Maximum humidity (%)', 'Minimum humidity (%)', 'Maximum pressure',
                           'Minimum pressure', 'Maximum windspeed (mph)',
                           'Maximum gust speed (mph)', 'Maximum heat index (°F)'])

done_flag = False

for year in range(FROM_YEAR, TO_YEAR + 1):
    if year == 2018:
        TO_MONTH = 10
    if done_flag:
        break
    for month in range(FROM_MONTH, TO_MONTH + 1):
        URL = "http://www.estesparkweather.net/archive_reports.php?date=" + str(year) + str(month).zfill(2)
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, "html.parser")
        results = dict()
        for row in soup.findAll('tr'):
            row_data = row.findAll('td')
            if len(row_data) == 1:
                single_str = row_data[0].string

                if results:
                    if mindex.strftime('%Y-%m-%d') == '2018-10-29':
                        done_flag = True
                        break
                    tmpdf = pd.DataFrame(results, index=[datetime.strptime(mindex.strftime('%Y-%m-%d'), '%Y-%m-%d')])
                    df = df.append(tmpdf, ignore_index=False)
                if 'Average and Extremes for Month' in single_str:
                    break
                month = single_str.split()[0]
                mdate = single_str.split()[1]
                mindex = datetime.strptime(month + ' ' + mdate + ' ' + str(year), '%b %d %Y')
                results.clear()
                continue

            e1 = row_data[0].string
            e2 = row_data[1].string
            if 'Average temperature' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Average temperature (°F)'] = float((tmp[:tmp.index('°')]).strip())
            if 'Average humidity' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Average humidity (%)'] = float((tmp[:tmp.index('%')]).strip())
            if 'Average dewpoint' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Average dewpoint (°F)'] = float((tmp[:tmp.index('°')]).strip())
            if 'Average barometer' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Average barometer (in)'] = float((tmp[:tmp.index(' ')]).strip())
            if 'Average windspeed' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Average windspeed (mph)'] = float((tmp[:tmp.index(' ')]).strip())
            if 'Average gustspeed' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Average gustspeed (mph)'] = float((tmp[:tmp.index(' ')]).strip())
            if 'Average direction' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Average direction (°deg)'] = float((tmp[:tmp.index('°')]).strip())
            if 'Rainfall for month' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Rainfall for month (in)'] = float((tmp[:tmp.index(' ')]).strip())
            if 'Rainfall for year' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Rainfall for year (in)'] = float((tmp[:tmp.index(' ')]).strip())
            if 'Maximum rain per minute' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Maximum rain per minute'] = float((tmp[:tmp.index(' ')]).strip())
            if 'Maximum temperature' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Maximum temperature (°F)'] = float((tmp[:tmp.index('°')]).strip())
            if 'Minimum temperature' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Minimum temperature (°F)'] = float((tmp[:tmp.index('°')]).strip())
            if 'Maximum humidity' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Maximum humidity (%)'] = float((tmp[:tmp.index('%')]).strip())
            if 'Minimum humidity' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Minimum humidity (%)'] = float((tmp[:tmp.index('%')]).strip())
            if 'Maximum pressure' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Maximum pressure'] = float((tmp[:tmp.index(' ')]).strip())
            if 'Minimum pressure' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Minimum pressure'] = float((tmp[:tmp.index(' ')]).strip())
            if 'Maximum windspeed' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Maximum windspeed (mph)'] = float((tmp[:tmp.index(' ')]).strip())
            if 'Maximum gust speed' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Maximum gust speed (mph)'] = float((tmp[:tmp.index(' ')]).strip())
            if 'Maximum heat index' in e1:
                tmp = e2.replace('<td>', '').strip()
                results['Maximum heat index (°F)'] = float((tmp[:tmp.index('°')]).strip())

df.to_csv('weather_data.csv')
