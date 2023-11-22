import streamlit as st


st.title('Sistema de adquisición de datos para medición concurrente de celdas de carga')

st.image('img1.jpeg')

st.write("""\nEste sistema se desarrolló para medir y registrar la carga aplicada sobre distintos puntos mediante el uso de sensores.\n\nSe implementaron siete sensores de carga conectados a una tarjeta electrónica capaz de adquirir datos de múltiples canales simultáneamente. Cada sensor permite medir la fuerza ejercida de manera independiente.\n\nEl software controla la lectura concurrente de los siete sensores para capturar las mediciones de forma asíncrona. Esto garantiza que se obtengan valores actualizados de todos los puntos en cada instante, de manera simultánea.\n\nAdicionalmente, cuenta con funciones de calibración individual para cada sensor. Esto asegura la precisión de las mediciones teniendo en cuenta las características particulares de cada uno.\n\nEn tiempo real se visualizan los datos de carga mediante una interfaz sencilla. Por otro lado, la información queda registrada en una tarjeta de memoria para análisis posteriores.\n\nGracias a este sistema basado en múltiples sensores de carga, es posible evaluar la distribución de fuerzas sobre una superficie de estudio bajo diferentes condiciones. El registro simultáneo de los valores en cada punto aporta visibilidad sobre el comportamiento y dinámica del sistema a prueba.\n\nEn resumen, se trata de una solución integral para medir, visualizar y almacenar de forma asíncrona y concurrente la carga ejercida en distintos puntos, mediante el uso de varios sensores trabajando en paralelo.\n""")

