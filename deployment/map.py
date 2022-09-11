import folium
import matplotlib.pyplot as plt

def mapPlot(df):
    df = df[:800]
    map = folium.Map(location=[10.024736517586764, 76.30792709032183],zoom_start=15)

    recovered = folium.FeatureGroup(name="Recovered")
    death = folium.FeatureGroup(name="Death")

    for index,row in df.iterrows():
        tooltip = row['Name of Patient']
        popup = tooltip + "\n" + row['Gender'] + "\n" + row['Vaccination Status']
        if row['Status'] == 'Recovered':
            folium.Marker(location=[row['Latitude'],row['Longitude']],popup=popup,tooltip=tooltip,icon=folium.Icon(color="green")).add_to(recovered)
        else:
            folium.Marker(location=[row['Latitude'],row['Longitude']],popup=popup,tooltip=tooltip,icon=folium.Icon(color="red", icon="info-sign")).add_to(death)

    map.add_child(recovered)
    map.add_child(death)
    map.add_child(folium.map.LayerControl())
    map.save('Img/map-new.html')
    