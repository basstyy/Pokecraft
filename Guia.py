import streamlit as st
import pandas as pd
import random 

# --- Título principal ---
st.title("⚡️ PokéCraft: Asistente Estratégico de Tipos")
st.subheader("Selecciona el tipo oponente y tu estrategia para el combate.")

# --- Base de datos de tipos ---
POKEMON_TYPES = [
    "Normal", "Fuego", "Agua", "Planta", "Eléctrico", 
    "Hielo", "Lucha", "Veneno", "Tierra", "Volador", 
    "Psíquico", "Bicho", "Roca", "Fantasma", "Dragón", 
    "Acero", "Hada"
]

# --- Tipos súper efectivos ---
SUPER_EFFECTIVE = {
    "Normal": [],
    "Fuego": ["Planta", "Hielo", "Bicho", "Acero"],
    "Agua": ["Fuego", "Tierra", "Roca"],
    "Planta": ["Agua", "Tierra", "Roca"],
    "Eléctrico": ["Agua", "Volador"],
    "Hielo": ["Planta", "Tierra", "Volador", "Dragón"],
    "Lucha": ["Normal", "Hielo", "Roca", "Acero"],
    "Veneno": ["Planta", "Hada"],
    "Tierra": ["Fuego", "Eléctrico", "Veneno", "Roca", "Acero"],
    "Volador": ["Planta", "Lucha", "Bicho"],
    "Psíquico": ["Lucha", "Veneno"],
    "Bicho": ["Planta", "Psíquico", "Siniestro"],
    "Roca": ["Fuego", "Hielo", "Volador", "Bicho"],
    "Fantasma": ["Fantasma", "Psíquico"],
    "Dragón": ["Dragón"],
    "Acero": ["Hielo", "Roca", "Hada"],
    "Hada": ["Lucha", "Dragón", "Siniestro"]
}

# --- Imágenes de iconos de tipos ---
TYPE_IMAGES = {
    "Normal": "https://archives.bulbagarden.net/media/upload/9/95/NormalIC_Big.png",
    "Fuego": "https://archives.bulbagarden.net/media/upload/5/56/FireIC_Big.png",
    "Agua": "https://archives.bulbagarden.net/media/upload/7/70/WaterIC_Big.png",
    "Planta": "https://archives.bulbagarden.net/media/upload/a/a8/GrassIC_Big.png",
    "Eléctrico": "https://archives.bulbagarden.net/media/upload/4/4a/ElectricIC_Big.png",
    "Hielo": "https://archives.bulbagarden.net/media/upload/7/7a/IceIC_Big.png",
    "Lucha": "https://archives.bulbagarden.net/media/upload/6/67/FightingIC_Big.png",
    "Veneno": "https://archives.bulbagarden.net/media/upload/8/88/PoisonIC_Big.png",
    "Tierra": "https://archives.bulbagarden.net/media/upload/8/8d/GroundIC_Big.png",
    "Volador": "https://archives.bulbagarden.net/media/upload/9/9b/FlyingIC_Big.png",
    "Psíquico": "https://archives.bulbagarden.net/media/upload/7/73/PsychicIC_Big.png",
    "Bicho": "https://archives.bulbagarden.net/media/upload/7/7d/BugIC_Big.png",
    "Roca": "https://archives.bulbagarden.net/media/upload/f/f1/RockIC_Big.png",
    "Fantasma": "https://archives.bulbagarden.net/media/upload/0/01/GhostIC_Big.png",
    "Dragón": "https://archives.bulbagarden.net/media/upload/6/6f/DragonIC_Big.png",
    "Acero": "https://archives.bulbagarden.net/media/upload/3/3c/SteelIC_Big.png",
    "Hada": "https://archives.bulbagarden.net/media/upload/d/df/FairyIC_Big.png"
}

# --- Configuración lateral ---
st.sidebar.header("🔍 Configuración de Estrategia")

opponent_type = st.sidebar.selectbox(
    "1. Tipo de Pokémon Oponente a Contrarrestar",
    POKEMON_TYPES,
    index=3
)

