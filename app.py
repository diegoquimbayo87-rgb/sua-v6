# SÚA v6.0 — Dashboard con pestañas funcionales, gráfico tendencias cuotas, diseño Apple/Bloomberg
import streamlit as st
import pandas as pd
import numpy as np
import math
from datetime import datetime, timedelta

st.set_page_config(page_title="SÚA v6.0 — Quant Intelligence", layout="wide", initial_sidebar_state="expanded")

# ==========================================
# ESTILOS MINIMALISTAS (APPLE + BLOOMBERG)
# ==========================================
TERMINAL_CSS = """
<style>
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

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

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
# NAVEGACIÓN MODULAR
# ==========================================
nav = st.sidebar.radio("Navegación", ["Overview", "Markets", "Intelligence", "Opportunities", "Portfolio", "Research", "Settings"])

# ==========================================
# LÓGICA DE PESTAÑAS
# ==========================================
if nav == "Overview":
    st.title("🏠 Overview — Centro de Inteligencia")
    st.markdown("Bienvenido al Sistema Operativo de Decisiones de SÚA.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-gigantic">+7.42%</div><div class="metric-label-sub">Edge Promedio Hoy</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-gigantic" style="color:#3B82F6;">94.2</div><div class="metric-label-sub">Score de Confianza</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-gigantic" style="color:#10B981;">80%</div><div class="metric-label-sub">Índice de Salud</div>', unsafe_allow_html=True)

elif nav == "Markets":
    st.title("📈 Markets — Tendencias de Cuotas")
    st.markdown("Monitor de comportamiento temporal de cuotas frente al modelo cuantitativo.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    horas = [f"-{h}h" for h in range(24, 0, -2)]
    df = pd.DataFrame({
        "SÚA Modelo": [72 + np.sin(i/3)*3 for i in range(len(horas))], 
        "Mercado": [65 + np.cos(i/2)*5 for i in range(len(horas))]
    }, index=horas)
    st.line_chart(df, color=["#3B82F6", "#64748B"])

elif nav == "Intelligence":
    st.title("🧠 Intelligence — Laboratorio de Poisson & Disparos")
    st.markdown("Simulación paramétrica de flujos ofensivos y remates esperados.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    lambda_param = st.slider("Media Proyectada de Goles (λ Lambda)", 1.0, 6.0, 2.8, 0.1)
    x_vals = list(range(0, 10))
    y_vals = [math.exp(-lambda_param) * (lambda_param**k) / math.factorial(k) for k in x_vals]
    df_pois = pd.DataFrame({"Probabilidad": y_vals}, index=x_vals)
    st.line_chart(df_pois, color="#3B82F6")

elif nav == "Opportunities":
    st.title("🎯 Opportunities — Feed de Partidos Filtrados")
    st.markdown("Encuentros validados bajo el estándar de arista positiva del motor.")
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

elif nav == "Portfolio":
    st.title("📊 Portfolio — Gestión y Rendimiento")
    st.markdown("Seguimiento del rendimiento acumulado de las decisiones del sistema.")
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("Módulo de gestión de capital y seguimiento activo de yield sincronizado.")

elif nav == "Research":
    st.title("📚 Research — Auditoría Histórica")
    st.markdown("Registro estructurado de backtesting mensual y auditoría de modelos.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    audit_data = pd.DataFrame([
        {"Mes": "Enero 2026", "Tendencias": 312, "Winrate": "76%", "Yield": "+22,3%"},
        {"Mes": "Febrero 2026", "Tendencias": 280, "Winrate": "74%", "Yield": "+18,5%"},
        {"Mes": "Marzo 2026", "Tendencias": 295, "Winrate": "77%", "Yield": "+21,1%"}
    ])
    st.dataframe(audit_data, use_container_width=True, hide_index=True)

elif nav == "Settings":
    st.title("⚙ Settings — Conexiones y APIs")
    st.markdown("Parámetros del sistema operativo y fuentes de datos en tiempo real.")
    st.markdown("<br>", unsafe_allow_html=True)
    st.text_input("API Key de Proveedor de Cuotas", "************************", type="password")
    st.text_input("Endpoint de Modelos de Poisson", "https://api.sua-quant.internal/v6/engine")
    st.button("Guardar Cambios")
