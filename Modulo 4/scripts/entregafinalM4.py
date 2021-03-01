#MODULO 4
#DataFrames 
import pandas as pd
numero = [10,20,10]
colores = ['Rojo','Verde','Azul']
datos = {"Número":numero,"Colores":colores}
df = pd.DataFrame(index = ['1','2','3'],data=datos)


#DataFrames parte 2
import pandas as pd
avengers = pd.read_csv('./data/pandas/avengers.csv')
avengers.head()
avengers.head(10)
avengers.tail()
avengers.shape
avengers_sorted = avengers.sort_values(by=['fecha_inicio'],ascending=False)
avengers_sorted.head()
avengers_sorted= avengers_sorted.reset_index(drop=True)
avengers_sorted.head()