import matplotlib.pyplot as plt


def barGraph(df):
    date_list = df['Date'].unique()
    death_date_data = {date:0 for date in date_list}
    recovery_date_data = {date:0 for date in date_list}

    for date,status in zip(df['Date'],df['Status']):
        if status == "Recovered":
            recovery_date_data[f'{date}']+=1
        else:
            death_date_data[f'{date}']+=1

    li = (recovery_date_data.items())
    li2 = (death_date_data.items())
    x,y = zip(*li)

    x1,y1 = zip(*li2)
    plt.figure(figsize=[14,8])
    # plt.style.use('dark_background')
    plt.title(f"Covid - 19 | Daily Status from {date_list[0]} to {date_list[-1]}")
    plt.plot(x,y,marker='o',label="Recovery",color='#048004')
    plt.plot(x1,y1,marker='o',label="Death",color='#FF3333')
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()
    plt.savefig('Img/bar.png',dpi=400)
    # plt.show()