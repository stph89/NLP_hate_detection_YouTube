#importar librerías necesarias
import streamlit as st
import pickle
import pandas as pd

#Extraer el archivo pickle
with open('modelo_entrenado.pkl','rb') as met:
    modelo_entrenado=pickle.load(met)

#Función para clasificar el mensaje
def clasify(text):
    if text == 0:
        return'El mensaje no es tóxico'
    elif text == 1:
        return'El mensaje es tóxico'

#Método de entrada a nuestro script
def main():
    st.title("Predicción de Mensajes Tóxicos")
    st.header("Introduce tu texto")

if __name__=='__main__':
    main()