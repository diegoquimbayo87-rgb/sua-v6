import streamlit as st
import pandas as pd

st.set_page_config(page_title="SÚA v6.1", layout="wide")

st.markdown("""
<style>
    .header {font-size: 2.8rem; font-weight: 900; letter-spacing: -2px;}
    .subheader {font-size: 1.1rem; color: #64748B;}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("SÚA v6.1")
st.sidebar.caption("Validador Rushbet - Bogotá")
nav = st.sidebar.radio("Módulos", [
    "Dashboard - Oportunidades",
    "Nuevo Análisis",
    "Checklists IC",
    "Matriz de Decisión",
    "Sharp Comparison",
    "Registro"
])

# DASHBOARD - OPORTUNIDADES
if nav == "Dashboard - Oportunidades":
    st.markdown('<div class="header">Oportunidades del Día</div>', unsafe_allow_html=True)
    st.caption("23 Julio 2026 - Hora Bogotá")

    st.subheader("Hoy")
    today = [
        {"hora": "14:00", "partido": "Manchester City vs Arsenal", "mercado": "Over 2.5 Goles", "cuota": 2.15, "ic": 86, "edge": 11.2},
        {"hora": "16:00", "partido": "Liverpool vs Chelsea", "mercado": "Over 2.5 Goles", "cuota": 1.95, "ic": 81, "edge": 8.5},
        {"hora": "19:00", "partido": "Bayern vs Dortmund", "mercado": "Over 4.5 Tarjetas", "cuota": 2.35, "ic": 79, "edge": 7.5},
    ]

    for opp in today:
        with st.expander(f"**{opp['hora']}** - {opp['partido']}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Cuota", opp['cuota'])
            with col2:
                st.metric("IC", opp['ic'])
            with col3:
                st.metric("Edge", f"+{opp['edge']}%")

    st.divider()

    st.subheader("Mañana - 24 Julio")
    tomorrow = [
        {"hora": "13:00", "partido": "Real Madrid vs Barcelona", "mercado": "Over 10.5 Corners", "cuota": 2.45, "ic": 82, "edge": 9.8},
        {"hora": "15:30", "partido": "Juventus vs Inter", "mercado": "Over 2.5 Goles", "cuota": 2.28, "ic": 84, "edge": 10.1},
        {"hora": "20:00", "partido": "PSG vs Marseille", "mercado": "Over 4.5 Tarjetas", "cuota": 2.40, "ic": 77, "edge": 6.8},
    ]

    for opp in tomorrow:
        with st.expander(f"**{opp['hora']}** - {opp['partido']}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Cuota", opp['cuota'])
            with col2:
                st.metric("IC", opp['ic'])
            with col3:
                st.metric("Edge", f"+{opp['edge']}%")

# NUEVO ANÁLISIS
elif nav == "Nuevo Análisis":
    st.markdown('<div class="header">Nuevo Análisis de Partido</div>', unsafe_allow_html=True)
    
    partido = st.text_input("Ingresa el partido", placeholder="Ej: Manchester City vs Arsenal")
    
    if partido:
        st.subheader(f"Análisis: {partido}")
        mercado = st.selectbox("Mercado", ["Over / Under Goles", "Córneres", "Tarjetas"])
        
        st.divider()
        
        if mercado == "Over / Under Goles":
            xG = st.slider("xG Combinado últimos 6 PJ", 1.5, 4.5, 3.4, 0.1)
            regresion = st.slider("Regresión (Goles - xG)", -1.5, 1.5, -0.5, 0.1)
            over_hist = st.slider("% Over 2.5 últimos 8 PJ", 30, 80, 62)
            
            ic = 30 if xG > 3.4 else 15
            ic += 25 if regresion < -0.4 else 10
            ic += 20 if over_hist > 62 else 8
            ic += 25
            
            st.metric("IC Calculado", int(ic))
            cuota = st.number_input("Cuota Rushbet", value=2.10, step=0.05)
            
            if st.button("Generar Recomendación"):
                if ic >= 80:
                    st.success("Recomendación: APOSTAR")
                elif ic >= 74:
                    st.warning("Recomendación: Apostar con moderación")
                else:
                    st.error("Recomendación: NO APOSTAR")

# Otras secciones básicas
elif nav == "Checklists IC":
    st.header("Checklists IC")
    st.info("En desarrollo - Selecciona un mercado")
elif nav == "Matriz de Decisión":
    st.header("Matriz de Decisión")
    st.dataframe(pd.DataFrame({
        "IC": ["90-100", "82-89", "74-81", "<68"],
        "Decisión": ["APOSTAR FUERTE", "APOSTAR", "MODERADO", "NO APOSTAR"],
        "Stake": ["3-5%", "2-3%", "1-2%", "0%"]
    }))
else:
    st.info("Sección en desarrollo.")

st.sidebar.success("Sistema Activo")
