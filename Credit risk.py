import kagglehub
import pandas as pd
# Import the adapter to tell kagglehub we want a pandas DataFrame
from kagglehub import KaggleDatasetAdapter 

#Use dataset_load to get the Dataframe directly
credit_data = kagglehub.dataset_load(KaggleDatasetAdapter.PANDAS, "nanditapore/credit-risk-analysis", "credit_risk.csv")

#Display thr first few rows of data
print(credit_data.head())

#Check the shape of ther dataset (number of rows and colums)
print ("Dataset Shapes: ", credit_data.shape)

#Summary statistics of numerical features
print ("Summary Statistics:")
print (credit_data.describe())

#Check for missing values
print("Missing Values:")
print(credit_data.isnull().sum())

#check data types of features
print ("Data Types:")
print (credit_data.dtypes)

