#Filtrado de DataFrames
import pandas as pd
airbnb = pd.read_csv("./data/pandas/airbnb.csv")
airbnb.head()
airbnbalicia=airbnb[(airbnb.accommodates==4) & (airbnb.reviews>=10) & (airbnb.overall_satisfaction>4) & (airbnb.bedrooms>1)]
airbnb_sorted = airbnbalicia.sort_values(by=['overall_satisfaction'],ascending=False)
airbnbordenado = airbnb_sorted.sort_values(by=['reviews'],ascending=False)
airbnbordenado.head(3)
airbnbroberto = airbnb[(airbnb.room_id==97503)]
airbnbali = airbnb[(airbnb.room_id==90387)]
airbnbroberto#identifiqué cada fila
airbnbali#identifiqué cada fila
airbnbcomparacion = airbnb.iloc[[41,48]]
airbnbcomparacion
airbnbcomparacion.to_excel('./roberto.xlsx',sheet_name="Comparacion",index=False)
airbnbdiana=airbnb[(airbnb.price<=50) & (airbnb.room_type=='Shared room')]
airbnb_dianasorted = airbnbdiana.sort_values(by=['price'],ascending=True)
airbnb_dianasorted.head(10)