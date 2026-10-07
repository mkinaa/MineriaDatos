import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# Colores de la paleta institucional SoundData
DARK_BG = RGBColor(11, 15, 25)        # #0B0F19 Fondo muy oscuro elegante
CARD_BG = RGBColor(24, 31, 46)        # #181F2E Contenedores de contenido
ACCENT_GREEN = RGBColor(29, 185, 84)  # #1DB954 Verde Spotify / Éxito
ACCENT_BLUE = RGBColor(56, 189, 248)  # #38BDF8 Azul cian tecnología
TEXT_WHITE = RGBColor(248, 250, 252)  # #F8FAFC Blanco texto principal
TEXT_MUTED = RGBColor(148, 163, 184)  # #94A3B8 Gris claro secundario
BORDER_COLOR = RGBColor(38, 48, 71)   # #263047 Borde sutil de tarjeta

def aplicar_fondo(slide, prs):
    bg_shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height
    )
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = DARK_BG
    bg_shape.line.fill.background()
    return bg_shape

def agregar_encabezado(slide, titulo_texto, categoria_texto="SOUNDDATA ANALYTICS"):
    # Categoría pill / Badge superior
    p_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
    tf_c = p_cat.text_frame
    tf_c.word_wrap = True
    p0 = tf_c.paragraphs[0]
    r0 = p0.add_run()
    r0.text = categoria_texto.upper()
    r0.font.size = Pt(10)
    r0.font.bold = True
    r0.font.color.rgb = ACCENT_GREEN

    # Título principal
    p_tit = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.7))
    tf_t = p_tit.text_frame
    tf_t.word_wrap = True
    p1 = tf_t.paragraphs[0]
    r1 = p1.add_run()
    r1.text = titulo_texto
    r1.font.size = Pt(22)
    r1.font.bold = True
    r1.font.color.rgb = TEXT_WHITE

def agregar_tarjeta(slide, left, top, width, height, bg_color=CARD_BG, border_color=BORDER_COLOR):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1)
    return card

def add_styled_run(paragraph, text, size=10, bold=False, color=None):
    r = paragraph.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.bold = bold
    if color:
        r.font.color.rgb = color
    return r

