import pandas as pd
import os

#importing the data

sales_data = pd.read_csv("~/Downloads/RetailSalesData.csv")


#inspecting data
print(sales_data.head())
print(sales_data.info())

# Check for missing values
print(sales_data.isnull().sum())

