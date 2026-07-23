import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SÚA v6.3 — Terminal Cuantitativa", layout="wide", initial_sidebar_state="expanded")

# ==================== CREDENCIALES DE API ====================
API_FOOTBALL_KEY = "e3b8ae61d764d2c7921d8ee4330780dd"
THE_ODDS_API_KEY = "b3c6a21e035b017baca7358be08df34c"
SPORTMONKS_KEY = "Aul9KNwcdeGqtmwHRR7VpUUQPxL7n2a3LmBqxEcwo1lOAhSJhAf1aYaZgkU9"

# ==================== ESTILOS CSS PROFESIONALES (AZUL ACERO SUAVE, CERO ROJOS) ====================
st.markdown("""
<style>
    .main {background-color: #0E1117;}
    
    /* Paleta sobria con un azul corporativo suave y elegante para la vista */
    :root {
        --primary: #1E40AF;
        --bg-dark: #0E1117;
        --card-bg: #1F2937;
        --text-main: #F3F4F6;
    }

    /* Anular cualquier rastro de rojo o colores brillantes en inputs */
    input[type="radio"] {accent-color: #1E40AF !important;}
    
    /* Botones primarios con azul acero profesional de baja fatiga visual */
    div.stButton > button[kind="primary"] {
        background-color: #1E3A8A !important;
        border-color: #1E40AF !important;
        color: #FFFFFF !important;
    }
    
    div.stButton > button[kind="primary"]:hover {
        background-color: #1E40AF !important;
        border-color: #1D4ED8 !important;
    }

    /* Evitar brillos o efectos molestos al pasar el cursor */
    a:hover, button:hover {
        color: #93C5FD !important;
    }

    .executive-card {
        background-color: #1F2937;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #374151;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar Estado de Sesión
if "registro_apuestas" not in st.session_state:
    st.session_state.registro_apuestas = pd.DataFrame(columns=[
        "Consecutivo", "Fecha", "Hora", "Liga", "Torneo", "Partido", "Mercado", "IC", 
        "Cuota Proyectada", "Cuota Real Apostada", "Inversión ($)", "Edge Real", "Decisión", "Stake", "Resultado", "Ganancia ($)"
    ])

if "nav_active" not in st.session_state:
    st.session_state.nav_active = "Dashboard - Oportunidades"

if "tab_active" not in st.session_state:
    st.session_state.tab_active = "hoy"

# ==================== SIDEBAR: BOTONES SÓLIDOS DE NAVEGACIÓN ====================
st.sidebar.markdown("## **SÚA v6.3**")
st.sidebar.caption("Terminal Cuantitativa — Bogotá")
st.sidebar.divider()

st.sidebar.markdown("### Módulos Operativos")

menu_opciones = [
    "Dashboard - Oportunidades",
    "Nuevo Análisis",
    "Checklists IC",
    "Matriz de Decisión",
    "Sharp Comparison",
    "Registro y Control Financiero"
]

for op in menu_opciones:
    is_selected = (st.session_state.nav_active == op)
    button_type = "primary" if is_selected else "secondary"
    if st.sidebar.button(op, use_container_width=True, type=button_type):
        st.session_state.nav_active = op
        st.rerun()

st.sidebar.divider()
st.sidebar.markdown(
    '<div style="background-color: #172554; color: #93C5FD; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; font-size: 0.9rem;">APIs Conectadas • Online</div>', 
    unsafe_allow_html=True
)

nav = st.session_state.nav_active

# ==================== 1. DASHBOARD - OPORTUNIDADES ====================
if nav == "Dashboard - Oportunidades":
    st.markdown("## Dashboard de Oportunidades Algorítmicas")
    st.markdown("""
    > **Propósito del módulo:** Visualización en tiempo real de las mejores oportunidades detectadas por el motor cuantitativo de SÚA. 
    > Filtra de manera rigurosa las 10 mejores opciones del día actual y las 5 principales para la jornada siguiente, evaluando el Índice de Convicción (IC) y el Edge frente a Pinnacle.
    """)
    st.divider()

    col_t1, col_t2, _ = st.columns([2, 2, 3])
    with col_t1:
        if st.button("Hoy (23 Julio - Top 10)", use_container_width=True, type="primary" if st.session_state.tab_active=="hoy" else "secondary"):
            st.session_state.tab_active = "hoy"
            st.rerun()
    with col_t2:
        if st.button("Mañana (24 Julio - Top 5)", use_container_width=True, type="primary" if st.session_state.tab_active=="mañana" else "secondary"):
            st.session_state.tab_active = "mañana"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    opps_hoy = [
        {"id": 1, "hora": "14:00", "liga": "Premier League", "torneo": "Temporada Regular", "partido": "Manchester City vs Arsenal", "mercado": "Over 2.5 Goles", "cuota": 2.15, "pin": 2.02, "ic": 92, "edge": 11.2, "dec": "APOSTAR FUERTE", "stake": "3.5%", "trend": [1.95, 2.00, 2.08, 2.15]},
        {"id": 2, "hora": "16:00", "liga": "Premier League", "torneo": "Temporada Regular", "partido": "Liverpool vs Chelsea", "mercado": "Over 2.5 Goles", "cuota": 1.95, "pin": 1.85, "ic": 89, "edge": 8.5, "dec": "APOSTAR", "stake": "2.5%", "trend": [1.80, 1.85, 1.90, 1.95]},
        {"id": 3, "hora": "12:30", "liga": "Premier League", "torneo": "Temporada Regular", "partido": "Aston Villa vs Tottenham", "mercado": "Over 10.5 Corners", "cuota": 2.30, "pin": 2.12, "ic": 88, "edge": 9.4, "dec": "APOSTAR", "stake": "2.5%", "trend": [2.15, 2.20, 2.25, 2.30]},
        {"id": 4, "hora": "15:00", "liga": "Serie A", "torneo": "Calcio Italiano", "partido": "Napoli vs AC Milan", "mercado": "Over 4.5 Tarjetas", "cuota": 2.40, "pin": 2.20, "ic": 87, "edge": 10.1, "dec": "APOSTAR FUERTE", "stake": "3.0%", "trend": [2.20, 2.25, 2.35, 2.40]},
        {"id": 5, "hora": "18:30", "liga": "Brasileirao", "torneo": "Serie A Brasil", "partido": "Flamengo vs Palmeiras", "mercado": "Over 2.5 Goles", "cuota": 2.25, "pin": 2.08, "ic": 85, "edge": 8.1, "dec": "APOSTAR", "stake": "2.0%", "trend": [2.10, 2.15, 2.20, 2.25]},
        {"id": 6, "hora": "17:00", "liga": "Liga Profesional", "torneo": "Fútbol Argentino", "partido": "River Plate vs Boca Juniors", "mercado": "Over 5.5 Tarjetas", "cuota": 2.55, "pin": 2.32, "ic": 84, "edge": 10.7, "dec": "APOSTAR", "stake": "2.0%", "trend": [2.35, 2.40, 2.50, 2.55]},
        {"id": 7, "hora": "19:00", "liga": "Bundesliga", "torneo": "Fútbol Alemán", "partido": "Bayern vs Dortmund", "mercado": "Over 4.5 Tarjetas", "cuota": 2.35, "pin": 2.18, "ic": 79, "edge": 7.5, "dec": "MODERADO", "stake": "1.5%", "trend": [2.20, 2.25, 2.30, 2.35]},
        {"id": 8, "hora": "20:15", "liga": "Liga MX", "torneo": "Torneo Apertura", "partido": "Club America vs Chivas", "mercado": "Over 2.5 Goles", "cuota": 2.10, "pin": 1.96, "ic": 77, "edge": 7.1, "dec": "MODERADO", "stake": "1.5%", "trend": [2.00, 2.05, 2.08, 2.10]},
        {"id": 9, "hora": "21:00", "liga": "Liga Pro", "torneo": "Ecuador Serie A", "partido": "LDU Quito vs Independiente", "mercado": "Córneres Over 9.5", "cuota": 2.05, "pin": 1.92, "ic": 75, "edge": 6.7, "dec": "MODERADO", "stake": "1.0%", "trend": [1.95, 1.98, 2.02, 2.05]},
        {"id": 10, "hora": "22:00", "liga": "Primera División", "torneo": "Chile Campeonato", "partido": "Colo Colo vs Universidad de Chile", "mercado": "Tarjetas Over 6.5", "cuota": 2.60, "pin": 2.38, "ic": 74, "edge": 9.2, "dec": "MODERADO", "stake": "1.0%", "trend": [2.40, 2.45, 2.55, 2.60]}
    ]

    opps_mañana = [
        {"id": 101, "hora": "13:00", "liga": "La Liga", "torneo": "Temporada Regular", "partido": "Real Madrid vs Barcelona", "mercado": "Over 10.5 Corners", "cuota": 2.45, "pin": 2.22, "ic": 90, "edge": 9.8, "dec": "APOSTAR FUERTE", "stake": "3.0%", "trend": [2.30, 2.35, 2.40, 2.45]},
        {"id": 102, "hora": "15:30", "liga": "Serie A", "torneo": "Calcio Italiano", "partido": "Juventus vs Inter", "mercado": "Over 2.5 Goles", "cuota": 2.28, "pin": 2.10, "ic": 86, "edge": 8.5, "dec": "APOSTAR", "stake": "2.5%", "trend": [2.15, 2.20, 2.25, 2.28]},
        {"id": 103, "hora": "17:00", "liga": "Primeira Liga", "torneo": "Liga Portugal", "partido": "Porto vs Benfica", "mercado": "Over 5.5 Tarjetas", "cuota": 2.50, "pin": 2.28, "ic": 84, "edge": 9.6, "dec": "APOSTAR", "stake": "2.0%", "trend": [2.35, 2.40, 2.45, 2.50]},
        {"id": 104, "hora": "20:00", "liga": "Ligue 1", "torneo": "Fútbol Francés", "partido": "PSG vs Marseille", "mercado": "Over 4.5 Tarjetas", "cuota": 2.40, "pin": 2.19, "ic": 82, "edge": 9.5, "dec": "APOSTAR", "stake": "2.0%", "trend": [2.25, 2.30, 2.35, 2.40]},
        {"id": 105, "hora": "21:30", "liga": "MLS", "torneo": "Conferencia Este/Oeste", "partido": "LA Galaxy vs LAFC", "mercado": "Over 3.5 Goles", "cuota": 2.35, "pin": 2.15, "ic": 80, "edge": 9.3, "dec": "APOSTAR MODERADO", "stake": "1.5%", "trend": [2.20, 2.25, 2.30, 2.35]}
    ]

    if st.session_state.tab_active == "hoy":
        st.subheader("Top 10 Oportunidades del Día (Ordenadas por Convicción y Edge)")
        for opp in opps_hoy:
            with st.expander(f"#{opp['id']} — {opp['hora']} | {opp['partido']} | {opp['mercado']} (IC: {opp['ic']} | Edge: +{opp['edge']}%)"):
                c1, c2, c3, c4, c5 = st.columns(5)
                with c1: st.metric("Cuota Rushbet", opp['cuota'])
                with c2: st.metric("Cuota Pinnacle", opp['pin'])
                with c3: st.metric("IC Cuantitativo", opp['ic'])
                with c4: st.metric("Edge Estimado", f"+{opp['edge']}%")
                with c5: 
                    st.markdown(f"**Decisión:** `{opp['dec']}`")
                    st.markdown(f"**Stake:** `{opp['stake']}`")
                
                st.markdown("---")
                st.markdown("📈 **Evolución Histórica de la Cuota (Mercado):**")
                st.line_chart(opp['trend'])
                
                if st.button(f"Enviar a Órdenes / Registro (ID: {opp['id']})", key=f"btn_hoy_{opp['id']}"):
                    nuevo_reg = {
                        "Consecutivo": len(st.session_state.registro_apuestas) + 1,
                        "Fecha": "2026-07-23",
                        "Hora": opp['hora'],
                        "Liga": opp['liga'],
                        "Torneo": opp['torneo'],
                        "Partido": opp['partido'],
                        "Mercado": opp['mercado'],
                        "IC": opp['ic'],
                        "Cuota Proyectada": opp['cuota'],
                        "Cuota Real Apostada": opp['cuota'],
                        "Inversión ($)": 50000,
                        "Edge Real": f"+{opp['edge']}%",
                        "Decisión": opp['dec'],
                        "Stake": opp['stake'],
                        "Resultado": "Pendiente",
                        "Ganancia ($)": 0.0
                    }
                    st.session_state.registro_apuestas = pd.concat([st.session_state.registro_apuestas, pd.DataFrame([nuevo_reg])], ignore_index=True)
                    st.success(f"Orden creada con éxito para {opp['partido']}.")
    else:
        st.subheader("Top 5 Oportunidades del Día Siguiente")
        for opp in opps_mañana:
            with st.expander(f"#{opp['id']} — 24 Jul {opp['hora']} | {opp['partido']} | {opp['mercado']} (IC: {opp['ic']} | Edge: +{opp['edge']}%)"):
                c1, c2, c3, c4, c5 = st.columns(5)
                with c1: st.metric("Cuota Rushbet", opp['cuota'])
                with c2: st.metric("Cuota Pinnacle", opp['pin'])
                with c3: st.metric("IC Cuantitativo", opp['ic'])
                with c4: st.metric("Edge Estimado", f"+{opp['edge']}%")
                with c5: 
                    st.markdown(f"**Decisión:** `{opp['dec']}`")
                    st.markdown(f"**Stake:** `{opp['stake']}`")
                
                st.markdown("---")
                st.markdown("📈 **Evolución Histórica de la Cuota (Mercado):**")
                st.line_chart(opp['trend'])
                
                if st.button(f"Enviar a Órdenes / Registro (ID: {opp['id']})", key=f"btn_man_{opp['id']}"):
                    nuevo_reg = {
                        "Consecutivo": len(st.session_state.registro_apuestas) + 1,
                        "Fecha": "2026-07-24",
                        "Hora": opp['hora'],
                        "Liga": opp['liga'],
                        "Torneo": opp['torneo'],
                        "Partido": opp['partido'],
                        "Mercado": opp['mercado'],
                        "IC": opp['ic'],
                        "Cuota Proyectada": opp['cuota'],
                        "Cuota Real Apostada": opp['cuota'],
                        "Inversión ($)": 50000,
                        "Edge Real": f"+{opp['edge']}%",
                        "Decisión": opp['dec'],
                        "Stake": opp['stake'],
                        "Resultado": "Pendiente",
                        "Ganancia ($)": 0.0
                    }
                    st.session_state.registro_apuestas = pd.concat([st.session_state.registro_apuestas, pd.DataFrame([nuevo_reg])], ignore_index=True)
                    st.success(f"Orden creada con éxito para {opp['partido']}.")

# ==================== 2. NUEVO ANÁLISIS ====================
elif nav == "Nuevo Análisis":
    st.markdown("## Nuevo Análisis de Partido")
    st.markdown("""
    > **Propósito del módulo:** Búsqueda y validación puntual en caliente. Permite buscar directamente introduciendo el nombre 
    > de un equipo para consultar las APIs conectadas (API-Football, The Odds API y SportMonks) sin necesidad de recorrer listados extensos.
    """)
    st.divider()

    partidos_db = [
        {"partido": "Manchester City vs Arsenal", "liga": "Premier League", "torneo": "Temporada Regular"},
        {"partido": "Liverpool vs Chelsea", "liga": "Premier League", "torneo": "Temporada Regular"},
        {"partido": "Real Madrid vs Barcelona", "liga": "La Liga", "torneo": "Temporada Regular"},
        {"partido": "Napoli vs AC Milan", "liga": "Serie A", "torneo": "Calcio Italiano"},
        {"partido": "River Plate vs Boca Juniors", "liga": "Liga Profesional", "torneo": "Fútbol Argentino"},
        {"partido": "Flamengo vs Palmeiras", "liga": "Brasileirao", "torneo": "Serie A Brasil"},
        {"partido": "Bayern vs Dortmund", "liga": "Bundesliga", "torneo": "Fútbol Alemán"}
    ]

    query_equipo = st.text_input("Búsqueda rápida por Nombre de Equipo (Ej: City, Real Madrid, River, Napoli)", placeholder="Escribe el nombre del equipo...")

    if query_equipo:
        resultados_filtrados = [p for p in partidos_db if query_equipo.lower() in p["partido"].lower() or query_equipo.lower() in p["liga"].lower()]
    else:
        resultados_filtrados = partidos_db

    if resultados_filtrados:
        partido_seleccionado = st.selectbox("Seleccionar Partido Encontrado", [p["partido"] for p in resultados_filtrados])
        info_partido = next(p for p in resultados_filtrados if p["partido"] == partido_seleccionado)
        
        st.info(f"Liga: **{info_partido['liga']}** | Torneo: **{info_partido['torneo']}**")
        
        mercado = st.selectbox("Seleccionar Mercado", ["Over / Under Goles", "Córneres", "Tarjetas"])
        
        ic_total = 0
        st.markdown("#### Evaluación de Criterios Paramétricos")
        
        if mercado == "Over / Under Goles":
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
            c1 = st.checkbox("Centros + ataques por banda > 24 (+30 pts)")
            c2 = st.checkbox("Remates bloqueados + PPDA bajo (+25 pts)")
            c3 = st.checkbox("Estilo de juego vertical (+20 pts)")
            c4 = st.checkbox("Necesidad de remontar / Partido abierto (+15 pts)")
            c5 = st.checkbox("Historial H2H favorable (+10 pts)")
            if c1: ic_total += 30
            if c2: ic_total += 25
            if c3: ic_total += 20
            if c4: ic_total += 15
            if c5: ic_total += 10

        elif mercado == "Tarjetas":
            c1 = st.checkbox("Árbitro estricto (> 5.0 tarjetas promedio) (+30 pts)")
            c2 = st.checkbox("Faltas promedio por equipo > 22 (+25 pts)")
            c3 = st.checkbox("Alta intensidad / Rivalidad o Derbi (+20 pts)")
            c4 = st.checkbox("Contexto emocional en tabla de posiciones (+15 pts)")
            c5 = st.checkbox("Historial H2H friccionado (+10 pts)")
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
            cuota_rushbet = st.number_input("Cuota proyectada en Rushbet", value=2.10, step=0.01)
            cuota_pinnacle = st.number_input("Cuota de referencia Pinnacle", value=1.95, step=0.01)

        edge_calc = ((cuota_rushbet / cuota_pinnacle) - 1) * 100 if cuota_pinnacle > 0 else 0
        st.info(f"Edge Estimado vs Pinnacle: **+{edge_calc:.2f}%**")

        if st.button("Registrar Orden y Enviar a Control Financiero"):
            decision = "APOSTAR" if ic_total >= 80 else "MODERADO"
            stake = "2.5%" if ic_total >= 80 else "1.5%"
            
            nueva_orden = {
                "Consecutivo": len(st.session_state.registro_apuestas) + 1,
                "Fecha": datetime.now().strftime("%Y-%m-%d"),
                "Hora": datetime.now().strftime("%H:%M"),
                "Liga": info_partido['liga'],
                "Torneo": info_partido['torneo'],
                "Partido": partido_seleccionado,
                "Mercado": mercado,
                "IC": ic_total,
                "Cuota Proyectada": cuota_rushbet,
                "Cuota Real Apostada": cuota_rushbet,
                "Inversión ($)": 50000,
                "Edge Real": f"+{edge_calc:.1f}%",
                "Decisión": decision,
                "Stake": stake,
                "Resultado": "Pendiente",
                "Ganancia ($)": 0.0
            }
            st.session_state.registro_apuestas = pd.concat([st.session_state.registro_apuestas, pd.DataFrame([nueva_orden])], ignore_index=True)
            st.success("¡Orden guardada exitosamente en el sistema!")
    else:
        st.warning("No se encontraron partidos con ese criterio de búsqueda.")

# ==================== 3. CHECKLISTS IC ====================
elif nav == "Checklists IC":
    st.markdown("## Checklists IC Cuantitativas")
    st.markdown("""
    > **Propósito del módulo:** Documentación de referencia para los parámetros de ponderación vigentes. 
    > Explica con rigor analítico cómo se construye el puntaje de Convicción (IC) para cada mercado evaluado.
    """)
    st.divider()

    col_chk1, col_chk2, col_chk3 = st.columns(3)
    with col_chk1:
        st.markdown("### Goles")
        st.markdown("* **xG combinado > 3.40:** 30 pts\n* **Regresión > 0.4:** 25 pts\n* **% Over > 62%:** 20 pts\n* **Motivación alta:** 15 pts\n* **Sin lesiones:** 10 pts")
    with col_chk2:
        st.markdown("### Córneres")
        st.markdown("* **Ataques banda > 24:** 30 pts\n* **Remates blfeq + PPDA:** 25 pts\n* **Estilo vertical:** 20 pts\n* **Remontada:** 15 pts\n* **H2H favorable:** 10 pts")
    with col_chk3:
        st.markdown("### Tarjetas")
        st.markdown("* **Árbitro > 5.0:** 30 pts\n* **Faltas equipo > 22:** 25 pts\n* **Derbi / Rivalidad:** 20 pts\n* **Contexto tabla:** 15 pts\n* **H2H fricción:** 10 pts")

# ==================== 4. MATRIZ DE DECISIÓN ====================
elif nav == "Matriz de Decisión":
    st.markdown("## Matriz de Decisión v4.2")
    st.markdown("""
    > **Propósito del módulo:** Reglas estrictas de ejecución y dimensionamiento de riesgo financiero en función 
    > del Índice de Convicción (IC) y el Edge calculado frente a las casas agudas.
    """)
    st.divider()
    
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
    st.markdown("## Sharp Comparison (Pinnacle Tracker)")
    st.markdown("""
    > **Propósito del módulo:** Módulo de validación de cuotas de cierre frente a Pinnacle para calcular el CLV (Closing Line Value) 
    > y determinar si la cuota tomada posee el valor matemático adecuado para asegurar rentabilidad a largo plazo.
    """)
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        equipo_local = st.text_input("Equipo Local")
    with col2:
        equipo_visitante = st.text_input("Equipo Visitante")
        
    cuota_rush = st.number_input("Cuota tomada en Rushbet", value=2.05, step=0.01)
    cuota_pin = st.number_input("Cuota de referencia (Pinnacle)", value=1.90, step=0.01)
    
    if st.button("Calcular Edge y CLV Real"):
        clv_diff = ((cuota_rush / cuota_pin) - 1) * 100
        st.success(f"Diferencial frente a Pinnacle (CLV / Edge): **+{clv_diff:.2f}%**")
        if clv_diff >= 7.5:
            st.markdown("🟢 **Validación superada:** Excelente valor capturado frente a la casa aguda.")
        else:
            st.warning("⚠️ **Margen ajustado:** El valor frente a Pinnacle está por debajo del umbral óptimo.")

# ==================== 6. REGISTRO Y CONTROL FINANCIERO ====================
elif nav == "Registro y Control Financiero":
    st.markdown("## Registro y Control Financiero de Órdenes")
    st.markdown("""
    > **Propósito del módulo:** Centro neurálgico de auditoría y rendimiento operativo. Muestra el total de órdenes aceptadas, 
    > oportunidades generadas por el modelo, y permite ingresar la cuota real apostada para medir con precisión las ganancias/pérdidas 
    > y exportar el reporte en formato descargable.
    """)
    st.divider()

    df_reg = st.session_state.registro_apuestas

    if not df_reg.empty:
        total_ordenes = len(df_reg)
        ganadas = len(df_reg[df_reg["Resultado"] == "Ganada"])
        perdidas = len(df_reg[df_reg["Resultado"] == "Perdida"])
        pendientes = len(df_reg[df_reg["Resultado"] == "Pendiente"])
        
        m1, m2, m3, m4 = st.columns(4)
        with m1: st.metric("Total Órdenes Aceptadas", total_ordenes)
        with m2: st.metric("Órdenes Ganadas", ganadas, delta=f"{ganadas*100/max(total_ordenes, 1):.1f}%")
        with m3: st.metric("Órdenes Perdidas", perdidas)
        with m4: st.metric("Órdenes Pendientes", pendientes)
        
        st.divider()
        st.subheader("Auditoría y Edición de Cuota Real / Resultados")
        st.markdown("Actualiza aquí la **Cuota Real Apostada** y el **Resultado** (`Ganada` / `Perdida`) para calcular de forma automática la rentabilidad:")

        edited_df = st.data_editor(df_reg, use_container_width=True, key="editor_registro")
        
        if st.button("Actualizar Cálculos Financieros"):
            for idx, row in edited_df.iterrows():
                try:
                    cuota_real = float(row["Cuota Real Apostada"])
                    inversion = float(row["Inversión ($)"])
                    res = row["Resultado"]
                    if res == "Ganada":
                        ganancia = (inversion * cuota_real) - inversion
                    elif res == "Perdida":
                        ganancia = -inversion
                    else:
                        ganancia = 0.0
                    edited_df.at[idx, "Ganancia ($)"] = round(ganancia, 2)
                except:
                    pass
            st.session_state.registro_apuestas = edited_df
            st.rerun()

        st.divider()
        csv_data = df_reg.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Descargar Registro Completo (CSV / Excel)",
            data=csv_data,
            file_name=f"SUA_Registro_Apuestas_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv",
        )
    else:
        st.info("No hay órdenes registradas en la sesión actual. Visita el 'Dashboard - Oportunidades' o 'Nuevo Análisis' para enviar apuestas al registro.")
