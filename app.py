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
    st.expander("16:00 - Liverpool vs Chelsea - Over 2.5 Goles").markdown("**IC:** 81 | **Edge:** +8.5% | **Recomendación:** Buena")

    st.subheader("Mañana - 24 Julio")
    st.expander("16:30 - Real Madrid vs Barcelona - Over 10.5 Corners").markdown("**IC:** 82 | **Edge:** +9.8% | **Recomendación:** Buena")

# NUEVO ANÁLISIS - CÁLCULO AUTOMÁTICO MEJORADO
elif nav == "Nuevo Análisis":
    st.markdown('<div class="header">Nuevo Análisis de Partido</div>', unsafe_allow_html=True)
    
    partido = st.text_input("Ingresa el partido", placeholder="Ej: Manchester City vs Arsenal")
    
    if partido:
        st.subheader(f"Análisis: {partido}")
        mercado = st.selectbox("Mercado", ["Over / Under Goles", "Córneres", "Tarjetas"])
        
        st.divider()
        
        if mercado == "Over / Under Goles":
            st.subheader("Cálculo Automático IC - Goles")
            
            col1, col2 = st.columns(2)
            with col1:
                xG = st.slider("xG Combinado últimos 6 PJ", 1.5, 4.5, 3.4, 0.1)
                regresion = st.slider("Regresión (Goles - xG)", -1.5, 1.5, -0.5, 0.1)
            with col2:
                over_hist = st.slider("% Over 2.5 últimos 8 PJ", 30, 80, 62)
                motivacion = st.slider("Nivel de Motivación (0-10)", 0, 10, 8)
            
            # Cálculo automático mejorado
            ic = 0
            ic += 30 if xG > 3.4 else (20 if xG > 3.0 else 10)
            ic += 25 if regresion < -0.4 else (15 if regresion < -0.2 else 5)
            ic += 20 if over_hist > 62 else (12 if over_hist > 55 else 5)
            ic += motivacion * 2.5
            
            ic = min(100, int(ic))
            
            st.metric("IC Calculado", ic, delta="Alto" if ic >= 80 else "Medio")
            
            cuota = st.number_input("Cuota Rushbet", value=2.10, step=0.05)
            
            if st.button("Generar Recomendación"):
                if ic >= 80 and cuota >= 1.90:
                    st.success("Recomendación: APOSTAR")
                elif ic >= 74:
                    st.warning("Recomendación: Apostar con moderación")
                else:
                    st.error("Recomendación: NO APOSTAR")

# Otras secciones (básicas)
elif nav == "Checklists IC":
    st.header("Checklists IC")
    st.info("Checklists cuantitativas en desarrollo")

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
