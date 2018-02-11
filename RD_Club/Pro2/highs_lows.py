# highs_lows
# Created by JKChang
# 22/01/2018, 15:40
# Tag:
# Description:

import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'resources/sitka_weather_2014.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d").date()
            high = int(row[1])
            low = int(row[3])

        except ValueError:
            print('missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='orange', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='white', alpha=0.1)
#
plt.title('Daily temperature in 2014', fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)
#
plt.savefig('temperature.png', bbox_inches='tight')
plt.show()
