import pandas as pd
import numpy
import matplotlib.pyplot as plt

df = pd.read_csv("covidDataset.csv")
sizes = []

df = pd.read_csv("covidDataset.csv")

key_counts = {}
key_counts1 = {}
key_counts['Vaccinated_recovered'] = 0 
key_counts['Not_Vaccinated_recovered'] = 0
key_counts1['Vaccinated_death'] = 0
key_counts1['Not_Vaccinated_death'] = 0

for Vaccination,status in zip(df['Vaccination Status'],df['Status']):
  if Vaccination == 'Vaccinated':
    if status == 'Recovered':
      key_counts['Vaccinated_recovered'] += 1
    else:
      key_counts1['Vaccinated_death'] += 1
  else :
    if status == 'Recovered':
      key_counts['Not_Vaccinated_recovered'] += 1
    else:
      key_counts1['Not_Vaccinated_death'] += 1

for key,value in key_counts.items():
  print(key.upper()," : ",value)
  sizes.append(value)
print(sizes)

fig1, ax1 = plt.subplots()
plt.title("Recovery pie plot based on Vaccination Status")
ax1.pie(sizes, colors=['#00FFFF','#BF3EFF'], autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.tight_layout()
plt.legend(["Vaccinated","Not_Vaccinated"])

sizes = []

for key,value in key_counts1.items():
  print(key.upper()," : ",value)
  sizes.append(value)
print(sizes)

fig1, ax1 = plt.subplots()
plt.title("Death pie plot based on Vaccination Status")
ax1.pie(sizes, colors=['#EEEE00','#FF1493'], autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.tight_layout()
plt.legend(["Vaccinated","Not_Vaccinated"])

plt.show()
