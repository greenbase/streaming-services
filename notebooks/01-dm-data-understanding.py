#%% [markdown]
# # Data Understanding
# 
#%%
ROOT=Path(__file__).parent.parent
# Load data
netflix_data=pd.read_csv(ROOT/"data"/"raw"/"netflix_titles.csv")
amazon_data=pd.read_csv(ROOT/"data"/"raw"/"amazon_prime_titles.csv")
disney_data=pd.read_csv(ROOT/"data"/"raw"/"disney_plus_titles.csv")
services=["netflix", "amazon","disney"]