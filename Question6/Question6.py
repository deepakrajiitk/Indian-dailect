# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Importing Libraries

# %%
import pandas as pd

# %% [markdown]
# # Importing libraries

# %%
df = pd.read_csv("cleaned_datafile2.csv")


# %%
df.head()

# %% [markdown]
# # Dropping irrelevant rows and columns

# %%
df = df[(df['TRU']=='Total')]
cols = ['State-Code','Name','Tot-P','Education-Level','Persons-atleast-3']
df = df[cols]
df = df[df['Education-Level']!='Total']


# %%
df.head()

# %% [markdown]
# # Finding literacy group that has highest percentage of speaking 3 or more languages

# %%
df2 = pd.DataFrame(columns=['state-code','education-level','percentage'])
df2[['state-code','education-level']] = df[['State-Code','Education-Level']]
df2['percentage'] = (df['Persons-atleast-3']/df['Tot-P'])*100


# %%
df2.head(10)


# %%
idx = df2.groupby(['state-code'])['percentage'].transform(max) == df2['percentage']


# %%
result = df2.loc[idx]


# %%
result


# %%
result.to_csv("literacy-india.csv",index=False)


