import streamlit as st
import pandas as pd

st.title("Nuevo Análisis de Partido")

# Input principal
partido = st.text_input("Ingresa el partido", placeholder="Ej: Manchester City vs Arsenal")

if partido:
    st.subheader(f"Análisis: {partido}")
    
    # Selección de mercado
    mercado = st.selectbox("Selecciona el Mercado a Analizar", 
                          ["Over / Under Goles", "Córneres", "Tarjetas", "Disparos a Puerta"])
    
    st.divider()
    
    # Checklist según mercado
    if mercado == "Over / Under Goles":
        st.subheader("Checklist - Over / Under Goles")
        xG = st.slider("xG Combinado últimos 6 partidos", 1.5, 4.5, 3.2, 0.1)
        regresion = st.slider("Regresión (Goles - xG)", -1.0, 1.0, -0.5, 0.1)
        over_hist = st.slider("% Over 2.5 últimos 8 PJ", 30, 80, 55)
        
        ic = int(30 * (xG > 3.4) + 20 * (regresion < -0.4) + 20 * (over_hist > 62) + 30)
        st.metric("IC Calculado", ic, delta="Alto" if ic >= 80 else "Medio")
    
    elif mercado == "Córneres":
        st.subheader("Checklist - Córneres")
        centros = st.slider("Promedio Centros + Ataques por banda", 15, 35, 24)
        bloqueos = st.slider("Remates bloqueados + PPDA bajo", 0, 30, 18)
        ic = int(30 * (centros > 24) + 25 * (bloqueos > 18) + 45)
        st.metric("IC Calculado", ic)
    
    elif mercado == "Tarjetas":
        st.subheader("Checklist - Tarjetas")
        arbitro = st.slider("Promedio tarjetas del árbitro", 2.0, 7.0, 4.8, 0.1)
        faltas = st.slider("Promedio faltas cometidas", 15, 30, 22)
        ic = int(30 * (arbitro > 5.0) + 25 * (faltas > 22) + 45)
        st.metric("IC Calculado", ic)
    
    # Recomendación final
    st.divider()
    cuota = st.number_input("Cuota Rushbet", value=2.10, step=0.05)
    if st.button("Generar Recomendación"):
        if ic >= 80 and cuota >= 1.90:
            st.success("Recomendación: APOSTAR")
            st.info(f"Stake sugerido: 2.0% del bankroll")
        elif ic >= 74:
            st.warning("Recomendación: Apostar con moderación")
        else:
            st.error("Recomendación: NO APOSTAR")
