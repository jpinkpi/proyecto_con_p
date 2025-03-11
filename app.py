import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Prueba del sprint 7')


df = pd.read_csv(r"C:\Users\josep\Downloads\vehicles_us.csv")
df.info()
print(df.sample(n=10))
df["model_year"].fillna(df["model_year"].median(), inplace=True)
df["model_year"]= df["model_year"].astype("int")
df["cylinders"].fillna(df["cylinders"].median(), inplace=True)
df["cylinders"]= df["cylinders"].astype("int")
df["odometer"].fillna(df["odometer"].median(), inplace=True)
df["is_4wd"].fillna(0,inplace=True)
df["is_4wd"]= df["is_4wd"].astype("boolean")
df["paint_color"].fillna(df["paint_color"].mode()[0], inplace=True)
df["paint_color"] = df["paint_color"].astype("category")

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(df, x="odometer", title="Histograma de Frecuencia del Kilometraje")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig)


#Creacion de un grafíco de dispersion entre  la Distribución de los  Precios por Cilindros
scatter_button = st.button("Construi un gráfico de dispersón")

if scatter_button:
    fig = px.scatter(data_frame=df, x="cylinders", y="price",title="Distribución del Precio por Cilindros")
    fig.update_traces(marker=dict(color="crimson"))
    st.plotly_chart(fig)

      
     
