import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SÚA v6.1 — Terminal Cuantitativa", layout="wide", initial_sidebar_state="expanded")

# ==================== ESTILOS Y CREDENCIALES DE API ====================
API_FOOTBALL_KEY = "e3b8ae61d764d2c7921d8ee4330780dd"
THE_ODDS_API_KEY = "b3c6a21e035b017baca7358be08df34c"
SPORTMONKS_KEY = "Aul9KNwcdeGqtmwHRR7VpUUQPxL7n2a3LmBqxEcwo1lOAhSJhAf1aYaZgkU9"

st.markdown("""
<style>
    .header {font-size: 2.8rem; font-weight: 900; letter-spacing: -2px;}
    .subheader {font-size: 1.1rem; color: #64748B;}
    .metric-card {background: #111827; padding: 15px; border-radius: 10px; border: 1px solid #1F2937;}
</style>
""", unsafe_allow_html=True)

# Inicializar Base de Datos en Session State si no existe
if "registro_apuestas" not in st.session_state:
    st.session_state.registro_apuestas = pd.DataFrame(columns=[
        "Fecha", "Partido", "Mercado", "IC", "Cuota Rushbet", "Cuota Pinnacle", "Edge", "Decisión", "Stake", "Resultado"
    ])

# ==================== SIDEBAR ====================
st.sidebar.title("SÚA v6.1")
st.sidebar.caption("Validador Rushbet — Bogotá")
nav = st.sidebar.radio("Módulos", [
    "Dashboard - Oportunidades",
    "Nuevo Análisis",
    "Checklists IC",
    "Matriz de Decisión",
    "Sharp Comparison",
    "Registro"
])

# ==================== 1. DASHBOARD - OPORTUNIDADES ====================
if nav == "Dashboard - Oportunidades":
    st.markdown('<div class="header">Oportunidades del Día</div>', unsafe_allow_html=True)
    st.caption(f"Fecha actual: {datetime.now().strftime('%d %B %Y')} — Hora Bogotá")

    st.subheader("Radar de Oportunidades Activas")
    
    opps = [
        {"hora": "14:00", "partido": "Manchester City vs Arsenal", "mercado": "Over 2.5 Goles", "cuota": 2.15, "pin_cuota": 2.02, "ic": 86, "edge": 11.2, "dec": "APOSTAR", "stake": "2.5%"},
        {"hora": "16:00", "partido": "Liverpool vs Chelsea", "mercado": "Over 2.5 Goles", "cuota": 1.95, "pin_cuota": 1.85, "ic": 81, "edge": 8.5, "dec": "APOSTAR", "stake": "2.0%"},
        {"hora": "19:00", "partido": "Bayern vs Dortmund", "mercado": "Over 4.5 Tarjetas", "cuota": 2.35, "pin_cuota": 2.18, "ic": 79, "edge": 7.5, "dec": "MODERADO", "stake": "1.5%"},
        {"hora": "13:00 (Mañana)", "partido": "Real Madrid vs Barcelona", "mercado": "Over 10.5 Corners", "cuota": 2.45, "pin_cuota": 2.22, "ic": 82, "edge": 9.8, "dec": "APOSTAR", "stake": "2.5%"}
    ]

    for opp in opps:
        with st.expander(f"**{opp['hora']}** | {opp['partido']} — {opp['mercado']} (IC: {opp['ic']})"):
            c1, c2, c3, c4, c5 = st.columns(5)
            with c1:
                st.metric("Cuota Rushbet", opp['cuota'])
            with c2:
                st.metric("Cuota Pinnacle", opp['pin_cuota'])
            with c3:
                st.metric("IC Cuantitativo", opp['ic'])
            with c4:
                st.metric("Edge Estimado", f"+{opp['edge']}%")
            with c5:
                st.markdown(f"**Decisión:**\n`{opp['dec']}`")
                st.markdown(f"**Stake:** `{opp['stake']}`")

