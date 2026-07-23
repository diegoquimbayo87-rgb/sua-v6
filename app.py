import streamlit as st
import pandas as pd
import requests
from datetime import datetime

st.set_page_config(page_title="SÚA v6.1", layout="wide")

st.markdown("""
<style>
    .header {font-size: 2.8rem; font-weight: 900; letter-spacing: -2px;}
    .subheader {font-size: 1.1rem; color: #64748B;}
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
st.sidebar.title("SÚA v6.1")
st.sidebar.caption("Validador Rushbet")
nav = st.sidebar.radio("Módulos", [
    "Dashboard - Oportunidades",
    "Nuevo Análisis",
    "Checklists IC",
    "Matriz de Decisión",
    "Sharp Comparison",
    "Registro"
])

# ==================== DASHBOARD - OPORTUNIDADES ====================
if nav == "Dashboard - Oportunidades":
    st.markdown('<div class="header">Oportunidades del Día Siguiente</div>', unsafe_allow_html=True)
    st.caption("24 Julio 2026 • Hipótesis Rushbet detectadas")

    opportunities = [
        {"hora": "14:00", "partido": "Manchester City vs Arsenal", "mercado": "Over 2.5 Goles", "cuota": 2.15, "ic": 86, "edge": 11.2},
        {"hora": "16:30", "partido": "Real Madrid vs Barcelona", "mercado": "Over 10.5 Corners", "cuota": 2.45, "ic": 82, "edge": 9.8},
        {"hora": "19:00", "partido": "Bayern vs Dortmund", "mercado": "Over 4.5 Tarjetas", "cuota": 2.35, "ic": 79, "edge": 7.5},
        {"hora": "21:00", "partido": "Juventus vs Inter", "mercado": "Over 2.5 Goles", "cuota": 2.28, "ic": 84, "edge": 10.1},
    ]

    for opp in opportunities:
        with st.expander(f"**{opp['hora']}** - {opp['partido']}"):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Cuota", opp['cuota'])
            with col2:
                st.metric("IC", opp['ic'])
            with col3:
                st.metric("Edge", f"+{opp['edge']}%")
            with col4:
                st.success("Recomendación: Fuerte" if opp['ic'] >= 80 else "Moderada")
            
            if st.button("Analizar", key=opp['partido']):
                st.session_state.selected = opp['partido']
                st.success(f"Abriendo análisis de {opp['partido']}")

# ==================== NUEVO ANÁLISIS ====================
elif nav == "Nuevo Análisis":
    st.markdown('<div class="header">Nuevo Análisis de Partido</div>', unsafe_allow_html=True)
    
    partido = st.text_input("Ingresa el partido", placeholder="Ej: Manchester City vs Arsenal")
    
    if partido:
        st.subheader(f"Análisis: {partido}")
        mercado = st.selectbox("Mercado", ["Over / Under Goles", "Córneres", "Tarjetas"])
        
        # Checklist ejemplo
        if mercado == "Over / Under Goles":
            xG = st.slider("xG Combinado", 1.5, 4.5, 3.4, 0.1)
            ic = 30 if xG > 3.4 else 15
            ic += 70
            st.metric("IC Calculado", ic)

# ==================== OTRAS SECCIONES ====================
else:
    st.info("Esta sección está en desarrollo.")

st.sidebar.success("Sistema Activo")
