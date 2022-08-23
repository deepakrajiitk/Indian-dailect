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
df2 = pd.DataFrame(columns=['state-code','3-to-2-ratio'])
df2[['state-code']] = df[['State-Code']]
df2['3-to-2-ratio'] = (df['Persons-atleast-3']/df['Persons-exactly-2'])


# %%
df2.head()


# %%
df2_top1 = df2.sort_values('3-to-2-ratio',ascending=False).head(3)
df2_worst1 = df2.sort_values('3-to-2-ratio').head(3)


# %%
result1 = df2_top1.append(df2_worst1)[['state-code','3-to-2-ratio']]


# %%
result1


# %%
result1.to_csv("3-to-2-ratio.csv",index = False)


