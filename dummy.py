import pandas as pd

df = pd.read_csv("Dummydataset.csv")
date_list = df['Date'].unique()
death_date_data = {date:0 for date in date_list}
#print(death_date_data)
recovery_date_data = {date:0 for date in date_list}
#print(recovery_date_data)
for date,status in zip(df['Date'],df['Status']):
  if status == "Recovered":
    recovery_date_data[f'{date}']+=1
  else:
    death_date_data[f'{date}']+=1

first_ten = dict(list(recovery_date_data.items())[0: 10])
#print(first_ten)
last_ten = dict(list(recovery_date_data.items())[-10:])
#print(last_ten)
value1 = list(first_ten.values())
value2 = list(last_ten.values())
print(value1,value2)
recover= 0
death = 0
recover_value = 0
death_value = 0
for i in range(10):
    if(value1[i] > value2[i]):
        recover += 1
        recover_value += value1[i]
    else:
        death += 1
        death_value += value2[i]

calculate_recovery = (recover_value/death_value)*10
calculate_death = (death_value/recover_value)*10
print(recover_value,death_value)
#print(recover,death)
print("Based on the provided facts, a prediction of death or recovery for the coming several months\n\n")

if(recover>death):
    print("Recovery percentage : ",calculate_recovery,"%\n")
    print("If current trends continue,"
          "it is likely that the number of persons \nrecovering during the"
          "course of the upcoming month will rise, according to the information provided.")
else:
    print("Death percentage : ",calculate_death,"%\n")
    print("If current trends continue, it is likely that the number of \ndeaths will rise in the coming month, according to the statistics.")

for status,vxn in zip(df['Status'],df["Vaccination Status"]):
  if status == "Recovered":
      if vxn == "Vaccinated" :
        recovery_date_data[f'{date}']+=1
  else:
      if vxn == "Vaccinated":
        death_date_data[f'{date}']+=1

first_ten = dict(list(recovery_date_data.items())[0: 10])
#print(first_ten)
last_ten = dict(list(recovery_date_data.items())[-10:])
#print(last_ten)
value1 = list(first_ten.values())
#print(value1)
value2 = list(last_ten.values())
for i in range(10):
    if(value1[i] > value2[i]):
        recover += 1
        recover_value += value1[i]
    else:
        death += 1
        death_value += value1[i]
calculate_recovery = (recover_value/death_value)*10
calculate_death = (death_value/recover_value)*10
print(recover_value,death_value)
#print(recover,death)
print("\n\nReport on the effectiveness of the vaccine and a forecast of what would happen if it were to be used in the next months\n\n")
if(recover>death):
     print("Recovery percentage : ",calculate_recovery,"%\n")
     print("The reports indicate that the vaccination"
          "is quite effective, and\n if this trend continues, there is a probability that the"
          "\nnumber of patients who recover may rise in the days to come.")
else:
     print("Death percentage : ",calculate_death,"%\n")
     print("The reports indicate that the vaccine is ineffective, \nand there is a possibility that the number of deaths will rise in the days to come.")
