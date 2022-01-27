# %% [markdown]
# # Data Quality
# In this notebook the data sets of the three streaming services will be validated in terms of data quality. The results will provide the necessary insights for subsequent analysis tasks. 
#
# Data quality will be assest by the following dimensions: 
# - Completeness
# - Uniqueness
# - Consistency
# - Validity
# - Accuracy 

# %%
from numpy.core.fromnumeric import shape
import pandas as pd
import numpy as np
from pathlib import Path
# %%
ROOT=Path(__file__).parent.parent
# Load data
netflix_data=pd.read_csv(ROOT/"data"/"raw"/"netflix_titles.csv")
amazon_data=pd.read_csv(ROOT/"data"/"raw"/"amazon_prime_titles.csv")
disney_data=pd.read_csv(ROOT/"data"/"raw"/"disney_plus_titles.csv")
services=["netflix", "amazon","disney"]

#%% [markdown]
# ## Consistency
# In order to be able to join data from the different streaming services  and compare them against each other each data set needs to contain the same features.
#%%
assert all(netflix_data.columns==amazon_data.columns) & all(netflix_data.columns==disney_data.columns)

#%% [markdown]
# Join Data Sets
# For easier handling the three data sets are joined together.
#%%
for service_name, service_data in zip(services,[netflix_data,amazon_data,disney_data]):
    service_data[service_name]=True
data=pd.concat(data_set_collection.values())
#%%
for feature in data.columns[-3:]:
    data[feature]=data[feature].replace(to_replace=np.NaN,value=False)


#service_features.replace(to_replace=None,value=0)
#%% [markdown]
# ## Uniqueness
# Check if the data contains duplicates
#%% [markdown]
# ## Data Completeness
# ### Missing values per feature

# As the follwing dataframes show, there is a significant amount of data missing for the features "director", "country" and "date_added". Note that for the later two features the amazon_data data set provides nearly no data.
#
# For none of the features containing missing values it is advisable to fill them in, since there can not be made reasonable assumptions about them. Further more they should not be removed from the data set either, because the remaining data might still be usefull for certain analytics.
# Total amount of missing values
#%%
# instantiate missing value dataframes
missing_values_total=pd.DataFrame(index=services+["total"],columns=data.columns)
missing_values_percent=missing_values_total.copy()

# compute missing values (total,ratio) for service

# count 
titles_count={}
for service in services:
    titles_count[service]=sum(data[service])
titles_count["total"]=sum(titles_count.values())

for service in services:
    for feature in data.columns:
        missing_values_count=data[data[service]==True][feature].isna().sum()
        missing_values_total.loc[service,feature]=missing_values_count
        missing_values_percent.loc[service,feature]=missing_values_count/titles_count[service]

# calculate total amount of missing values for all data sets and add it to the
# corresponding dataframe
# total
missing_values_total.loc["total"]=[missing_values_total[feature].sum() for feature in missing_values_total.columns]
# ratio
missing_values_percent.loc["total"]=[missing_values_total.loc["total",feature]/titles_count["total"] for feature in missing_values_percent.columns]
missing_values_percent=missing_values_percent.astype(float).round(2)

#%%[markdown]
# Total amount of missing values for each data set.
#%%
missing_values_total
#%% [markdown]
# Ration of missing values in percent compared to number of titles in each dataset.
#%%
missing_values_percent
#%%[markdown]
# # Uniqueness
# No movie or TV show should appear in the data more than once