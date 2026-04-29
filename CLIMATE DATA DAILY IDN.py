# CLIMATE DATA DAILY IDN

import pandas as pd   
import matplotlib.pyplot as plt
import seaborn as sns

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

# Visualisasi
RRmax.plot(kind='bar')
plt.title('Top 5 Stasiun dengan Curah Hujan Tertinggi')
plt.xlabel('Station ID')
plt.ylabel('Rata-rata Curah Hujan (mm)')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()
sns.histplot(climate[climate['RR'] < 50]['RR'], kde=True)
plt.title('Distribusi Curah Hujan Harian (<50 mm)')
plt.xlabel('Curah Hujan (mm)')
plt.ylabel('Frekuensi')
plt.show()
climate['date'] = pd.to_datetime(climate['date'], dayfirst=True)
climate['year'] = climate['date'].dt.year

year_temp = climate.groupby('year')['Tavg'].mean()

year_temp.plot()
plt.title('Rata-rata Suhu Tahunan di Indonesia')
plt.xlabel('Tahun')
plt.ylabel('Suhu (°C)')
plt.grid()
plt.show()

print("\n5 stasiun dengan curah hujan tertinggi:")
print(RRmax)
print("\nInsight:")
print("Stasiun dengan curah hujan rata-rata tertinggi adalah:", RRmax.index[0])
print("Dengan nilai:", RRmax['RR'].iloc[0])
print("Rata-rata curah hujan seluruh stasiun:", climate['RR'].mean())

