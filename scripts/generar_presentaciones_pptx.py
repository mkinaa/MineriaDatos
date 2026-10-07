import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# ==============================================================================
# PALETA DE COLORES REDISEÑADA — MODERNA, OSCURA Y DE ALTO CONTRASTE
# ==============================================================================
DARK_BG = RGBColor(10, 14, 23)         # #0A0E17 Fondo profundo
CARD_BG = RGBColor(22, 30, 46)         # #161E2E Tarjetas elevadas
CARD_BORDER = RGBColor(46, 61, 89)     # #2E3D59 Borde sutil
GREEN_ACCENT = RGBColor(16, 185, 129)  # #10B981 Verde Esmeralda / Spotify
CYAN_ACCENT = RGBColor(56, 189, 248)   # #38BDF8 Cian Eléctrico
AMBER_ACCENT = RGBColor(245, 158, 11)  # #F59E0B Ámbar Destacado
PURPLE_ACCENT = RGBColor(168, 85, 247) # #A855F7 Púrpura Moderno
TEXT_MAIN = RGBColor(255, 255, 255)    # #FFFFFF Blanco puro alto contraste
TEXT_SUB = RGBColor(203, 213, 225)     # #CBD5E1 Gris claro altamente legible
TEXT_MUTED = RGBColor(148, 163, 184)   # #94A3B8 Gris secundario

def aplicar_fondo(slide, prs):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = DARK_BG
    bg.line.fill.background()
    return bg

def agregar_tarjeta(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1.5)
    return card

def agregar_encabezado_redisenado(slide, titulo_texto, tag_texto="SOUNDDATA ANALYTICS", tag_color=GREEN_ACCENT):
    # Tag superior
    tb_tag = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
    tf_tag = tb_tag.text_frame
    tf_tag.word_wrap = True
    p0 = tf_tag.paragraphs[0]
    r0 = p0.add_run()
    r0.text = tag_texto.upper()
    r0.font.size = Pt(11)
    r0.font.bold = True
    r0.font.color.rgb = tag_color

    # Título grande y conciso
    tb_tit = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
    tf_tit = tb_tit.text_frame
    tf_tit.word_wrap = True
    p1 = tf_tit.paragraphs[0]
    r1 = p1.add_run()
    r1.text = titulo_texto
    r1.font.size = Pt(25)
    r1.font.bold = True
    r1.font.color.rgb = TEXT_MAIN

def add_run(paragraph, text, size=13, bold=False, color=TEXT_SUB):
    r = paragraph.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = color
    return r

