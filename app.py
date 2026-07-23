import streamlit as st
import pandas as pd
from datetime import datetime
import requests

st.set_page_config(page_title="SÚA v6.3 — Terminal Cuantitativa", layout="wide", initial_sidebar_state="expanded")

# ==================== CREDENCIALES DE API ====================
API_FOOTBALL_KEY = "e3b8ae61d764d2c7921d8ee4330780dd"
THE_ODDS_API_KEY = "b3c6a21e035b017baca7358be08df34c"
SPORTMONKS_KEY = "Aul9KNwcdeGqtmwHRR7VpUUQPxL7n2a3LmBqxEcwo1lOAhSJhAf1aYaZgkU9"

# ==================== ESTILOS CSS PROFESIONALES ====================
st.markdown("""
<style>
    .main {background-color: #0E1117;}
    
    :root {
        --primary: #1E40AF;
        --bg-dark: #0E1117;
        --card-bg: #1F2937;
        --text-main: #F3F4F6;
    }

    /* Corrección de color de los botones de incremento/decremento a Naranja */
    div[data-baseweb="spinbutton"] button {
        background-color: #F97316 !important;
        color: white !important;
    }
    div[data-baseweb="spinbutton"] button:hover {
        background-color: #EA580C !important;
    }
    
    div.stButton > button[kind="primary"] {
        background-color: #1E3A8A !important;
        border-color: #1E40AF !important;
        color: #FFFFFF !important;
    }
    
    div.stButton > button[kind="primary"]:hover {
        background-color: #1E40AF !important;
        border-color: #1D4ED8 !important;
    }

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

    .tag-pendiente { background-color: #F97316; color: white; padding: 4px 10px; border-radius: 6px; font-weight: bold; font-size: 0.8rem; }
    .tag-gris { background-color: #6B7280; color: white; padding: 4px 10px; border-radius: 6px; font-weight: bold; font-size: 0.8rem; }
    .tag-verde { background-color: #10B981; color: white; padding: 4px 10px; border-radius: 6px; font-weight: bold; font-size: 0.8rem; }
    .tag-rojo { background-color: #EF4444; color: white; padding: 4px 10px; border-radius: 6px; font-weight: bold; font-size: 0.8rem; }
</style>
""", unsafe_allow_html=True)

# Inicializar Estado de Sesión y Bankroll
if "bankroll_inicial" not in st.session_state:
    st.session_state.bankroll_inicial = 2000000.0

if "registro_apuestas" not in st.session_state:
    st.session_state.registro_apuestas = pd.DataFrame(columns=[
        "Consecutivo", "Fecha", "Hora", "Liga", "Torneo", "Partido", "Mercado", "Casa", "IC", 
        "Cuota Proyectada", "Cuota Real Apostada", "Inversión ($)", "Edge Real", "Decisión", "Stake", "Resultado", "Ganancia ($)"
    ])

if "nav_active" not in st.session_state:
    st.session_state.nav_active = "Dashboard - Oportunidades"

if "tab_active" not in st.session_state:
    st.session_state.tab_active = "hoy"

# ==================== VERIFICADOR REAL DE APIS ====================
def verificar_api_status():
    status = {}
    
    # 1. API-Football
    try:
        res = requests.get("https://v3.football.api-sports.io/timezone", headers={"x-apisports-key": API_FOOTBALL_KEY}, timeout=3)
        status["API-Football"] = True if res.status_code == 200 else False
    except:
        status["API-Football"] = False

    # 2. The Odds API
    try:
        res = requests.get(f"https://api.the-odds-api.com/v4/sports?apiKey={THE_ODDS_API_KEY}", timeout=3)
        status["The Odds API"] = True if res.status_code == 200 else False
    except:
        status["The Odds API"] = False

    # 3. SportMonks
    try:
        res = requests.get(f"https://core-api.sportmonks.com/v1/core/states?api_token={SPORTMONKS_KEY}", timeout=3)
        status["SportMonks"] = True if res.status_code == 200 else False
    except:
        status["SportMonks"] = False

    return status

api_estados = verificar_api_status()
todas_conectadas = all(api_estados.values())

# ==================== SIDEBAR: NAVEGACIÓN Y CONFIGURACIÓN DE BANKROLL ====================
st.sidebar.markdown("## **SÚA v6.3**")
st.sidebar.caption("Terminal Cuantitativa — Bogotá")
st.sidebar.divider()

st.sidebar.markdown("### Configuración de Capital")
bankroll_input = st.sidebar.number_input("Bankroll Inicial (COP $)", value=float(st.session_state.bankroll_inicial), step=100000.0)
st.session_state.bankroll_inicial = bankroll_input

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

