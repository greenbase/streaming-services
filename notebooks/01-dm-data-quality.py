# %% [markdown]
# # Data Quality
# In this notebook the data sets of the three streaming services will be validated in terms of data quality. The results will provide the necessary insights for subsequent analysis tasks. 
#
# Data quality will be assest in these steps: 
# - asses wether data sets are compatable with each other
# - Check data for missing values
#  

# %%
from numpy.core.fromnumeric import shape
import pandas as pd
import numpy as np

# %%
# Load data
netflix=pd.read_csv(r"D:\Portfolio\Projects\Streaming-Services\data\raw\netflix_titles.csv")
amazon=pd.read_csv(r"D:\Portfolio\Projects\Streaming-Services\data\raw\amazon_prime_titles.csv")
disney=pd.read_csv(r"D:\Portfolio\Projects\Streaming-Services\data\raw\disney_plus_titles.csv")
services={"netflix":netflix,"amazon":amazon,"disney":disney}

#%% [markdown]
# ## Data compatability
# In order to compare movies and TV shows from different streaming services each data set need to contain the same features.
#%%
assert all(netflix.columns==amazon.columns) & all(netflix.columns==disney.columns)
#%% [markdown]
# ## Check data for missing values
# ### Missing values per feature
# Total amount of missing values
#%%
missing_values_total=pd.DataFrame(index=["netflix","amazon","disney","total"],columns=netflix.columns)
missing_values_percent=missing_values
for service_name, service_df in zip(services.keys(),services.values()):
    titles_in_dataset_total=service_df.shape[0]
    for feature in netflix.columns: # columns are the same for all services
        missing_values_count=service_df[feature].isna().sum()
        # build df with total amount of missing values to dataframe
        missing_values_total.loc[service_name,feature]=missing_values_count
        # add ratio
        missing_values_percent.loc[service_name,feature]=missing_values_count/titles_in_dataset_total*100

# calculate total amount of missing values for all data sets
missing_values_total.loc["total"]=[missing_values_total[feature].sum() for feature in missing_values_total.columns]
titles_total=netflix.shape[0]+amazon.shape[0]+disney.shape[0]
missing_values_percent.loc["total"]=missing_values_total.loc["total"]/titles_total*100
missing_values_percent=missing_values_percent.astype(float).round(2)


missing_values_total
#%% [markdown]
# Ration of missing values in percent compared to number of titles in each dataset.

#%%
missing_values_percent
# %%
