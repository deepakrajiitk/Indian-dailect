# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Importing libraries

# %%
import pandas as pd

# %% [markdown]
# # Importing datasets

# %%
df = pd.read_csv("cleaned_datafile2.csv")


# %%
df.head(10)

# %% [markdown]
# # Dropping irrelevant columns and rows

# %%
df3 = df[(df['TRU']=='Total')]
cols = ['State-Code','Name','Education-Level','Tot-M','Tot-F','Males-atleast-3','Females-atleast-3']
df3 = df3[cols]
df3 = df3[df3['Education-Level']!='Total']


# %%
df3.head(10)

# %% [markdown]
# # finding literacy group for males that has the highest ratio of population that can speak 3 or more languages

# %%
df_male3 = pd.DataFrame(columns=['State-Code','Name','Male-Education-Level','males-ratio-of-3'])
df_male3[['State-Code','Name','Male-Education-Level']] = df3[['State-Code','Name','Education-Level']]
df_male3['males-ratio-of-3'] = (df3['Males-atleast-3']/df3['Tot-M'])


# %%
df_male3.head()


# %%
idx = df_male3.groupby(['Name'])['males-ratio-of-3'].transform(max) == df_male3['males-ratio-of-3']


# %%
result_male3 = df_male3.loc[idx].reset_index(drop=True)


# %%
result_male3

# %% [markdown]
# # finding literacy group for females that has the highest ratio of population that can speak 3 or more languages

# %%
df_female3 = pd.DataFrame(columns=['State-Code','Name','Female-Education-Level','females-ratio-of-3'])
df_female3[['State-Code','Name','Female-Education-Level']] = df3[['State-Code','Name','Education-Level']]
df_female3['females-ratio-of-3'] = (df3['Females-atleast-3']/df3['Tot-F'])


# %%
df_female3.head()


# %%
idx = df_female3.groupby(['Name'])['females-ratio-of-3'].transform(max) == df_female3['females-ratio-of-3']


# %%
result_female3 = df_female3.loc[idx].reset_index(drop=True)


# %%
result_female3

# %% [markdown]
# # Combinig male and female result dataframes

# %%
result3 = result_male3
result3[['Female-Education-Level','Females-ratio-of-3']] = result_female3[['Female-Education-Level','females-ratio-of-3']]


# %%
result3

# %% [markdown]
# # finding literacy group for males that has the highest ratio of population that can speak 2 languages

# %%
df2 = df[(df['TRU']=='Total')]
cols = ['State-Code','Name','Education-Level','Tot-M','Tot-F','Males-exactly-2','Females-exactly-2']
df2 = df2[cols]
df2 = df2[df2['Education-Level']!='Total']


# %%
df2.head()


# %%
df_male2 = pd.DataFrame(columns=['State-Code','Name','Male-Education-Level','Males-ratio-of-2'])
df_male2[['State-Code','Name','Male-Education-Level']] = df2[['State-Code','Name','Education-Level']]
df_male2['Males-ratio-of-2'] = (df2['Males-exactly-2']/df2['Tot-M'])


# %%
df_male2.head()


# %%
idx = df_male2.groupby(['Name'])['Males-ratio-of-2'].transform(max) == df_male2['Males-ratio-of-2']


# %%
result_male2 = df_male2[idx].reset_index(drop=True)


# %%
result_male2

# %% [markdown]
# # finding literacy group for females that has the highest ratio of population that can speak 2 languages

# %%
df_female2 = pd.DataFrame(columns=['State-Code','Name','Female-Education-Level','Females-ratio-of-2'])
df_female2[['State-Code','Name','Female-Education-Level']] = df2[['State-Code','Name','Education-Level']]
df_female2['Females-ratio-of-2'] = (df2['Females-exactly-2']/df2['Tot-F'])


# %%
df_female2.head()


# %%
idx = df_female2.groupby(['Name'])['Females-ratio-of-2'].transform(max) == df_female2['Females-ratio-of-2']


# %%
result_female2 = df_female2[idx].reset_index(drop=True)


# %%
result_female2

# %% [markdown]
# # Combining male and femal result dataframes

# %%
result2 = result_male2
result2[['Female-Education-Level','Females-ratio-of-2']] = result_female2[['Female-Education-Level','Females-ratio-of-2']]


# %%
result2

# %% [markdown]
# # finding literacy group for males that has the highest ratio of population that can speak only 1 language

# %%
df1 = df[(df['TRU']=='Total')]
cols = ['State-Code','Name','Education-Level','Tot-M','Tot-F','Males-exactly-1','Females-exactly-1']
df1 = df1[cols]
df1 = df1[df1['Education-Level']!='Total']


# %%
df1.head()


# %%
df_male1 = pd.DataFrame(columns=['State-Code','Name','Male-Education-Level','Males-ratio-of-1'])
df_male1[['State-Code','Name','Male-Education-Level']] = df1[['State-Code','Name','Education-Level']]
df_male1['Males-ratio-of-1'] = (df1['Males-exactly-1']/df1['Tot-M'])


# %%
df_male1.head()


# %%
idx = df_male1.groupby(['Name'])['Males-ratio-of-1'].transform(max) == df_male1['Males-ratio-of-1']


# %%
result_male1 = df_male1[idx].reset_index(drop=True)


# %%
result_male1

# %% [markdown]
# # finding literacy group for females that has the highest ratio of population that can speak 2 languages

# %%
df_female1 = pd.DataFrame(columns=['State-Code','Name','Female-Education-Level','Females-ratio-of-1'])
df_female1[['State-Code','Name','Female-Education-Level']] = df1[['State-Code','Name','Education-Level']]
df_female1['Females-ratio-of-1'] = (df1['Females-exactly-1']/df1['Tot-F'])


# %%
df_female1.head()


# %%
idx = df_female1.groupby(['Name'])['Females-ratio-of-1'].transform(max) == df_female1['Females-ratio-of-1']


# %%
result_female1 = df_female1[idx].reset_index(drop=True)


# %%
result_female1

# %% [markdown]
# # Combining male and female result dataframes

# %%
result1 = result_male1
result1[['Female-Education-Level','Females-ratio-of-1']] = result_female1[['Female-Education-Level','Females-ratio-of-1']]


# %%
result1


# %%
result1.drop('Name',inplace=True, axis=1)
result2.drop('Name',axis=1,inplace=True)
result3.drop('Name',inplace=True, axis=1)
result1.columns = ['state/ut', 'literacy-group-males', 'ratio-males','literacy-group-females', 'ratio-females']
result2.columns = ['state/ut', 'literacy-group-males', 'ratio-males','literacy-group-females', 'ratio-females']
result3.columns = ['state/ut', 'literacy-group-males', 'ratio-males','literacy-group-females', 'ratio-females']


# %%
result1.to_csv("literacy-gender-c.csv",index=False)
result2.to_csv("literacy-gender-b.csv",index=False)
result3.to_csv("literacy-gender-a.csv",index=False)


