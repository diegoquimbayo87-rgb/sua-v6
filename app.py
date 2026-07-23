import streamlit as st

# Configuración de la página con los colores y estilo institucional
st.set_page_config(
    page_title="Dashboard Corporativo - Cloud & Investment Banking",
    page_icon="⚡",
    layout="wide"
)

# Estilos CSS personalizados (Paleta: Azul oscuro #0f172a, Azul acento #3b82f6, Fondo #f4f6f8)
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f8;
    }
    .stApp {
        background-color: #f4f6f8;
    }
    .header-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        color: white;
        padding: 25px;
        border-radius: 8px;
        border-bottom: 4px solid #3b82f6;
        margin-bottom: 20px;
    }
    .card {
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado principal
st.markdown("""
    <div class="header-box">
        <h1 style="margin:0; font-size: 24px;">Panel de Control & Dashboard Corporativo</h1>
        <p style="margin:5px 0 0 0; color: #93c5fd;">Cloud Solutions, Módulo de Investment Banking y Estado de APIs</p>
    </div>
""", unsafe_allow_html=True)

# Layout en dos columnas: Izquierda (APIs y Estados), Derecha (Investment Banking)
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🔌 Estado de Conectividad de APIs")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("Monitoreo en tiempo real de los endpoints del sistema:")
    
    # Indicadores de API (Verde = Conectada, Rojo = Desconectada)
    api_status = {
        "API Licensing (Microsoft/Azure)": True,
        "API Cybersecurity (Kaspersky/Sophos)": True,
        "API Investment Banking Core": False, # Desconectada para pruebas
        "API Billing & ERP Gateway": True
    }
    
    for api_name, is_connected in api_status.items():
        color = "#22c55e" if is_connected else "#ef4444"
        status_text = "Conectada (Online)" if is_connected else "Desconectada (Offline)"
        badge_bg = "#dcfce7" if is_connected else "#fee2e2"
        badge_color = "#166534" if is_connected else "#991b1b"
        
        st.markdown(f"""
            <div style="display: flex; align-items: center; padding: 8px 12px; background: #fff; border: 1px solid #cbd5e1; border-radius: 6px; margin-bottom: 8px;">
                <span style="height: 12px; width: 12px; border-radius: 50%; background-color: {color}; margin-right: 10px;"></span>
                <span style="font-size: 13px; font-weight: bold; color: #0f172a;">{api_name}</span>
                <span style="margin-left: auto; font-size: 11px; padding: 2px 8px; border-radius: 4px; background-color: {badge_bg}; color: {badge_color}; font-weight: bold;">{status_text}</span>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("### 💼 Módulo Investment Banking")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h4 style='color: #1e3a8a; margin-top:0;'>Gestión Financiera y Portafolios</h4>", unsafe_allow_html=True)
    st.write("Administración de activos, valoraciones corporativas y líneas de crédito estructuradas.")
    
    # Métricas rápidas del Bank de Inversión
    mcol1, mcol2 = st.columns(2)
    with mcol1:
        st.metric(label="Portafolio Activo", value="$24,500 COP", delta="+4.2%")
    with mcol2:
        st.metric(label="Líneas de Crédito", value="$12,100 COP", delta="-1.5%")
        
    st.info("Módulo sincronizado con la capa de servicios y reglas de negocio.")
    st.markdown('</div>', unsafe_allow_html=True)

# Sección Inferior: Acciones y Ajustes
st.markdown("### 🛠️ Configuración y Herramientas")
st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("Utiliza este espacio para alternar entre entornos de prueba (Mocks) y conexiones productivas de base de datos.")
if st.button("🔄 Sincronizar Todos los Endpoints"):
    st.success("¡Sincronización completada con éxito!")
st.markdown('</div>', unsafe_allow_html=True)
