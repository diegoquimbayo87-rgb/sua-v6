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
import streamlit as st
import pandas as pd

st.set_page_config(page_title="SÚA v6.1 — Validador Rushbet", layout="wide")

# Estilos limpios
st.markdown("""
<style>
    .header {font-size: 2.8rem; font-weight: 900; letter-spacing: -2px; margin-bottom: 8px;}
    .subheader {font-size: 1.1rem; color: #64748B;}
    .metric {font-size: 2.8rem; font-weight: 800;}
</style>
""", unsafe_allow_html=True)

# Sidebar
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
    st.markdown("**23 Julio 2026 • Hipótesis Rushbet detectadas**")

    opportunities = [
        {"partido": "Manchester City vs Arsenal", "mercado": "Over 2.5 Goles", "cuota": 2.15, "ic": 86, "edge": 11.2, "status": "Fuerte"},
        {"partido": "Real Madrid vs Barcelona", "mercado": "Over 10.5 Corners", "cuota": 2.45, "ic": 82, "edge": 9.8, "status": "Buena"},
        {"partido": "Bayern vs Dortmund", "mercado": "Over 4.5 Tarjetas", "cuota": 2.35, "ic": 79, "edge": 7.5, "status": "Moderada"},
    ]

    for opp in opportunities:
        with st.expander(f"{opp['partido']} - {opp['mercado']}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Cuota Rushbet", opp['cuota'])
            with col2:
                st.metric("IC", opp['ic'])
            with col3:
                st.metric("Edge", f"+{opp['edge']}%")
            st.caption(f"Recomendación: {opp['status']}")

# ==================== NUEVO ANÁLISIS ====================
elif nav == "Nuevo Análisis":
    st.markdown('<div class="header">Nuevo Análisis de Partido</div>', unsafe_allow_html=True)
    
    partido = st.text_input("Ingresa el partido", placeholder="Ej: Manchester City vs Arsenal")
    
    if partido:
        st.subheader(f"Análisis: {partido}")
        mercado = st.selectbox("Mercado", ["Over / Under Goles", "Córneres", "Tarjetas", "Disparos a Puerta"])
        
        st.divider()
        
        if mercado == "Over / Under Goles":
            st.subheader("Checklist - Over / Under Goles")
            xG = st.slider("xG Combinado (últimos 6 PJ)", 1.5, 4.5, 3.2, 0.1)
            regresion = st.slider("Regresión (Goles - xG)", -1.0, 1.0, -0.4, 0.1)
            over_hist = st.slider("% Over 2.5 últimos 8 PJ", 30, 80, 62)
            
            ic = 30 if xG > 3.4 else 15
            ic += 20 if regresion < -0.4 else 0
            ic += 20 if over_hist > 62 else 10
            ic += 30
            
            st.metric("IC Calculado", ic)
            cuota = st.number_input("Cuota Rushbet", value=2.10, step=0.05)
            
            if st.button("Generar Recomendación"):
                if ic >= 80 and cuota >= 1.90:
                    st.success("Recomendación: APOSTAR")
                elif ic >= 74:
                    st.warning("Recomendación: Apostar con moderación")
                else:
                    st.error("Recomendación: NO APOSTAR")

# ==================== CHECKLISTS IC ====================
elif nav == "Checklists IC":
    st.header("Checklists IC")
    st.info("Selecciona un mercado para ver la checklist cuantitativa")

# ==================== MATRIZ ====================
elif nav == "Matriz de Decisión":
    st.header("Matriz de Decisión")
    st.dataframe(pd.DataFrame({
        "IC": ["90-100", "82-89", "74-81", "<68"],
        "Decisión": ["APOSTAR FUERTE", "APOSTAR", "MODERADO", "NO APOSTAR"],
        "Stake": ["3-5%", "2-3%", "1-2%", "0%"]
    }))

# ==================== SHARP COMPARISON ====================
elif nav == "Sharp Comparison":
    st.header("Sharp Comparison (Pinnacle)")
    st.info("Aquí se comparará con Pinnacle usando The Odds API")

# ==================== REGISTRO ====================
elif nav == "Registro":
    st.header("Registro de Apuestas")
    st.write("Histórico de operaciones aparecerá aquí.")

st.sidebar.success("Sistema Activo")