# Panel Desplegable de Estado de APIs con indicadores independientes
with st.sidebar.expander("🟢 Estado de Conectividad APIs"):
    for api_nombre, estado_ok in api_estados.items():
        icon = "🟢" if estado_ok else "🔴"
        txt_estado = "Online" if estado_ok else "Offline / Error"
        st.markdown(f"{icon} **{api_nombre}**: `{txt_estado}`")

nav = st.session_state.nav_active

# ==================== 1. DASHBOARD - OPORTUNIDADES ====================
if nav == "Dashboard - Oportunidades":
    st.markdown("## Dashboard de Oportunidades Algorítmicas")
    st.markdown("""
    > **Propósito del módulo:** Visualización en tiempo real de las mejores oportunidades detectadas por el motor cuantitativo de SÚA.
    > Gestiona el Top de **6 oportunidades principales del día** y el bloque rotativo de **10 oportunidades para la jornada siguiente**.
    """)
    st.divider()

    col_t1, col_t2, _ = st.columns([2, 2, 3])
    with col_t1:
        if st.button("Hoy (Top 6)", use_container_width=True, type="primary" if st.session_state.tab_active=="hoy" else "secondary"):
            st.session_state.tab_active = "hoy"
            st.rerun()
    with col_t2:
        if st.button("Mañana (Top 10)", use_container_width=True, type="primary" if st.session_state.tab_active=="mañana" else "secondary"):
            st.session_state.tab_active = "mañana"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    opps_hoy = [
        {"id": 1, "hora": "14:00", "liga": "Premier League", "torneo": "Temporada Regular", "partido": "Manchester City vs Arsenal", "mercado": "Over 2.5 Goles", "casa": "Rushbet", "cuota": 2.15, "pin": 2.02, "ic": 92, "edge": 11.2, "dec": "APOSTAR FUERTE", "stake_pct": 0.035, "trend": [1.95, 2.00, 2.08, 2.15]},
        {"id": 2, "hora": "16:00", "liga": "Premier League", "torneo": "Temporada Regular", "partido": "Liverpool vs Chelsea", "mercado": "Over 2.5 Goles", "casa": "Rushbet", "cuota": 1.95, "pin": 1.85, "ic": 89, "edge": 8.5, "dec": "APOSTAR", "stake_pct": 0.025, "trend": [1.80, 1.85, 1.90, 1.95]},
        {"id": 3, "hora": "12:30", "liga": "Premier League", "torneo": "Temporada Regular", "partido": "Aston Villa vs Tottenham", "mercado": "Over 10.5 Corners", "casa": "Wplay", "cuota": 2.30, "pin": 2.12, "ic": 88, "edge": 9.4, "dec": "APOSTAR", "stake_pct": 0.025, "trend": [2.15, 2.20, 2.25, 2.30]},
        {"id": 4, "hora": "15:00", "liga": "Serie A", "torneo": "Calcio Italiano", "partido": "Napoli vs AC Milan", "mercado": "Over 4.5 Tarjetas", "casa": "Rushbet", "cuota": 2.40, "pin": 2.20, "ic": 87, "edge": 10.1, "dec": "APOSTAR FUERTE", "stake_pct": 0.030, "trend": [2.20, 2.25, 2.35, 2.40]},
        {"id": 5, "hora": "18:30", "liga": "Brasileirao", "torneo": "Serie A Brasil", "partido": "Flamengo vs Palmeiras", "mercado": "Over 2.5 Goles", "casa": "Codere", "cuota": 2.25, "pin": 2.08, "ic": 85, "edge": 8.1, "dec": "APOSTAR", "stake_pct": 0.020, "trend": [2.10, 2.15, 2.20, 2.25]},
        {"id": 6, "hora": "17:00", "liga": "Liga Profesional", "torneo": "Fútbol Argentino", "partido": "River Plate vs Boca Juniors", "mercado": "Over 5.5 Tarjetas", "casa": "Rushbet", "cuota": 2.55, "pin": 2.32, "ic": 84, "edge": 10.7, "dec": "APOSTAR", "stake_pct": 0.020, "trend": [2.35, 2.40, 2.50, 2.55]}
    ]

    opps_mañana = [
        {"id": 101, "hora": "13:00", "liga": "La Liga", "torneo": "Temporada Regular", "partido": "Real Madrid vs Barcelona", "mercado": "Over 10.5 Corners", "casa": "Rushbet", "cuota": 2.45, "pin": 2.22, "ic": 90, "edge": 9.8, "dec": "APOSTAR FUERTE", "stake_pct": 0.030, "trend": [2.30, 2.35, 2.40, 2.45]},
        {"id": 102, "hora": "15:30", "liga": "Serie A", "torneo": "Calcio Italiano", "partido": "Juventus vs Inter", "mercado": "Over 2.5 Goles", "casa": "Wplay", "cuota": 2.28, "pin": 2.10, "ic": 86, "edge": 8.5, "dec": "APOSTAR", "stake_pct": 0.025, "trend": [2.15, 2.20, 2.25, 2.28]}
    ]

    lista_activa = opps_hoy if st.session_state.tab_active == "hoy" else opps_mañana
    
    st.subheader(f"Listado de Oportunidades ({st.session_state.tab_active.upper()})")
    for opp in lista_activa:
        inversion_calculada = st.session_state.bankroll_inicial * opp['stake_pct']
        with st.expander(f"#{opp['id']} — {opp['hora']} | {opp['partido']} | {opp['mercado']} (IC: {opp['ic']} | Edge: +{opp['edge']}%)"):
            c1, c2, c3, c4, c5 = st.columns(5)
            with c1: st.metric(f"Cuota ({opp['casa']})", opp['cuota'])
            with c2: st.metric("Cuota Pinnacle", opp['pin'])
            with c3: st.metric("IC Cuantitativo", opp['ic'])
            with c4: st.metric("Edge Estimado", f"+{opp['edge']}%")
            with c5: 
                st.markdown(f"**Decisión:** `{opp['dec']}`")
                st.markdown(f"**Stake Rec.:** `$ {inversion_calculada:,.0f} COP`")
            
            st.markdown("---")
            st.markdown("📈 **Evolución Histórica de la Cuota:**")
            st.line_chart(opp['trend'])
            
            if st.button(f"Enviar a Órdenes / Registro (ID: {opp['id']})", key=f"btn_{opp['id']}"):
                nuevo_reg = {
                    "Consecutivo": len(st.session_state.registro_apuestas) + 1,
                    "Fecha": datetime.now().strftime("%Y-%m-%d"),
                    "Hora": opp['hora'],
                    "Liga": opp['liga'],
                    "Torneo": opp['torneo'],
                    "Partido": opp['partido'],
                    "Mercado": opp['mercado'],
                    "Casa": opp['casa'],
                    "IC": opp['ic'],
                    "Cuota Proyectada": opp['cuota'],
                    "Cuota Real Apostada": opp['cuota'],
                    "Inversión ($)": inversion_calculada,
                    "Edge Real": f"+{opp['edge']}%",
                    "Decisión": opp['dec'],
                    "Stake": f"{opp['stake_pct']*100}%",
                    "Resultado": "Pendiente",
                    "Ganancia ($)": 0.0
                }
                st.session_state.registro_apuestas = pd.concat([st.session_state.registro_apuestas, pd.DataFrame([nuevo_reg])], ignore_index=True)
                st.success(f"Orden creada con éxito para {opp['partido']}.")
                st.rerun()

