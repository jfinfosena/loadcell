import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Análisis de Datos de Celdas de Carga')

st.subheader('SISEMB SENA-TIC-Electrónica')
st.caption('Instructor Investigador: Jhon Fredy Valencia Gómez')
st.caption('Instructor Investigador: Hugo Alberto Santana')
st.divider()

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        registers = df.shape[0]

        st.subheader(str(registers)+ " Samples")        
                      
        st.caption("Load Cells")
        format_str = "{:.2f}"
        loadcell_data = {
            'time': df.loc[:, 'Time(us)'].apply(lambda x: format_str.format(x/1000000)),
            'LoadCell1': df.loc[:, 'LoadCell1'],
            'LoadCell2': df.loc[:, 'LoadCell2'],
            'LoadCell3': df.loc[:, 'LoadCell3'],
            'LoadCell4': df.loc[:, 'LoadCell4'], 
            'LoadCell5': df.loc[:, 'LoadCell5'],  
            'LoadCell6': df.loc[:, 'LoadCell6'],  
            'LoadCell7': df.loc[:, 'LoadCell7'],            
        }
        loadcells_df = pd.DataFrame(loadcell_data)        
        loadcells_df.set_index('time', inplace=True) 
       
        fig = px.line(loadcells_df)    
        st.plotly_chart(fig)        

        # Calculate load cell statistics
        stats = loadcells_df.agg(['min', 'max', 'mean'])

        # Display load cell statistics as a table
        st.header("Load Cell Statistics")
        st.dataframe(stats)
        
        st.header("Load Cell 1")
        loadcell_data = {
            'time': df.loc[:, 'Time(us)'],
            'LoadCell1': df.loc[:, 'LoadCell1']                        
        }
        loadcells_df = pd.DataFrame(loadcell_data)        
        loadcells_df.set_index('time', inplace=True)  
        fig = px.line(loadcells_df)    
        st.plotly_chart(fig)

        st.header("Load Cell 2")
        loadcell_data = {
            'time': df.loc[:, 'Time(us)'],
            'LoadCell2': df.loc[:, 'LoadCell2']                        
        }
        loadcells_df = pd.DataFrame(loadcell_data)        
        loadcells_df.set_index('time', inplace=True)  
        fig = px.line(loadcells_df)    
        st.plotly_chart(fig)

        st.header("Load Cell 3")
        loadcell_data = {
            'time': df.loc[:, 'Time(us)'],
            'LoadCell3': df.loc[:, 'LoadCell3']                        
        }
        loadcells_df = pd.DataFrame(loadcell_data)        
        loadcells_df.set_index('time', inplace=True)  
        fig = px.line(loadcells_df)    
        st.plotly_chart(fig)

        st.header("Load Cell 4")
        loadcell_data = {
            'time': df.loc[:, 'Time(us)'],
            'LoadCell4': df.loc[:, 'LoadCell4']                        
        }
        loadcells_df = pd.DataFrame(loadcell_data)        
        loadcells_df.set_index('time', inplace=True)  
        fig = px.line(loadcells_df)    
        st.plotly_chart(fig)

        st.header("Load Cell 5")
        loadcell_data = {
            'time': df.loc[:, 'Time(us)'],
            'LoadCell5': df.loc[:, 'LoadCell5']                        
        }
        loadcells_df = pd.DataFrame(loadcell_data)        
        loadcells_df.set_index('time', inplace=True)  
        fig = px.line(loadcells_df)    
        st.plotly_chart(fig)

        st.header("Load Cell 6")
        loadcell_data = {
            'time': df.loc[:, 'Time(us)'],
            'LoadCell6': df.loc[:, 'LoadCell6']                        
        }
        loadcells_df = pd.DataFrame(loadcell_data)        
        loadcells_df.set_index('time', inplace=True)   
        fig = px.line(loadcells_df)    
        st.plotly_chart(fig)

        st.header("Load Cell 7")
        loadcell_data = {
            'time': df.loc[:, 'Time(us)'],
            'LoadCell7': df.loc[:, 'LoadCell7']                        
        }
        loadcells_df = pd.DataFrame(loadcell_data)        
        loadcells_df.set_index('time', inplace=True)  
        fig = px.line(loadcells_df)    
        st.plotly_chart(fig)

        st.header("Data")
        st.markdown("<style> .dataframe { max-height: 200px; overflow: auto; } </style>", unsafe_allow_html=True)
        st.dataframe(df)       

    except Exception as e:
        st.error("Error: Unable to load CSV file. Please make sure it's a valid CSV file.")



