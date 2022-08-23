# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Importing libraries

# %%
import pandas as pd
from scipy.stats import ttest_ind

# %% [markdown]
# # Importing datasets

# %%
df = pd.read_csv("cleaned_datafile.csv")


# %%
df.head()

# %% [markdown]
# # Dropping irrelevant rows and columns

# %%
df = df[(df['Age-Group']=='Total')]
cols = ['State-Code','TRU','Tot-P','Persons-exactly-1','Persons-exactly-2','Persons-atleast-3']
df = df[cols]


# %%
df.head()


# %%
df_rural = df[df['TRU']=='Rural'].reset_index(drop = True)
df_urban = df[df['TRU']=='Urban'].reset_index(drop = True)

# %% [markdown]
# ## finding results for people who can speak exactly one language

# %%
result1 = pd.DataFrame(columns=['state-code','urban-percentage','rural-percentage','p-value'])
result1[['state-code']] = df_rural[['State-Code']]
result1['urban-percentage'] = (df_urban['Persons-exactly-1']/df_urban['Tot-P'])*100
result1['rural-percentage'] = (df_rural['Persons-exactly-1']/df_rural['Tot-P'])*100


# %%
r1=[]
r2=[]
for i in range(36):
    a = df_rural.iloc[i]['Persons-exactly-1']/df_urban.iloc[i]['Persons-exactly-1']
    b = df_rural.iloc[i]['Persons-exactly-2']/df_urban.iloc[i]['Persons-exactly-2']
    c = df_rural.iloc[i]['Persons-atleast-3']/df_urban.iloc[i]['Persons-atleast-3']
    d = df_rural.iloc[i]['Tot-P']/df_urban.iloc[i]['Tot-P']
    r1.append([a,b,c])
    r2.append([d,d,d])


# %%
p_value = []
for x,y in zip(r1,r2):
    p_value.append(ttest_ind(x,y,equal_var=False).pvalue)


# %%
result1['p-value'] = p_value


# %%
result1.head()

# %% [markdown]
# ## finding results for people who can speak exactly two language

# %%
result2 = pd.DataFrame(columns=['state-code','urban-percentage','rural-percentage','p-value'])
result2[['state-code']] = df_rural[['State-Code']]
result2['urban-percentage'] = (df_urban['Persons-exactly-2']/df_urban['Tot-P'])*100
result2['rural-percentage'] = (df_rural['Persons-exactly-2']/df_rural['Tot-P'])*100
result2['p-value'] = p_value


# %%
result2.head()

# %% [markdown]
# ## finding results for people who can speak atleast 3 language

# %%
result3 = pd.DataFrame(columns=['state-code','urban-percentage','rural-percentage','p-value'])
result3[['state-code']] = df_rural[['State-Code']]
result3['urban-percentage'] = (df_urban['Persons-atleast-3']/df_urban['Tot-P'])*100
result3['rural-percentage'] = (df_rural['Persons-atleast-3']/df_rural['Tot-P'])*100
result3['p-value'] = p_value


# %%
result3.head()


# %%
result1.to_csv("geography-india-a.csv",index = False)
result2.to_csv("geography-india-b.csv",index = False)
result3.to_csv("geography-india-c.csv",index = False)


