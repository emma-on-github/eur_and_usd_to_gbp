import pandas as pd
currency = pd.read_excel('downloads/EUR and USD to GBP June 2022 to June 2023.xlsx',
                        sheet_name= 'BoE-Database_export',
                        parse_dates=["Date"],
                        index_col="Date")

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(currency.index, currency["EUR"],
        color='blue')
ax.set_title("EUR and USD to GBP June 2022 to June 2023")
ax.set_xlabel('Date')
ax.set_ylabel('EUR', color='blue')
ax.tick_params('y', colors='blue')
ax2 = ax.twinx()
ax2.plot(currency.index,
         currency["USD"],
         color='red')
ax2.set_ylabel('USD',
        color='red')
ax2.tick_params('y', colors='red')
plt.show()
