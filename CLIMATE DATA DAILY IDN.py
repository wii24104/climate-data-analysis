# CLIMATE DATA DAILY IDN

import pandas as pd   

climate = pd.read_csv('Publish Github/Climate Data Daily IDN/climate_data.csv')   
print(climate.head()) 

climate.info()
climate.isnull().any()  
climate.isnull().sum()

# mengisi missing value dengan median disetiap kolomnya
num_cols = ['Tn','Tx','Tavg','RH_avg','RR','ss','ff_x','ddd_x','ff_avg']
for col in num_cols:
    climate[col] = climate[col].fillna(climate[col].median())
climate['ddd_car'] = climate['ddd_car'].fillna(climate['ddd_car'].mode()[0])
# Menghapus data duplikat
climate = climate.drop_duplicates()

# Analisis Data dan Mencari Insight
print ('\f Jumlah data curah hujan disetiap stasiun :\f', climate.groupby('station_id')['RR'].count().to_frame())

climate_data = climate.groupby('station_id').agg({
    'RR':'mean',
    'Tavg':'mean'
})
RRmax = climate_data.sort_values(by='RR', ascending=False).head()
print(RRmax)
Tavg_max = climate_data.sort_values(by='Tavg', ascending=False).head()
print("\nTop 5 suhu tertinggi:")
print(Tavg_max)

print("\n5 stasiun dengan curah hujan tertinggi:")
print(RRmax)
print("\nInsight:")
print("Stasiun dengan curah hujan rata-rata tertinggi adalah:", RRmax.index[0])
print("Dengan nilai:", RRmax['RR'].iloc[0])
print("Rata-rata curah hujan seluruh stasiun:", climate['RR'].mean())