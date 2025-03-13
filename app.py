import streamlit as st
import pandas as pd
import plotly.express as px


def cargar_datos():
        df = pd.read_csv(r"C:\Users\josep\Downloads\vehicles_us.csv")
        df["model_year"].fillna(df["model_year"].median(), inplace=True)
        df["model_year"]= df["model_year"].astype("int")
        df["cylinders"].fillna(df["cylinders"].median(), inplace=True)
        df["cylinders"]= df["cylinders"].astype("int")
        df["odometer"].fillna(df["odometer"].median(), inplace=True)
        df["is_4wd"].fillna(0,inplace=True)
        df["is_4wd"]= df["is_4wd"].astype("boolean")
        df["paint_color"].fillna(df["paint_color"].mode()[0], inplace=True)
        df["paint_color"] = df["paint_color"].astype("category")
        return df 



st.header('Prueba del sprint 7')

st.write("""
**Sabías que** en nuestra empresa, AutoDrive Motors, nos enorgullece ofrecer a nuestros clientes no solo vehículos de alta calidad, sino también una experiencia de compra completamente transparente. 
Para reforzar nuestro compromiso con la confianza y la satisfacción del cliente, hemos decidido compartir con ustedes datos reales de las ventas realizadas durante los últimos meses.

Esta decisión se basa en la creencia de que la transparencia es clave para crear una relación sólida y confiable con nuestros compradores. 
Al mostrar cómo nuestras ventas reflejan las tendencias del mercado y las preferencias de los consumidores, queremos que todos tengan acceso a información precisa que les permita tomar decisiones informadas a la hora de adquirir su próximo automóvil.
""")

df = cargar_datos()

st.subheader("He aquí un breve ejemplo de nuestra base de datos utilizada")
st.write(df.head())



columna_hist = st.selectbox("Seleccionar una columna para hacer un histograma", ["price", "model_year", "cylinders", "odometer","days_listed"])
hist_button = st.button('Construir histograma') # crear un botón



fig_hist = px.histogram(df,x=columna_hist, title=f"Histograma de {columna_hist}")
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist)


#Creacion de un grafíco de dispersion entre  la Distribución de los  Precios por Cilindros
eje_x = st.selectbox("Seleccionar el eje X", ["price", "model_year", "cylinders", "odometer","days_listed"])
eje_y = st.selectbox("Seleccionar el eje y", ["price", "model_year", "cylinders", "odometer","days_listed"])

scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    fig = px.scatter(df, x=eje_x, y=eje_y, title=f"Dispersión de {eje_x} vs {eje_y}")
    fig.update_traces(marker=dict(color="crimson"))
    st.plotly_chart(fig)








      
     
