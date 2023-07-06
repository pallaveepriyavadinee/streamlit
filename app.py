import streamlit as st 
import pandas as pd

st.title("Web app with Streamlit")
import plotly.express as px

st.write('# Avocado Prices dashboard')  #st.title('Avocado Prices dashboard')
st.markdown('''
This is a dashboard showing the *average prices* of different types of :avocado:  
Data source: [Kaggle](https://www.kaggle.com/datasets/timmate/avocado-prices-2020)
''')
st.header('Summary statistics')

st.header('Line chart by geographies')  
avocado = pd.read_csv('avocado-updated-2020.csv')
avocado_stats = avocado.groupby('type')['average_price'].mean()
top5_row = avocado.head()
st.dataframe(top5_row)
st.dataframe(avocado_stats)
#st.line_chart(avocado_stats)

with st.sidebar:
    st.subheader('About')
    st.markdown('here we can add something')
    
st.sidebar.image('https://streamlit.io/images/brand/streamlit-mark-color.png', width=50)
# Line chart by geographies
selected_geography = st.selectbox(label='Geography', options=avocado['geography'].unique())
submitted = st.button('Submit')
if submitted:
    filtered_avocado = avocado[avocado['geography'] == selected_geography]
    line_fig = px.line(filtered_avocado,
                       x='date', y='average_price',
                       color='type',
                       title=f'Avocado Prices in {selected_geography}')
    st.plotly_chart(line_fig)

