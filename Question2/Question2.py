# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Importing libraries

# %%
import pandas as pd
from scipy.stats import ttest_ind

# %% [markdown]
# # Importing data files

# %%
df = pd.read_csv("cleaned_datafile.csv")


# %%
df.head()

# %% [markdown]
# # Removing irrelevant data and adding column names

# %%
df = df[(df['TRU']=='Total') & (df['Age-Group']=='Total')]
cols = ['State-Code','Name','Tot-M','Tot-F','Males-exactly-1','Females-exactly-1','Males-exactly-2','Females-exactly-2','Males-atleast-3','Females-atleast-3']
df = df[cols]


# %%
df.head()

# %% [markdown]
# # Finding required values
# %% [markdown]
# ## finding required values for people who can speak exactly one language

# %%
result1 = pd.DataFrame(columns=['state-code','male-percentage','female-percentage','p-value'])
result1[['state-code']] = df[['State-Code']]
result1['male-percentage'] = (df['Males-exactly-1']/df['Tot-M'])*100
result1['female-percentage'] = (df['Females-exactly-1']/df['Tot-F'])*100


# %%
r1=[]
r2=[]
for index, row in df.iterrows():
    a = row['Males-exactly-1']/row['Females-exactly-1']
    b = row['Males-exactly-2']/row['Females-exactly-2']
    c = row['Males-atleast-3']/row['Females-atleast-3']
    d = row['Tot-M']/row['Tot-F']
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
# ## finding required values for people who can speak exactly two language

# %%
result2 = pd.DataFrame(columns=['state-code','male-percentage','female-percentage','p-value'])
result2[['state-code']] = df[['State-Code']]
result2['male-percentage'] = (df['Males-exactly-2']/df['Tot-M'])*100
result2['female-percentage'] = (df['Females-exactly-2']/df['Tot-F'])*100


# %%
result2['p-value'] = p_value


# %%
result2.head()

# %% [markdown]
# ## finding required values for people who can speak at least 3 languages

# %%
result3 = pd.DataFrame(columns=['state-code','male-percentage','female-percentage','p-value'])
result3[['state-code']] = df[['State-Code']]
result3['male-percentage'] = (df['Males-atleast-3']/df['Tot-M'])*100
result3['female-percentage'] = (df['Females-atleast-3']/df['Tot-F'])*100


# %%
result3['p-value'] = p_value


# %%
result3.head()


# %%
result1.to_csv("gender-india-a.csv",index = False)
result2.to_csv("gender-india-b.csv",index = False)
result3.to_csv("gender-india-c.csv",index = False)


