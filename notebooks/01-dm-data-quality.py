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
netflix_data=pd.read_csv(r"D:\Portfolio\Projects\Streaming-Services\data\raw\netflix_titles.csv")
amazon_data=pd.read_csv(r"D:\Portfolio\Projects\Streaming-Services\data\raw\amazon_prime_titles.csv")
disney_data=pd.read_csv(r"D:\Portfolio\Projects\Streaming-Services\data\raw\disney_plus_titles.csv")
data_set_collection={"netflix_data":netflix_data,"amazon_data":amazon_data,"disney_data":disney_data}

#%% [markdown]
# ## Data compatability
# In order to compare movies and TV shows from different streaming services each data set need to contain the same features.
#%%
assert all(netflix_data.columns==amazon_data.columns) & all(netflix_data.columns==disney_data.columns)
#%% [markdown]
# ## Check data for missing values
# ### Missing values per feature

# As the follwing dataframes show, there is a significant amount of data missing for the features "director", "country" and "date_added". Note that for the later two features the amazon_data data set provides nearly no data.
#
# For none of the features containing missing values it is avisable to fill them in, since there can not be made reasonable assumptions about them. Further more they should not be removed from the data set either, because the remaining data might still be usefull for certain analytics.
# Total amount of missing values
#%%
# instantiate missing value dataframes
missing_values_total=pd.DataFrame(index=["netflix_data","amazon_data","disney_data","total"],columns=netflix_data.columns)
missing_values_percent=missing_values_total.copy()

# compute missing values (tatal,ratio) for each data set
for service_name, service_df in zip(data_set_collection.keys(),data_set_collection.values()):
    titles_in_dataset_total=service_df.shape[0]
    for feature in netflix_data.columns: # columns are the same for all services
        missing_values_count=service_df[feature].isna().sum()
        # build df with total amount of missing values to dataframe
        missing_values_total.loc[service_name,feature]=missing_values_count
        # add ratio
        missing_values_percent.loc[service_name,feature]=missing_values_count/titles_in_dataset_total*100

# calculate total amount of missing values for all data sets and add it to the
# corresponding dataframe
# total
missing_values_total.loc["total"]=[missing_values_total[feature].sum() for feature in missing_values_total.columns]
# ratio
titles_total=netflix_data.shape[0]+amazon_data.shape[0]+disney_data.shape[0]
missing_values_percent.loc["total"]=missing_values_total.loc["total"]/titles_total*100
missing_values_percent=missing_values_percent.astype(float).round(2)

#%%[markdown]
# Total amount of missing values for each data set.
#%%
missing_values_total
#%% [markdown]
# Ration of missing values in percent compared to number of titles in each dataset.
#%%
missing_values_percent
