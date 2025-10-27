# Importaciones necesarias
import streamlit as st
import pandas as pd

# --- Configuración y Nombre de Fantasía ---
APP_NAME = "PokéCraft"

# Configuración de la página
st.title(f"✨ ¡Bienvenido a {APP_NAME}! ⚡️")
st.markdown("---")

# --- Problema a Resolver ---
st.header("1. El Problema a Resolver: La Confusión de Tipos")
st.markdown("""
En el mundo Pokémon, la clave de la victoria está en el conocimiento de los **tipos** y sus interacciones. 
Muchos entrenadores, especialmente los nuevos, se confunden con la tabla de tipos: ¿Es Fuego súper efectivo contra Acero? ¿Qué pasa con los tipos Hada?

El problema central es: **¿Cómo puedo determinar rápidamente los mejores tipos para contrarrestar a un oponente específico y construir un equipo equilibrado?**
""")
st.image("combate.jpeg", caption="Ilustración de un desafío de tipos en combate.", use_container_width=True)

st.markdown("---")

# --- Usuario Objetivo y sus Características ---
st.header("2. Nuestro Usuario Objetivo: El Entrenador Estratégico")

# Uso de columnas para organizar la información del usuario
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("#### **Ficha del Entrenador**")
    st.image("entrenador.png", caption="Entrenador Típico", use_container_width=True)
    
with col2:
    st.markdown("""
    - **Edad:** 8 a 17 años (fanáticos de Pokémon y videojugadores).
    - **Ubicación:** Jugadores de juegos de consola, cartas o aplicaciones móviles de Pokémon.
    - **Estilo de Vida:** Buscan mejorar en las batallas, entender la estrategia detrás de los tipos y ganar ligas.
    - **Necesidad Clave:** Necesitan una herramienta simple para verificar debilidades y fortalezas complejas sin memorizar toda la tabla de tipos.

    **Su reto:** Superar a los líderes de gimnasio y a sus amigos con estrategias de tipo superiores.
    """)

st.markdown("---")

# --- Cómo PokéCraft Resuelve el Problema ---
st.header("3. La Solución: PokéCraft, Tu Guía de Combate")

st.info("""
**PokéCraft** resuelve este problema actuando como una **Calculadora de Debilidades y Fortalezas**. 

En lugar de revisar tablas complejas, el usuario:
1. **Selecciona** el **Tipo del Oponente** que quiere vencer (ej. Tipo Roca).
2. **Define** la **Estrategia** (ej. Encontrar todos los tipos que son Súper Efectivos).
3. **Muestra instantáneamente** qué tipos usar para el ataque o para la defensa, transformando la confusión en conocimiento estratégico.
""")

# --- Ejemplo de Archivo Multimedia Adicional ---
st.subheader("¡Mira cómo funciona conceptualmente!")
# Simulación de un video explicativo
st.video("https://www.youtube.com/watch?v=KrvA0fznXGM")
st.caption("Explicación simple de la tabla de tipos de pokémon")

st.markdown("---")
st.markdown("¡Si quieres saber más, dirígete a la página **'Guia'** para crear tu estrategia!")

