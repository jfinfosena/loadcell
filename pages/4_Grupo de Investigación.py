import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Semillero de Investigación SISEMB")
st.header("SENA-TIC-Electrónica")




st.divider()
st.header('Jaime Alberto Jaramillo Carvalho')

with st.container():
    col1,col2=st.columns(2)
    col1.write('')
    col1.write('')
    col1.write('')   
    col1.write('**Cargo:**    Dinamizador SENNOVA.')   
    col1.write('**Función:**    Lider del proyecto')
    col1.write('**Contacto:**    jjaramilloc@sena.edu.co')    
    col2.image('jaime.png')


st.divider()
st.header('Jhon Fredy valencia Gómez')

with st.container():
    col1,col2=st.columns(2)
    col1.write('')
    col1.write('')
    col1.write('')   
    col1.write('**Cargo:**    Instructor Investigador')   
    col1.write('**Función:**    Diseño y desarrollo de software, firmware y hardware.')
    col1.write('**Contacto:**    jfvalenciag@sena.edu.co')    
    col2.image('fredy.png')

st.divider()
st.header('Hugo Alberto Santana')

with st.container():
    col1,col2=st.columns(2)
    col1.write('')
    col1.write('')
    col1.write('')    
    col1.write('**Cargo:**    Instructor Investigador')   
    col1.write('**Función:**    Diseño y desarrollo firmware y hardware.')
    col1.write('**Contacto:**    jfvalenciag@sena.edu.co')    
    col2.image('hugo.png')


st.divider()
st.title('Sebastián Tobón Tobón')

with st.container():
    col1,col2=st.columns(2)
    col1.write('')
    col1.write('')
    col1.write('')    
    col1.write('**Cargo:**    Investigador')   
    col1.write('**Función:**    Diseño y desarrollo mecanico y 3D.')
    col1.write('**Contacto:**    jfvalenciag@sena.edu.co')    
    col2.image('sebastian.png')