strategy_focus = st.sidebar.radio(
    "2. Estrategia Principal",
    ['Atacar (Súper Efectivo 2x)', 'Defender (Resistir o Inmune)'],
    index=0
)

search_button = st.sidebar.button("¡Calcular Debilidades!")

st.sidebar.markdown("---")
st.sidebar.markdown("*(Usando la tabla de tipos de la Generación VI en adelante)*")

# --- Lógica principal ---
if search_button:
    if strategy_focus == 'Atacar (Súper Efectivo 2x)':
        st.markdown(f"## ⚔️ Tipos Súper Efectivos Contra **{opponent_type}**")
        st.info("Buscando tipos que causan 2x de daño al tipo oponente seleccionado.")
        
        counter_types = []
        for attacking_type, effective_against in SUPER_EFFECTIVE.items():
            if opponent_type in effective_against:
                counter_types.append(attacking_type)
        
        if counter_types:
            st.balloons()
            st.markdown(f"Los siguientes tipos son **Súper Efectivos (2x daño)** contra el tipo **{opponent_type}**:")

            colA, colB, colC = st.columns(3)
            cols = [colA, colB, colC]

            for i, c_type in enumerate(counter_types):
                img_url = TYPE_IMAGES.get(c_type, "https://placehold.co/100x100?text=No+Image")
                cols[i % 3].image(img_url, width=80)
                cols[i % 3].markdown(f"""
                ### 💥 {c_type}
                <div style="padding: 10px; background-color: #f0f0f0; border-radius: 10px;">
                    <p style="margin: 0; font-weight: bold;">¡Doble Daño!</p>
                </div>
                """, unsafe_allow_html=True)
            
            # --- RECOMENDACIÓN DE EQUIPO ---
            st.markdown("---")
            st.subheader("Recomendación de Equipo")

            # Diccionario con Pokémon reales por tipo
            POKEMON_IMAGES = {
                "Normal": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png",     # Eevee
                "Fuego": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png",      # Charmander
                "Agua": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/007.png",       # Squirtle
                "Planta": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png",     # Bulbasaur
                "Eléctrico": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png",  # Pikachu
                "Hielo": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/087.png",      # Dewgong
                "Lucha": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/066.png",      # Machop
                "Veneno": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/002.png",     # Ivysaur
                "Tierra": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/050.png",     # Diglett
                "Volador": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/016.png",    # Pidgey
                "Psíquico": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/063.png",   # Abra
                "Bicho": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/010.png",      # Caterpie
                "Roca": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/074.png",       # Geodude
                "Fantasma": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/092.png",   # Gastly
                "Dragón": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/147.png",     # Dratini
                "Acero": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/081.png",      # Magnemite
                "Hada": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/035.png"        # Clefairy
            }

            if len(counter_types) >= 3:
                st.markdown("### 🌟 Equipo Recomendado")
                cols = st.columns(3)

                for i, poke_type in enumerate(counter_types[:3]):
                    img_url = POKEMON_IMAGES.get(
                        poke_type,
                        TYPE_IMAGES.get(poke_type, "https://placehold.co/150x150?text=Sin+Imagen")
                    )
                    with cols[i]:
                        st.image(img_url, width=150, caption=f"Ejemplo Tipo {poke_type}")
                        st.markdown(
                            f"""
                            <div style='text-align:center; font-size:14px;'>
                                <b>{poke_type}</b> es una gran opción para contrarrestar a <b>{opponent_type}</b>.
                            </div>
                            """, 
                            unsafe_allow_html=True
                        )
            else:
                st.warning("Se necesitan al menos 3 tipos para una recomendación de equipo equilibrada.")
        
        else:
            st.error(f"❌ Ningún tipo es Súper Efectivo contra {opponent_type}.")
    
    else:
        st.markdown(f"## 🛡️ Tipos que Resisten o son Inmunes al Daño de **{opponent_type}**")
        st.warning("Esta funcionalidad estará disponible próximamente.")
        st.progress(75, text="Progreso de la función de Defensa...")

else:
    st.info("Selecciona el tipo de Pokémon a vencer en la barra lateral izquierda y presiona el botón.")