# ==============================================================================
# PRESENTACIÓN 1: FUNCIONAMIENTO DE LA APLICACIÓN WEB (6 a 7 slides)
# ==============================================================================
def generar_ppt_aplicacion():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # SLIDE 1: Portada
    s1 = prs.slides.add_slide(blank_layout)
    aplicar_fondo(s1, prs)
    agregar_tarjeta(s1, Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.1), bg_color=CARD_BG, border_color=ACCENT_GREEN)
    
    tb = s1.shapes.add_textbox(Inches(2.0), Inches(1.6), Inches(9.333), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.alignment = PP_ALIGN.CENTER
    add_styled_run(p0, "PLATAFORMA WEB: SOUNDDATA ANALYTICS\n", size=28, bold=True, color=ACCENT_GREEN)

    p1 = tf.add_paragraph()
    p1.alignment = PP_ALIGN.CENTER
    add_styled_run(p1, "Inteligencia de Datos y Simulación Predictiva para la Industria Musical\n", size=16, bold=True, color=TEXT_WHITE)

    p2 = tf.add_paragraph()
    p2.alignment = PP_ALIGN.CENTER
    add_styled_run(p2, "Demostración de Funcionalidades, Vistas Interactivas y Persistencia Transaccional\n\n", size=12, color=TEXT_MUTED)

    p3 = tf.add_paragraph()
    p3.alignment = PP_ALIGN.CENTER
    add_styled_run(p3, "Equipo: Vicente Muñoz • Juan Ortiz • Jordan Murillo • Jorge Moncada • Jose Mendez • Bastian Parraguez\n", size=11, color=TEXT_WHITE)

    p4 = tf.add_paragraph()
    p4.alignment = PP_ALIGN.CENTER
    add_styled_run(p4, "FastAPI • Bootstrap 5 Dark • Chart.js • SQLite • Scikit-Learn\nUniversidad Santo Tomás — Minería de Datos (IEI-067)", size=10, color=ACCENT_BLUE)

    # SLIDE 2: Propósito y Arquitectura
    s2 = prs.slides.add_slide(blank_layout)
    aplicar_fondo(s2, prs)
    agregar_encabezado(s2, "Propósito de la Plataforma y Arquitectura del Sistema", "VISIÓN GENERAL DEL SISTEMA")

    agregar_tarjeta(s2, Inches(0.8), Inches(1.5), Inches(5.2), Inches(5.4))
    tb_s2 = s2.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.8), Inches(5.0))
    tf_s2 = tb_s2.text_frame
    tf_s2.word_wrap = True

    p = tf_s2.paragraphs[0]
    add_styled_run(p, "¿Qué problema resuelve SoundData?\n", size=14, bold=True, color=ACCENT_GREEN)

    items_s2 = [
        ("Toma de Decisiones Guiada por Datos:", "Permite a sellos y productores evaluar maquetas musicales antes de invertir en promoción."),
        ("Simulación en Tiempo Real:", "Ajuste dinámico de parámetros acústicos (BPM, energía, bailabilidad) con inferencia instantánea."),
        ("Persistencia de Portafolio:", "Almacenamiento corporativo de canciones analizadas con base de datos SQLite integrada."),
        ("Arquitectura Ligera y Desacoplada:", "Frontend rápido en Bootstrap 5 consumiendo una API REST asíncrona en FastAPI.")
    ]
    for tit, desc in items_s2:
        p = tf_s2.add_paragraph()
        p.space_before = Pt(8)
        add_styled_run(p, f"• {tit} ", size=11, bold=True, color=TEXT_WHITE)
        add_styled_run(p, desc, size=10.5, color=TEXT_MUTED)

    agregar_tarjeta(s2, Inches(6.3), Inches(1.5), Inches(6.2), Inches(5.4))
    img_arq = os.path.join("docs", "img", "arquitectura_sistema.png")
    if os.path.exists(img_arq):
        s2.shapes.add_picture(img_arq, Inches(6.45), Inches(1.9), Inches(5.9))

    # SLIDE 3: Vista 1 - Análisis Global de Oyentes
    s3 = prs.slides.add_slide(blank_layout)
    aplicar_fondo(s3, prs)
    agregar_encabezado(s3, "Pestaña 1: Análisis Global de Oyentes y Métricas Clave", "VISTA 1 — DASHBOARD GENERAL")

    agregar_tarjeta(s3, Inches(0.8), Inches(1.5), Inches(7.5), Inches(5.4))
    img_v1 = os.path.join("docs", "img", "app_vista_1_analisis_oyentes.png")
    if os.path.exists(img_v1):
        s3.shapes.add_picture(img_v1, Inches(0.9), Inches(1.65), Inches(7.3))

    agregar_tarjeta(s3, Inches(8.5), Inches(1.5), Inches(4.0), Inches(5.4))
    tb_s3 = s3.shapes.add_textbox(Inches(8.7), Inches(1.7), Inches(3.6), Inches(5.0))
    tf_s3 = tb_s3.text_frame
    tf_s3.word_wrap = True
    
    p = tf_s3.paragraphs[0]
    add_styled_run(p, "Capacidades de la Vista:\n", size=14, bold=True, color=ACCENT_GREEN)

    puntos_s3 = [
        ("KPIs en Tiempo Real:", "Muestra oyentes acumulados (841.0 M), género predominante (Clásica/Pop) y país líder en reproducciones (Alemania)."),
        ("Gráficos Dinámicos Chart.js:", "Distribución comparativa de volumen de streams por cada uno de los 12 géneros musicales."),
        ("Participación Territorial:", "Gráfico de dona con porcentaje de cuota de mercado por país."),
        ("Barra de Resumen Porcentual:", "Porcentaje de penetración de oyentes ordenado por popularidad.")
    ]
    for tit, desc in puntos_s3:
        p = tf_s3.add_paragraph()
        p.space_before = Pt(8)
        add_styled_run(p, f"• {tit} ", size=10.5, bold=True, color=TEXT_WHITE)
        add_styled_run(p, desc, size=10, color=TEXT_MUTED)

    # SLIDE 4: Vista 2 - Segmentación por Atributo
    s4 = prs.slides.add_slide(blank_layout)
    aplicar_fondo(s4, prs)
    agregar_encabezado(s4, "Pestaña 2: Segmentación Univariada de Oyentes", "VISTA 2 — SEGMENTACIÓN DETALLADA")

    agregar_tarjeta(s4, Inches(0.8), Inches(1.5), Inches(7.5), Inches(5.4))
    img_v2 = os.path.join("docs", "img", "app_vista_2_segmentacion_atributo.png")
    if os.path.exists(img_v2):
        s4.shapes.add_picture(img_v2, Inches(0.9), Inches(1.65), Inches(7.3))

    agregar_tarjeta(s4, Inches(8.5), Inches(1.5), Inches(4.0), Inches(5.4))
    tb_s4 = s4.shapes.add_textbox(Inches(8.7), Inches(1.7), Inches(3.6), Inches(5.0))
    tf_s4 = tb_s4.text_frame
    tf_s4.word_wrap = True

    p = tf_s4.paragraphs[0]
    add_styled_run(p, "Filtros y Segmentación:\n", size=14, bold=True, color=ACCENT_GREEN)

    puntos_s4 = [
        ("Selectores por Pill (100% Español):", "Permite segmentar con un clic por Género, País, Año de Lanzamiento, Popularidad, Bailabilidad, Energía y Contenido Explícito."),
        ("Conteo de Categorías:", "Cálculo instantáneo de millones de oyentes y porcentaje de peso de cada grupo."),
        ("Tabla de Participación:", "Visualización ordenada de penetración sobre los 85.000 registros."),
        ("Exportación JSON:", "Botón para exportar el resumen analítico filtrado para su uso en reportes ejecutivos.")
    ]
    for tit, desc in puntos_s4:
        p = tf_s4.add_paragraph()
        p.space_before = Pt(8)
        add_styled_run(p, f"• {tit} ", size=10.5, bold=True, color=TEXT_WHITE)
        add_styled_run(p, desc, size=10, color=TEXT_MUTED)

    # SLIDE 5: Vista 3 - Simulador de Éxito ML
    s5 = prs.slides.add_slide(blank_layout)
    aplicar_fondo(s5, prs)
    agregar_encabezado(s5, "Pestaña 3: Simulador de Éxito en Tiempo Real (Machine Learning)", "VISTA 3 — MOTOR DE INFERENCIA")

    agregar_tarjeta(s5, Inches(0.8), Inches(1.5), Inches(7.5), Inches(5.4))
    img_v3 = os.path.join("docs", "img", "app_vista_3_simulador_ml.png")
    if os.path.exists(img_v3):
        s5.shapes.add_picture(img_v3, Inches(0.9), Inches(1.65), Inches(7.3))

    agregar_tarjeta(s5, Inches(8.5), Inches(1.5), Inches(4.0), Inches(5.4))
    tb_s5 = s5.shapes.add_textbox(Inches(8.7), Inches(1.7), Inches(3.6), Inches(5.0))
    tf_s5 = tb_s5.text_frame
    tf_s5.word_wrap = True

    p = tf_s5.paragraphs[0]
    add_styled_run(p, "Inferencia Triple Unificada:\n", size=14, bold=True, color=ACCENT_GREEN)

    puntos_s5 = [
        ("Control Acústico Intuitivo:", "Deslizadores en tiempo real para BPM (50-220), Energía, Bailabilidad, Sonoridad (dB) e Instrumentalidad."),
        ("Modelo 1 (Árbol de Decisión):", "Predice si la canción alcanzará el Top 25% de streams y entrega la probabilidad porcentual estimada."),
        ("Modelo 2 (K-Means Clustering):", "Clasifica el tema en uno de los 4 arquetipos sonoros (Pop Radio, Chill, Rock/Fiesta o Urbano)."),
        ("Modelo 3 (Reglas Apriori):", "Entrega recomendaciones accionables de afinidad de género y mercado."),
        ("Guardado en Portafolio:", "Botón directo para registrar el demo evaluado en SQLite sin recargar la página.")
    ]
    for tit, desc in puntos_s5:
        p = tf_s5.add_paragraph()
        p.space_before = Pt(6)
        add_styled_run(p, f"• {tit} ", size=10, bold=True, color=TEXT_WHITE)
        add_styled_run(p, desc, size=9.5, color=TEXT_MUTED)

    # SLIDE 6: Vista 4 - Portafolio y Gestión CRUD
    s6 = prs.slides.add_slide(blank_layout)
    aplicar_fondo(s6, prs)
    agregar_encabezado(s6, "Pestaña 4: Portafolio de Canciones & Gestión CRUD (SQLite)", "VISTA 4 — PERSISTENCIA Y ADMINISTRACIÓN")

    agregar_tarjeta(s6, Inches(0.8), Inches(1.5), Inches(7.5), Inches(5.4))
    img_v4 = os.path.join("docs", "img", "app_vista_4_portafolio_crud.png")
    if os.path.exists(img_v4):
        s6.shapes.add_picture(img_v4, Inches(0.9), Inches(1.65), Inches(7.3))

    agregar_tarjeta(s6, Inches(8.5), Inches(1.5), Inches(4.0), Inches(5.4))
    tb_s6 = s6.shapes.add_textbox(Inches(8.7), Inches(1.7), Inches(3.6), Inches(5.0))
    tf_s6 = tb_s6.text_frame
    tf_s6.word_wrap = True

    p = tf_s6.paragraphs[0]
    add_styled_run(p, "Funciones Transaccionales:\n", size=14, bold=True, color=ACCENT_GREEN)

    puntos_s6 = [
        ("Persistencia Real (SQLite 3):", "Base de datos relacional 'sounddata.db' que preserva el catálogo y los demos evaluados."),
        ("Operaciones CRUD Completas:", "Crear nuevas pistas manuales, consultar con filtros dinámicos, editar atributos en modal interactivo y eliminar registros obsoletos."),
        ("Búsqueda Rápida y Filtros:", "Filtrado en vivo por texto, género musical y diagnóstico de éxito (Éxito vs Estándar)."),
        ("Semillado Demostrativo:", "Carga inicial automática de canciones semilla para evaluación inmediata de la comisión.")
    ]
    for tit, desc in puntos_s6:
        p = tf_s6.add_paragraph()
        p.space_before = Pt(8)
        add_styled_run(p, f"• {tit} ", size=10.5, bold=True, color=TEXT_WHITE)
        add_styled_run(p, desc, size=10, color=TEXT_MUTED)

    # SLIDE 7: Calidad, Pruebas y Despliegue en la Nube
    s7 = prs.slides.add_slide(blank_layout)
    aplicar_fondo(s7, prs)
    agregar_encabezado(s7, "Calidad del Software, Pruebas Unitarias y Despliegue", "ESTABILIDAD Y DESPLIEGUE")

    cajas_s7 = [
        ("🧪 Pruebas Unitarias (Pytest)", "17 Tests Aprobados al 100%", [
            "test_api.py: Endpoints HTTP, esquemas Pydantic y códigos de respuesta.",
            "test_database.py: Ciclo CRUD completo en SQLite aislado.",
            "test_modelos.py: Carga de joblib, transformador Scaler e inferencia matemática.",
            "Tiempo de ejecución: < 3 segundos."
        ], ACCENT_GREEN),
        ("🛡️ Tolerancia a Errores", "Manejo Amigable en Español", [
            "Captura de excepciones en esquemas Pydantic.",
            "Cero pantallas de error o tracebacks de Python para el usuario final.",
            "Alertas visuales en interfaz ante valores fuera de rango.",
            "Auto-recuperación de conexión a base de datos."
        ], ACCENT_BLUE),
        ("☁️ Despliegue Cloud (Render)", "Acceso Público 24/7", [
            "Servidor ASGI Uvicorn contenerizable.",
            "Archivo Procfile configurado en la raíz.",
            "Repositorio sincronizado con GitHub CI/CD.",
            "Video de respaldo de 2 min ante contingencias de red."
        ], RGBColor(168, 85, 247))
    ]

    for i, (tit_c, sub_c, bullets_c, col_c) in enumerate(cajas_s7):
        x = Inches(0.8 + i * 4.0)
        agregar_tarjeta(s7, x, Inches(1.6), Inches(3.7), Inches(5.2), border_color=col_c)
        tb_c = s7.shapes.add_textbox(x + Inches(0.2), Inches(1.8), Inches(3.3), Inches(4.8))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True

        p = tf_c.paragraphs[0]
        add_styled_run(p, f"{tit_c}\n", size=13, bold=True, color=col_c)

        p_sub = tf_c.add_paragraph()
        add_styled_run(p_sub, f"{sub_c}\n\n", size=11, bold=True, color=TEXT_WHITE)

        for b in bullets_c:
            p_b = tf_c.add_paragraph()
            p_b.space_before = Pt(4)
            add_styled_run(p_b, f"• {b}", size=10, color=TEXT_MUTED)

    output_path = os.path.join("docs", "PRESENTACION_APLICACION_WEB.pptx")
    prs.save(output_path)
    print(f"PPT Aplicación Web creado exitosamente en: {output_path}")

