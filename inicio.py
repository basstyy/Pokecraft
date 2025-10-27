# Importación necesaria
import streamlit as st

# Configuración básica de la página
st.set_page_config(
    page_title="PokéCraft: Asistente Estratégico de Tipos",
    page_icon="⚡️", # Ícono de rayo
    layout="wide",
)

pg = st.navigation(["Homepage.py", "Guia.py", "Contacto.py"])
pg.run()

# st.sidebar.success("Selecciona una página arriba.")