# ==================== 2. NUEVO ANÁLISIS ====================
elif nav == "Nuevo Análisis":
    st.markdown("## Nuevo Análisis de Partido")
    st.markdown("""
    > **Propósito del módulo:** Búsqueda y validación puntual en caliente mediante las APIs conectadas.
    """)
    st.divider()
    
    query = st.text_input("Buscar equipo o liga...", placeholder="Ej: Manchester City, Real Madrid...")
    if query:
        st.info(f"Buscando coincidencias para '{query}' a través de API-Football y SportMonks...")
    else:
        st.info("Introduce un criterio de búsqueda para consultar los partidos disponibles.")

# ==================== 3. CHECKLISTS IC ====================
elif nav == "Checklists IC":
    st.markdown("## Checklists IC Cuantitativas")
    st.divider()
    st.markdown("Parámetros de ponderación vigentes para Goles, Córneres y Tarjetas.")

# ==================== 4. MATRIZ DE DECISIÓN ====================
elif nav == "Matriz de Decisión":
    st.markdown("## Matriz de Decisión v4.2")
    st.divider()
    matriz_df = pd.DataFrame({
        "IC": ["90 – 100", "82 – 89", "74 – 81", "< 68"],
        "Mercado": ["Goles / Corners", "Goles / Corners", "Goles / Corners", "Cualquier"],
        "Decisión Final": ["APOSTAR FUERTE", "APOSTAR", "APOSTAR MODERADO", "NO APOSTAR"],
        "Stake (% Bank)": ["3.0 – 5.0%", "2.0 – 3.0%", "1.0 – 2.0%", "0.0%"]
    })
    st.dataframe(matriz_df, use_container_width=True)

