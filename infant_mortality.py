import requests
import pandas as pd
import matplotlib.pyplot as plt

# Define the API endpoint for the MDG_0000000001 indicator (Infant Mortality Rate) 
# from the World Health Organization (WHO) Athena API
url = 'https://ghoapi.azureedge.net/api/MDG_0000000001'

# Make a GET request to the WHO Athena API and retrieve the data
response = requests.get(url)
data = response.json()

# Define the desired region code, for example, 'AFR' for Africa
region_code = 'AFR'

# Filter the data to get only the countries from the specified region
filtered_countries = [item for item in data['value'] if item['ParentLocationCode'] == region_code and item['TimeDim'] == 2020]

# Print the results
for country in filtered_countries:
    print(f"Country: {country['SpatialDim']}, Year: {country['TimeDim']}, Value: {country['Value']}")

# Convert the filtered data into a DataFrame
df = pd.DataFrame(filtered_countries)

# Sort the dataframe in descending order of 'NumericValue' and take the first 10
top_10_countries = df.sort_values('NumericValue', ascending=False).head(10)

# Create a bar plot with the data of the top 10 countries with the higher mortality rate
top_10_countries.plot(kind='bar', x='SpatialDim', y='NumericValue', legend=False)
plt.title('Top 10 Countries with Highest Infant Mortality Rates in the AFR Region (2020)')
plt.xlabel('Country Code')
plt.ylabel('Infant mortality rate per 1000 live births)')

# Save the plot
plt.savefig('top_10_infant_mortality.png')