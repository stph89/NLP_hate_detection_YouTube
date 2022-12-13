
![imagen](https://user-images.githubusercontent.com/110174766/207089375-bbf334fb-d93b-4225-9e99-58af79b217a0.png)

# Detector de mensajes tóxicos en comentarios de videos de Youtube

Generación de un modelo  entrenado de Machine Learning para la detección de mensajes de odio en comentarios de videos de Youtube.


Para generar los archivos necesarios para que el modelo realice la detección del mensaje de odio, es necesario correr el notebook `ver_toxico.ipynb`.De esta manera se generará el set de entrenamiento `X_train.pkl`, el vectorizador utilizado que está entrenado 
con nuestros data set `vectorizador.pkl` y finalmente el modelo entrenado con las mejores métricas: `modelo_entrenado.pkl`.

## Despliegue del modelo
El modelo se despliega en un dash de Streamlit, donde se puede introducir un comentario y el modelo nos predice si es Tóxico o no lo es.
Para cargar este despliegue se debe utilizar el siguiente comando: `streamlit run mi_odioso.py` desde la terminal de trabajo. 

![image](https://user-images.githubusercontent.com/108665441/207269025-f4e9c5e3-0500-4af2-b663-8b8071f333ad.png)

El despliegue se realizará en el localhost donde se podrá ingresar manualmente el comentario que quieres evaluar si es tóxico o no. 

![imagen](https://user-images.githubusercontent.com/110174766/207091093-7167c460-1512-4927-a6e2-37c0224362bc.png)


## Estructura de este repositorio

|  Fichero               |            Descripción                                                             |
|------------------------|------------------------------------------------------------------------------------|
| `toxico.ipynb`         | Notebook con análisis y preprocesamiento de texto para entrenamiento de modelos ML.|
| `toxico_web.ipynb`     | Despliegue en Streamlit del modelo de detección de mensajes de odio.               |
| `requirements.txt`     | Librerías y paquetes utilizados en este proyecto.                                  |

## Descargar este repositorio:
[GitHub Repositorio Equipo_Adverbio](https://github.com/Factoria-F5-AI-Bootcamp-1-Edicion/Equipo_Adverbio.git)

## Instalar todos los paquetes y librerias del fichero:
`requirements.txt`
