# SÚA v6.0 — Terminal de Inteligencia Cuantitativa (Decision Operating System)
import streamlit as st
import pandas as pd
import numpy as np
import math

st.set_page_config(page_title="SÚA — Sports Intelligence Engine", layout="wide", initial_sidebar_state="expanded")

# ==========================================
# ESTILOS TERMINAL PROFESIONAL (APPLE + BLOOMBERG)
# ==========================================
TERMINAL_CSS = """
<style>
@import url('https://api.fontshare.com/v2/css?f[]=satoshi@900,700,500,400&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700;800&display=swap');

:root {
    --bg-base: #0B0F17;
    --text-main: #FFFFFF;
    --text-muted: #64748B;
    --accent-blue: #3B82F6;
    --border-subtle: rgba(255, 255, 255, 0.06);
}

body, [class*="css"] {
    font-family: 'Satoshi', sans-serif;
    color: var(--text-main);
    background-color: var(--bg-base);
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.metric-gigantic {
    font-family: 'JetBrains Mono', monospace;
    font-size: 4.5rem;
    font-weight: 800;
    line-height: 1.0;
    color: #FFFFFF;
    letter-spacing: -3px;
}
.metric-label-sub {
    font-family: 'Satoshi', sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-top: 8px;
}
.delta-blue {
    color: var(--accent-blue);
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
}

.terminal-card {
    background: transparent;
    border-bottom: 1px solid var(--border-subtle);
    padding-bottom: 24px;
    margin-bottom: 24px;
}

.section-divider {
    height: 1px;
    background: var(--border-subtle);
    margin: 48px 0;
}
</style>
"""

st.markdown(TERMINAL_CSS, unsafe_allow_html=True)

# ==========================================
# SIDEBAR — SISTEMA OPERATIVO
# ==========================================
st.sidebar.markdown("""
<div style="font-family:'JetBrains Mono'; font-weight:800; font-size:1.2rem; letter-spacing:-1px; margin-bottom:4px;">SÚA</div>
<div style="font-size:0.75rem; color:#64748B; text-transform:uppercase; letter-spacing:1px; margin-bottom:24px;">Sports Intelligence Engine</div>
""", unsafe_allow_html=True)

nav = st.sidebar.radio("Navegación", ["Overview", "Opportunities", "Markets", "Intelligence", "Models", "Portfolio", "History"], label_visibility="collapsed")

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="font-family:'JetBrains Mono'; font-size:0.75rem; color:#64748B; line-height:1.6;">
    <strong>Motor</strong><br>● Online<br><br>
    <strong>API</strong><br>2/2<br><br>
    <strong>Última Sync</strong><br>14:22
</div>
""", unsafe_allow_html=True)

# ==========================================
# CUERPO PRINCIPAL — DECISION OPERATING SYSTEM
# ==========================================

# 1. HEADER & INTRO CONTEXTUAL (CERO ESPACIO VACÍO)
st.markdown("""
<div style="font-size:2.8rem; font-weight:900; letter-spacing:-1px; margin-bottom:4px;">Overview</div>
<div style="font-size:1rem; color:#64748B; font-weight:500; margin-bottom:24px;">Sistema Operativo de Decisiones</div>
<div style="font-family:'JetBrains Mono'; font-size:0.9rem; color:#94A3B8; background:rgba(255,255,255,0.02); padding:16px 20px; border-radius:12px; border:1px solid rgba(255,255,255,0.04); margin-bottom:32px;">
    Buenos días Diego. Hoy el sistema encontró <strong style="color:#FFF;">27 partidos</strong> ↓ <strong style="color:#FFF;">6 oportunidades</strong> ↓ <strong style="color:#FFF;">2 apuestas Premium</strong>.
