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

# DASHBOARD
if nav == "Dashboard - Oportunidades":
    st.markdown('<div class="header">Oportunidades del Día</div>', unsafe_allow_html=True)
    st.caption("23 Julio 2026 - Hora Bogotá")

    st.subheader("Hoy")
    st.expander("14:00 - Manchester City vs Arsenal - Over 2.5 Goles").markdown("**IC:** 86 | **Edge:** +11.2% | **Recomendación:** Fuerte")

    st.subheader("Mañana - 24 Julio")
    st.expander("16:30 - Real Madrid vs Barcelona - Over 10.5 Corners").markdown("**IC:** 82 | **Edge:** +9.8% | **Recomendación:** Buena")

# NUEVO ANÁLISIS - CON CÁLCULO MEJORADO
elif nav == "Nuevo Análisis":
    st.markdown('<div class="header">Nuevo Análisis de Partido</div>', unsafe_allow_html=True)
    
    partido = st.text_input("Ingresa el partido", placeholder="Ej: Manchester City vs Arsenal")
    
    if partido:
        st.subheader(f"Análisis: {partido}")
        mercado = st.selectbox("Mercado", ["Over / Under Goles", "Córneres", "Tarjetas"])
        
        st.divider()
        
        if mercado == "Over / Under Goles":
            st.subheader("Checklist Cuantitativa - Goles")
            
            xG = st.slider("xG Combinado últimos 6 PJ", 1.5, 4.5, 3.4, 0.1)
            regresion = st.slider("Regresión (Goles - xG)", -1.5, 1.5, -0.5, 0.1)
            over_hist = st.slider("% Over 2.5 últimos 8 PJ", 30, 80, 62)
            motivacion = st.slider("Nivel de Motivación (0-10)", 0, 10, 8)
            
            # Cálculo mejorado
            ic = 0
            ic += 30 if xG > 3.4 else 15
            ic += 25 if regresion < -0.4 else 10
            ic += 20 if over_hist > 62 else 8
            ic += motivacion * 2.5
            
            ic = min(100, int(ic))
            
            st.metric("IC Calculado", ic, delta="Alto" if ic >= 80 else "Medio")
            
            cuota = st.number_input("Cuota Rushbet", value=2.10, step=0.05)
            
            if st.button("Generar Recomendación"):
                if ic >= 80 and cuota >= 1.90:
                    st.success("Recomendación: APOSTAR")
                    st.info(f"Stake sugerido: 2.5% del bankroll")
                elif ic >= 74:
                    st.warning("Recomendación: Apostar con moderación")
                else:
                    st.error("Recomendación: NO APOSTAR")

        # Puedes agregar los otros mercados aquí más adelante
        else:
            st.info("Checklist para este mercado en desarrollo")

# Otras secciones
else:
    st.info("Sección en desarrollo.")

st.sidebar.success("Sistema Activo")