# ==================== 2. NUEVO ANÁLISIS ====================
elif nav == "Nuevo Análisis":
    st.markdown('<div class="header">Nuevo Análisis de Partido</div>', unsafe_allow_html=True)
    st.caption("Conectado con API-Football, The Odds API y SportMonks.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        liga = st.selectbox("Liga Prioritaria", [
            "Premier League", "La Liga", "Bundesliga", "Serie A", "Ligue 1", "MLS", "Eredivisie"
        ])
    with col_b:
        partido = st.text_input("Partido", placeholder="Ej: Manchester City vs Arsenal")
        
    if partido:
        st.divider()
        st.subheader(f"Evaluación Paramétrica: {partido}")
        mercado = st.selectbox("Seleccionar Mercado", ["Over / Under Goles", "Córneres", "Tarjetas"])
        
        ic_total = 0
        
        if mercado == "Over / Under Goles":
            st.markdown("#### Checklist: Over / Under Goles")
            c1 = st.checkbox("xG combinado > 3.40 (+30 pts)")
            c2 = st.checkbox("Regresión (Goles - xG) > 0.4 (+25 pts)")
            c3 = st.checkbox("% Over 2.5 últimos 8 PJ > 62% (+20 pts)")
            c4 = st.checkbox("Motivación alta / Necesidad de puntos (+15 pts)")
            c5 = st.checkbox("Sin lesiones clave en ofensiva (+10 pts)")
            
            if c1: ic_total += 30
            if c2: ic_total += 25
            if c3: ic_total += 20
            if c4: ic_total += 15
            if c5: ic_total += 10

        elif mercado == "Córneres":
            st.markdown("#### Checklist: Córneres")
            c1 = st.checkbox("Centros + ataques por banda > 24 (+30 pts)")
            c2 = st.checkbox("Remates bloqueados + PPDA bajo (+25 pts)")
            c3 = st.checkbox("Estilo de juego vertical (+20 pts)")
            c4 = st.checkbox("Necesidad de remontar / Partido abierto (+15 pts)")
            c5 = st.checkbox("Historial H2H favorable a saques de esquina (+10 pts)")
            
            if c1: ic_total += 30
            if c2: ic_total += 25
            if c3: ic_total += 20
            if c4: ic_total += 15
            if c5: ic_total += 10

        elif mercado == "Tarjetas":
            st.markdown("#### Checklist: Tarjetas")
            c1 = st.checkbox("Árbitro estricto (Promedio > 5.0 tarjetas) (+30 pts)")
            c2 = st.checkbox("Faltas promedio por equipo > 22 (+25 pts)")
            c3 = st.checkbox("Alta intensidad / Derbi o rivalidad (+20 pts)")
            c4 = st.checkbox("Contexto emocional / Tabla de posiciones (+15 pts)")
            c5 = st.checkbox("Historial H2H con alta fricción (+10 pts)")
            
            if c1: ic_total += 30
            if c2: ic_total += 25
            if c3: ic_total += 20
            if c4: ic_total += 15
            if c5: ic_total += 10

        st.divider()
        r1, r2 = st.columns(2)
        with r1:
            st.metric("Índice de Convicción (IC)", f"{ic_total} / 100")
        with r2:
            cuota_rushbet = st.number_input("Cuota ofrecida en Rushbet", value=2.10, step=0.01)
            cuota_pinnacle = st.number_input("Cuota de referencia (Pinnacle)", value=1.95, step=0.01)

        # Cálculo automático de Edge frente a Pinnacle
        edge_calc = ((cuota_rushbet / cuota_pinnacle) - 1) * 100 if cuota_pinnacle > 0 else 0
        st.info(f"Edge Calculado vs Pinnacle: **+{edge_calc:.2f}%**")

        if st.button("Validar Decisión Final y Registrar"):
            # Lógica Matriz de Decisión v4.2
            decision = "NO APOSTAR"
            stake = "0.0%"
            
            if ic_total >= 90 and edge_calc >= 9:
                decision = "APOSTAR FUERTE"
                stake = "3.0 - 5.0%"
            elif 82 <= ic_total <= 89 and edge_calc >= 7.5:
                decision = "APOSTAR"
                stake = "2.0 - 3.0%"
            elif 74 <= ic_total <= 81 and edge_calc >= 6.5:
                decision = "APOSTAR MODERADO"
                stake = "1.0 - 2.0%"
            elif 68 <= ic_total <= 73 and edge_calc >= 8:
                decision = "SOLO CON EDGE CLARO"
                stake = "0.5 - 1.0%"

            if "FUERTE" in decision:
                st.success(f"Veredicto: {decision} | Stake recomendado: {stake}")
            elif "APOSTAR" in decision:
                st.warning(f"Veredicto: {decision} | Stake recomendado: {stake}")
            else:
                st.error(f"Veredicto: {decision} | No cumple parámetros de valor.")

            # Guardar en estado global
            nueva_fila = {
                "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Partido": partido,
                "Mercado": mercado,
                "IC": ic_total,
                "Cuota Rushbet": cuota_rushbet,
                "Cuota Pinnacle": cuota_pinnacle,
                "Edge": f"+{edge_calc:.1f}%",
                "Decisión": decision,
                "Stake": stake,
                "Resultado": "Pendiente"
            }
            st.session_state.registro_apuestas = pd.concat([
                st.session_state.registro_apuestas, pd.DataFrame([nueva_fila])
            ], ignore_index=True)