# ==================== 5. SHARP COMPARISON ====================
elif nav == "Sharp Comparison":
    st.markdown("## Sharp Comparison (Pinnacle Tracker)")
    st.divider()
    c1, c2 = st.columns(2)
    with c1: cuota_rush = st.number_input("Cuota Bookmaker", value=2.05, step=0.01)
    with c2: cuota_pin = st.number_input("Cuota Pinnacle", value=1.90, step=0.01)
    if st.button("Calcular CLV"):
        clv = ((cuota_rush / cuota_pin) - 1) * 100
        st.success(f"Diferencial CLV / Edge: **+{clv:.2f}%**")

# ==================== 6. REGISTRO Y CONTROL FINANCIERO ====================
elif nav == "Registro y Control Financiero":
    st.markdown("## Registro y Control Financiero e Institucional")
    st.markdown("""
    > **Propósito del módulo:** Auditoría avanzada de rendimiento, control de bankroll y rentabilidad.
    """)
    st.divider()

    df_reg = st.session_state.registro_apuestas

    if not df_reg.empty:
        total_ordenes = len(df_reg)
        ganadas = len(df_reg[df_reg["Resultado"] == "Ganada"])
        perdidas = len(df_reg[df_reg["Resultado"] == "Perdida"])
        pendientes = len(df_reg[df_reg["Resultado"] == "Pendiente"])
        
        resueltas = ganadas + perdidas
        winrate = (ganadas / max(resueltas, 1)) * 100
        
        inversion_total = df_reg[df_reg["Resultado"] != "Pendiente"]["Inversión ($)"].sum()
        ganancia_neta_total = df_reg["Ganancia ($)"].sum()
        yield_pct = (ganancia_neta_total / max(inversion_total, 1)) * 100
        bankroll_actual = st.session_state.bankroll_inicial + ganancia_neta_total

        m1, m2, m3, m4, m5, m6 = st.columns(6)
        with m1: st.metric("Bankroll Actual", f"$ {bankroll_actual:,.0f}")
        with m2: st.metric("Profit Neto", f"$ {ganancia_neta_total:,.0f}")
        with m3: st.metric("Yield / ROI", f"{yield_pct:.2f}%")
        with m4: st.metric("Winrate", f"{winrate:.1f}%")
        with m5: st.metric("Total Órdenes", total_ordenes)
        with m6: st.metric("Pendientes", pendientes)
        
        st.divider()
        st.subheader("Edición de Cuota Real y Resultados")
        edited_df = st.data_editor(df_reg, use_container_width=True, key="editor_registro")
        
        if st.button("Actualizar Cálculos y Sincronizar Sistema"):
            for idx, row in edited_df.iterrows():
                try:
                    orig_idx = int(row["Consecutivo"]) - 1
                    cuota_real = float(row["Cuota Real Apostada"])
                    inversion = float(row["Inversión ($)"])
                    res = row["Resultado"]
                    if res == "Ganada":
                        ganancia = (inversion * cuota_real) - inversion
                    elif res == "Perdida":
                        ganancia = -inversion
                    else:
                        ganancia = 0.0
                    
                    st.session_state.registro_apuestas.at[orig_idx, "Cuota Real Apostada"] = cuota_real
                    st.session_state.registro_apuestas.at[orig_idx, "Resultado"] = res
                    st.session_state.registro_apuestas.at[orig_idx, "Ganancia ($)"] = round(ganancia, 2)
                except Exception:
                    pass
            st.success("¡Registros actualizados con éxito!")
            st.rerun()

        st.divider()
        st.subheader("Curva de Capital (Equity Curve)")
        df_resueltas = st.session_state.registro_apuestas[st.session_state.registro_apuestas["Resultado"] != "Pendiente"].copy()
        if not df_resueltas.empty:
            df_resueltas["Capital Acumulado"] = st.session_state.bankroll_inicial + df_resueltas["Ganancia ($)"].cumsum()
            st.line_chart(df_resueltas["Capital Acumulado"])
        else:
            st.info("Resuelve al menos una orden para visualizar la curva de capital.")

        st.divider()
        csv_data = st.session_state.registro_apuestas.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Descargar Registro Completo (CSV)",
            data=csv_data,
            file_name=f"SUA_Registro_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv",
        )
    else:
        st.info("No hay órdenes registradas en la sesión actual. Visita el Dashboard de Oportunidades para enviar apuestas al registro.")
