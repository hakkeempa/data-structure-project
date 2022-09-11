import matplotlib.pyplot as plt

def vaccinationPlot(df):
    key_counts = {}
    key_counts1 = {}
    key_counts['Vaccinated_recovered'] = 0 
    key_counts['Not_Vaccinated_recovered'] = 0
    key_counts1['Vaccinated_death'] = 0
    key_counts1['Not_Vaccinated_death'] = 0

    sizes = []
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
    plt.title("Recovery based on Vaccination Status")
    ax1.pie(sizes, colors=['#00FFFF','#BF3EFF'], autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.tight_layout()
    plt.legend(["Vaccinated","Not_Vaccinated"])
    plt.savefig('Img/vaccinated-recover',dpi=400)
    plt.show()

    sizes = []

    for key,value in key_counts1.items():
        print(key.upper()," : ",value)
        sizes.append(value)
    print(sizes)

    fig1, ax1 = plt.subplots()
    plt.title("Death based on Vaccination Status")
    ax1.pie(sizes, colors=['#EEEE00','#FF1493'], autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.tight_layout()
    plt.legend(["Vaccinated","Not_Vaccinated"])
    plt.savefig('Img/vaccinated-death.png',dpi=400)
    plt.show()