import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Carbon Dioxide Emission Estimates.csv')

#print(df) 

#print(pd.options.display.max_rows) #60

#print(df.head(10))

#-------------
#Data cleaning
#-------------

df = df.rename(columns={"CO2 emission estimates": "Country"})
print(df)


"""
#------------
#Scatter plot
#------------

#df.plot(kind = 'scatter', x = 'Value', y = 'Year')

fig, ax = plt.subplots(figsize=(10, 6))

#Enables colour coding by country
for country, group in df.groupby("Country"):
    ax.scatter(
        group["Year"],
        group["Value"],
        label=country
    )

#Creates graph
ax.set_xlabel("Year")
ax.set_ylabel("Value (thousand metric tons CO₂)")
ax.set_title("CO₂ Emissions by Country")

#Creates legend
ax.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.show()
"""

#--------------------------
#Scatter plot with forecast
#--------------------------

fig, ax = plt.subplots(figsize=(10, 6))

#Enables colour coding by country
for country, group in df.groupby("Country"):
    group = group.sort_values("Year")

    ax.scatter(
        group["Year"], 
        group["Value"], 
        label=country
    )

    #Linear fit (forecast trend)
    x = group["Year"]
    y = group["Value"]

    if len(group) > 1:
        m, b = np.polyfit(x, y, 1)  #Slope + intercept

        #Extend line into the future - 5 years
        future_years = np.arange(x.max(), x.max() + 6)
        forecast = m * future_years + b

        ax.plot(future_years, forecast, linestyle="--")

#Shading forecast region
last_year = df["Year"].max()
ax.axvspan(
    last_year,
    last_year + 5,
    color="grey",
    alpha=0.2,
    label="Forecast region"
)

#Creates graph
ax.set_xlabel("Year")
ax.set_ylabel("Value (thousand metric tons CO₂)")
ax.set_title("CO₂ Emissions - 5 Year Forecast")

#Creates legend
ax.legend(title="Country", loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)

plt.show()


"""
#---------
#Line plot
#---------

fig, ax = plt.subplots(figsize=(10, 6))

for country, group in df.groupby("Country"):
    group = group.sort_values("Year")  # Sort by year
    ax.plot(
        group["Year"],      # x-axis
        group["Value"],     # y-axis
        label=country
    )

ax.set_xlabel("Year")
ax.set_ylabel("Value")
ax.set_title("CO₂ Emissions by Country")

ax.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.show()
"""

#Test