# ==============================================================================
# PRESENTACIÓN 2: PROYECTO & METODOLOGÍA CRISP-DM / INFORME TÉCNICO (7 a 8 slides)
# ==============================================================================
def generar_ppt_crisp_dm():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # SLIDE 1: Portada
    s1 = prs.slides.add_slide(blank_layout)
    aplicar_fondo(s1, prs)
    agregar_tarjeta(s1, Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.1), bg_color=CARD_BG, border_color=ACCENT_BLUE)
    
    tb = s1.shapes.add_textbox(Inches(2.0), Inches(1.6), Inches(9.333), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.alignment = PP_ALIGN.CENTER
    add_styled_run(p0, "PROYECTO FINAL: MINERÍA DE DATOS (IEI-067)\n", size=26, bold=True, color=ACCENT_BLUE)

    p1 = tf.add_paragraph()
    p1.alignment = PP_ALIGN.CENTER
    add_styled_run(p1, "Metodología CRISP-DM Aplicada al Streaming Musical (Spotify 2015–2025)\n", size=16, bold=True, color=TEXT_WHITE)

    p2 = tf.add_paragraph()
    p2.alignment = PP_ALIGN.CENTER
    add_styled_run(p2, "Modelado de Clasificación, Clustering de Audiencias y Reglas de Asociación\n\n", size=12, color=TEXT_MUTED)

    p3 = tf.add_paragraph()
    p3.alignment = PP_ALIGN.CENTER
    add_styled_run(p3, "Grupo 4: Vicente Muñoz • Juan Ortiz • Jordan Murillo • Jorge Moncada • Jose Mendez • Bastian Parraguez\n", size=11, color=TEXT_WHITE)

    p4 = tf.add_paragraph()
    p4.alignment = PP_ALIGN.CENTER
    add_styled_run(p4, "Universidad Santo Tomás — Docentes: Florentino Vargas & Rosa Rao\nOctubre de 2026", size=10, color=ACCENT_GREEN)

    # SLIDE 2: Fases 1 & 2 - Comprensión del Negocio y Datos
    s2 = prs.slides.add_slide(blank_layout)
    aplicar_fondo(s2, prs)
    agregar_encabezado(s2, "Fases 1 y 2: Comprensión del Negocio y Análisis Exploratorio (EDA)", "CRISP-DM — FASES 1 & 2")

    agregar_tarjeta(s2, Inches(0.8), Inches(1.5), Inches(5.2), Inches(5.4))
    tb_s2 = s2.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.8), Inches(5.0))
    tf_s2 = tb_s2.text_frame
    tf_s2.word_wrap = True

    p = tf_s2.paragraphs[0]
    add_styled_run(p, "Definición del Problema y Datos:\n", size=14, bold=True, color=ACCENT_BLUE)

    puntos_s2 = [
        ("Contexto de Negocio:", "Más de 100.000 lanzamientos diarios en Spotify; necesidad de transformar la intuición de A&R en decisiones analíticas."),
        ("Dimensión del Dataset:", "85.000 canciones y 17 variables originales que cubren atributos acústicos y metadatos de mercado."),
        ("Variable Objetivo (Class):", "es_exito = 1 si las reproducciones superan el percentil 75 (Q₃ ≈ 85.2 M de streams), 0 en caso contrario."),
        ("Hallazgo Clave del EDA:", "Fuerte asimetría positiva: el 25% superior de canciones concentra el 68% de los streams totales de la plataforma.")
    ]
    for tit, desc in puntos_s2:
        p = tf_s2.add_paragraph()
        p.space_before = Pt(8)
        add_styled_run(p, f"• {tit} ", size=11, bold=True, color=TEXT_WHITE)
        add_styled_run(p, desc, size=10, color=TEXT_MUTED)

    agregar_tarjeta(s2, Inches(6.3), Inches(1.5), Inches(6.2), Inches(5.4))
    img_dist = os.path.join("docs", "img", "distribucion_streams.png")
    if os.path.exists(img_dist):
        s2.shapes.add_picture(img_dist, Inches(6.45), Inches(1.85), Inches(5.9))

    # SLIDE 3: Fase 3 - Preparación de Datos
    s3 = prs.slides.add_slide(blank_layout)
    aplicar_fondo(s3, prs)
    agregar_encabezado(s3, "Fase 3: Preparación Rigurosa de Datos y Preprocesamiento", "CRISP-DM — FASE 3")

    cajas_s3 = [
        ("🧹 Valores Nulos y Limpieza", "Menos del 0.2% del dataset", [
            "Auditoría con df.isnull().sum().",
            "Eliminación por lista (listwise deletion) sobre 180 filas con texto o audio ausente.",
            "Preservación total de las 85.000 canciones válidas sin sesgos artificiales."
        ], ACCENT_GREEN),
        ("📐 Outliers con Rango IQR", "Fórmula: IQR = Q₃ - Q₁", [
            "Límite Inferior: Q₁ - (1,5 × IQR)",
            "Límite Superior: Q₃ + (1,5 × IQR)",
            "Winsorización acotada (1% y 99%) en BPM y variables extremas.",
            "Conservación justificada de Mega-Hits por valor estratégico de negocio."
        ], ACCENT_BLUE),
        ("⚖️ Estandarización y Split", "StandardScaler + 80/20", [
            "Fórmula Z: z = (x - μ) / σ",
            "Atributos con media μ = 0 y varianza unitaria σ² = 1.",
            "Evita distorsión en distancias euclidianas de K-Means.",
            "Partición estratificada (stratify=y): 68.000 Train / 17.000 Test."
        ], RGBColor(234, 179, 8))
    ]

    for i, (tit_c, sub_c, bullets_c, col_c) in enumerate(cajas_s3):
        x = Inches(0.8 + i * 4.0)
        agregar_tarjeta(s3, x, Inches(1.6), Inches(3.7), Inches(5.2), border_color=col_c)
        tb_c = s3.shapes.add_textbox(x + Inches(0.2), Inches(1.8), Inches(3.3), Inches(4.8))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True

        p = tf_c.paragraphs[0]
        add_styled_run(p, f"{tit_c}\n", size=13, bold=True, color=col_c)

        p_sub = tf_c.add_paragraph()
        add_styled_run(p_sub, f"{sub_c}\n\n", size=11, bold=True, color=TEXT_WHITE)

        for b in bullets_c:
            p_b = tf_c.add_paragraph()
            p_b.space_before = Pt(4)
            add_styled_run(p_b, f"• {b}", size=10, color=TEXT_MUTED)

    # SLIDE 4: Fase 4A - Reglas de Asociación (Apriori)
    s4 = prs.slides.add_slide(blank_layout)
    aplicar_fondo(s4, prs)
    agregar_encabezado(s4, "Fase 4A: Minería de Reglas de Asociación con Apriori", "CRISP-DM — FASE 4 (MODELADO)")

    agregar_tarjeta(s4, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.4))
    tb_s4 = s4.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(11.1), Inches(5.0))
    tf_s4 = tb_s4.text_frame
    tf_s4.word_wrap = True

    p = tf_s4.paragraphs[0]
    add_styled_run(p, "Descubrimiento de Patrones de Afinidad (Librería mlxtend):\n", size=14, bold=True, color=ACCENT_BLUE)

    reglas_data = [
        ("Regla N° 1: [ Canción con Alta Popularidad ]  ➔  [ Alto Volumen de Streams + Género Pop ]",
         "Soporte: 1,21% | Confianza: 6,69% | Lift: 3,40 (Multiplicador de probabilidad respecto al azar)"),
        ("Regla N° 2: [ Alto Volumen de Streams + Género Pop ]  ➔  [ Canción con Alta Popularidad ]",
         "Soporte: 1,21% | Confianza: 61,33% (El 61,3% de temas Pop con alto stream logran alta popularidad) | Lift: 3,40"),
        ("Regla N° 3: [ Género R&B + Alto Volumen de Streams ]  ➔  [ Canción con Alta Popularidad ]",
         "Soporte: 1,23% | Confianza: 60,03% (6 de cada 10 temas de R&B con tracción son populares) | Lift: 3,33")
    ]

    for tit_r, met_r in reglas_data:
        p = tf_s4.add_paragraph()
        p.space_before = Pt(8)
        add_styled_run(p, f"📌 {tit_r}\n", size=11.5, bold=True, color=ACCENT_GREEN)
        add_styled_run(p, f"    {met_r}", size=10.5, color=TEXT_WHITE)

    p_int = tf_s4.add_paragraph()
    p_int.space_before = Pt(14)
    add_styled_run(p_int, "💡 Impacto Estratégico para el Negocio:\n", size=12, bold=True, color=ACCENT_BLUE)
    add_styled_run(p_int, "Un valor de Lift > 3,3 demuestra que la combinación Pop/R&B + tracción inicial triplica la probabilidad de éxito comercial en streaming frente a cualquier otro género del catálogo musical.", size=11, color=TEXT_MUTED)

    # SLIDE 5: Fase 4B - Clustering (K-Means)
    s5 = prs.slides.add_slide(blank_layout)
    aplicar_fondo(s5, prs)
    agregar_encabezado(s5, "Fase 4B: Segmentación de Catálogo con K-Means (K = 4)", "CRISP-DM — FASE 4 (CLUSTERING)")

    agregar_tarjeta(s5, Inches(0.8), Inches(1.5), Inches(6.5), Inches(5.4))
    img_codo = os.path.join("docs", "img", "metodo_codo_silueta.png")
    if os.path.exists(img_codo):
        s5.shapes.add_picture(img_codo, Inches(0.95), Inches(1.85), Inches(6.2))

    agregar_tarjeta(s5, Inches(7.5), Inches(1.5), Inches(5.0), Inches(5.4))
    tb_s5 = s5.shapes.add_textbox(Inches(7.7), Inches(1.7), Inches(4.6), Inches(5.0))
    tf_s5 = tb_s5.text_frame
    tf_s5.word_wrap = True

    p = tf_s5.paragraphs[0]
    add_styled_run(p, "Los 4 Arquetipos Sonoros Identificados:\n", size=13, bold=True, color=ACCENT_GREEN)

    clusters_info = [
        ("Cluster 0: Acústico, Instrumental & Chill", "Baja energía, alta instrumentalidad. Ideal para listas de estudio, lectura y concentración."),
        ("Cluster 1: Pop Comercial & Radio FM", "Bailabilidad y energía optimizadas. Gran rotación radial, playlists de gran alcance y streaming viral."),
        ("Cluster 2: Rock, Electrónica & Alta Potencia", "Máxima energía, BPM elevado y alto loudness. Entrenamientos, playlists 'workout' y festivales."),
        ("Cluster 3: Urbano, Trap & Modern Hits", "Ritmos sincopados y letra explícita predominante. Fuerte penetración en audiencias Gen Z.")
    ]
    for c_tit, c_desc in clusters_info:
        p = tf_s5.add_paragraph()
        p.space_before = Pt(6)
        add_styled_run(p, f"• {c_tit}: ", size=10.5, bold=True, color=TEXT_WHITE)
        add_styled_run(p, c_desc, size=9.5, color=TEXT_MUTED)

    # SLIDE 6: Fase 4C - Árbol de Decisión
    s6 = prs.slides.add_slide(blank_layout)
    aplicar_fondo(s6, prs)
    agregar_encabezado(s6, "Fase 4C: Clasificación de Hits con Árbol de Decisión", "CRISP-DM — FASE 4 (CLASIFICACIÓN)")

    agregar_tarjeta(s6, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.4))
    img_tree = os.path.join("docs", "img", "arbol_decision_grafico.png")
    if os.path.exists(img_tree):
        s6.shapes.add_picture(img_tree, Inches(1.0), Inches(1.65), Inches(11.3))

    tb_s6 = s6.shapes.add_textbox(Inches(1.0), Inches(5.6), Inches(11.3), Inches(1.1))
    tf_s6 = tb_s6.text_frame
    tf_s6.word_wrap = True
    p = tf_s6.paragraphs[0]
    add_styled_run(p, "Control Riguroso de Sobreajuste (Overfitting): ", size=11, bold=True, color=ACCENT_GREEN)
    add_styled_run(p, "Se evaluaron profundidades de 2 a 15. Para max_depth ≥ 8 existía sobreajuste severo (Train 84% vs Test < 52%). Se fijó max_depth = 3 con criterio Gini para garantizar 8 nodos hoja interpretables y alta capacidad de generalización.", size=10.5, color=TEXT_WHITE)

    # SLIDE 7: Fase 5 - Evaluación y Matriz de Confusión
    s7 = prs.slides.add_slide(blank_layout)
    aplicar_fondo(s7, prs)
    agregar_encabezado(s7, "Fase 5: Evaluación de Desempeño y Matriz de Confusión", "CRISP-DM — FASE 5 (EVALUACIÓN)")

    agregar_tarjeta(s7, Inches(0.8), Inches(1.5), Inches(5.2), Inches(5.4))
    img_cm = os.path.join("docs", "img", "matriz_confusion.png")
    if os.path.exists(img_cm):
        s7.shapes.add_picture(img_cm, Inches(1.1), Inches(1.8), Inches(4.6))

    agregar_tarjeta(s7, Inches(6.3), Inches(1.5), Inches(6.2), Inches(5.4))
    tb_s7 = s7.shapes.add_textbox(Inches(6.5), Inches(1.7), Inches(5.8), Inches(5.0))
    tf_s7 = tb_s7.text_frame
    tf_s7.word_wrap = True

    p = tf_s7.paragraphs[0]
    add_styled_run(p, "Resultados sobre 17.000 Canciones de Prueba:\n", size=13, bold=True, color=ACCENT_GREEN)

    items_eval = [
        ("Exactitud Global (Accuracy):", "57,95% sobre el conjunto independiente de validación."),
        ("Alta Precisión en Clase Estándar:", "74% de precisión (8.253 Verdaderos Negativos), permitiendo descartar maquetas con bajo potencial con alta fiabilidad."),
        ("Detección de Hits Comerciales:", "1.598 Verdaderos Positivos detectados exclusivamente por acústica."),
        ("¿Por qué existe un límite predictivo?:", "El éxito musical es multifactorial: la inversión de marketing, la viralización en TikTok y la fama del artista determinan gran parte de la tracción final."),
        ("Valor Práctico para la Industria:", "El modelo funciona como un filtro inteligente de precalificación (screening) para priorizar presupuestos de A&R.")
    ]
    for tit, desc in items_eval:
        p = tf_s7.add_paragraph()
        p.space_before = Pt(6)
        add_styled_run(p, f"• {tit} ", size=10.5, bold=True, color=TEXT_WHITE)
        add_styled_run(p, desc, size=10, color=TEXT_MUTED)

    # SLIDE 8: Conclusiones y Despliegue
    s8 = prs.slides.add_slide(blank_layout)
    aplicar_fondo(s8, prs)
    agregar_encabezado(s8, "Fases 6 y 7: Conclusiones Estratégicas y Despliegue Web", "CRISP-DM — FASES 6 & 7")

    cajas_s8 = [
        ("🎯 Recomendaciones de Negocio", "Acciones por Clúster", [
            "Clúster 1 (Pop): Concentrar inversión de pauta publicitaria en temas con bailabilidad > 0,65 y energía > 0,60.",
            "Clúster 0 (Acústico): No gastar en radio; colocar en playlists funcionales de estudio y concentración (mayor retención).",
            "Clúster 3 (Urbano): Pauta digital vertical móvil (TikTok/Reels) para audiencias de 16 a 24 años."
        ], ACCENT_GREEN),
        ("🚀 Despliegue y Entrega Completa", "Producto Funcional", [
            "Aplicación web interactiva en FastAPI y Bootstrap 5 Dark.",
            "Persistencia relacional con SQLite y suite de 17 pruebas unitarias.",
            "Repositorio sincronizado en GitHub con historial de trabajo colaborativo.",
            "Informe técnico completo de 5 a 8 páginas y diapositivas de defensa."
        ], ACCENT_BLUE)
    ]

    for i, (tit_c, sub_c, bullets_c, col_c) in enumerate(cajas_s8):
        x = Inches(0.8 + i * 5.9)
        agregar_tarjeta(s8, x, Inches(1.6), Inches(5.7), Inches(5.2), border_color=col_c)
        tb_c = s8.shapes.add_textbox(x + Inches(0.2), Inches(1.8), Inches(5.3), Inches(4.8))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True

        p = tf_c.paragraphs[0]
        add_styled_run(p, f"{tit_c}\n", size=13, bold=True, color=col_c)

        p_sub = tf_c.add_paragraph()
        add_styled_run(p_sub, f"{sub_c}\n\n", size=11, bold=True, color=TEXT_WHITE)

        for b in bullets_c:
            p_b = tf_c.add_paragraph()
            p_b.space_before = Pt(6)
            add_styled_run(p_b, f"• {b}", size=10.5, color=TEXT_MUTED)

    output_path = os.path.join("docs", "PRESENTACION_PROYECTO_CRISP_DM.pptx")
    prs.save(output_path)
    print(f"PPT Proyecto CRISP-DM creado exitosamente en: {output_path}")

if __name__ == "__main__":
    generar_ppt_aplicacion()
    generar_ppt_crisp_dm()
