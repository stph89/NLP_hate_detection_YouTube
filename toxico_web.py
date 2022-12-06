#importar librerías necesarias
import streamlit as st
import pickle
import pandas as pd
import pickle 
from pickle import dump
from pickle import load
#from streamlit_option_menu import option_menu
import joblib

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
    st.title("Predicción de mensajes de odio en la plataforma YouTube")
    st.text_input('INTRODUCE EL COMENTARIO QUE QUIERES EVALUAR')
    st.text_input('ESTE COMENTARIO ES: ')
button = st.button('Predict')   

input_dict = []
input_df = pd.DataFrame(input_dict, index=[0]) 

# if button:
#         st.write(input_df)
      
#         carga_transformer = pickle.load(open('modelo_entrenado.pkl' , 'rb'))
      
#         carga_modelo = pickle.load(open('modelo_entrenado.pkl', 'rb'))
#         transformer = carga_transformer
#         modelo = carga_modelo
#         df = transformer.transform(input_df)
#         st.write(df)
#         predict=modelo.predict(df)
        
#         result = (predict) 
     
#         st.success('el resultado de su prueba es:  {}'.format(result))    
list_variables_predictoras = ['Toxico']

columns = ['Toxico']

X_valid = []
X_valid = pd.DataFrame(list_variables_predictoras, columns=columns)

## Matrix. Transformacion variables predictoras
X_valid
print(X_valid)

#limpieza "funcion" (variable)
load_transformer = pickle.load(open('transformer.pkl', 'rb'))
load_modelo = pickle.load(open('filename.pkl', 'rb'))


transformer = load_transformer
model = load_modelo


X_valid = transformer.transform(X_valid)

predict = model.predict(X_valid)

st.write(f"Estaría: {predict}")


if __name__=='__main__':
    main()