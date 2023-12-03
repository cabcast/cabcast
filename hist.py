import geopandas as gpd
cd = gpd.read_file('./public/Chicago.geojson')
dc
cd
cd
cd.columns
cd['id']
cd
import pandas as pd
df = pd.read_csv('/home/karthic/Downloads/FINAL.csv')
df
df = pd.read_csv('/home/karthic/Downloads/FINAL.csv', index_col='Unnamed: 0')
df
df['surge_multiplier'].describe()
df['pred_demand'].describe()
df['Hourly_Timestamp"]
df['Hourly_Timestamp']
df['Hourly_Timestamp'].min()
df['Hourly_Timestamp'].max()
df['Pickup_Community_Area'].describe()
len(df['Pickup_Community_Area'].unique())
df['Pickup_Community_Area'].describe()
df['cartodb_id']
import os
os.listdir('Public')
os.listdir('./public/')
nationaldf = pd.read_csv('./public/national_cd116.txt', delimiter='|')
nationaldf
nationaldf[national['STATE'] == 'IL']
nationaldf[nationaldf['STATE'] == 'IL']
socdf = pd.read_csv('/home/karthic/Downloads/Socio Economic data (2016-2020) - Sheet1.csv')
socdf
df1, df2 = socdf, cd
values_list = df1['Community Area'].unique()
filtered_df1 = df1[df1['Community Area'].isin(values_list)]
filtered_df2 = df2[df2['name'].isin(values_list)]
filtered_df1
filtered_df2
df1[~df1['Community Area'].isin(values_list)]
df1[~df1['Community Area'].isin(values_list)]
df2[~df2['Community Area'].isin(values_list)]
df2[~df2['name'].isin(values_list)]
df2[~df2['name'].isin(values_list)]
df1['Community Area']
df1['Community Area'].value_counts()
df1['Community Area'].value_counts().min()
df1['Community Area'].value_counts().max()
filtered_df1
filtered_df1.shape
filtered_df2
filtered_df1
filtered_df1.columns
df1
df1.columns
df
cd
filtered_df1
filtered_df2
filtered_df2.reset_index(drop=True)
filtered_df2.iloc[0]['geometry']
fdf = filtered_df2.iloc[0]['geometry']
fdf
fdf
filtered_df2
grouped_df = df.groupby(df['timestamp_column'].dt.hour)
grouped_df = df.groupby(df['updated_at'].dt.hour)
grouped_df = filtered_df2.groupby(filtered_df2['updated_at'].dt.hour)
filtered_df2
filtered_df2.columns
filtered_df2['updated_at']
filtered_df2['updated_at'].min()
filtered_df2['updated_at'].max()
filtered_df1
filtered_df1.columns
cd.columns
df
grouped_df = df.groupby(df['Hourly_Timestamp'].dt.hour)
df['Hourly_Timestamp']
df['Hourly_Timestamp'] = pd.to_datetime(df['Hourly_Timestamp'])
df['Hourly_Timestamp']
grouped_df = df.groupby(df['Hourly_Timestamp'].dt.hour)
grouped_df
for hour, group in grouped_df:
    print(hour)
    print(group)
    break
grouped_df = df.groupby(df['Hourly_Timestamp'].dt.date, df['Hourly_Timestamp'].dt.hour)
grouped_df = df.groupby([df['Hourly_Timestamp'].dt.date, df['Hourly_Timestamp'].dt.hour])
for hour, group in grouped_df:
    print(hour)
    print(group)
    break
group
df2
hour
df2[df2['updated_at'].dt.date == hour[0]]
df2
pd.to_datetime(df2['updated_at'])
df2['updated_at'] = pd.to_datetime(df2['updated_at'])
df2[df2['updated_at'].dt.date == hour[0]]
df2
filtered_df2
group
filtered_df2
filtered_df1
merged_df = filtered_df2.merge(filtered_df1[['Community Area', 'Community ID']], left_on='name', right_on='Community Area', how='left')
filtered_df2['Pickup_Community_Area'] = merged_df['Community ID']
filtered_df2.drop(columns=['Community Area'], inplace=True)
filtered_df1
filtered_df1['Community Area']
filtered_df1
filtered_df2
merged_df = filtered_df2.merge(filtered_df1[['Community Area', 'Community ID']], left_on='name', right_on='Community Area', how='left')
filtered_df2['Pickup_Community_Area'] = merged_df['Community ID']
filtered_df2.drop(columns=['Community Area'], inplace=True)
filtered_df2
filtered_df2[filtered_df2['Pickup_Community_Area'] == filtered_df2['Pickup_Community_Area']]
filtered_df2 = filtered_df2[filtered_df2['Pickup_Community_Area'] == filtered_df2['Pickup_Community_Area']]
filtered_df2['Pickup_Community_Area'] = filtered_df2['Pickup_Community_Area'].int()
filtered_df2['Pickup_Community_Area'] = filtered_df2['Pickup_Community_Area'].apply(int)
filtered_df2
filtered_df2.head()
def update_grp(group):
    filtered_df2['Pickup_Community_Area'] = filtered_df2['Pickup_Community_Area'].astype(int)
    group['Pickup_Community_Area'] = group['Pickup_Community_Area'].astype(int)
    group['pred_demand'] = group['pred_demand'].astype(int)
    merged_df = filtered_df2.merge(group[['Pickup_Community_Area', 'pred_demand']], on='Pickup_Community_Area', how='left')
    filtered_df2['cartodb_id'] = merged_df['pred_demand']
def update_grp(group):
    filtered_df2['Pickup_Community_Area'] = filtered_df2['Pickup_Community_Area'].astype(int)
    group['Pickup_Community_Area'] = group['Pickup_Community_Area'].astype(int)
    group['pred_demand'] = group['pred_demand'].astype(int)
    merged_df = filtered_df2.merge(group[['Pickup_Community_Area', 'pred_demand']], on='Pickup_Community_Area', how='left')
    filtered_df2['cartodb_id'] = merged_df['pred_demand']
    return filtered_df2, group
update_grp(group)
adf, bdf = _
adf
hour
gdp.to_file(f'public/Chicago_{hour[0].year[-2:]}_{hour[0].month.zfill(2)}_{hour[0].day.zfill(2)}_{hour[1].zfill(2)}.geojson')
gpd.to_file(f'public/Chicago_{hour[0].year[-2:]}_{hour[0].month.zfill(2)}_{hour[0].day.zfill(2)}_{hour[1].zfill(2)}.geojson')
adf.to_file(f'public/Chicago_{hour[0].year[-2:]}_{hour[0].month.zfill(2)}_{hour[0].day.zfill(2)}_{hour[1].zfill(2)}.geojson')
hour[1]
hour[0]
adf.to_file(f'public/Chicago_{hour[0].year[-2:]}_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[1]).zfill(2)}.geojson')
adf.to_file(f'public/Chicago_{str(hour[0].year)[-2:]}_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[1]).zfill(2)}.geojson')
for hour, group in grouped_df:
    adf, bdf = update_group(group)
    adf.to_file(f'public/Chicago_{hour[0].year[-2:]}_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[1]).zfill(2)}.geojson')
for hour, group in grouped_df:
    adf, bdf = update_grp(group)
    adf.to_file(f'public/Chicago_{hour[0].year[-2:]}_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[1]).zfill(2)}.geojson')
for hour, group in grouped_df:
    adf, bdf = update_grp(group)
    adf.to_file(f'public/Chicago_{str(hour[0].year)[-2:]}_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[1]).zfill(2)}.geojson')
for hour, group in grouped_df:
    adf, bdf = update_grp(group)
    adf.to_file(f'public/Chicago_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[0].year)[-2:]}_{str(hour[1]).zfill(2)}.geojson')
    break
for hour, group in grouped_df:
    adf, bdf = update_grp(group)
    adf.to_file(f'public/Chicago_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[0].year)[-2:]}_{str(hour[1]).zfill(2)}.geojson')
for hour, group in grouped_df:
    gj = f'public/Chicago_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[0].year)[-2:]}_{str(hour[1]).zfill(2)}.geojson'
    adf, bdf = update_grp(group)
    adf.to_file(gj)
for hour, group in grouped_df:
    if os.path.exists(gj):
        continue
    gj = f'public/Chicago_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[0].year)[-2:]}_{str(hour[1]).zfill(2)}.geojson'
    adf, bdf = update_grp(group)
    adf.to_file(gj)
grouped_df
for hour, group in grouped_df:
    gj = f'public/Chicago_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[0].year)[-2:]}_{str(hour[1]).zfill(2)}.geojson'
    if os.path.exists(gj):
        continue
    adf, bdf = update_grp(group)
    adf.to_file(gj)
for hour, group in grouped_df:
    gj = f'public/Chicago_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[0].year)[-2:]}_{str(hour[1]).zfill(2)}.geojson'
    if os.path.exists(gj):
        continue
    adf, bdf = update_grp(group)
    adf.to_file(gj)
def update_grp(group):
    gj = f'public/Chicago_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[0].year)[-2:]}_{str(hour[1]).zfill(2)}.geojson'
    if os.path.exists(gj):
        return (None, None)

    filtered_df2['Pickup_Community_Area'] = filtered_df2['Pickup_Community_Area'].astype(int)
    group['Pickup_Community_Area'] = group['Pickup_Community_Area'].astype(int)
    group['pred_demand'] = group['pred_demand'].astype(int)
    merged_df = filtered_df2.merge(group[['Pickup_Community_Area', 'pred_demand']], on='Pickup_Community_Area', how='left')
    filtered_df2['cartodb_id'] = merged_df['pred_demand']
    group.to_file(gj)
def update_grp(group):
    gj = f'public/Chicago_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[0].year)[-2:]}_{str(hour[1]).zfill(2)}.geojson'
    if os.path.exists(gj):
        return (None, None)

    filtered_df2['Pickup_Community_Area'] = filtered_df2['Pickup_Community_Area'].astype(int)
    group['Pickup_Community_Area'] = group['Pickup_Community_Area'].astype(int)
    group['pred_demand'] = group['pred_demand'].astype(int)
    merged_df = filtered_df2.merge(group[['Pickup_Community_Area', 'pred_demand']], on='Pickup_Community_Area', how='left')
    filtered_df2['cartodb_id'] = merged_df['pred_demand']
    group.to_file(gj)
def update_grp(filtered_df2, group):
    gj = f'public/Chicago_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[0].year)[-2:]}_{str(hour[1]).zfill(2)}.geojson'
    if os.path.exists(gj):
        return (None, None)

    filtered_df2['Pickup_Community_Area'] = filtered_df2['Pickup_Community_Area'].astype(int)
    group['Pickup_Community_Area'] = group['Pickup_Community_Area'].astype(int)
    group['pred_demand'] = group['pred_demand'].astype(int)
    merged_df = filtered_df2.merge(group[['Pickup_Community_Area', 'pred_demand']], on='Pickup_Community_Area', how='left')
    filtered_df2['cartodb_id'] = merged_df['pred_demand']
    group.to_file(gj)
import multiprocessing as mp
with mp.Pool(processes=mp.cpu_count) as pool:
    args = [(hour, group) for hour, group in grouped_df]
    pool.starmap(update_grp, args)
mp.cpu_count
mp.cpu_count()
with mp.Pool(processes=mp.cpu_count()) as pool:
    args = [(hour, group) for hour, group in grouped_df]
    pool.starmap(update_grp, args)
def update_grp(filtered_df2, group):
    gj = f'public/Chicago_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[0].year)[-2:]}_{str(hour[1]).zfill(2)}.geojson'
    print(gj)
    if os.path.exists(gj):
        return (None, None)

    filtered_df2['Pickup_Community_Area'] = filtered_df2['Pickup_Community_Area'].astype(int)
    group['Pickup_Community_Area'] = group['Pickup_Community_Area'].astype(int)
    group['pred_demand'] = group['pred_demand'].astype(int)
    merged_df = filtered_df2.merge(group[['Pickup_Community_Area', 'pred_demand']], on='Pickup_Community_Area', how='left')
    filtered_df2['cartodb_id'] = merged_df['pred_demand']
    group.to_file(gj)
with mp.Pool(processes=mp.cpu_count()) as pool:
    args = [(hour, group) for hour, group in grouped_df]
    pool.starmap(update_grp, args)
def update_grp(filtered_df2, hour, group):
    gj = f'public/Chicago_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[0].year)[-2:]}_{str(hour[1]).zfill(2)}.geojson'
    print(gj)
    if os.path.exists(gj):
        return (None, None)

    filtered_df2['Pickup_Community_Area'] = filtered_df2['Pickup_Community_Area'].astype(int)
    group['Pickup_Community_Area'] = group['Pickup_Community_Area'].astype(int)
    group['pred_demand'] = group['pred_demand'].astype(int)
    merged_df = filtered_df2.merge(group[['Pickup_Community_Area', 'pred_demand']], on='Pickup_Community_Area', how='left')
    filtered_df2['cartodb_id'] = merged_df['pred_demand']
    group.to_file(gj)
with mp.Pool(processes=mp.cpu_count()) as pool:
    args = [(filtered_df, hour, group) for hour, group in grouped_df]
    pool.starmap(update_grp, args)
with mp.Pool(processes=mp.cpu_count()) as pool:
    args = [(filtered_df2, hour, group) for hour, group in grouped_df]
    pool.starmap(update_grp, args)
filtered_df2
def update_grp(filtered_df2, hour, group):
    gj = f'public/Chicago_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[0].year)[-2:]}_{str(hour[1]).zfill(2)}.geojson'
    print(gj)
    if os.path.exists(gj):
        return (None, None)

    filtered_df2['Pickup_Community_Area'] = filtered_df2['Pickup_Community_Area'].astype(int)
    group['Pickup_Community_Area'] = group['Pickup_Community_Area'].astype(int)
    group['pred_demand'] = group['pred_demand'].astype(int)
    merged_df = filtered_df2.merge(group[['Pickup_Community_Area', 'pred_demand']], on='Pickup_Community_Area', how='left')
    filtered_df2['cartodb_id'] = merged_df['pred_demand']
    try:
        group.to_file(gj)
    except:
        print(f'cant write {gj}')
with mp.Pool(processes=mp.cpu_count()) as pool:
    args = [(filtered_df2, hour, group) for hour, group in grouped_df]
    pool.starmap(update_grp, args)
df1, df2 = socdf, cd
values_list = df1['Community Area'].unique()
filtered_df1 = df1[df1['Community Area'].isin(values_list)]
filtered_df2 = df2[df2['name'].isin(values_list)]
def update_grp(filtered_df2, hour, group):
    gj = f'public/Chicago_{str(hour[0].month).zfill(2)}_{str(hour[0].day).zfill(2)}_{str(hour[0].year)[-2:]}_{str(hour[1]).zfill(2)}.geojson'
    print(gj)
    if os.path.exists(gj):
        return (None, None)

    fdf2 = filtered_df2.copy()
    fdf2['Pickup_Community_Area'] = fdf2['Pickup_Community_Area'].astype(int)
    group['Pickup_Community_Area'] = group['Pickup_Community_Area'].astype(int)
    group['pred_demand'] = group['pred_demand'].astype(int)
    merged_df = fdf2.merge(group[['Pickup_Community_Area', 'pred_demand']], on='Pickup_Community_Area', how='left')
    fdf2['cartodb_id'] = merged_df['pred_demand']
    try:
        group.to_file(gj)
    except:
        print(f'cant write {gj}')
filtered_df2
filtered_df2 = filtered_df2[filtered_df2['Pickup_Community_Area'] == filtered_df2['Pickup_Community_Area']]
filtered_df2
merged_df = filtered_df2.merge(filtered_df1[['Community Area', 'Community ID']], left_on='name', right_on='Community Area', how='left')
filtered_df2['Pickup_Community_Area'] = merged_df['Community ID']
filtered_df2.drop(columns=['Community Area'], inplace=True)
filtered_df2
hist

