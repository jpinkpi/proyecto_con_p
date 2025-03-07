import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv(r"C:\Users\josep\Downloads\vehicles_us.csv")
hist_button = st.button('Construir histograma') # crear un botón
        
        if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo