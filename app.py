import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="SÚA v6.1", layout="wide")

st.markdown("""
<style>
    .header {font-size: 2.8rem; font-weight: 900; letter-spacing: -2px;}
    .subheader {font-size: 1.1rem; color: #64748B;}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("SÚA v6.1")
st.sidebar.caption("Validador Rushbet - Bogotá (UTC-5)")
nav = st.sidebar.radio("Módulos", [
    "Dashboard - Oportunidades",
    "Nuevo Análisis",
    "Checklists IC",
    "Matriz de Decisión",
    "Sharp Comparison",
    "Registro"
])

# ==================== DASHBOARD ====================
if nav == "Dashboard - Oportunidades":
    st.markdown('<div class="header">Oportunidades del Día</div>', unsafe_allow_html=True)
    st.caption("23 Julio 2026 - Hora Bogotá")

    # Día actual
    st.subheader("Hoy - 23 Julio")
    today_opps = [
        {"hora": "14:00", "partido": "Manchester City vs Arsenal", "mercado": "Over 2.5 Goles", "cuota": 2.15, "ic": 86, "edge": 11.2},
        {"hora": "19:00", "partido": "Bayern vs Dortmund", "mercado": "Over 4.5 Tarjetas", "cuota": 2.35, "ic": 79, "edge": 7.5},
    ]

    for opp in today_opps:
        with st.expander(f"**{opp['hora']}** - {opp['partido']}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Cuota", opp['cuota'])
            with col2:
                st.metric("IC", opp['ic'])
            with col3:
                st.metric("Edge", f"+{opp['edge']}%")

    st.divider()

    # Día siguiente
    st.subheader("Mañana - 24 Julio")
    tomorrow_opps = [
        {"hora": "16:30", "partido": "Real Madrid vs Barcelona", "mercado": "Over 10.5 Corners", "cuota": 2.45, "ic": 82, "edge": 9.8},
        {"hora": "21:00", "partido": "Juventus vs Inter", "mercado": "Over 2.5 Goles", "cuota": 2.28, "ic": 84, "edge": 10.1},
    ]

    for opp in tomorrow_opps:
        with st.expander(f"**{opp['hora']}** - {opp['partido']}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Cuota", opp['cuota'])
            with col2:
                st.metric("IC", opp['ic'])
            with col3:
                st.metric("Edge", f"+{opp['edge']}%")

# ==================== NUEVO ANÁLISIS ====================
elif nav == "Nuevo Análisis":
    st.markdown('<div class="header">Nuevo Análisis de Partido</div>', unsafe_allow_html=True)
    
    partido = st.text_input("Ingresa el partido", placeholder="Ej: Manchester City vs Arsenal")
    
    if partido:
        st.subheader(f"Análisis: {partido}")
        mercado = st.selectbox("Mercado", ["Over / Under Goles", "Córneres", "Tarjetas"])
        
        st.divider()
        if mercado == "Over / Under Goles":
            xG = st.slider("xG Combinado", 1.5, 4.5, 3.4, 0.1)
            ic = 75 if xG > 3.4 else 50
            st.metric("IC Calculado", ic)

# Otras secciones
else:
    st.info("Sección en desarrollo.")

st.sidebar.success("Sistema Activo - Bogotá")
