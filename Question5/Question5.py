# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Importing libraries

# %%
import pandas as pd

# %% [markdown]
# # Importing datasets

# %%
df = pd.read_csv("cleaned_datafile.csv")


# %%
df.head()

# %% [markdown]
# # Dropping irrelevant rows and columns

# %%
df = df[(df['TRU']=='Total')]
cols = ['State-Code','Tot-P','Age-Group','Persons-atleast-3']
df = df[cols]
df = df[df['Age-Group']!='Total']


# %%
df.head(10)

# %% [markdown]
# # Finding age-group that has highest percentage of people speaking 3 or more languages

# %%
df2 = pd.DataFrame(columns=['state-code','age-group','percentage'])
df2[['state-code','age-group']] = df[['State-Code','Age-Group']]
df2['percentage'] = (df['Persons-atleast-3']/df['Tot-P'])*100


# %%
df2.head()


# %%
idx = df2.groupby(['state-code'])['percentage'].transform(max) == df2['percentage']


# %%
result = df2.loc[idx]


# %%
result


# %%
result.to_csv("age-india.csv",index = False)


