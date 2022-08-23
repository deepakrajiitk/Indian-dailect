# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Importing Libraries

# %%
import pandas as pd


# %%
group_1_files = ['DDW-C17-0100.CSV','DDW-C17-0200.CSV','DDW-C17-0300.CSV','DDW-C17-0400.CSV','DDW-C17-0500.CSV','DDW-C17-0600.CSV','DDW-C17-0700.CSV']
group_2_files = ['DDW-C17-0800.CSV','DDW-C17-2400.CSV','DDW-C17-2500.CSV','DDW-C17-2600.CSV','DDW-C17-2700.CSV','DDW-C17-3000.CSV']
group_3_files = ['DDW-C17-0900.CSV','DDW-C17-2200.CSV','DDW-C17-2300.CSV']
group_4_files = ['DDW-C17-1000.CSV','DDW-C17-1900.CSV','DDW-C17-2000.CSV','DDW-C17-2100.CSV']
group_5_files = ['DDW-C17-2800.CSV','DDW-C17-2900.CSV','DDW-C17-3100.CSV','DDW-C17-3200.CSV','DDW-C17-3300.CSV','DDW-C17-3400.CSV']
group_6_files = ['DDW-C17-1100.CSV','DDW-C17-1200.CSV','DDW-C17-1300.CSV','DDW-C17-1400.CSV','DDW-C17-1500.CSV','DDW-C17-1600.CSV','DDW-C17-1700.CSV','DDW-C17-1800.CSV','DDW-C17-3500.CSV']


# %%
groups_files = [group_1_files,group_2_files,group_3_files,group_4_files,group_5_files,group_6_files]


# %%
group = pd.DataFrame(columns=['State-Code','Name','Lang-1-Code','Lang-1-Name','Lang-1-Tot-P','Lang-1-Tot-M','Lang-1-Tot-F',
                'Lang-2-Code','Lang-2-Name','Lang-2-Tot-P','Lang-2-Tot-M','Lang-2-Tot-F',
                'Lang-3-Code','Lang-3-Name','Lang-3-Tot-P','Lang-3-Tot-M','Lang-3-Tot-F'])


# %%
df_groups = [group, group, group, group, group, group]

# %% [markdown]
# # Merging all the files of same group

# %%
for i in range(len(groups_files)):
    group_files = groups_files[i]
    for file in group_files:
        df = pd.read_csv(file)
        df = df.iloc[5:]
        df.columns = ['State-Code','Name','Lang-1-Code','Lang-1-Name','Lang-1-Tot-P','Lang-1-Tot-M','Lang-1-Tot-F',
                    'Lang-2-Code','Lang-2-Name','Lang-2-Tot-P','Lang-2-Tot-M','Lang-2-Tot-F',
                    'Lang-3-Code','Lang-3-Name','Lang-3-Tot-P','Lang-3-Tot-M','Lang-3-Tot-F']
        df_groups[i] = pd.concat([df_groups[i],df],axis=0)
    df_groups[i] = df_groups[i].sort_values('State-Code')
    df_groups[i].reset_index(drop=True,inplace=True)

    


# %%
df_groups[0]

# %% [markdown]
# # Finding top three languages using mother tongue

# %%
result1= pd.DataFrame(columns=['region','language-1','language-2','language-3'])
regions = ['North','West','Central','East','South','North-East']
for i in range(len(regions)):
    df = df_groups[i][['State-Code','Name','Lang-1-Code','Lang-1-Name','Lang-1-Tot-P']].dropna()
    df = df[['Lang-1-Name','Lang-1-Tot-P']]
    df = df.groupby('Lang-1-Name').sum().reset_index()
    df = df.sort_values('Lang-1-Tot-P',ascending=False)
    result1.loc[len(result1.index)] = [regions[i], df['Lang-1-Name'].iloc[0], df['Lang-1-Name'].iloc[1], df['Lang-1-Name'].iloc[2]] 
result1

# %% [markdown]
# # Finding top three language using language 1, 2 and 3

# %%
result2= pd.DataFrame(columns=['region','language-1','language-2','language-3'])
regions = ['North','West','Central','East','South','North-East']
for i in range(len(regions)):
    df = df_groups[i][['State-Code','Name','Lang-1-Code','Lang-1-Name','Lang-1-Tot-P','Lang-2-Name','Lang-2-Tot-P','Lang-3-Name','Lang-3-Tot-P']].drop_duplicates()
    df1 = df[['Lang-1-Name','Lang-1-Tot-P']].dropna()
    df1 = df1.groupby('Lang-1-Name').sum().reset_index()
    df1.columns = ['language','Total-P']

    df2 = df[['Lang-2-Name','Lang-2-Tot-P']].dropna()
    df2 = df2.groupby(['Lang-2-Name']).sum().reset_index()
    df2.columns = ['language','Total-P']

    
    df3 = df[['Lang-3-Name','Lang-3-Tot-P']].dropna()
    df3 = df3.groupby(['Lang-3-Name']).sum().reset_index()
    df3.columns = ['language','Total-P']

    df4 = pd.concat([df1,df2,df3],axis=0)
    df4 = df4.groupby('language').sum().reset_index()

    df4 = df4.sort_values('Total-P',ascending=False)
    result2.loc[len(result2.index)] = [regions[i], df4['language'].iloc[0], df4['language'].iloc[1], df4['language'].iloc[2]]

result2
    


# %%
result1.to_csv("region-india-a.csv",index=False)
result2.to_csv("region-india-b.csv",index=False)


