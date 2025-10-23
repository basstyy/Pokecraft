import streamlit as st

# Título de la sección
st.title("✉️ Contacto y Equipo de la Liga PokéCraft")
st.markdown("""
Agradecemos tu interés en **PokéCraft**. Este proyecto fue desarrollado 
para ayudar a los entrenadores en su aventura.
""")

st.markdown("---")

# Información del curso
st.header("Información de la Pokédex del Curso")
st.info("Proyecto de Desarrollo Web con Streamlit, utilizando Python para la estrategia de tipos.")
st.subheader("Curso: Informática, 3° Medio.")
st.subheader("Año: 2025")

st.markdown("---")

# Datos de los Integrantes (Reemplazar con datos reales)
st.header("Nuestro Equipo de Entrenadores")

# Uso de columnas para listar a los integrantes
col_integrante1, col_integrante2, col_integrante3 = st.columns(3)

with col_integrante1:
    st.subheader("Miembro 1 (Developer)")
    st.markdown("""
    - **Nombre:** Vicente Pizarro
    - **Rol:** Developer (Maestro Coder)
    - **Email:** V.pizarro@gmail.com
    """)
    st.image("planta.webp", caption="Developer", use_column_width=True)

with col_integrante2:
    st.subheader("Miembro 2 (Product Manager)")
    st.markdown("""
    - **Nombre:** Richard Ríos
    - **Rol:** Product Manager (Coordinador Pokémon)
    - **Email:** R.rios@gmail.com
    """)
    st.image("oak.webp", caption="Product Manager", use_column_width=True)

with col_integrante3:
    st.subheader("Miembro 3 (CEO)")
    st.markdown("""
    - **Nombre:** Carlos Palacios
    - **Rol:** CEO (Campeón de la Liga)
    - **Email:** C.palacios@gmail.com
    """)
    st.image("steven.webp", caption="CEO", use_column_width=True)
    
st.markdown("---")
st.markdown("### ¡Gracias por usar PokéCraft! ¡Atrápalos a todos! 🏆")