# SÚA v6.0 | Quantitative Decision Operating System
import streamlit as st
import pandas as pd
import numpy as np
import math
from datetime import datetime, timedelta

st.set_page_config(
    page_title="SÚA — Quant Intelligence Terminal", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ==========================================
# ESTILOS MAESTROS: APPLE + LINEAR + BLOOMBERG
# ==========================================
TERMINAL_CSS = """
@import url('https://api.fontshare.com/v2/css?f[]=satoshi@900,700,500,400&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&display=swap');

:root {
    --bg-base: #0B0F17;
    --bg-surface: #111827;
    --text-main: #F8FAFC;
    --text-muted: #64748B;
    --accent-blue: #3B82F6;
    --border-subtle: rgba(255, 255, 255, 0.04);
}

body, [class*="css"] {
    font-family: 'Satoshi', sans-serif;
    color: var(--text-main);
    background-color: var(--bg-base);
}

/* Ocultar elementos nativos innecesarios de Streamlit para limpieza total */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Tarjetas Minimalistas Estilo Apple Wallet (Sin cajas pesadas, puro aire) */
.wallet-card {
    background: rgba(17, 24, 39, 0.7);
    border: 1px solid var(--border-subtle);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 20px;
    transition: all 0.2s ease;
    backdrop-filter: blur(10px);
}
.wallet-card:hover {
    border-color: rgba(59, 130, 246, 0.3);
}

/* Tipografía de Métricas Gigantes (Sin componentes nativos) */
.metric-gigantic {
    font-family: 'JetBrains Mono', monospace;
    font-size: 3.2rem;
    font-weight: 800;
    line-height: 1.0;
    color: #FFFFFF;
    letter-spacing: -2px;
}
.metric-label-sub {
    font-family: 'Satoshi', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 6px;
}
</style>
"""

st.markdown(TERMINAL_CSS, unsafe_allow_html=True)

# ==========================================
# HEADER LIMPIO & AIREADO
# ==========================================
fecha_actual_str = datetime.now().strftime("%A, %d de %B de %Y — %H:%M")

st.markdown(f"""
<div style="display:flex; justify-content:space-between; align-items:flex-end; padding: 20px 0 30px 0; border-bottom: 1px solid rgba(255,255,255,0.04); margin-bottom: 30px;">
    <div>
        <div style="font-family:'Satoshi', sans-serif; font-size: 2.8rem; font-weight: 950; letter-spacing: -2px; line-height: 1.0; color: #FFFFFF;">
            SÚ<span style="color: #3B82F6;">A</span>
        </div>
        <div style="font-family:'JetBrains Mono', monospace; font-size: 0.7rem; color: #64748B; text-transform: uppercase; letter-spacing: 5px; margin-top: 8px;">
            Sports Intelligence Engine • {fecha_actual_str}
        </div>
    </div>
    <div style="display:flex; gap:20px; font-family:'JetBrains Mono', monospace; font-size: 0.75rem; color: #64748B;">
        <div>MOTOR: <span style="color:#10B981; font-weight:700;">SYNC</span></div>
        <div>APIs: <span style="color:#3B82F6; font-weight:700;">ACTIVE</span></div>
        <div>YIELD: <span style="color:#F8FAFC; font-weight:700;">+21.4%</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# NAVEGACIÓN MODULAR (ESTILO LINEAR / LIMPIA)
# ==========================================
with st.sidebar:
    st.markdown("<div style='font-family:Satoshi; font-weight:900; font-size:0.9rem; letter-spacing:1px; color:#F8FAFC; margin-bottom:20px;'>SÚA OS v6.0</div>", unsafe_allow_html=True)
    
    nav_tab = st.radio(
        "Navegación", 
        [
            "🏠 Overview", 
            "📈 Markets", 
            "🧠 Intelligence", 
            "🎯 Opportunities", 
            "📊 Portfolio", 
            "📚 Research", 
            "⚙ Settings"
        ], 
        label_visibility="collapsed"
    )
    
    st.markdown("<div style='position:fixed; bottom:30px; font-size:0.65rem; color:#64748B;'>Diego Fernando Quimbayo<br>Compurent S.A.S.</div>", unsafe_allow_html=True)

# ==========================================
# SECCIÓN 1: OVERVIEW (CENTRO DE INTELIGENCIA)
# ==========================================
if nav_tab == "🏠 Overview":
    st.markdown("""
    <div style="font-size: 1.8rem; font-weight: 900; letter-spacing: -1px; margin-bottom: 8px;">
        Buenos días, Diego.
    </div>
    <div style="font-size: 1rem; color: #64748B; margin-bottom: 35px;">
        Hoy el motor procesó <strong style="color:#F8FAFC;">23 oportunidades</strong> en el mercado global, pero solo <strong style="color:#3B82F6;">4 cumplen el estándar estricto SÚA</strong>.
    </div>
    """, unsafe_allow_html=True)

    # Bloque de métricas gigantes (Sin cajas pesadas de Streamlit)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-gigantic">+7.42%</div><div class="metric-label-sub">Edge Promedio Hoy</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-gigantic" style="color:#3B82F6;">94.2</div><div class="metric-label-sub">Score de Confianza (A+)</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-gigantic">80%</div><div class="metric-label-sub">Índice de Salud (Últimos 10)</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-gigantic" style="color:#10B981;">A+</div><div class="metric-label-sub">Calificación de Ciclo</div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### Estados del Sistema", unsafe_allow_html=True)
    
    # Estados limpios tipo Terminal Bloomberg/Linear
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    with col_s1:
        st.markdown('<div class="wallet-card" style="padding:16px;"><div style="font-size:0.65rem; color:#64748B;">MODELO</div><div style="font-size:1.1rem; font-weight:800; color:#10B981; margin-top:4px;">Excelente</div></div>', unsafe_allow_html=True)
    with col_s2:
        st.markdown('<div class="wallet-card" style="padding:16px;"><div style="font-size:0.65rem; color:#64748B;">MERCADO</div><div style="font-size:1.1rem; font-weight:800; color:#3B82F6; margin-top:4px;">Estable</div></div>', unsafe_allow_html=True)
    with col_s3:
        st.markdown('<div class="wallet-card" style="padding:16px;"><div style="font-size:0.65rem; color:#64748B;">LIQUIDEZ</div><div style="font-size:1.1rem; font-weight:800; color:#F8FAFC; margin-top:4px;">Alta</div></div>', unsafe_allow_html=True)
    with col_s4:
        st.markdown('<div class="wallet-card" style="padding:16px;"><div style="font-size:0.65rem; color:#64748B;">RIESGO</div><div style="font-size:1.1rem; font-weight:800; color:#F59E0B; margin-top:4px;">Controlado</div></div>', unsafe_allow_html=True)

# ==========================================
# SECCIÓN 2: MARKETS
# ==========================================
elif nav_tab == "📈 Markets":
    st.markdown("### 📈 Markets — Fluctuación y Desviación", unsafe_allow_html=True)
    st.markdown("Monitor de comportamiento temporal de cuotas frente al modelo cuantitativo.", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    horas = [f"-{h}h" for h in range(24, 0, -2)]
    df_chart = pd.DataFrame({
        "SÚA Model Probability": [72 + np.sin(i/3)*3 for i in range(len(horas))],
        "Market Implied Odds": [65 + np.cos(i/2)*5 for i in range(len(horas))]
    }, index=horas)
    st.line_chart(df_chart, color=["#3B82F6", "#64748B"])

# ==========================================
# SECCIÓN 3: INTELLIGENCE
# ==========================================
elif nav_tab == "🧠 Intelligence":
    st.markdown("### 🧠 Intelligence — Laboratorio de Poisson & Disparos", unsafe_allow_html=True)
    st.markdown("Simulación paramétrica de flujos ofensivos y remates esperados.", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    lambda_param = st.slider("Media Proyectada de Goles (λ Lambda)", 1.0, 6.0, 2.8, 0.1)
    x_vals = list(range(0, 10))
    y_vals = [math.exp(-lambda_param) * (lambda_param**k) / math.factorial(k) for k in x_vals]
    df_pois = pd.DataFrame({"Probabilidad": y_vals}, index=x_vals)
    st.line_chart(df_pois, color="#3B82F6")

# ==========================================
# SECCIÓN 4: OPPORTUNITIES
# ==========================================
elif nav_tab == "🎯 Opportunities":
    st.markdown("### 🎯 Opportunities — Feed de Partidos Filtrados", unsafe_allow_html=True)
    st.markdown("Encuentros validados bajo el estándar de arista positiva del motor.", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    oportunidades = [
        {"liga": "UEFA Europa League", "hora": "17:00", "local": "Dinamo de Kyiv", "visitante": "PAOK", "mercado": "Menos de 2,5 goles", "arista": "+16,4%", "conf": "96"},
        {"liga": "Amistosos de Clubes", "hora": "16:30", "local": "Francos Borains", "visitante": "Tubize", "mercado": "Más de 2,5 goles", "arista": "+16,4%", "conf": "92"}
    ]

    for op in oportunidades:
        st.markdown(f"""
        <div class="wallet-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                <span style="font-family:'JetBrains Mono'; font-size:0.7rem; color:var(--text-muted); text-transform:uppercase;">{op['liga']} • {op['hora']}</span>
                <span style="background:rgba(59,130,246,0.1); color:#3B82F6; padding:4px 10px; border-radius:20px; font-size:0.7rem; font-weight:700;">Arista {op['arista']}</span>
            </div>
            <div style="font-size:1.2rem; font-weight:900; margin-bottom:12px;">{op['local']} <span style="color:#64748B; font-weight:400; font-size:0.9rem;">vs</span> {op['visitante']}</div>
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.85rem; color:#64748B;">
                <div>Selección: <strong style="color:#F8FAFC;">{op['mercado']}</strong></div>
                <div>Confidence Score: <strong style="color:#3B82F6; font-family:'JetBrains Mono';">{op['conf']}% (A+)</strong></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# SECCIÓN 5: PORTFOLIO
# ==========================================
elif nav_tab == "📊 Portfolio":
    st.markdown("### 📊 Portfolio — Gestión y Rendimiento", unsafe_allow_html=True)
    st.markdown("Seguimiento del rendimiento acumulado de las decisiones del sistema.", unsafe_allow_html=True)

# ==========================================
# SECCIÓN 6: RESEARCH
# ==========================================
elif nav_tab == "📚 Research":
    st.markdown("### 📚 Research — Auditoría Histórica (Notion Style)", unsafe_allow_html=True)
    st.markdown("Registro estructurado de backtesting mensual.", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    audit_data = pd.DataFrame([
        {"Mes": "Enero 2026", "Tendencias": 312, "Winrate": "76%", "Yield": "+22,3%"},
        {"Mes": "Febrero 2026", "Tendencias": 280, "Winrate": "74%", "Yield": "+18,5%"},
        {"Mes": "Marzo 2026", "Tendencias": 295, "Winrate": "77%", "Yield": "+21,1%"}
    ])
    st.dataframe(audit_data, use_container_width=True, hide_index=True)

# ==========================================
# SECCIÓN 7: SETTINGS
# ==========================================
elif nav_tab == "⚙ Settings":
    st.markdown("### ⚙ Settings — Conexiones y APIs", unsafe_allow_html=True)
    st.markdown("Parámetros del sistema operativo y fuentes de datos en tiempo real.", unsafe_allow_html=True)
