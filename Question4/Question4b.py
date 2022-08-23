# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Importing Libraries

# %%
import pandas as pd


# %%
df = pd.read_csv("cleaned_datafile.csv")


# %%
df.head()

# %% [markdown]
# # Dropping irrelevant rows and columns

# %%
df = df[(df['TRU']=='Total') & (df['Age-Group']=='Total')]
cols = ['State-Code','Persons-exactly-1','Persons-exactly-2','Persons-atleast-3']
df = df[cols]


# %%
df.head()

# %% [markdown]
# # Finding required ratios

# %%
df2 = pd.DataFrame(columns=['state-code','2-to-1-ratio'])
df2[['state-code']] = df[['State-Code']]
df2['2-to-1-ratio'] = (df['Persons-exactly-2']/df['Persons-exactly-1'])


# %%
df2.head()


# %%
df2_top2 = df2.sort_values('2-to-1-ratio',ascending=False).head(3)
df2_worst2 = df2.sort_values('2-to-1-ratio').head(3)


# %%
result2 = df2_top2.append(df2_worst2)[['state-code','2-to-1-ratio']]


# %%
result2


# %%
result2.to_csv("2-to-1-ratio.csv",index = False)


