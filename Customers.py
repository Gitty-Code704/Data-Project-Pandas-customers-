# Question: What dates had the most customer subscription(s)? 

import pandas as pd
data = pd.read_csv("customers-100.csv")
print(data.shape)
data.head(5)

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('customers-100.csv')

# Display the first few rows to confirm the data is loaded
print(df.head())

import pandas as pd

# Step 1: Load the CSV file into a DataFrame
df = pd.read_csv('customers-100.csv')

# Step 2: Create a new column 'Full Name' by combining 'First Name' and 'Last Name'
df['Full Name'] = df['First Name'] + ' ' + df['Last Name']

# Step 3: Display the DataFrame to check the result
print(df[['First Name', 'Last Name', 'Full Name']])

# Optional: Step 4: Save the modified DataFrame back to a CSV
df.to_csv('customers-100.csv', index=False)

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV data into a DataFrame
df = pd.read_csv('customers-100.csv')

# Step 2: Check the first few rows to understand the data
print(df.head())

# Step 3: Convert 'Subscription Date' to datetime if it's not already in that format
df['Subscription Date'] = pd.to_datetime(df['Subscription Date'], errors='coerce')  # Convert to datetime

# Step 4: Drop rows where 'Subscription Date' could not be converted (optional)
df = df.dropna(subset=['Subscription Date'])

# Step 5: Create a plot (e.g., Subscription Date)
plt.figure(figsize=(10, 25))

# If you're plotting dates, you might want to use a histogram or count per time period
# Example: Plot a histogram of Subscription Dates
plt.hist(df['Subscription Date'], bins=30, color='blue', edgecolor='black', alpha=0.7)

# Step 6: Customize the plot
plt.title('Distribution of Subscription Dates')
plt.xlabel('Date')
plt.ylabel('Frequency')
plt.xticks(rotation=45)  # Rotate date labels for better visibility
plt.tight_layout()  # Adjust the layout to avoid clipping
plt.grid(True)

# Step 7: Display the plot
plt.show()

# The highest number of subscriptions occurred in January of 2022. The lowest occurred in January of 2021 and April of 2022. The median for customer subscriptions occurred in March and April of 2021.  
# Further analysis needed for what websites were most subscribed to. 