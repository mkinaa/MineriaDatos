"""
Generador de Documento Word (.docx) para el Guion Oficial de Defensa Oral
SoundData Analytics — Minería de Datos (IEI-067), Universidad Santo Tomás
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_shading(cell, color_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_callout_borders(cell, border_color="1DB954", border_sz="36"):
    # Borde grueso a la izquierda, sin bordes en top/bottom/right
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="{border_sz}" w:space="0" w:color="{border_color}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    cell._tc.get_or_add_tcPr().append(borders)

def set_table_borders(table, color="CCCCCC", sz="4"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:left w:val="none"/>
            <w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def add_header_footer(doc):
    for s in doc.sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)

        # Header
        header = s.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("SoundData Analytics · Guion Oficial de Defensa Oral (IEI-067)")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(120, 120, 120)

        # Footer
        footer = s.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Universidad Santo Tomás · Minería de Datos · Grupo 4 · Página ")
        frun.font.name = "Calibri"
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = RGBColor(120, 120, 120)

def construir_documento():
    doc = Document()
    add_header_footer(doc)

    # Colores institucionales
    VERDE_OSCURO = RGBColor(16, 124, 65)     # #107C41
    VERDE_SPOTIFY = RGBColor(29, 185, 84)    # #1DB954
    TEXTO_OSCURO = RGBColor(31, 41, 55)      # #1F2937
    GRIS_SECUNDARIO = RGBColor(107, 114, 128) # #6B7280

    # ==============================================================================
    # PORTADA / ENCABEZADO FORMAL
    # ==============================================================================
    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_after = Pt(2)
    r_meta = p_meta.add_run("UNIVERSIDAD SANTO TOMÁS · ESCUELA DE INGENIERÍA · MINERÍA DE DATOS (IEI-067)")
    r_meta.font.name = "Calibri"
    r_meta.font.size = Pt(9.5)
    r_meta.font.bold = True
    r_meta.font.color.rgb = VERDE_OSCURO

    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(4)
    p_title.paragraph_format.space_after = Pt(4)
    r_title = p_title.add_run("Guion Oficial para la Defensa Oral")
    r_title.font.name = "Calibri"
    r_title.font.size = Pt(24)
    r_title.font.bold = True
    r_title.font.color.rgb = TEXTO_OSCURO

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(14)
    r_sub = p_sub.add_run("SoundData Analytics: Inteligencia de Negocios y Predicción de Éxito en Streaming")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(13)
    r_sub.font.italic = True
    r_sub.font.color.rgb = GRIS_SECUNDARIO

    # Tabla de Metadatos
    t_meta = doc.add_table(rows=4, cols=2)
    t_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_meta, color="E5E7EB", sz="6")
    
    meta_data = [
        ("Docentes Evaluadores", "Florentino Vargas y Rosa Rao"),
        ("Integrantes (Grupo 4)", "Vicente Muñoz, Juan Ortiz, Jordan Murillo, Jorge Moncada, Jose Mendez, Bastian Parraguez"),
        ("Duración Total Estimada", "12 a 13 minutos (Parte 1: ~7 min · Parte 2: ~5 min · Demo y Preguntas: ~2 min)"),
        ("Archivos de Presentación", "docs/PARTE1_ANALISIS_SOUNDDATA_V2.pptx y docs/PARTE2_APLICACION_SOUNDDATA_V2.pptx")
    ]
    for row_idx, (k, v) in enumerate(meta_data):
        row = t_meta.rows[row_idx]
        cell_k, cell_v = row.cells[0], row.cells[1]
        cell_k.width = Inches(2.2)
        cell_v.width = Inches(4.3)
        set_cell_shading(cell_k, "F9FAFB")
        set_cell_shading(cell_v, "FFFFFF")
        
        pk = cell_k.paragraphs[0]
        pk.paragraph_format.space_after = Pt(2)
        rk = pk.add_run(k)
        rk.font.name = "Calibri"
        rk.font.size = Pt(9.5)
        rk.font.bold = True
        rk.font.color.rgb = TEXTO_OSCURO

        pv = cell_v.paragraphs[0]
        pv.paragraph_format.space_after = Pt(2)
        rv = pv.add_run(v)
        rv.font.name = "Calibri"
        rv.font.size = Pt(9.5)
        rv.font.color.rgb = TEXTO_OSCURO

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # ==============================================================================
    # SECCIÓN 1: RECOMENDACIONES CLAVE DE PRESENTACIÓN
    # ==============================================================================
    h1 = doc.add_heading("1. Recomendaciones Estratégicas para la Defensa", level=1)
    h1.paragraph_format.space_before = Pt(14)
    h1.paragraph_format.space_after = Pt(6)
    for r in h1.runs:
        r.font.name = "Calibri"
        r.font.color.rgb = VERDE_OSCURO

    p_rec = doc.add_paragraph()
    p_rec.paragraph_format.space_after = Pt(4)
    p_rec.add_run("Para maximizar el puntaje en la rúbrica de presentación oral, sigan estas cuatro directivas de equipo:\n")
    
    recs = [
        ("No lean la pantalla:", " Las diapositivas fueron rediseñadas con letras gigantes (≥20 pt) y un máximo de 40 palabras. La diapositiva es un impacto visual para los profesores; el desarrollo argumentativo y técnico lo dicen ustedes."),
        ("Respeten el cronómetro:", " Cada integrante tiene entre 40 segundos y 1 minuto y 15 segundos por turno. Hablen pausado pero con convicción. Un pase fluido transmite coordinación profesional."),
        ("Contacto visual y postura ejecutiva:", " Miren de frente a los docentes Florentino Vargas y Rosa Rao. Proyecten seguridad ingenieril en las decisiones estadísticas tomadas."),
        ("Anexos Ocultos para Preguntas Difíciles:", " Ambas presentaciones incluyen diapositivas técnicas ocultas (A1 a A5). Si el profesor pide la matriz de confusión completa, el coeficiente de silueta o la arquitectura FastAPI, naveguen directo al anexo correspondiente.")
    ]
    for bold_text, normal_text in recs:
        p_item = doc.add_paragraph(style='List Bullet')
        p_item.paragraph_format.space_after = Pt(3)
        r_b = p_item.add_run(bold_text)
        r_b.font.bold = True
        r_b.font.color.rgb = VERDE_OSCURO
        r_n = p_item.add_run(normal_text)
        r_n.font.color.rgb = TEXTO_OSCURO

    # ==============================================================================
    # SECCIÓN 2: TABLA RESUMEN DE ORADORES Y TIEMPOS
    # ==============================================================================
    h2 = doc.add_heading("2. Distribución de Roles, Tiempos y Diapositivas", level=1)
    h2.paragraph_format.space_before = Pt(14)
    h2.paragraph_format.space_after = Pt(6)
    for r in h2.runs:
        r.font.name = "Calibri"
        r.font.color.rgb = VERDE_OSCURO

    t_roles = doc.add_table(rows=7, cols=4)
    t_roles.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_roles, color="CCCCCC", sz="4")

    headers_roles = ["Integrante", "Rol en la Defensa", "Diapositivas Asignadas", "Tiempo"]
    widths_roles = [Inches(1.6), Inches(2.3), Inches(1.8), Inches(0.8)]
    for i, h_text in enumerate(headers_roles):
        c = t_roles.rows[0].cells[i]
        c.width = widths_roles[i]
        set_cell_shading(c, "107C41")
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h_text)
        r.font.name = "Calibri"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data_roles = [
        ("Vicente Muñoz", "Apertura, Problema, Negocio y Cierre", "D1, D2, D8, D9, D16", "2:50 min"),
        ("Juan Ortiz", "Datos, Preprocesamiento e Inventario CRUD", "D3, D4, D14", "2:15 min"),
        ("Jorge Moncada", "K-Means (4 Clústeres) y Vista Segmentación", "D5, D12", "1:45 min"),
        ("Jose Mendez", "Árbol de Decisión y Demo del Simulador", "D6, D13", "2:15 min"),
        ("Jordan Murillo", "Reglas Apriori y Vista Análisis Oyentes", "D7, D11", "1:35 min"),
        ("Bastian Parraguez", "Arquitectura Web, Tests Pytest y Despliegue", "D10, D15", "1:30 min")
    ]
    for r_idx, row_vals in enumerate(data_roles):
        row = t_roles.rows[r_idx + 1]
        bg = "F9FAFB" if r_idx % 2 == 0 else "FFFFFF"
        for c_idx, val in enumerate(row_vals):
            c = row.cells[c_idx]
            c.width = widths_roles[c_idx]
            set_cell_shading(c, bg)
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            if c_idx == 3:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(9)
            if c_idx == 0:
                r.font.bold = True
            r.font.color.rgb = TEXTO_OSCURO

    doc.add_page_break()

    # ==============================================================================
    # SECCIÓN 3: GUION DETALLADO PARTE 1 — CRISP-DM Y ANÁLISIS
    # ==============================================================================
    h3 = doc.add_heading("3. Guion Detallado — Parte 1: El Análisis CRISP-DM", level=1)
    h3.paragraph_format.space_after = Pt(4)
    for r in h3.runs:
        r.font.name = "Calibri"
        r.font.color.rgb = VERDE_OSCURO

    p_p1_desc = doc.add_paragraph()
    p_p1_desc.paragraph_format.space_after = Pt(12)
    r_p1_desc = p_p1_desc.add_run("Archivo: docs/PARTE1_ANALISIS_SOUNDDATA_V2.pptx  ·  Duración estimada: 7 minutos  ·  9 diapositivas visibles + 4 anexos")
    r_p1_desc.font.italic = True
    r_p1_desc.font.size = Pt(9.5)
    r_p1_desc.font.color.rgb = GRIS_SECUNDARIO

    slides_p1 = [
        {
            "id": "D1 · Portada",
            "orador": "Vicente Muñoz",
            "tiempo": "0:00 – 0:30 (30 seg)",
            "pantalla": "Título 'De los datos al éxito musical', pregunta guía, integrantes y datos institucionales.",
            "guion": (
                "Muy buenos días, profesores Florentino Vargas y Rosa Rao, y compañeros. Hoy el Grupo 4 les presenta "
                "SoundData Analytics, un sistema de inteligencia de negocios para la industria musical basado en la metodología CRISP-DM.\n\n"
                "Como equipo nos planteamos una pregunta fundamental: ¿Es posible saber, antes de desembolsar millones en producir y "
                "promocionar una canción, a qué tipo de oyente le va a gustar y si tiene probabilidades reales de convertirse en un éxito comercial?\n\n"
                "Nuestra defensa está dividida en dos partes: primero, les explicaremos qué descubrimos a partir de 85.000 canciones; y luego, "
                "les mostraremos la aplicación web que construimos para que cualquier sello discográfico use estos modelos con un solo clic. "
                "Comencemos con el problema."
            ),
            "cue": "(Avanzar a Diapositiva 2)"
        },
        {
            "id": "D2 · El Problema de Negocio",
            "orador": "Vicente Muñoz",
            "tiempo": "0:30 – 1:20 (50 seg)",
            "pantalla": "Cifra protagónica '+100.000 canciones nuevas al día' y las tres preguntas críticas del negocio.",
            "guion": (
                "En la industria musical actual existe una saturación sin precedentes: cada día se suben más de 100.000 canciones nuevas a las plataformas de streaming. "
                "Históricamente, las casas discográficas y los productores independientes han invertido presupuestos millonarios basándose únicamente en la intuición "
                "o el 'olfato artístico', lo que genera una tasa de fracaso de inversión superior al 80 %.\n\n"
                "Para mitigar este riesgo financiero, definimos tres objetivos concretos de minería de datos:\n"
                "1. Primero: Clasificar y predecir si una canción tiene potencial de alto impacto antes de su masterización.\n"
                "2. Segundo: Identificar qué arquetipo sonoro u oyente objetivo la va a recibir mejor.\n"
                "3. Y tercero: Descubrir qué combinaciones de género y popularidad generan sinergia real en el mercado.\n\n"
                "Ahora Juan les explicará los datos que recolectamos para responder estas preguntas."
            ),
            "cue": "(Avanzar a Diapositiva 3)"
        },
        {
            "id": "D3 · Los Datos y la Asimetría del Éxito",
            "orador": "Juan Ortiz",
            "tiempo": "1:20 – 2:10 (50 seg)",
            "pantalla": "Cifra destacada '25 % → 68 % de reproducciones' y gráfico oscuro de distribución asimétrica.",
            "guion": (
                "Gracias, Vicente. Para este estudio analizamos un catálogo masivo de 85.000 canciones de Spotify, abarcando una década completa, entre 2015 y 2025, "
                "con 17 atributos acústicos y comerciales en 12 géneros musicales.\n\n"
                "Al realizar el análisis exploratorio, nos encontramos con la realidad brutal del mercado musical que ven en el gráfico de la derecha: "
                "una distribución fuertemente asimétrica. Un pequeño grupo de canciones acapara la gran mayoría del tráfico. Específicamente, el 25 % superior "
                "de las canciones concentra el 68 % de todas las reproducciones mundiales.\n\n"
                "Por esta razón estadística, definimos rigurosamente como 'Éxito Comercial' a aquellas canciones situadas en el cuartil superior (Q3), "
                "es decir, canciones con 85,2 millones de reproducciones o más. Este es el umbral que el modelo debe predecir."
            ),
            "cue": "(Avanzar a Diapositiva 4)"
        },
        {
            "id": "D4 · Preparación de Datos con Rigor",
            "orador": "Juan Ortiz",
            "tiempo": "2:10 – 2:50 (40 seg)",
            "pantalla": "Cifra '99,8 % conservado' y las 3 tarjetas de preparación (Limpieza, Protección de Éxitos, Escala).",
            "guion": (
                "En minería de datos, la calidad de los resultados depende directamente de la limpieza. De las 85.180 filas originales, descartamos únicamente "
                "180 registros con valores nulos o corruptos, lo que representa apenas un 0,2 % de pérdida. Es decir, conservamos el 99,8 % de los datos limpios.\n\n"
                "Pero el desafío más importante fue el tratamiento de valores extremos: en música, un tema con millones de reproducciones o con tempo muy acelerado "
                "no es un 'error de tipeo', es un megahit. Por lo tanto, no eliminamos los outliers de streams; aplicamos winsorización en percentiles 1 y 99 para ritmos "
                "atípicos y estandarizamos todas las variables acústicas con StandardScaler para que ninguna dominara artificialmente la distancia.\n\n"
                "Con los datos preparados, Jorge les explicará el primer modelo: la segmentación por K-Means."
            ),
            "cue": "(Avanzar a Diapositiva 5)"
        },
        {
            "id": "D5 · Segmentación Acústica (K-Means)",
            "orador": "Jorge Moncada",
            "tiempo": "2:50 – 3:50 (1:00 min)",
            "pantalla": "4 tarjetas con perfiles sonoros y sus colores oficiales: Turquesa, Fucsia, Naranja y Púrpura.",
            "guion": (
                "Gracias, Juan. Para entender a qué audiencia pertenece cada canción, aplicamos el algoritmo de agrupamiento no supervisado K-Means. "
                "Mediante el Método del Codo y el Coeficiente de Silueta, determinamos que K = 4 es la estructura óptima del catálogo.\n\n"
                "El modelo descubrió cuatro perfiles acústicos con identidad muy clara:\n"
                "• En Turquesa (Clúster 0): Chill y Acústico, dominado por baladas, música clásica y acústica, con baja energía y alto valor instrumental.\n"
                "• En Fucsia (Clúster 1): Pop Enérgico, canciones sumamente luminosas, de alta positividad y ritmo comercial.\n"
                "• En Naranja (Clúster 2): Rock y Sonidos Orgánicos, temas potentes donde priman guitarras y volumen elevado con baja bailabilidad electrónica.\n"
                "• Y en Púrpura (Clúster 3): Urbano y Bailable, el territorio del reggaetón, hip-hop y trap latino, caracterizado por una máxima bailabilidad e intensas frecuencias graves.\n\n"
                "Esto le permite a un productor saber al instante en qué playlist y nicho de mercado encaja su sonido. Ahora, Jose les mostrará cómo predecimos si será un éxito."
            ),
            "cue": "(Avanzar a Diapositiva 6)"
        },
        {
            "id": "D6 · Modelo Predictivo (Árbol de Decisión)",
            "orador": "Jose Mendez",
            "tiempo": "3:50 – 4:50 (1:00 min)",
            "pantalla": "Métrica '74 % de precisión en descarte' y diagrama simplificado del árbol con 8 caminos.",
            "guion": (
                "Gracias, Jorge. Para predecir el éxito comercial entrenamos un Árbol de Decisión. Decidimos acotar intencionalmente la profundidad máxima a max_depth = 3. "
                "¿Por qué? Porque un árbol de solo 8 caminos posibles es interpretable para los ejecutivos de un sello discográfico y previene que el modelo memorice el ruido del dataset.\n\n"
                "El árbol demostró que los factores decisivos para escalar a las grandes ligas son el volumen sonoro medio (loudness), la energía y la bailabilidad.\n\n"
                "Pero lo más valioso para el negocio es su rol como filtro de descarte: cuando el árbol clasifica una pista como 'No Éxito', acierta el 74 % de las veces. "
                "En la industria, evitar gastar cientos de miles de dólares en promocionar canciones inviables genera más ahorro y rentabilidad que intentar adivinar un golpe de suerte.\n\n"
                "A continuación, Jordan les presentará las reglas de asociación que completan este análisis."
            ),
            "cue": "(Avanzar a Diapositiva 7)"
        },
        {
            "id": "D7 · Reglas de Asociación (Algoritmo Apriori)",
            "orador": "Jordan Murillo",
            "tiempo": "4:50 – 5:40 (50 seg)",
            "pantalla": "Métrica 'Lift 3,40' y tarjetas con las 3 reglas comerciales (Pop, Urbano e Instrumental).",
            "guion": (
                "Gracias, Jose. Mientras los modelos anteriores analizan el sonido de forma individual, con el algoritmo Apriori buscamos qué combinaciones de género, "
                "popularidad y presencia en el catálogo ocurren juntas de manera recurrente.\n\n"
                "Minamos cientos de reglas con mlxtend y filtramos aquellas con verdadero impacto comercial:\n"
                "• La regla reina nos reveló un Lift de 3,40 y 61,3 % de confianza: indica que cuando una pista del género Pop logra alta exposición, su probabilidad de alcanzar popularidad masiva es 3,4 veces superior a lo esperable por puro azar.\n"
                "• La segunda regla demostró que la música Urbana con alta bailabilidad mantiene una confianza sostenida sobre el 58 % en listas de éxitos.\n"
                "• Y la tercera regla nos advierte que los temas instrumentales rara vez traspasan al top 25 % masivo, requiriendo estrategias de marketing de nicho.\n\n"
                "Ahora Vicente sintetizará el impacto financiero de estos tres hallazgos."
            ),
            "cue": "(Avanzar a Diapositiva 8)"
        },
        {
            "id": "D8 · Impacto en el Negocio y Retorno de Inversión",
            "orador": "Vicente Muñoz",
            "tiempo": "5:40 – 6:20 (40 seg)",
            "pantalla": "Tres pilares de impacto financiero: Ahorro de capital, pauta dirigida y colaboraciones comerciales.",
            "guion": (
                "En resumen, integrar minería de datos transforma la toma de decisiones en tres niveles:\n"
                "1. Optimización de Presupuesto: Usar el árbol como filtro de entrada reduce drásticamente las pérdidas en canciones sin tracción acústica.\n"
                "2. Segmentación de Audiencia: Asignar cada tema a uno de los 4 clústeres permite dirigir la pauta publicitaria en TikTok y Spotify Ads exactamente al público objetivo.\n"
                "3. Estrategia de Lanzamientos: Utilizar las reglas de asociación para juntar artistas urbanos y pop maximiza el retorno publicitario.\n\n"
                "Pero estos modelos no podían quedarse en un Jupyter Notebook. Para que un equipo de marketing o un productor los utilice en su día a día, construimos una solución accesible."
            ),
            "cue": "(Avanzar a Diapositiva 9)"
        },
        {
            "id": "D9 · Transición a la Aplicación Web",
            "orador": "Vicente Muñoz",
            "tiempo": "6:20 – 6:50 (30 seg)",
            "pantalla": "Tarjeta de transición con el logo de SoundData y puente interactivo hacia la Parte 2.",
            "guion": (
                "Y es así como nace SoundData Analytics Web: un sistema full-stack donde cualquier usuario, sin saber de código ni de estadística, puede interactuar con el catálogo, "
                "simular canciones en vivo y gestionar su propio portafolio.\n\n"
                "Damos paso a la Parte 2, donde Bastian y el equipo les presentarán el funcionamiento de la herramienta."
            ),
            "cue": "(Cambio de archivo PPTX a PARTE 2 · Diapositiva 10)"
        }
    ]

    for s in slides_p1:
        # Encabezado de la diapositiva
        p_sh = doc.add_paragraph()
        p_sh.paragraph_format.space_before = Pt(10)
        p_sh.paragraph_format.space_after = Pt(2)
        r_sid = p_sh.add_run(s["id"])
        r_sid.font.name = "Calibri"
        r_sid.font.size = Pt(13)
        r_sid.font.bold = True
        r_sid.font.color.rgb = VERDE_OSCURO

        # Metadatos del turno (Tabla pequeña)
        t_s = doc.add_table(rows=1, cols=3)
        t_s.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(t_s, color="E5E7EB", sz="4")
        
        c0, c1, c2 = t_s.rows[0].cells[0], t_s.rows[0].cells[1], t_s.rows[0].cells[2]
        c0.width, c1.width, c2.width = Inches(2.2), Inches(1.8), Inches(2.5)
        set_cell_shading(c0, "F3F4F6")
        set_cell_shading(c1, "F3F4F6")
        set_cell_shading(c2, "F3F4F6")

        c0.paragraphs[0].add_run(f"👤 Orador: {s['orador']}").font.bold = True
        c1.paragraphs[0].add_run(f"⏱️ {s['tiempo']}")
        c2.paragraphs[0].add_run(f"🖥️ {s['pantalla']}").font.italic = True
        for ci in (c0, c1, c2):
            ci.paragraphs[0].runs[0].font.size = Pt(8.5)
            ci.paragraphs[0].runs[0].font.name = "Calibri"

        # Caja de Callout para el Guion Verbal
        t_callout = doc.add_table(rows=1, cols=1)
        t_callout.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell_callout = t_callout.rows[0].cells[0]
        cell_callout.width = Inches(6.5)
        set_cell_shading(cell_callout, "F0FDF4") # Fondo verde tenue
        set_callout_borders(cell_callout, border_color="1DB954", border_sz="36")

        p_speech = cell_callout.paragraphs[0]
        p_speech.paragraph_format.space_before = Pt(4)
        p_speech.paragraph_format.space_after = Pt(4)
        p_speech.paragraph_format.line_spacing = 1.15
        
        r_speech_tag = p_speech.add_run("🗣️ Lo que debes decir en voz alta:\n")
        r_speech_tag.font.name = "Calibri"
        r_speech_tag.font.size = Pt(9.5)
        r_speech_tag.font.bold = True
        r_speech_tag.font.color.rgb = VERDE_OSCURO

        r_speech = p_speech.add_run(f'"{s["guion"]}"')
        r_speech.font.name = "Calibri"
        r_speech.font.size = Pt(10)
        r_speech.font.color.rgb = TEXTO_OSCURO

        # Cue de avance
        p_cue = doc.add_paragraph()
        p_cue.paragraph_format.space_before = Pt(2)
        p_cue.paragraph_format.space_after = Pt(8)
        r_cue = p_cue.add_run(s["cue"])
        r_cue.font.name = "Calibri"
        r_cue.font.size = Pt(8.5)
        r_cue.font.bold = True
        r_cue.font.color.rgb = GRIS_SECUNDARIO

    doc.add_page_break()

    # ==============================================================================
    # SECCIÓN 4: GUION DETALLADO PARTE 2 — APLICACIÓN WEB Y DEMO
    # ==============================================================================
    h4 = doc.add_heading("4. Guion Detallado — Parte 2: La Aplicación Web y Demo", level=1)
    h4.paragraph_format.space_after = Pt(4)
    for r in h4.runs:
        r.font.name = "Calibri"
        r.font.color.rgb = VERDE_OSCURO

    p_p2_desc = doc.add_paragraph()
    p_p2_desc.paragraph_format.space_after = Pt(12)
    r_p2_desc = p_p2_desc.add_run("Archivo: docs/PARTE2_APLICACION_SOUNDDATA_V2.pptx  ·  Duración estimada: 5 minutos  ·  7 diapositivas visibles + 1 anexo")
    r_p2_desc.font.italic = True
    r_p2_desc.font.size = Pt(9.5)
    r_p2_desc.font.color.rgb = GRIS_SECUNDARIO

    slides_p2 = [
        {
            "id": "D10 · Portada de la Aplicación y Arquitectura",
            "orador": "Bastian Parraguez",
            "tiempo": "6:50 – 7:35 (45 seg)",
            "pantalla": "Diagrama en 3 pasos (Ajustas → Analiza → Decides) y credenciales técnicas (<0,25s, SQLite, 100 % en español).",
            "guion": (
                "Muchas gracias, Vicente. Bienvenidos a la Parte 2. SoundData Web fue diseñada con un principio fundamental: "
                "complejidad en los modelos, simplicidad absoluta para el usuario final.\n\n"
                "Su arquitectura está montada sobre FastAPI en Python, lo que nos permite tiempos de respuesta menores a 250 milisegundos por inferencia. "
                "Para la persistencia creamos una base de datos SQLite transaccional, y en el frontend utilizamos una interfaz oscura moderna, responsiva "
                "y completamente en español.\n\n"
                "A continuación, revisaremos las cuatro vistas principales que componen el sistema."
            ),
            "cue": "(Avanzar a Diapositiva 11)"
        },
        {
            "id": "D11 · Vista 1: Análisis de Oyentes",
            "orador": "Jordan Murillo",
            "tiempo": "7:35 – 8:20 (45 seg)",
            "pantalla": "Captura de la Vista 1 (4 KPIs superiores, barras por género y dona geográfica por país).",
            "guion": (
                "La primera pantalla es la Vista de Análisis de Oyentes. Su propósito es ofrecer una radiografía ejecutiva inmediata del mercado musical.\n\n"
                "En la parte superior encontramos cuatro indicadores clave que resumen más de 841 millones de oyentes acumulados. Debajo, un gráfico dinámico "
                "de barras compara el volumen de reproducciones entre los 12 géneros musicales, evidenciando el dominio del Pop y lo Urbano; y a la derecha, "
                "un gráfico de dona desglosa el reparto geográfico entre los principales mercados mundiales.\n\n"
                "Todo el módulo se alimenta directamente de la API REST de forma fluida."
            ),
            "cue": "(Avanzar a Diapositiva 12)"
        },
        {
            "id": "D12 · Vista 2: Segmentación por Atributo",
            "orador": "Jorge Moncada",
            "tiempo": "8:20 – 9:05 (45 seg)",
            "pantalla": "Captura de la Vista 2, selectores de filtrado dinámico y tabla de distribución porcentual.",
            "guion": (
                "La segunda pantalla es la Vista de Segmentación. Esta herramienta permite al analista explorar interactivamente el catálogo completo según cualquier dimensión: "
                "por género, país, año de lanzamiento o clúster acústico.\n\n"
                "Al cambiar los selectores, la tabla recalcula al instante qué porcentaje del catálogo representa ese segmento y su nivel medio de streams. "
                "Además, cuenta con un botón de exportación directa que genera un reporte descargable para presentaciones de directorio."
            ),
            "cue": "(Avanzar a Diapositiva 13)"
        },
        {
            "id": "D13 · Vista 3: Simulador Predictivo (DEMO EN VIVO)",
            "orador": "Jose Mendez",
            "tiempo": "9:05 – 10:20 (1:15 min)",
            "pantalla": "Captura de la Vista 3 o Pantalla en vivo de la aplicación en el navegador (http://127.0.0.1:8000).",
            "guion": (
                "Llegamos al corazón de la plataforma: el Simulador Predictivo de Inteligencia Artificial.\n\n"
                "[Si se hace demo en vivo, cambiar a la ventana del navegador; si no, señalar los controles en la diapositiva]:\n"
                "Aquí un productor puede ingresar las características de una canción antes de lanzarla: ajustamos el tempo en BPM, la energía, el volumen y la bailabilidad mediante estos controles deslizantes.\n\n"
                "Al hacer clic en 'Evaluar Potencial', en menos de un cuarto de segundo la API normaliza los valores y consulta nuestros tres modelos en paralelo:\n"
                "1. El velocímetro nos indica la probabilidad de éxito según el árbol de decisión.\n"
                "2. El badge nos asigna automáticamente a cuál de los 4 clústeres sonoros pertenece.\n"
                "3. Y en la tarjeta inferior recibimos consejos de negocio personalizados derivados de las reglas de asociación.\n\n"
                "Con el botón inferior, podemos guardar esta evaluación directamente en nuestro portafolio sin recargar la página."
            ),
            "cue": "(Avanzar a Diapositiva 14)"
        },
        {
            "id": "D14 · Vista 4: Portafolio y Gestión CRUD",
            "orador": "Juan Ortiz",
            "tiempo": "10:20 – 11:05 (45 seg)",
            "pantalla": "Captura de la tabla de portafolio con acciones Crear, Editar, Buscar y Eliminar conectadas a SQLite.",
            "guion": (
                "La cuarta pantalla es la Gestión del Portafolio. Aquí implementamos un ciclo CRUD completo conectado a SQLite:\n"
                "• El analista puede registrar nuevas canciones evaluadas.\n"
                "• Puede editar sus parámetros acústicos si el productor modificó la mezcla en el estudio.\n"
                "• Cuenta con un buscador en tiempo real por título o artista.\n"
                "• Y puede eliminar pistas descartadas con confirmación de seguridad.\n\n"
                "Para garantizar que la aplicación nunca se vea vacía en la nube, el sistema incluye un mecanismo de auto-semillado que inicializa seis canciones de referencia en la base de datos."
            ),
            "cue": "(Avanzar a Diapositiva 15)"
        },
        {
            "id": "D15 · Calidad, Validación y Pruebas",
            "orador": "Bastian Parraguez",
            "tiempo": "11:05 – 11:50 (45 seg)",
            "pantalla": "Cifra protagónica '17 / 17 pruebas aprobadas', validación tipada con Pydantic y despliegue.",
            "guion": (
                "Como futuros ingenieros, la robustez del software era fundamental. La aplicación no solo se ve bien, sino que está respaldada por una suite rigurosa de calidad:\n"
                "• Contamos con 17 pruebas unitarias automatizadas con Pytest, todas aprobadas al 100 %, verificando los endpoints HTTP, el ciclo CRUD de la base de datos y la inferencia de los modelos serializados.\n"
                "• Cada entrada de usuario está protegida por esquemas tipados con Pydantic; si alguien introduce un BPM negativo o texto en un campo numérico, el sistema responde con mensajes de error claros en español, sin romperse.\n"
                "• Además, la plataforma está configurada y lista para despliegue en la nube mediante un archivo Procfile contenerizable."
            ),
            "cue": "(Avanzar a Diapositiva 16)"
        },
        {
            "id": "D16 · Conclusiones y Cierre",
            "orador": "Vicente Muñoz (Todo el Grupo)",
            "tiempo": "11:50 – 12:30 (40 seg)",
            "pantalla": "Título 'Los datos no reemplazan al oído, pero ayudan a invertir mejor' y agradecimiento final.",
            "guion": (
                "Para concluir: los datos y los algoritmos jamás van a reemplazar la creatividad ni la sensibilidad de un músico o productor. Sin embargo, en una industria donde se lanzan cien mil temas diarios, "
                "la minería de datos permite transformar la incertidumbre en una ventaja estratégica medible.\n\n"
                "Hoy les demostramos que con rigor metodológico CRISP-DM y buenas prácticas de ingeniería de software, es posible pasar desde un conjunto de 85.000 filas hasta una herramienta productiva, "
                "confiable y con valor comercial real.\n\n"
                "Agradecemos sinceramente su atención y quedamos a total disposición de la comisión para responder sus preguntas."
            ),
            "cue": "(Fin de la presentación · Paso a la Ronda de Preguntas)"
        }
    ]

    for s in slides_p2:
        p_sh = doc.add_paragraph()
        p_sh.paragraph_format.space_before = Pt(10)
        p_sh.paragraph_format.space_after = Pt(2)
        r_sid = p_sh.add_run(s["id"])
        r_sid.font.name = "Calibri"
        r_sid.font.size = Pt(13)
        r_sid.font.bold = True
        r_sid.font.color.rgb = VERDE_OSCURO

        t_s = doc.add_table(rows=1, cols=3)
        t_s.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(t_s, color="E5E7EB", sz="4")
        
        c0, c1, c2 = t_s.rows[0].cells[0], t_s.rows[0].cells[1], t_s.rows[0].cells[2]
        c0.width, c1.width, c2.width = Inches(2.2), Inches(1.8), Inches(2.5)
        set_cell_shading(c0, "F3F4F6")
        set_cell_shading(c1, "F3F4F6")
        set_cell_shading(c2, "F3F4F6")

        c0.paragraphs[0].add_run(f"👤 Orador: {s['orador']}").font.bold = True
        c1.paragraphs[0].add_run(f"⏱️ {s['tiempo']}")
        c2.paragraphs[0].add_run(f"🖥️ {s['pantalla']}").font.italic = True
        for ci in (c0, c1, c2):
            ci.paragraphs[0].runs[0].font.size = Pt(8.5)
            ci.paragraphs[0].runs[0].font.name = "Calibri"

        t_callout = doc.add_table(rows=1, cols=1)
        t_callout.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell_callout = t_callout.rows[0].cells[0]
        cell_callout.width = Inches(6.5)
        set_cell_shading(cell_callout, "F0FDF4")
        set_callout_borders(cell_callout, border_color="1DB954", border_sz="36")

        p_speech = cell_callout.paragraphs[0]
        p_speech.paragraph_format.space_before = Pt(4)
        p_speech.paragraph_format.space_after = Pt(4)
        p_speech.paragraph_format.line_spacing = 1.15
        
        r_speech_tag = p_speech.add_run("🗣️ Lo que debes decir en voz alta:\n")
        r_speech_tag.font.name = "Calibri"
        r_speech_tag.font.size = Pt(9.5)
        r_speech_tag.font.bold = True
        r_speech_tag.font.color.rgb = VERDE_OSCURO

        r_speech = p_speech.add_run(f'"{s["guion"]}"')
        r_speech.font.name = "Calibri"
        r_speech.font.size = Pt(10)
        r_speech.font.color.rgb = TEXTO_OSCURO

        p_cue = doc.add_paragraph()
        p_cue.paragraph_format.space_before = Pt(2)
        p_cue.paragraph_format.space_after = Pt(8)
        r_cue = p_cue.add_run(s["cue"])
        r_cue.font.name = "Calibri"
        r_cue.font.size = Pt(8.5)
        r_cue.font.bold = True
        r_cue.font.color.rgb = GRIS_SECUNDARIO

    doc.add_page_break()

    # ==============================================================================
    # SECCIÓN 5: GUÍA PARA LA RONDA DE PREGUNTAS (ANEXOS OCULTOS)
    # ==============================================================================
    h5 = doc.add_heading("5. Guía de Respuestas para Preguntas del Jurado", level=1)
    h5.paragraph_format.space_after = Pt(6)
    for r in h5.runs:
        r.font.name = "Calibri"
        r.font.color.rgb = VERDE_OSCURO

    p_qa_intro = doc.add_paragraph()
    p_qa_intro.paragraph_format.space_after = Pt(10)
    p_qa_intro.add_run(
        "Si los docentes evaluadores hacen preguntas técnicas específicas o cuestionan algún valor, "
        "mantengan la calma y utilicen las diapositivas de anexo ocultas como respaldo visual:"
    )

    t_qa = doc.add_table(rows=6, cols=4)
    t_qa.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_qa, color="CCCCCC", sz="4")

    qa_headers = ["Pregunta Probable del Docente", "Anexo", "Quién Responde", "Respuesta Maestra Demoledora"]
    qa_widths = [Inches(1.8), Inches(0.8), Inches(1.1), Inches(2.8)]
    for i, h_text in enumerate(qa_headers):
        c = t_qa.rows[0].cells[i]
        c.width = qa_widths[i]
        set_cell_shading(c, "107C41")
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h_text)
        r.font.name = "Calibri"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    qa_data = [
        (
            "¿Por qué eligieron K=4 y no K=3 o K=5?",
            "A2 / A4",
            "Jorge Moncada",
            "Evaluamos el coeficiente de silueta entre K=2 y K=8. Aunque K=2 tenía un puntaje matemático ligeramente mayor, solo dividía canciones lentas de rápidas sin valor comercial. K=4 logró una silueta sólida de 0,22 caracterizando los 4 nichos acústicos reales que exige la industria: Chill, Pop, Rock y Urbano."
        ),
        (
            "El árbol tiene 58 % de exactitud global, ¿por qué dicen que es un buen modelo?",
            "A3",
            "Jose Mendez",
            "Porque ante una distribución desbalanceada (75/25), el costo de un Falso Positivo es perder dinero produciendo un fracaso. Nuestro árbol alcanza un 74 % de precisión en la clase No Éxito, operando exactamente como un filtro de descarte conservador que evita pérdidas millonarias."
        ),
        (
            "¿Qué significa exactamente el Lift de 3,40?",
            "A4",
            "Jordan Murillo",
            "Un Lift igual a 1 significa independencia estadística. Un Lift de 3,40 demuestra matemáticamente que la conjunción de género Pop con alta rotación en listas es 3,4 veces más frecuente que si ambos eventos ocurrieran por puro azar dentro del catálogo."
        ),
        (
            "¿Por qué descartaron los nulos en vez de imputar?",
            "A1",
            "Juan Ortiz",
            "Eran solo 180 registros sobre 85.180 (el 0,21 %). Imputar con media o mediana habría introducido sesgos artificiales en los ritmos acústicos; descartar el 0,2 % permitió mantener el 99,8 % de los datos completamente puros y reales."
        ),
        (
            "¿Por qué eligieron SQLite y no PostgreSQL?",
            "A5",
            "Bastian Parraguez",
            "SQLite opera como un motor embebido de cero latencia de red, garantizando transacciones ACID completas y portabilidad inmediata sin requerir un servidor dedicado adicional para esta escala de usuarios."
        )
    ]

    for r_idx, row_vals in enumerate(qa_data):
        row = t_qa.rows[r_idx + 1]
        bg = "F9FAFB" if r_idx % 2 == 0 else "FFFFFF"
        for c_idx, val in enumerate(row_vals):
            c = row.cells[c_idx]
            c.width = qa_widths[c_idx]
            set_cell_shading(c, bg)
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(3)
            if c_idx in (1, 2):
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8.5)
            if c_idx == 0:
                r.font.bold = True
            r.font.color.rgb = TEXTO_OSCURO

    out_path = os.path.join("docs", "GUION_OFICIAL_DEFENSA_ORAL.docx")
    doc.save(out_path)
    print(f"Documento Word guardado exitosamente en: {out_path}")

if __name__ == "__main__":
    construir_documento()