</div>
""", unsafe_allow_html=True)

# 2. MÉTRICAS PRINCIPALES (TODO BLANCO, DELTA EN AZUL)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('''
        <div class="metric-gigantic">+7.42%</div>
        <div class="metric-label-sub">Edge Promedio Hoy <span class="delta-blue">(+0.8%)</span></div>
    ''', unsafe_allow_html=True)
with col2:
    st.markdown('''
        <div class="metric-gigantic">94.2</div>
        <div class="metric-label-sub">Confidence Score <span class="delta-blue">(+2.4%)</span></div>
    ''', unsafe_allow_html=True)
with col3:
    st.markdown('''
        <div class="metric-gigantic">80%</div>
        <div class="metric-label-sub">Índice de Salud <span class="delta-blue">(Stable)</span></div>
    ''', unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# 3. PANEL DE INTELIGENCIA / ESTADO DEL MOTOR
st.markdown("""
<div style="font-size:1.4rem; font-weight:800; margin-bottom:16px;">Estado del Motor Cuantitativo</div>
""", unsafe_allow_html=True)

col_i1, col_i2, col_i3, col_i4 = st.columns(4)
with col_i1:
    st.markdown('<div style="font-family:\'JetBrains Mono\'; font-size:0.85rem; color:#64748B;">● IA</div><div style="font-size:1.1rem; font-weight:700; margin-top:4px;">Activo</div>', unsafe_allow_html=True)
with col_i2:
    st.markdown('<div style="font-family:\'JetBrains Mono\'; font-size:0.85rem; color:#64748B;">● APIs</div><div style="font-size:1.1rem; font-weight:700; margin-top:4px;">Sincronizadas</div>', unsafe_allow_html=True)
with col_i3:
    st.markdown('<div style="font-family:\'JetBrains Mono\'; font-size:0.85rem; color:#64748B;">● Monte Carlo</div><div style="font-size:1.1rem; font-weight:700; margin-top:4px;">10 000 simulaciones</div>', unsafe_allow_html=True)
with col_i4:
    st.markdown('<div style="font-family:\'JetBrains Mono\'; font-size:0.85rem; color:#64748B;">● Última actualización</div><div style="font-size:1.1rem; font-weight:700; margin-top:4px;">Hace 34 segundos</div>', unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# 4. MARKETS — MOVIMIENTO DEL EDGE (3 LÍNEAS MULTI-FUENTE)
st.markdown("""
<div style="font-size:1.4rem; font-weight:800; margin-bottom:4px;">Movimiento del Edge</div>
<div style="font-size:0.85rem; color:#64748B; margin-bottom:20px;">Seguimiento temporal a 24 horas (RushBet vs Pinnacle vs Modelo SÚA)</div>
""", unsafe_allow_html=True)

horas = [f"-{h}h" for h in range(24, 0, -2)]
df_edges = pd.DataFrame({
    "RushBet": [62 + np.sin(i/3)*4 for i in range(len(horas))],
    "Pinnacle": [68 + np.cos(i/2)*3 for i in range(len(horas))],
    "Modelo SUA": [75 + np.sin(i/2.5)*5 for i in range(len(horas))]
}, index=horas)
st.line_chart(df_edges, color=["#64748B", "#94A3B8", "#3B82F6"])

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# 5. RESUMEN EJECUTIVO & ACCIÓN INMEDIATA ("¿QUÉ DEBERÍA HACER HOY?")
st.markdown("""
<div style="font-size:1.4rem; font-weight:800; margin-bottom:16px;">Recomendación Inmediata de Hoy</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="terminal-card">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <span style="font-family:'JetBrains Mono'; font-size:0.75rem; color:#64748B; text-transform:uppercase;">Ejecución Prioritaria</span>
        <span style="color:#3B82F6; font-family:'JetBrains Mono'; font-weight:700;">Confianza A+</span>
    </div>
    <div style="font-size:1.5rem; font-weight:900; margin-bottom:8px;">Mayor Edge Detectado: <span style="color:#3B82F6;">+11.8%</span></div>
    <div style="font-size:0.9rem; color:#94A3B8; margin-bottom:20px;">24 partidos analizados validados bajo filtros estrictos de valor esperado y modelos estocásticos.</div>
</div>
""", unsafe_allow_html=True)

if st.button("Ver oportunidades", type="primary", use_container_width=True):
    st.toast("Cargando matriz de oportunidades filtradas...", icon="⚡")
