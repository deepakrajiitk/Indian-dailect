# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Importing Libraries

# %%
import pandas as pd

# %% [markdown]
# # Importing Datasets

# %%
df = pd.read_csv("cleaned_datafile.csv")


# %%
df.head()

# %% [markdown]
# # Droping irrelevant columns

# %%
df = df[(df['TRU']=='Total') & (df['Age-Group']=='Total')]
cols = ['State-Code','Name','Tot-P','Persons-exactly-1','Persons-exactly-2','Persons-atleast-3']
df = df[cols]


# %%
df.head()

# %% [markdown]
# # Finding required percentages

# %%
result = pd.DataFrame(columns=['State-Code','Name','exactly-1-percentage','exactly-2-percentage','atleast-3-percentage'])
result[['State-Code','Name']] = df[['State-Code','Name']]
result['exactly-1-percentage'] = (df['Persons-exactly-1']/df['Tot-P'])*100
result['exactly-2-percentage'] = (df['Persons-exactly-2']/df['Tot-P'])*100
result['atleast-3-percentage'] = (df['Persons-atleast-3']/df['Tot-P'])*100


# %%
result.drop('Name',axis=1,inplace=True)
result.columns = ['state-code','percent-one','percent-two','percent-three']
result.head()


# %%
result.to_csv("percent-india.csv",index = False)


