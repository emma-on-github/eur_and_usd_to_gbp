# import pandas
import pandas as pd

# read excel file, specifying sheet name, parse dates, column index
currency = pd.read_excel('downloads/EUR and USD to GBP June 2022 to June 2023.xlsx',
                        sheet_name= 'BoE-Database_export',
                        parse_dates=["Date"],
                        index_col="Date")

# import matplotlib
import matplotlib.pyplot as plt

# create a figure and set of subplots
fig, ax = plt.subplots()

# plot Eur currency as Blue
ax.plot(currency.index, currency["EUR"],
        color='blue')

# set title, x and y labels
ax.set_title("EUR and USD to GBP June 2022 to June 2023")
ax.set_xlabel('Date')
ax.set_ylabel('EUR', color='blue')

# set y label (EUR) colour
ax.tick_params('y', colors='blue')

# create a twin axes sharing the x axis
ax2 = ax.twinx()

# plot USD currency as Red
ax2.plot(currency.index,
         currency["USD"],
         color='red')

#set y label (USD) colour
ax2.set_ylabel('USD',
        color='red')

# set y label (USD) colour
ax2.tick_params('y', colors='red')

# show the graph
plt.show()




