# Let's update the PDF code to include:
# 1. "Bank de inversión" (Investment Banking / módulo financiero o sección de banca de inversión).
# 2. Status visual indicator for APIs (verde para conectadas, rojo para no conectadas).

html_content_updated = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte Técnico de Integración, Banca de Inversión y Estado de APIs</title>
    <style>
        @page {
            size: A4;
            margin: 20mm 15mm;
            background-color: #f4f6f8;
            @bottom-right {
                content: counter(page);
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                font-size: 9pt;
                color: #64748b;
            }
        }
        *, *::before, *::after {
            box-sizing: border-box;
        }
        body {
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            color: #1e293b;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f6f8;
        }
        .header-container {
            background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
            color: #ffffff;
            margin: -20mm -15mm 25px -15mm;
            padding: 30px 20mm;
            border-bottom: 4px solid #3b82f6;
        }
        .header-container h1 {
            margin: 0 0 8px 0;
            font-size: 20pt;
            font-weight: 700;
            letter-spacing: -0.5px;
        }
        .header-container p {
            margin: 0;
            font-size: 10.5pt;
            color: #93c5fd;
            font-weight: 400;
        }
        h2 {
            font-size: 13pt;
            color: #1e3a8a;
            border-left: 4px solid #3b82f6;
            padding-left: 10px;
            margin-top: 22px;
            margin-bottom: 10px;
            page-break-after: avoid;
        }
        p, li {
            font-size: 9.5pt;
            color: #334155;
            margin-bottom: 8px;
        }
        ul {
            margin: 0 0 12px 0;
            padding-left: 20px;
        }
        .card {
            background-color: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            padding: 14px;
            margin-bottom: 12px;
            page-break-inside: avoid;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        .card-title {
            font-weight: bold;
            color: #0f172a;
            margin-bottom: 6px;
            font-size: 10.5pt;
        }
        pre {
            background-color: #0f172a;
            color: #e2e8f0;
            padding: 10px;
            border-radius: 5px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 8pt;
            overflow-x: auto;
            margin: 8px 0;
            line-height: 1.4;
            border: 1px solid #334155;
        }
        .badge {
            display: inline-block;
            padding: 3px 8px;
            font-size: 7.5pt;
            font-weight: bold;
            border-radius: 4px;
        }
        .badge-green {
            background-color: #dcfce7;
            color: #166534;
            border: 1px solid #bbf7d0;
        }
        .badge-red {
            background-color: #fee2e2;
            color: #991b1b;
            border: 1px solid #fecaca;
        }
        .status-dot {
            height: 10px;
            width: 10px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 6px;
        }
        .dot-green { background-color: #22c55e; }
        .dot-red { background-color: #ef4444; }
    </style>
</head>
<body>

    <div class="header-container">
        <h1>Reporte Técnico Actualizado: Módulo Investment Banking & Dashboard de APIs</h1>
        <p>Incorporación de Banca de Inversión, indicadores visuales de estado (Verde/Rojo) y paleta corregida.</p>
    </div>

    <h2>1. Indicadores Visuales de Conectividad de APIs</h2>
    <div class="card">
        <div class="card-title">Panel de Monitoreo de Conexiones (Dashboard Status)</div>
        <p>Se ha implementado el indicador visual en tiempo real para reflejar el estado operativo de cada integración:</p>
        <ul>
            <li><span class="status-dot dot-green"></span><strong>Verde (<code>#22c55e</code>):</strong> API conectada y respondiendo correctamente (Códigos HTTP 200-299). <span class="badge badge-green">Activa</span></li>
            <li><span class="status-dot dot-red"></span><strong>Rojo (<code>#ef4444</code>):</strong> API desconectada, sin respuesta o con error crítico de enlace. <span class="badge badge-red">Sin Conexión</span></li>
        </ul>
        <pre><code>// Componente de Estado de API en la Interfaz
function ApiStatusIndicator({ apiName, isConnected }) {
    return (
        <div style={{ display: 'flex', alignItems: 'center', padding: '6px 10px', background: '#fff', border: '1px solid #cbd5e1', borderRadius: '4px', marginBottom: '6px' }}>
            <span style={{ height: '10px', width: '10px', borderRadius: '50%', backgroundColor: isConnected ? '#22c55e' : '#ef4444', marginRight: '8px' }}></span>
            <span style={{ fontSize: '9pt', fontWeight: 'bold', color: '#0f172a' }}>{apiName}</span>
            <span style={{ marginLeft: 'auto', fontSize: '8pt', color: isConnected ? '#166534' : '#991b1b' }}>
                {isConnected ? 'Conectada (Online)' : 'Desconectada (Offline)'}
            </span>
        </div>
    );
}</code></pre>
    </div>

    <h2>2. Integración del Módulo de Investment Banking (Bank de Inversión)</h2>
    <div class="card">
        <div class="card-title">Estructura del Módulo Financiero / Banca de Inversión</div>
        <p>Se ha incorporado la sección dedicada a <strong>Investment Banking</strong> dentro del flujo de la plataforma, permitiendo gestionar portafolios, valoraciones de activos y líneas de crédito corporativo:</p>
        <ul>
            <li><strong>Gestión de Activos y Portafolios:</strong> Monitoreo de inversiones estructuradas y proyecciones de retorno.</li>
            <li><strong>Evaluación de Riesgo:</strong> Conexión con modelos cuantitativos y métricas financieras corporativas.</li>
            <li><strong>Etiquetas y Componentes Normalizados:</strong> Alineados bajo la paleta institucional (Azul oscuro <code>#0f172a</code>, acento <code>#3b82f6</code> y tarjetas limpias).</li>
        </ul>
    </div>

    <h2>3. Código de Integración del Módulo Financiero</h2>
    <div class="card">
        <div class="card-title">Estructura Base del Componente Investment Banking</div>
        <pre><code>const InvestmentBankingModule = () => {
    return (
        <div className="investment-container" style={{ padding: '15px', background: '#f4f6f8' }}>
            <h3 style={{ color: '#1e3a8a', borderBottom: '2px solid #3b82f6', paddingBottom: '5px' }}>Banca de Inversión & Portafolios</h3>
            <p>Módulo configurado para la administración de activos, licencias y operaciones financieras corporativas.</p>
        </div>
    );
};</code></pre>
    </div>

</body>
</html>
"""

output_pdf = "Reporte_Tecnico_Investment_Banking_APIs.pdf"
HTML(string=html_content_updated).write_pdf(output_pdf)
print(f"PDF actualizado generado exitosamente: {output_pdf}")