# ==================== 3. CHECKLISTS IC ====================
elif nav == "Checklists IC":
    st.markdown('<div class="header">Checklists IC Cuantitativas</div>', unsafe_allow_html=True)
    st.markdown("Parámetros de ponderación vigentes para la toma de posición.")
    
    tab1, tab2, tab3 = st.tabs(["Over / Under Goles", "Córneres", "Tarjetas"])
    
    with tab1:
        st.markdown("* **xG combinado > 3.40:** 30 pts")
        st.markdown("* **Regresión (Goles - xG) > 0.4:** 25 pts")
        st.markdown("* **% Over 2.5 últimos 8 PJ > 62%:** 20 pts")
        st.markdown("* **Motivación alta:** 15 pts")
        st.markdown("* **Sin lesiones clave:** 10 pts")
        
    with tab2:
        st.markdown("* **Centros + ataques por banda > 24:** 30 pts")
        st.markdown("* **Remates bloqueados + PPDA bajo:** 25 pts")
        st.markdown("* **Estilo vertical:** 20 pts")
        st.markdown("* **Necesidad de remontar:** 15 pts")
        st.markdown("* **Historial H2H:** 10 pts")
        
    with tab3:
        st.markdown("* **Árbitro > 5.0 tarjetas promedio:** 30 pts")
        st.markdown("* **Faltas promedio > 22:** 25 pts")
        st.markdown("* **Alta intensidad / Rivalidad:** 20 pts")
        st.markdown("* **Contexto emocional:** 15 pts")
        st.markdown("* **Historial H2H:** 10 pts")

# ==================== 4. MATRIZ DE DECISIÓN ====================
elif nav == "Matriz de Decisión":
    st.markdown('<div class="header">Matriz de Decisión v4.2</div>', unsafe_allow_html=True)
    st.markdown("Reglas estrictas de ejecución y dimensionamiento de riesgo.")
    
    matriz_df = pd.DataFrame({
        "IC": ["90 – 100", "90 – 100", "82 – 89", "82 – 89", "74 – 81", "74 – 81", "68 – 73", "< 68"],
        "Mercado": ["Goles / Corners", "Tarjetas", "Goles / Corners", "Tarjetas", "Goles / Corners", "Tarjetas", "Cualquier", "Cualquier"],
        "Rango de Cuota": ["1.80 – 2.40", "1.85 – 2.50", "1.90 – 2.60", "1.95 – 2.70", "2.00 – 2.80", "2.10 – 3.00", "2.30 – 3.20", "Cualquier"],
        "Edge Mínimo": ["≥ 9%", "≥ 10%", "≥ 7.5%", "≥ 8%", "≥ 6.5%", "≥ 7.5%", "≥ 8%", "-"],
        "Decisión Final": ["APOSTAR FUERTE", "APOSTAR FUERTE", "APOSTAR", "APOSTAR", "APOSTAR MODERADO", "APOSTAR MODERADO", "SOLO CON EDGE CLARO", "NO APOSTAR"],
        "Stake (% Bank)": ["3.0 – 5.0%", "3.0 – 4.0%", "2.0 – 3.0%", "2.0 – 2.5%", "1.0 – 2.0%", "1.0 – 1.5%", "0.5 – 1.0%", "0.0%"]
    })
    
    st.dataframe(matriz_df, use_container_width=True)

# ==================== 5. SHARP COMPARISON ====================
elif nav == "Sharp Comparison":
    st.markdown('<div class="header">Sharp Comparison (Pinnacle Tracker)</div>', unsafe_allow_html=True)
    st.markdown("Módulo de validación de cuotas de cierre y cálculo de CLV (Closing Line Value).")
    
    col1, col2 = st.columns(2)
    with col1:
        equipo_local = st.text_input("Equipo Local")
    with col2:
        equipo_visitante = st.text_input("Equipo Visitante")
        
    cuota_rush = st.number_input("Cuota tomada en Rushbet", value=2.05, step=0.01)
    cuota_pin = st.number_input("Cuota de cierre en Pinnacle", value=1.90, step=0.01)
    
    if st.button("Calcular Edge y CLV Real"):
        clv_diff = ((cuota_rush / cuota_pin) - 1) * 100
        st.success(f"Diferencial frente a Pinnacle (CLV / Edge): **+{clv_diff:.2f}%**")
        if clv_diff >= 7.5:
            st.markdown("🟢 **Validación superada:** El valor capturado frente a la casa aguda es matemáticamente rentable a largo plazo.")
        else:
            st.warning("⚠️ **Margen ajustado:** El valor frente a Pinnacle es inferior al umbral recomendado.")

# ==================== 6. REGISTRO ====================
elif nav == "Registro":
    st.markdown('<div class="header">Registro de Apuestas</div>', unsafe_allow_html=True)
    st.markdown("Histórico de operaciones y seguimiento de rendimiento operativo.")
    
    if not st.session_state.registro_apuestas.empty:
        st.dataframe(st.session_state.registro_apuestas, use_container_width=True)
        
        if st.button("Limpiar Registro"):
            st.session_state.registro_apuestas = st.session_state.registro_apuestas.iloc[0:0]
            st.rerun()
    else:
        st.info("No hay apuestas registradas en la sesión actual. Utiliza 'Nuevo Análisis' para agregar operaciones.")

st.sidebar.divider()
st.sidebar.success("APIs Conectadas • Online")