# ==============================================================================
# PPT 1: FUNCIONAMIENTO DE LA APLICACIÓN WEB (REDISEÑO VISUAL Y MINIMALISTA)
# ==============================================================================
def generar_ppt_aplicacion_redisenado():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    # --- SLIDE 1: Portada Moderna ---
    s1 = prs.slides.add_slide(blank)
    aplicar_fondo(s1, prs)
    agregar_tarjeta(s1, Inches(1.2), Inches(1.0), Inches(10.933), Inches(5.5), bg_color=CARD_BG, border_color=GREEN_ACCENT)

    tb = s1.shapes.add_textbox(Inches(1.6), Inches(1.5), Inches(10.133), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    add_run(p, "SOUNDDATA ANALYTICS\n", size=36, bold=True, color=GREEN_ACCENT)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(8)
    add_run(p, "Plataforma Web de Inteligencia y Simulación Musical\n", size=20, bold=True, color=TEXT_MAIN)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(16)
    add_run(p, "FastAPI  •  Bootstrap 5 Dark  •  SQLite  •  Machine Learning\n", size=15, bold=True, color=CYAN_ACCENT)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(28)
    add_run(p, "Demostración Funcional y Vistas de Usuario\n", size=13, bold=False, color=TEXT_SUB)
    add_run(p, "Universidad Santo Tomás — Minería de Datos (IEI-067)", size=12, bold=False, color=TEXT_MUTED)

    # --- SLIDE 2: Propósito y Arquitectura ---
    s2 = prs.slides.add_slide(blank)
    aplicar_fondo(s2, prs)
    agregar_encabezado_redisenado(s2, "Arquitectura y Valor para el Usuario", "PROPÓSITO DEL SISTEMA", GREEN_ACCENT)

    # 3 Tarjetas concisas a la izquierda
    items_s2 = [
        ("🎯 Decisiones con Datos", "Evaluación analítica de maquetas antes de invertir en producción musical.", GREEN_ACCENT),
        ("⚡ Inferencia Inmediata", "3 modelos de Machine Learning respondiendo en milisegundos.", CYAN_ACCENT),
        ("💾 Portafolio Transaccional", "Base de datos SQLite integrada para gestionar canciones evaluadas.", PURPLE_ACCENT)
    ]
    for i, (tit, desc, col) in enumerate(items_s2):
        y = Inches(1.6 + i * 1.75)
        agregar_tarjeta(s2, Inches(0.8), y, Inches(4.8), Inches(1.55), border_color=col)
        tb_card = s2.shapes.add_textbox(Inches(1.0), y + Inches(0.15), Inches(4.4), Inches(1.25))
        tf_c = tb_card.text_frame
        tf_c.word_wrap = True
        p = tf_c.paragraphs[0]
        add_run(p, f"{tit}\n", size=15, bold=True, color=col)
        p2 = tf_c.add_paragraph()
        p2.space_before = Pt(4)
        add_run(p2, desc, size=13, color=TEXT_SUB)

    # Imagen arquitectura a la derecha (Grande y destacada)
    agregar_tarjeta(s2, Inches(5.9), Inches(1.6), Inches(6.6), Inches(5.3))
    img_arq = os.path.join("docs", "img", "arquitectura_sistema.png")
    if os.path.exists(img_arq):
        s2.shapes.add_picture(img_arq, Inches(6.05), Inches(1.9), Inches(6.3))

    # --- SLIDE 3: Vista 1 - Dashboard de Oyentes ---
    s3 = prs.slides.add_slide(blank)
    aplicar_fondo(s3, prs)
    agregar_encabezado_redisenado(s3, "Vista 1: Análisis Global de Oyentes", "MONITOR DE AUDIENCIAS", GREEN_ACCENT)

    # Captura a la izquierda
    agregar_tarjeta(s3, Inches(0.8), Inches(1.6), Inches(7.8), Inches(5.3))
    img_v1 = os.path.join("docs", "img", "app_vista_1_analisis_oyentes.png")
    if os.path.exists(img_v1):
        s3.shapes.add_picture(img_v1, Inches(0.92), Inches(1.75), Inches(7.55))

    # Puntos concisos derecha
    puntos_s3 = [
        ("841 Millones", "Total de oyentes acumulados en el catálogo.", CYAN_ACCENT),
        ("12 Géneros Musicales", "Comparativa interactiva en gráficos de barras (Chart.js).", GREEN_ACCENT),
        ("Cuota de Mercado", "Distribución territorial por países en gráfico de dona.", AMBER_ACCENT)
    ]
    for i, (tit, desc, col) in enumerate(puntos_s3):
        y = Inches(1.6 + i * 1.75)
        agregar_tarjeta(s3, Inches(8.9), y, Inches(3.6), Inches(1.55), border_color=col)
        tb_c = s3.shapes.add_textbox(Inches(9.1), y + Inches(0.2), Inches(3.2), Inches(1.15))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        p = tf_c.paragraphs[0]
        add_run(p, f"{tit}\n", size=16, bold=True, color=col)
        p2 = tf_c.add_paragraph()
        p2.space_before = Pt(4)
        add_run(p2, desc, size=12.5, color=TEXT_SUB)

    # --- SLIDE 4: Vista 2 - Segmentación por Atributo ---
    s4 = prs.slides.add_slide(blank)
    aplicar_fondo(s4, prs)
    agregar_encabezado_redisenado(s4, "Vista 2: Segmentación Univariada de Audiencias", "ANÁLISIS POR CATEGORÍA", CYAN_ACCENT)

    agregar_tarjeta(s4, Inches(0.8), Inches(1.6), Inches(7.8), Inches(5.3))
    img_v2 = os.path.join("docs", "img", "app_vista_2_segmentacion_atributo.png")
    if os.path.exists(img_v2):
        s4.shapes.add_picture(img_v2, Inches(0.92), Inches(1.75), Inches(7.55))

    puntos_s4 = [
        ("7 Selectores Dinámicos", "Filtro rápido por Género, País, Año, Popularidad, Bailabilidad y Energía.", CYAN_ACCENT),
        ("Tabla de Penetración", "Cálculo en tiempo real del porcentaje de peso de cada segmento.", GREEN_ACCENT),
        ("Descarga en 1 Clic", "Botón para exportar el resumen analítico estructurado en JSON.", AMBER_ACCENT)
    ]
    for i, (tit, desc, col) in enumerate(puntos_s4):
        y = Inches(1.6 + i * 1.75)
        agregar_tarjeta(s4, Inches(8.9), y, Inches(3.6), Inches(1.55), border_color=col)
        tb_c = s4.shapes.add_textbox(Inches(9.1), y + Inches(0.2), Inches(3.2), Inches(1.15))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        p = tf_c.paragraphs[0]
        add_run(p, f"{tit}\n", size=15, bold=True, color=col)
        p2 = tf_c.add_paragraph()
        p2.space_before = Pt(4)
        add_run(p2, desc, size=12.5, color=TEXT_SUB)

    # --- SLIDE 5: Vista 3 - Simulador ML ---
    s5 = prs.slides.add_slide(blank)
    aplicar_fondo(s5, prs)
    agregar_encabezado_redisenado(s5, "Vista 3: Simulador Predictivo con Machine Learning", "MOTOR DE INFERENCIA EN VIVO", GREEN_ACCENT)

    agregar_tarjeta(s5, Inches(0.8), Inches(1.6), Inches(7.8), Inches(5.3))
    img_v3 = os.path.join("docs", "img", "app_vista_3_simulador_ml.png")
    if os.path.exists(img_v3):
        s5.shapes.add_picture(img_v3, Inches(0.92), Inches(1.75), Inches(7.55))

    puntos_s5 = [
        ("🎛️ Sliders Acústicos", "Ajuste en vivo de BPM, Energía, Sonoridad, Bailabilidad e Instrumentalidad.", CYAN_ACCENT),
        ("🧠 Triple Diagnóstico", "Predicción de Hit (Árbol) + Clúster Sonoro (K-Means) + Afinidad (Apriori).", GREEN_ACCENT),
        ("💾 Guardar en Portafolio", "Registro directo de la canción evaluada en SQLite con un solo clic.", PURPLE_ACCENT)
    ]
    for i, (tit, desc, col) in enumerate(puntos_s5):
        y = Inches(1.6 + i * 1.75)
        agregar_tarjeta(s5, Inches(8.9), y, Inches(3.6), Inches(1.55), border_color=col)
        tb_c = s5.shapes.add_textbox(Inches(9.1), y + Inches(0.2), Inches(3.2), Inches(1.15))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        p = tf_c.paragraphs[0]
        add_run(p, f"{tit}\n", size=15, bold=True, color=col)
        p2 = tf_c.add_paragraph()
        p2.space_before = Pt(4)
        add_run(p2, desc, size=12.5, color=TEXT_SUB)

    # --- SLIDE 6: Vista 4 - Portafolio y CRUD ---
    s6 = prs.slides.add_slide(blank)
    aplicar_fondo(s6, prs)
    agregar_encabezado_redisenado(s6, "Vista 4: Portafolio de Canciones & Gestión CRUD", "ADMINISTRACIÓN Y PERSISTENCIA", PURPLE_ACCENT)

    agregar_tarjeta(s6, Inches(0.8), Inches(1.6), Inches(7.8), Inches(5.3))
    img_v4 = os.path.join("docs", "img", "app_vista_4_portafolio_crud.png")
    if os.path.exists(img_v4):
        s6.shapes.add_picture(img_v4, Inches(0.92), Inches(1.75), Inches(7.55))

    puntos_s6 = [
        ("Base de Datos SQLite", "Persistencia segura y liviana mediante la base de datos 'sounddata.db'.", PURPLE_ACCENT),
        ("Operaciones Completas", "Creación manual, edición modal, filtrado por género y eliminación.", GREEN_ACCENT),
        ("Búsqueda en Tiempo Real", "Filtrado instantáneo sin recargar la página web.", CYAN_ACCENT)
    ]
    for i, (tit, desc, col) in enumerate(puntos_s6):
        y = Inches(1.6 + i * 1.75)
        agregar_tarjeta(s6, Inches(8.9), y, Inches(3.6), Inches(1.55), border_color=col)
        tb_c = s6.shapes.add_textbox(Inches(9.1), y + Inches(0.2), Inches(3.2), Inches(1.15))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        p = tf_c.paragraphs[0]
        add_run(p, f"{tit}\n", size=15, bold=True, color=col)
        p2 = tf_c.add_paragraph()
        p2.space_before = Pt(4)
        add_run(p2, desc, size=12.5, color=TEXT_SUB)

    # --- SLIDE 7: Calidad y Despliegue Cloud ---
    s7 = prs.slides.add_slide(blank)
    aplicar_fondo(s7, prs)
    agregar_encabezado_redisenado(s7, "Calidad de Software y Despliegue en la Nube", "CONFIABILIDAD Y ESTABILIDAD", GREEN_ACCENT)

    cajas_s7 = [
        ("🧪 17/17 Pruebas Unitarias", "100% de Tests Aprobados", [
            "Validación de endpoints en test_api.py",
            "Ciclo CRUD completo en test_database.py",
            "Inferencia exacta en test_modelos.py"
        ], GREEN_ACCENT),
        ("🛡️ Tolerancia a Fallos", "Mensajes Amigables", [
            "Control de esquemas con Pydantic.",
            "Cero pantallas de error o tracebacks.",
            "Validación de rangos numéricos."
        ], CYAN_ACCENT),
        ("☁️ Despliegue en Render", "Acceso Público 24/7", [
            "Servidor ASGI Uvicorn contenerizable.",
            "Integración continua desde GitHub.",
            "Video de respaldo de 2 minutos."
        ], PURPLE_ACCENT)
    ]
    for i, (tit_c, sub_c, bullets_c, col_c) in enumerate(cajas_s7):
        x = Inches(0.8 + i * 4.0)
        agregar_tarjeta(s7, x, Inches(1.6), Inches(3.7), Inches(5.3), border_color=col_c)
        tb_c = s7.shapes.add_textbox(x + Inches(0.25), Inches(1.85), Inches(3.2), Inches(4.8))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True

        p = tf_c.paragraphs[0]
        add_run(p, f"{tit_c}\n", size=17, bold=True, color=col_c)
        p_sub = tf_c.add_paragraph()
        p_sub.space_before = Pt(4)
        add_run(p_sub, f"{sub_c}\n\n", size=13, bold=True, color=TEXT_MAIN)

        for b in bullets_c:
            p_b = tf_c.add_paragraph()
            p_b.space_before = Pt(8)
            add_run(p_b, f"✔ {b}", size=12.5, color=TEXT_SUB)

    output_path = os.path.join("docs", "PRESENTACION_APLICACION_WEB.pptx")
    prs.save(output_path)
    print(f"Rediseño PPT Aplicación Web guardado en: {output_path}")

# ==============================================================================
# PPT 2: PROYECTO & METODOLOGÍA CRISP-DM (REDISEÑO VISUAL Y MINIMALISTA)
# ==============================================================================
def generar_ppt_crisp_dm_redisenado():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    # --- SLIDE 1: Portada Moderna ---
    s1 = prs.slides.add_slide(blank)
    aplicar_fondo(s1, prs)
    agregar_tarjeta(s1, Inches(1.2), Inches(1.0), Inches(10.933), Inches(5.5), bg_color=CARD_BG, border_color=CYAN_ACCENT)

    tb = s1.shapes.add_textbox(Inches(1.6), Inches(1.5), Inches(10.133), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    add_run(p, "MINERÍA DE DATOS CON CRISP-DM\n", size=34, bold=True, color=CYAN_ACCENT)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(8)
    add_run(p, "SoundData Analytics: Segmentación y Predicción de Éxito Musical\n", size=20, bold=True, color=TEXT_MAIN)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(16)
    add_run(p, "Catálogo de 85.000 Canciones de Spotify (2015–2025)\n", size=15, bold=True, color=GREEN_ACCENT)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(28)
    add_run(p, "Grupo 4: Vicente Muñoz • Juan Ortiz • Jordan Murillo • Jorge Moncada • Jose Mendez • Bastian Parraguez\n", size=12.5, color=TEXT_SUB)
    add_run(p, "Docentes Guía: Florentino Vargas & Rosa Rao  |  Universidad Santo Tomás", size=11.5, color=TEXT_MUTED)

    # --- SLIDE 2: Fases 1 & 2 - Negocio y Datos ---
    s2 = prs.slides.add_slide(blank)
    aplicar_fondo(s2, prs)
    agregar_encabezado_redisenado(s2, "Fases 1 y 2: Negocio y Comprensión de los Datos", "CRISP-DM — FASES 1 & 2", CYAN_ACCENT)

    # Gráfico a la izquierda
    agregar_tarjeta(s2, Inches(0.8), Inches(1.6), Inches(7.6), Inches(5.3))
    img_dist = os.path.join("docs", "img", "distribucion_streams.png")
    if os.path.exists(img_dist):
        s2.shapes.add_picture(img_dist, Inches(0.95), Inches(1.8), Inches(7.3))

    # Puntos derecha
    puntos_s2 = [
        ("85.000 Registros", "Catálogo global con 17 atributos acústicos y metadatos de mercado.", CYAN_ACCENT),
        ("Top 25% = Éxito", "Corte en Percentil 75 (≥ 85.2M de streams) para definir la clase 'es_exito'.", GREEN_ACCENT),
        ("Fuerte Asimetría", "El 25% de canciones concentra el 68% de las reproducciones totales.", AMBER_ACCENT)
    ]
    for i, (tit, desc, col) in enumerate(puntos_s2):
        y = Inches(1.6 + i * 1.75)
        agregar_tarjeta(s2, Inches(8.7), y, Inches(3.8), Inches(1.55), border_color=col)
        tb_c = s2.shapes.add_textbox(Inches(8.9), y + Inches(0.2), Inches(3.4), Inches(1.15))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        p = tf_c.paragraphs[0]
        add_run(p, f"{tit}\n", size=16, bold=True, color=col)
        p2 = tf_c.add_paragraph()
        p2.space_before = Pt(4)
        add_run(p2, desc, size=12.5, color=TEXT_SUB)

    # --- SLIDE 3: Fase 3 - Preparación de Datos ---
    s3 = prs.slides.add_slide(blank)
    aplicar_fondo(s3, prs)
    agregar_encabezado_redisenado(s3, "Fase 3: Preparación Rigurosa de los Datos", "CRISP-DM — FASE 3", CYAN_ACCENT)

    cajas_s3 = [
        ("🧹 Limpieza de Nulos", "99.8% de Calidad", [
            "Eliminación por lista de solo 180 registros incompletos.",
            "Cero sesgos por imputación artificial en variables acústicas.",
            "Preservación íntegra de 85.000 pistas."
        ], GREEN_ACCENT),
        ("📐 Outliers con IQR", "Fórmula: Q₃ - Q₁", [
            "Límites: Q₁ - 1.5×IQR y Q₃ + 1.5×IQR.",
            "Winsorización (1% y 99%) en BPM y variables extremas.",
            "Conservación intencional de Mega-Hits."
        ], CYAN_ACCENT),
        ("⚖️ Escalado y Split", "StandardScaler (Z)", [
            "Estandarización: media 0 y varianza unitaria 1.",
            "Evita distorsión en distancias de K-Means.",
            "Split estratificado: 80% Train / 20% Test."
        ], AMBER_ACCENT)
    ]
    for i, (tit_c, sub_c, bullets_c, col_c) in enumerate(cajas_s3):
        x = Inches(0.8 + i * 4.0)
        agregar_tarjeta(s3, x, Inches(1.6), Inches(3.7), Inches(5.3), border_color=col_c)
        tb_c = s3.shapes.add_textbox(x + Inches(0.25), Inches(1.85), Inches(3.2), Inches(4.8))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True

        p = tf_c.paragraphs[0]
        add_run(p, f"{tit_c}\n", size=17, bold=True, color=col_c)
        p_sub = tf_c.add_paragraph()
        p_sub.space_before = Pt(4)
        add_run(p_sub, f"{sub_c}\n\n", size=13, bold=True, color=TEXT_MAIN)

        for b in bullets_c:
            p_b = tf_c.add_paragraph()
            p_b.space_before = Pt(8)
            add_run(p_b, f"✔ {b}", size=12.5, color=TEXT_SUB)

    # --- SLIDE 4: Fase 4A - Reglas de Asociación ---
    s4 = prs.slides.add_slide(blank)
    aplicar_fondo(s4, prs)
    agregar_encabezado_redisenado(s4, "Fase 4A: Reglas de Asociación con Apriori", "CRISP-DM — ASOCIACIÓN", GREEN_ACCENT)

    # Gran tarjeta con la regla estelar y métricas grandes
    agregar_tarjeta(s4, Inches(0.8), Inches(1.6), Inches(11.733), Inches(2.5), border_color=GREEN_ACCENT)
    tb_top = s4.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.1), Inches(2.1))
    tf_top = tb_top.text_frame
    tf_top.word_wrap = True

    p = tf_top.paragraphs[0]
    add_run(p, "REGLA CLAVE DE MERCADO (LIFT = 3,40)\n", size=16, bold=True, color=GREEN_ACCENT)
    p2 = tf_top.add_paragraph()
    p2.space_before = Pt(6)
    add_run(p2, "[ Alto Volumen de Streams  +  Género Pop ]  ➔  [ Canción de Alta Popularidad ]\n", size=20, bold=True, color=TEXT_MAIN)
    p3 = tf_top.add_paragraph()
    p3.space_before = Pt(6)
    add_run(p3, "• Confianza: 61,33% (6 de cada 10 temas cumplen la regla)   • Soporte: 1,21% (+1.020 canciones)", size=14, color=CYAN_ACCENT)

    # 2 Tarjetas inferiores complementarias
    agregar_tarjeta(s4, Inches(0.8), Inches(4.35), Inches(5.7), Inches(2.55), border_color=CYAN_ACCENT)
    tb_b1 = s4.shapes.add_textbox(Inches(1.0), Inches(4.5), Inches(5.3), Inches(2.2))
    tf_b1 = tb_b1.text_frame
    tf_b1.word_wrap = True
    p = tf_b1.paragraphs[0]
    add_run(p, "Regla Alternativa: Género R&B\n", size=16, bold=True, color=CYAN_ACCENT)
    p2 = tf_b1.add_paragraph()
    p2.space_before = Pt(4)
    add_run(p2, "[ Género R&B + Alto Stream ] ➔ [ Alta Popularidad ]\n", size=14, bold=True, color=TEXT_MAIN)
    add_run(p2, "Lift: 3,33  |  Confianza: 60,03% en el catálogo musical.", size=13, color=TEXT_SUB)

    agregar_tarjeta(s4, Inches(6.833), Inches(4.35), Inches(5.7), Inches(2.55), border_color=AMBER_ACCENT)
    tb_b2 = s4.shapes.add_textbox(Inches(7.033), Inches(4.5), Inches(5.3), Inches(2.2))
    tf_b2 = tb_b2.text_frame
    tf_b2.word_wrap = True
    p = tf_b2.paragraphs[0]
    add_run(p, "Conclusión de Negocio:\n", size=16, bold=True, color=AMBER_ACCENT)
    p2 = tf_b2.add_paragraph()
    p2.space_before = Pt(4)
    add_run(p2, "Las canciones Pop y R&B que logran tracción inicial tienen el triple de probabilidad de convertirse en éxitos transversales frente al resto.", size=13.5, color=TEXT_MAIN)

    # --- SLIDE 5: Fase 4B - Clustering K-Means ---
    s5 = prs.slides.add_slide(blank)
    aplicar_fondo(s5, prs)
    agregar_encabezado_redisenado(s5, "Fase 4B: Segmentación de Catálogo (K-Means, K = 4)", "CRISP-DM — CLUSTERING", GREEN_ACCENT)

    # Imagen codo y silueta a la izquierda
    agregar_tarjeta(s5, Inches(0.8), Inches(1.6), Inches(6.8), Inches(5.3))
    img_codo = os.path.join("docs", "img", "metodo_codo_silueta.png")
    if os.path.exists(img_codo):
        s5.shapes.add_picture(img_codo, Inches(0.95), Inches(1.85), Inches(6.5))

    # 4 Arquetipos sonoros a la derecha (grandes)
    arquetipos = [
        ("Clúster 0: Chill & Instrumental", "Baja energía, acústico. Listas de estudio y concentración.", CYAN_ACCENT),
        ("Clúster 1: Pop Comercial", "Bailabilidad y energía optimizadas. Gran rotación radial.", GREEN_ACCENT),
        ("Clúster 2: Rock & Fiesta", "Alta potencia acústica y tempo elevado. Festivales y deportes.", AMBER_ACCENT),
        ("Clúster 3: Urbano & Explícito", "Ritmo marcado y lenguaje explícito. Audiencia Gen Z.", PURPLE_ACCENT)
    ]
    for i, (tit, desc, col) in enumerate(arquetipos):
        y = Inches(1.6 + i * 1.35)
        agregar_tarjeta(s5, Inches(7.9), y, Inches(4.6), Inches(1.2), border_color=col)
        tb_c = s5.shapes.add_textbox(Inches(8.1), y + Inches(0.12), Inches(4.2), Inches(0.95))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        p = tf_c.paragraphs[0]
        add_run(p, f"{tit}\n", size=14, bold=True, color=col)
        p2 = tf_c.add_paragraph()
        add_run(p2, desc, size=11.5, color=TEXT_SUB)

    # --- SLIDE 6: Fase 4C - Árbol de Decisión ---
    s6 = prs.slides.add_slide(blank)
    aplicar_fondo(s6, prs)
    agregar_encabezado_redisenado(s6, "Fase 4C: Clasificación de Hits con Árbol de Decisión", "CRISP-DM — CLASIFICACIÓN", GREEN_ACCENT)

    # Imagen árbol
    agregar_tarjeta(s6, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.3))
    img_tree = os.path.join("docs", "img", "arbol_decision_grafico.png")
    if os.path.exists(img_tree):
        s6.shapes.add_picture(img_tree, Inches(1.0), Inches(1.75), Inches(11.3))

    tb_s6 = s6.shapes.add_textbox(Inches(1.1), Inches(5.7), Inches(11.1), Inches(1.0))
    tf_s6 = tb_s6.text_frame
    tf_s6.word_wrap = True
    p = tf_s6.paragraphs[0]
    add_run(p, "Control de Sobreajuste (max_depth = 3): ", size=14, bold=True, color=GREEN_ACCENT)
    add_run(p, "Se limitó a 3 niveles para evitar memorización (profundidades mayores provocaban overfitting de 84% train vs <52% test). Entrega 8 reglas claras e interpretables para productores.", size=13, color=TEXT_MAIN)

    # --- SLIDE 7: Fase 5 - Evaluación y Matriz de Confusión ---
    s7 = prs.slides.add_slide(blank)
    aplicar_fondo(s7, prs)
    agregar_encabezado_redisenado(s7, "Fase 5: Evaluación y Matriz de Confusión", "CRISP-DM — EVALUACIÓN", AMBER_ACCENT)

    # Heatmap a la izquierda
    agregar_tarjeta(s7, Inches(0.8), Inches(1.6), Inches(5.5), Inches(5.3))
    img_cm = os.path.join("docs", "img", "matriz_confusion.png")
    if os.path.exists(img_cm):
        s7.shapes.add_picture(img_cm, Inches(1.15), Inches(1.9), Inches(4.8))

    # Métricas destacadas derecha
    puntos_s7 = [
        ("74% Precisión en Descarte", "8.253 Verdaderos Negativos. Permite filtrar maquetas sin potencial con alta fiabilidad.", GREEN_ACCENT),
        ("57,95% Exactitud Global", "Desempeño sobre 17.000 canciones de prueba independientes.", CYAN_ACCENT),
        ("Límite Acústico Natural", "El éxito musical es multifactorial: depende además de inversión en marketing y viralización.", AMBER_ACCENT)
    ]
    for i, (tit, desc, col) in enumerate(puntos_s7):
        y = Inches(1.6 + i * 1.75)
        agregar_tarjeta(s7, Inches(6.6), y, Inches(5.9), Inches(1.55), border_color=col)
        tb_c = s7.shapes.add_textbox(Inches(6.8), y + Inches(0.2), Inches(5.5), Inches(1.15))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        p = tf_c.paragraphs[0]
        add_run(p, f"{tit}\n", size=16, bold=True, color=col)
        p2 = tf_c.add_paragraph()
        p2.space_before = Pt(4)
        add_run(p2, desc, size=13, color=TEXT_SUB)

    # --- SLIDE 8: Conclusiones Estratégicas ---
    s8 = prs.slides.add_slide(blank)
    aplicar_fondo(s8, prs)
    agregar_encabezado_redisenado(s8, "Conclusiones y Recomendaciones de Negocio", "CRISP-DM — FASE 6", GREEN_ACCENT)

    cajas_s8 = [
        ("🎯 Estrategia Pop & Urbano", "Inversión en Publicidad", [
            "Concentrar pauta en canciones con bailabilidad > 0.65 y energía > 0.60.",
            "Promoción vertical en TikTok/Reels para audiencias de 16 a 24 años."
        ], GREEN_ACCENT),
        ("🧘 Estrategia Acústica / Chill", "Listas Funcionales", [
            "Evitar costosas campañas de radio comercial.",
            "Posicionar en playlists de estudio, concentración y sueño (mayor retención)."
        ], CYAN_ACCENT),
        ("🚀 De Datos a Producto Web", "Entrega Completa", [
            "Plataforma web interactiva con backend FastAPI y persistencia SQLite.",
            "17 pruebas unitarias aprobadas y código listo para producción en la nube."
        ], PURPLE_ACCENT)
    ]
    for i, (tit_c, sub_c, bullets_c, col_c) in enumerate(cajas_s8):
        x = Inches(0.8 + i * 4.0)
        agregar_tarjeta(s8, x, Inches(1.6), Inches(3.7), Inches(5.3), border_color=col_c)
        tb_c = s8.shapes.add_textbox(x + Inches(0.25), Inches(1.85), Inches(3.2), Inches(4.8))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True

        p = tf_c.paragraphs[0]
        add_run(p, f"{tit_c}\n", size=16, bold=True, color=col_c)
        p_sub = tf_c.add_paragraph()
        p_sub.space_before = Pt(4)
        add_run(p_sub, f"{sub_c}\n\n", size=13, bold=True, color=TEXT_MAIN)

        for b in bullets_c:
            p_b = tf_c.add_paragraph()
            p_b.space_before = Pt(10)
            add_run(p_b, f"✔ {b}", size=12.5, color=TEXT_SUB)

    output_path = os.path.join("docs", "PRESENTACION_PROYECTO_CRISP_DM.pptx")
    prs.save(output_path)
    print(f"Rediseño PPT Proyecto CRISP-DM guardado en: {output_path}")

if __name__ == "__main__":
    generar_ppt_aplicacion_redisenado()
    generar_ppt_crisp_dm_redisenado()
