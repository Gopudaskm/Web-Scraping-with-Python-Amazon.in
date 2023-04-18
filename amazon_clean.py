import pandas as pd

df = pd.read_csv("Amazon_data1.csv")
df['MRP(Rs.)'] = pd.to_numeric(df['MRP(Rs.)'])
df['Price(Rs.)'] = pd.to_numeric(df['Price(Rs.)'])

for i in range(len(df)):   
    if 'Kilowatt Hours Per Year' in str(df.loc[i, 'Annual Energy Consumption']):
        df.loc[i, 'Annual Energy Consumption'] = df.loc[i, 'Annual Energy Consumption'].replace('Kilowatt Hours Per Year','kWh')
    elif 'Kilowatt Hours' in str(df.loc[i, 'Annual Energy Consumption']):
        df.loc[i, 'Annual Energy Consumption'] = df.loc[i, 'Annual Energy Consumption'].replace('Kilowatt Hours','kWh')
    elif 'Watts' in str(df.loc[i, 'Annual Energy Consumption']):
        df.loc[i, 'Annual Energy Consumption'] = str(round(float(((float(df.loc[i, 'Annual Energy Consumption'].replace('Watts','').strip())/1000)*365)),2))+ " kWh"
    elif 'Kilowatts' in str(df.loc[i, 'Annual Energy Consumption']):
        df.loc[i, 'Annual Energy Consumption'] = str(round(float((float(df.loc[i, 'Annual Energy Consumption'].replace('Kilowatts','').strip()))),2))+ " kWh"
    df.loc[i, 'Title'] = df.loc[i, 'Title'].replace('\"','')

df = df.dropna(how='any')
df.drop_duplicates(subset='Title', keep='first', inplace=True)
df.to_csv('Amazone_data2.csv', index=False)