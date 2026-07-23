import streamlit as st
import pandas as pd
import requests
from datetime import datetime

st.set_page_config(page_title="SÚA v6.1 — Validador Rushbet", layout="wide", initial_sidebar_state="expanded")

# ==================== ESTILOS ====================
st.markdown("""
<style>
    .header {font-size: 2.8rem; font-weight: 900; letter-spacing: -2px;}
    .subheader {font-size: 1.1rem; color: #64748B;}
    .metric-big {font-size: 3.5rem; font-weight: 800; font-family: monospace;}
    .card {background: #111827; padding: 20px; border-radius: 12px; border: 1px solid #1F2937;}
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
st.sidebar.title("SÚA v6.1")
st.sidebar.caption("Validador de Hipótesis Rushbet")
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
    st.markdown(f'<div class="subheader">23 Julio 2026 • 6 oportunidades detectadas</div>', unsafe_allow_html=True)

    # Datos de ejemplo (en producción vendrían de APIs)
    opps = [
        {"partido": "Man City vs Arsenal", "mercado": "Over 2.5 Goles", "cuota": 2.15, "ic": 86, "edge": 11.2, "status": "🟢 FUERTE"},
        {"partido": "Real Madrid vs Barcelona", "mercado": "Over 10.5 Corners", "cuota": 2.45, "ic": 82, "edge": 9.8, "status": "🟢 BUENA"},
        {"partido": "Bayern vs Dortmund", "mercado": "Over 4.5 Tarjetas", "cuota": 2.35, "ic": 79, "edge": 7.5, "status": "🟡 Moderada"},
    ]

    for opp in opps:
        with st.expander(f"**{opp['partido']}** — {opp['mercado']}"):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Cuota Rushbet", opp['cuota'])
            with col2:
                st.metric("IC", opp['ic'])
            with col3:
                st.metric("Edge", f"+{opp['edge']}%")
            with col4:
                st.success(opp['status'])
            
            if st.button("Analizar →", key=opp['partido']):
                st.session_state.selected_match = opp['partido']
                st.switch_page("pages/2_Analisis.py")

# ==================== NUEVO ANÁLISIS ====================
elif nav == "Nuevo Análisis":
    st.header("Nuevo Análisis de Partido")
    partido = st.text_input("Partido (ej: Man City vs Arsenal)")
    if st.button("Cargar Datos de APIs"):
        st.success("Datos cargados desde API-Football y The Odds API")
        # Aquí iría la lógica real de APIs

# ==================== CHECKLISTS IC ====================
elif nav == "Checklists IC":
    st.header("Checklists IC por Mercado")
    mercado = st.selectbox("Mercado", ["Over/Under Goles", "Corners", "Tarjetas", "Disparos"])
    st.info("Completa las métricas para calcular IC automáticamente")

# ==================== MATRIZ ====================
elif nav == "Matriz de Decisión":
    st.header("Matriz de Decisión v4.1")
    st.dataframe(pd.DataFrame({
        "IC": ["90-100", "82-89", "74-81"],
        "Decisión": ["🟢 FUERTE", "🟢 APOSTAR", "🟡 Moderado"],
        "Stake": ["3-5%", "2-3%", "1-2%"]
    }))

# ==================== SHARP COMPARISON ====================
elif nav == "Sharp Comparison":
    st.header("🔍 Sharp Comparison (Pinnacle)")
    home = st.text_input("Equipo Local")
    away = st.text_input("Equipo Visitante")
    if st.button("Consultar Pinnacle"):
        st.info("Comparando con The Odds API... (en producción mostraría datos reales)")

# ==================== REGISTRO ====================
elif nav == "Registro":
    st.header("Registro de Apuestas")
    st.write("Histórico de operaciones y estadísticas")

st.sidebar.success("APIs Conectadas • Online")
