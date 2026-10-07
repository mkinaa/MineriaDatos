import os
import shutil
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# ==============================================================================
# SISTEMA DE DISEÑO ESTRICTO (CORRECCIONES_PRESENTACIONES_SOUNDDATA.MD)
# ==============================================================================
BG_COLOR = RGBColor(10, 10, 10)         # #0A0A0A Fondo general oscuro
CARD_COLOR = RGBColor(24, 24, 24)       # #181818 Superficie de tarjeta
BORDER_COLOR = RGBColor(42, 42, 42)     # #2A2A2A Borde neutro 1 pt
ACCENT_GREEN = RGBColor(29, 185, 84)    # #1DB954 Verde Spotify / Cifras
TEXT_WHITE = RGBColor(255, 255, 255)    # #FFFFFF Texto principal
TEXT_GRAY = RGBColor(179, 179, 179)     # #B3B3B3 Texto secundario (>= 14 pt)
TEXT_FOOTER = RGBColor(115, 115, 115)   # #737373 Pie de diapositiva (12 pt)

# Colores fijos de datos / clústeres
COLOR_CHILL = RGBColor(20, 184, 166)    # #14B8A6 Turquesa Clúster 0
COLOR_POP = RGBColor(236, 72, 153)      # #EC4899 Rosa Clúster 1
COLOR_ROCK = RGBColor(249, 115, 22)     # #F97316 Naranja Clúster 2
COLOR_URBANO = RGBColor(168, 85, 247)   # #A855F7 Morado Clúster 3
COLOR_AMBER = RGBColor(245, 158, 11)    # #F59E0B Advertencia / Cautela
COLOR_BLUE = RGBColor(59, 130, 246)     # #3B82F6 Azul datos

FONT_FAMILY = "Segoe UI"

def set_slide_bg(slide, prs):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_COLOR
    bg.line.fill.background()
    return bg

def add_footer(slide, current_slide, total_slides=9):
    # Pie izquierdo
    tb_l = slide.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(5.0), Inches(0.35))
    tf_l = tb_l.text_frame
    p_l = tf_l.paragraphs[0]
    r_l = p_l.add_run()
    r_l.text = "SoundData Analytics · Grupo 4"
    r_l.font.name = FONT_FAMILY
    r_l.font.size = Pt(12)
    r_l.font.color.rgb = TEXT_FOOTER

    # Pie derecho
    tb_r = slide.shapes.add_textbox(Inches(10.5), Inches(6.9), Inches(2.0), Inches(0.35))
    tf_r = tb_r.text_frame
    p_r = tf_r.paragraphs[0]
    p_r.alignment = PP_ALIGN.RIGHT
    r_r = p_r.add_run()
    r_r.text = f"{current_slide:02d} / {total_slides:02d}"
    r_r.font.name = FONT_FAMILY
    r_r.font.size = Pt(12)
    r_r.font.color.rgb = TEXT_FOOTER

def add_header(slide, title_text, kicker_text):
    # Kicker (14 pt bold green)
    tb_k = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.7), Inches(0.35))
    tf_k = tb_k.text_frame
    tf_k.word_wrap = True
    p0 = tf_k.paragraphs[0]
    r0 = p0.add_run()
    r0.text = kicker_text.upper()
    r0.font.name = FONT_FAMILY
    r0.font.size = Pt(14)
    r0.font.bold = True
    r0.font.color.rgb = ACCENT_GREEN

    # Title (36 pt bold white, message-oriented)
    tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.8))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p1 = tf_t.paragraphs[0]
    r1 = p1.add_run()
    r1.text = title_text
    r1.font.name = FONT_FAMILY
    r1.font.size = Pt(32)
    r1.font.bold = True
    r1.font.color.rgb = TEXT_WHITE

def add_card(slide, left, top, width, height, bg_color=CARD_COLOR, border_color=BORDER_COLOR):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1)
    return card

def add_speaker_notes(slide, notes_text):
    notes = slide.notes_slide.notes_text_frame
    notes.text = notes_text

# ==============================================================================
# CONSTRUCTOR: PARTE 1 — EL ANÁLISIS (CRISP-DM)
# ==============================================================================
def construir_parte1_crisp():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    # --- D1: Portada ---
    s1 = prs.slides.add_slide(blank)
    set_slide_bg(s1, prs)
    add_card(s1, Inches(0.8), Inches(0.8), Inches(11.733), Inches(5.9), bg_color=CARD_COLOR, border_color=BORDER_COLOR)

    # Chip Kicker
    tb_tag = s1.shapes.add_textbox(Inches(1.3), Inches(1.3), Inches(10.5), Inches(0.4))
    r_tag = tb_tag.text_frame.paragraphs[0].add_run()
    r_tag.text = "PARTE 1 · EL ANÁLISIS"
    r_tag.font.name = FONT_FAMILY
    r_tag.font.size = Pt(14)
    r_tag.font.bold = True
    r_tag.font.color.rgb = ACCENT_GREEN

    tb_t = s1.shapes.add_textbox(Inches(1.3), Inches(1.8), Inches(10.5), Inches(1.5))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p = tf_t.paragraphs[0]
    r = p.add_run()
    r.text = "De los datos al éxito musical"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(46)
    r.font.bold = True
    r.font.color.rgb = TEXT_WHITE

    p2 = tf_t.add_paragraph()
    p2.space_before = Pt(8)
    r2 = p2.add_run()
    r2.text = "¿Podemos saber, antes de lanzar una canción, a quién le va a gustar y si tiene opciones de ser un éxito?"
    r2.font.name = FONT_FAMILY
    r2.font.size = Pt(20)
    r2.font.italic = True
    r2.font.color.rgb = TEXT_GRAY

    # Separador
    tb_meta = s1.shapes.add_textbox(Inches(1.3), Inches(4.3), Inches(10.5), Inches(1.8))
    tf_m = tb_meta.text_frame
    tf_m.word_wrap = True
    p = tf_m.paragraphs[0]
    r = p.add_run()
    r.text = "SoundData Analytics · 85.000 canciones de Spotify (2015–2025)\n"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(16)
    r.font.color.rgb = ACCENT_GREEN
    r.font.bold = True

    p = tf_m.add_paragraph()
    p.space_before = Pt(6)
    r = p.add_run()
    r.text = "Equipo: Vicente Muñoz · Juan Ortiz · Jordan Murillo · Jorge Moncada · Jose Mendez · Bastian Parraguez\n"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(15)
    r.font.color.rgb = TEXT_WHITE

    p = tf_m.add_paragraph()
    p.space_before = Pt(4)
    r = p.add_run()
    r.text = "Docentes: Florentino Vargas y Rosa Rao · Universidad Santo Tomás · Minería de Datos (IEI-067)"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(14)
    r.font.color.rgb = TEXT_GRAY

    add_speaker_notes(s1, "Orador: Vicente Muñoz (0:30 min)\nPresentarse y anunciar el recorrido: 'Primero les contamos qué descubrimos, después les mostramos la herramienta que construimos.'")

    # --- D2: El problema ---
    s2 = prs.slides.add_slide(blank)
    set_slide_bg(s2, prs)
    add_header(s2, "Las discográficas invierten millones sin saber qué funcionará", "EL PROBLEMA")
    add_footer(s2, 2, 9)

    # Hero stat a la izquierda
    add_card(s2, Inches(0.8), Inches(1.7), Inches(4.6), Inches(4.9))
    tb_hero = s2.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(4.2), Inches(3.8))
    tf_h = tb_hero.text_frame
    tf_h.word_wrap = True
    p = tf_h.paragraphs[0]
    r = p.add_run()
    r.text = "+100.000\n"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(64)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN

    p2 = tf_h.add_paragraph()
    p2.space_before = Pt(8)
    r2 = p2.add_run()
    r2.text = "lanzamientos nuevos cada día en el mundo musical."
    r2.font.name = FONT_FAMILY
    r2.font.size = Pt(20)
    r2.font.color.rgb = TEXT_WHITE

    p3 = tf_h.add_paragraph()
    p3.space_before = Pt(16)
    r3 = p3.add_run()
    r3.text = "La intuición ya no basta para asignar presupuestos."
    r3.font.name = FONT_FAMILY
    r3.font.size = Pt(15)
    r3.font.color.rgb = TEXT_GRAY

    # 3 Preguntas a la derecha
    preguntas = [
        ("1", "¿Esta canción puede ser un éxito comercial?"),
        ("2", "¿Qué tipo de oyente la va a escuchar?"),
        ("3", "¿Qué combinaciones de sonido suelen funcionar?")
    ]
    for i, (num, preg) in enumerate(preguntas):
        y = Inches(1.7 + i * 1.65)
        add_card(s2, Inches(5.7), y, Inches(6.8), Inches(1.45))
        
        # Chip número
        add_card(s2, Inches(6.0), y + Inches(0.3), Inches(0.85), Inches(0.85), bg_color=CARD_COLOR, border_color=ACCENT_GREEN)
        tb_num = s2.shapes.add_textbox(Inches(6.0), y + Inches(0.35), Inches(0.85), Inches(0.85))
        p_n = tb_num.text_frame.paragraphs[0]
        p_n.alignment = PP_ALIGN.CENTER
        r_n = p_n.add_run()
        r_n.text = num
        r_n.font.name = FONT_FAMILY
        r_n.font.size = Pt(22)
        r_n.font.bold = True
        r_n.font.color.rgb = ACCENT_GREEN

        # Texto pregunta
        tb_p = s2.shapes.add_textbox(Inches(7.1), y + Inches(0.35), Inches(5.2), Inches(0.8))
        tf_p = tb_p.text_frame
        tf_p.word_wrap = True
        p_t = tf_p.paragraphs[0]
        r_t = p_t.add_run()
        r_t.text = preg
        r_t.font.name = FONT_FAMILY
        r_t.font.size = Pt(18)
        r_t.font.bold = True
        r_t.font.color.rgb = TEXT_WHITE

    add_speaker_notes(s2, "Orador: Vicente Muñoz (0:50 min)\n'Hoy muchas decisiones se toman por intuición. Nosotros usamos datos para responder tres preguntas.'")

    # --- D3: Los datos ---
    s3 = prs.slides.add_slide(blank)
    set_slide_bg(s3, prs)
    add_header(s3, "Pocas canciones se llevan casi todo el público", "LOS DATOS")
    add_footer(s3, 3, 9)

    # Hero Izquierda
    add_card(s3, Inches(0.8), Inches(1.7), Inches(5.2), Inches(4.9))
    tb_d3 = s3.shapes.add_textbox(Inches(1.1), Inches(1.9), Inches(4.6), Inches(4.4))
    tf_d3 = tb_d3.text_frame
    tf_d3.word_wrap = True
    
    p = tf_d3.paragraphs[0]
    r = p.add_run()
    r.text = "25 % → 68 %\n"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(50)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN

    p = tf_d3.add_paragraph()
    p.space_before = Pt(6)
    r = p.add_run()
    r.text = "El 25 % de las canciones concentra el 68 % de todas las reproducciones.\n\n"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(18)
    r.font.color.rgb = TEXT_WHITE

    p = tf_d3.add_paragraph()
    r = p.add_run()
    r.text = "• Catálogo: 85.000 canciones (2015–2025)\n• 17 atributos: ritmo, energía, país, género...\n\n"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(14)
    r.font.color.rgb = TEXT_GRAY

    p = tf_d3.add_paragraph()
    r = p.add_run()
    r.text = "Definición de éxito: superar el 25 % más escuchado (≥ 85,2 M de reproducciones)."
    r.font.name = FONT_FAMILY
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN

    # Gráfico Derecha (Oscuro)
    add_card(s3, Inches(6.3), Inches(1.7), Inches(6.2), Inches(4.9))
    img_d3 = os.path.join("docs", "img", "distribucion_streams_dark.png")
    if os.path.exists(img_d3):
        s3.shapes.add_picture(img_d3, Inches(6.5), Inches(1.85), Inches(5.8))

    add_speaker_notes(s3, "Orador: Juan Ortiz (0:50 min)\nExplicar la fuerte asimetría; por eso se eligió el percentil 75 como umbral para definir el éxito.")

    # --- D4: Preparación ---
    s4 = prs.slides.add_slide(blank)
    set_slide_bg(s4, prs)
    add_header(s4, "Cuidamos los datos antes de analizarlos", "PREPARACIÓN")
    add_footer(s4, 4, 9)

    # 3 Tarjetas grandes
    cajas_d4 = [
        ("Limpiamos", "Descartamos solo 180 canciones con datos incompletos (0,2 %). El 99,8 % se conservó íntegro.", ACCENT_GREEN),
        ("Protegimos los Éxitos", "Los valores extremos no se eliminan: los Mega-Hits son justo lo que buscamos predecir.", COLOR_BLUE),
        ("Probamos sin Trampas", "80 % para aprender y 20 % para comprobar con canciones que el modelo nunca vio.", COLOR_AMBER)
    ]
    for i, (tit, desc, col) in enumerate(cajas_d4):
        x = Inches(0.8 + i * 4.0)
        add_card(s4, x, Inches(1.7), Inches(3.7), Inches(4.9))
        
        # Chip indicador
        add_card(s4, x + Inches(0.3), Inches(2.1), Inches(0.7), Inches(0.12), bg_color=col, border_color=col)
        
        tb_c = s4.shapes.add_textbox(x + Inches(0.3), Inches(2.5), Inches(3.1), Inches(3.8))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        
        p = tf_c.paragraphs[0]
        r = p.add_run()
        r.text = f"{tit}\n\n"
        r.font.name = FONT_FAMILY
        r.font.size = Pt(22)
        r.font.bold = True
        r.font.color.rgb = TEXT_WHITE

        p2 = tf_c.add_paragraph()
        r2 = p2.add_run()
        r2.text = desc
        r2.font.name = FONT_FAMILY
        r2.font.size = Pt(16)
        r2.font.color.rgb = TEXT_GRAY

    add_speaker_notes(s4, "Orador: Juan Ortiz (0:40 min)\nDetalles técnicos hablados: IQR y límites 1,5 × IQR, winsorización en 1%/99% para ritmo, estandarización (media 0, varianza 1) y split estratificado con semilla 42.")

    # --- D5: Hallazgo 1 ---
    s5 = prs.slides.add_slide(blank)
    set_slide_bg(s5, prs)
    add_header(s5, "Pop y R&B con buen arranque se vuelven populares más fácil", "HALLAZGO 1 · ASOCIACIÓN")
    add_footer(s5, 5, 9)

    # Hero Izquierda
    add_card(s5, Inches(0.8), Inches(1.7), Inches(5.0), Inches(4.9))
    tb_h5 = s5.shapes.add_textbox(Inches(1.1), Inches(2.3), Inches(4.4), Inches(3.8))
    tf_h5 = tb_h5.text_frame
    tf_h5.word_wrap = True
    
    p = tf_h5.paragraphs[0]
    r = p.add_run()
    r.text = "6 de cada 10\n"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(54)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN

    p2 = tf_h5.add_paragraph()
    p2.space_before = Pt(8)
    r2 = p2.add_run()
    r2.text = "canciones Pop con muchas reproducciones alcanzan alta popularidad."
    r2.font.name = FONT_FAMILY
    r2.font.size = Pt(20)
    r2.font.color.rgb = TEXT_WHITE

    # 2 Tarjetas Derecha
    tarjetas_d5 = [
        ("Género Pop", "61 %", "Más de 3 veces más probable que al azar (Lift: 3,40)."),
        ("Género R&B", "60 %", "Más de 3 veces más probable que al azar (Lift: 3,33).")
    ]
    for i, (gen, pct, desc) in enumerate(tarjetas_d5):
        y = Inches(1.7 + i * 1.8)
        add_card(s5, Inches(6.1), y, Inches(6.4), Inches(1.6))
        tb_t5 = s5.shapes.add_textbox(Inches(6.4), y + Inches(0.2), Inches(5.8), Inches(1.2))
        tf_t5 = tb_t5.text_frame
        tf_t5.word_wrap = True
        
        p = tf_t5.paragraphs[0]
        r = p.add_run()
        r.text = f"{gen}: {pct}  "
        r.font.name = FONT_FAMILY
        r.font.size = Pt(24)
        r.font.bold = True
        r.font.color.rgb = TEXT_WHITE

        r_sub = p.add_run()
        r_sub.text = f"\n{desc}"
        r_sub.font.name = FONT_FAMILY
        r_sub.font.size = Pt(15)
        r_sub.font.color.rgb = TEXT_GRAY

    # Conclusión
    add_card(s5, Inches(6.1), Inches(5.4), Inches(6.4), Inches(1.2), bg_color=CARD_COLOR, border_color=ACCENT_GREEN)
    tb_c5 = s5.shapes.add_textbox(Inches(6.3), Inches(5.6), Inches(6.0), Inches(0.8))
    p = tb_c5.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = "💡 Conclusión: Impulsar el arranque de una canción Pop o R&B vale la pena."
    r.font.name = FONT_FAMILY
    r.font.size = Pt(17)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN

    add_speaker_notes(s5, "Orador: Jordan Murillo (1:00 min)\nSoporte 1,21% (≈1.020 canciones), Confianza 61,33%, Lift 3,40; R&B: 60,03% y Lift 3,33. Decir que es asociación, no causalidad.")

    # --- D6: Hallazgo 2 ---
    s6 = prs.slides.add_slide(blank)
    set_slide_bg(s6, prs)
    add_header(s6, "Las canciones se agrupan en 4 perfiles de escucha", "HALLAZGO 2 · CLUSTERING")
    add_footer(s6, 6, 9)

    clusters_d6 = [
        ("Chill / Instrumental", "Baja energía y acústico.\nIdeal para listas de estudio, lectura y sueño.", COLOR_CHILL),
        ("Pop Comercial", "Bailabilidad y energía equilibradas.\nAlta rotación radial y listas masivas.", COLOR_POP),
        ("Rock y Fiesta", "Potencia acústica y tempo alto.\nPara entrenamientos y festivales en vivo.", COLOR_ROCK),
        ("Urbano", "Ritmo sincopado y letras explícitas.\nFuerte conexión con el público joven (Gen Z).", COLOR_URBANO)
    ]
    for i, (nom, desc, col) in enumerate(clusters_d6):
        x = Inches(0.8 + i * 2.98)
        add_card(s6, x, Inches(1.7), Inches(2.8), Inches(4.9))
        
        # Banda superior con color fijo de clúster
        add_card(s6, x + Inches(0.2), Inches(2.0), Inches(0.9), Inches(0.12), bg_color=col, border_color=col)
        
        tb_cl = s6.shapes.add_textbox(x + Inches(0.2), Inches(2.3), Inches(2.4), Inches(4.0))
        tf_cl = tb_cl.text_frame
        tf_cl.word_wrap = True
        
        p = tf_cl.paragraphs[0]
        r = p.add_run()
        r.text = f"{nom}\n\n"
        r.font.name = FONT_FAMILY
        r.font.size = Pt(20)
        r.font.bold = True
        r.font.color.rgb = col

        p2 = tf_cl.add_paragraph()
        r2 = p2.add_run()
        r2.text = desc
        r2.font.name = FONT_FAMILY
        r2.font.size = Pt(15)
        r2.font.color.rgb = TEXT_GRAY

    add_speaker_notes(s6, "Orador: Jorge Moncada (1:00 min)\nK-Means con K = 4 sobre 6 atributos; el codo y la silueta (≈ 0,38) justifican K = 4 (están en el anexo A2).")

    # --- D7: Hallazgo 3 ---
    s7 = prs.slides.add_slide(blank)
    set_slide_bg(s7, prs)
    add_header(s7, "Un árbol de preguntas sencillas estima si tiene potencial", "HALLAZGO 3 · CLASIFICACIÓN")
    add_footer(s7, 7, 9)

    # Imagen del árbol a la izquierda (Oscura y limpia)
    add_card(s7, Inches(0.8), Inches(1.7), Inches(7.5), Inches(4.9))
    img_d7 = os.path.join("docs", "img", "arbol_decision_grafico_dark.png")
    if os.path.exists(img_d7):
        s7.shapes.add_picture(img_d7, Inches(0.95), Inches(1.9), Inches(7.2))

    # 3 Puntos a la derecha
    add_card(s7, Inches(8.6), Inches(1.7), Inches(3.9), Inches(4.9))
    tb_d7 = s7.shapes.add_textbox(Inches(8.8), Inches(2.0), Inches(3.5), Inches(4.4))
    tf_d7 = tb_d7.text_frame
    tf_d7.word_wrap = True

    puntos_d7 = [
        "Solo 3 niveles de preguntas → 8 caminos posibles.",
        "Lo mantuvimos simple a propósito: con más niveles memorizaba y fallaba.",
        "Cualquier productor o analista puede leerlo y entenderlo."
    ]
    for i, pt_txt in enumerate(puntos_d7):
        p = tf_d7.paragraphs[0] if i == 0 else tf_d7.add_paragraph()
        if i > 0:
            p.space_before = Pt(18)
        r = p.add_run()
        r.text = f"• {pt_txt}"
        r.font.name = FONT_FAMILY
        r.font.size = Pt(17)
        r.font.color.rgb = TEXT_WHITE

    add_speaker_notes(s7, "Orador: Jose Mendez (1:00 min)\nmax_depth = 3, criterio Gini; con ≥ 8 niveles el entrenamiento llegaba a 84% pero en validación caía bajo 52% (sobreajuste).")

    # --- D8: Evaluación ---
    s8 = prs.slides.add_slide(blank)
    set_slide_bg(s8, prs)
    add_header(s8, "Muy bueno descartando; una orientación para elegir", "EVALUACIÓN")
    add_footer(s8, 8, 9)

    # 2 Hero stats lado a lado
    add_card(s8, Inches(0.8), Inches(1.7), Inches(5.7), Inches(2.7))
    tb_e1 = s8.shapes.add_textbox(Inches(1.1), Inches(1.9), Inches(5.1), Inches(2.3))
    tf_e1 = tb_e1.text_frame
    tf_e1.word_wrap = True
    p = tf_e1.paragraphs[0]
    r = p.add_run()
    r.text = "3 de cada 4\n"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(48)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN
    p2 = tf_e1.add_paragraph()
    r2 = p2.add_run()
    r2.text = "veces acierta cuando dice 'no tiene potencial' (74 % de precisión)."
    r2.font.name = FONT_FAMILY
    r2.font.size = Pt(17)
    r2.font.color.rgb = TEXT_WHITE

    add_card(s8, Inches(6.8), Inches(1.7), Inches(5.7), Inches(2.7))
    tb_e2 = s8.shapes.add_textbox(Inches(7.1), Inches(1.9), Inches(5.1), Inches(2.3))
    tf_e2 = tb_e2.text_frame
    tf_e2.word_wrap = True
    p = tf_e2.paragraphs[0]
    r = p.add_run()
    r.text = "58 %\n"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(48)
    r.font.bold = True
    r.font.color.rgb = COLOR_BLUE
    p2 = tf_e2.add_paragraph()
    r2 = p2.add_run()
    r2.text = "de exactitud general evaluada sobre 17.000 canciones nuevas."
    r2.font.name = FONT_FAMILY
    r2.font.size = Pt(17)
    r2.font.color.rgb = TEXT_WHITE

    # Tarjeta de cautela ámbar abajo
    add_card(s8, Inches(0.8), Inches(4.7), Inches(11.7), Inches(1.9), bg_color=CARD_COLOR, border_color=COLOR_AMBER)
    tb_caut = s8.shapes.add_textbox(Inches(1.1), Inches(4.9), Inches(11.1), Inches(1.5))
    tf_caut = tb_caut.text_frame
    tf_caut.word_wrap = True
    p = tf_caut.paragraphs[0]
    r = p.add_run()
    r.text = "⚠️ Realidad de la industria musical:\n"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(17)
    r.font.bold = True
    r.font.color.rgb = COLOR_AMBER
    p2 = tf_caut.add_paragraph()
    p2.space_before = Pt(4)
    r2 = p2.add_run()
    r2.text = "El éxito comercial no depende solo del audio: intervienen marketing, redes sociales y base de fans. Nuestro modelo es un filtro de preselección, no una bola de cristal."
    r2.font.name = FONT_FAMILY
    r2.font.size = Pt(16)
    r2.font.color.rgb = TEXT_WHITE

    add_speaker_notes(s8, "Orador: Jose Mendez (1:00 min)\nPreparar la pregunta previsible: si dijera siempre 'no éxito' acertaría 74% pero no encontraría ningún hit. El árbol rescata el 36% de los éxitos reales.")

    # --- D9: Recomendaciones + Puente ---
    s9 = prs.slides.add_slide(blank)
    set_slide_bg(s9, prs)
    add_header(s9, "Tres decisiones que los datos respaldan", "QUÉ HACER")
    add_footer(s9, 9, 9)

    cajas_d9 = [
        ("Pop y Urbano", "Concentrar inversión en canciones muy bailables (> 0,65) y videos verticales en TikTok/Reels.", COLOR_POP),
        ("Chill / Acústico", "Evitar gasto en radio comercial. Apuntar a playlists de estudio y sueño con mayor retención.", COLOR_CHILL),
        ("Usar la Herramienta", "Simular los parámetros acústicos antes de invertir capital en producción y máster.", ACCENT_GREEN)
    ]
    for i, (tit, desc, col) in enumerate(cajas_d9):
        x = Inches(0.8 + i * 4.0)
        add_card(s9, x, Inches(1.7), Inches(3.7), Inches(3.8))
        add_card(s9, x + Inches(0.3), Inches(2.0), Inches(0.7), Inches(0.12), bg_color=col, border_color=col)
        
        tb_c = s9.shapes.add_textbox(x + Inches(0.3), Inches(2.3), Inches(3.1), Inches(2.9))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        p = tf_c.paragraphs[0]
        r = p.add_run()
        r.text = f"{tit}\n\n"
        r.font.name = FONT_FAMILY
        r.font.size = Pt(20)
        r.font.bold = True
        r.font.color.rgb = TEXT_WHITE
        p2 = tf_c.add_paragraph()
        r2 = p2.add_run()
        r2.text = desc
        r2.font.name = FONT_FAMILY
        r2.font.size = Pt(15)
        r2.font.color.rgb = TEXT_GRAY

    # Franja puente inferior verde
    add_card(s9, Inches(0.8), Inches(5.8), Inches(11.7), Inches(0.8), bg_color=CARD_COLOR, border_color=ACCENT_GREEN)
    tb_p = s9.shapes.add_textbox(Inches(1.0), Inches(5.95), Inches(11.3), Inches(0.5))
    p = tb_p.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "➔  A continuación: la herramienta interactiva que construimos"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN

    add_speaker_notes(s9, "Orador: Vicente Muñoz (0:50 min)\nCerrar la parte 1 y pasar la palabra a la parte 2.")

    # --- ANEXOS OCULTOS (A1, A2, A3, A4) ---
    anexos_crisp = [
        ("ANEXO A1: PREPARACIÓN DE DATOS EN DETALLE", "Detalle de IQR, winsorización 1%/99% y StandardScaler (Z-Score)."),
        ("ANEXO A2: MÉTODO DEL CODO Y COEFICIENTE DE SILUETA", "Gráfico de justificación cuantitativa de K = 4 clústeres."),
        ("ANEXO A3: MATRIZ DE CONFUSIÓN Y MÉTRICAS COMPLETAS", "Matriz completa sobre 17.000 datos con Accuracy, Precision y Recall."),
        ("ANEXO A4: REGLAS DE ASOCIACIÓN APRIORI (TABLA COMPLETA)", "Soporte, Confianza y Lift para las reglas minadas con mlxtend.")
    ]
    for idx_a, (tit_a, desc_a) in enumerate(anexos_crisp):
        s_anx = prs.slides.add_slide(blank)
        set_slide_bg(s_anx, prs)
        s_anx._element.set('show', '0')  # Diapositiva oculta
        add_header(s_anx, tit_a, "ANEXO TÉCNICO (SOLO PREGUNTAS)")
        add_card(s_anx, Inches(0.8), Inches(1.7), Inches(11.7), Inches(4.9))
        
        if idx_a == 1:
            img = os.path.join("docs", "img", "metodo_codo_silueta_dark.png")
            if os.path.exists(img):
                s_anx.shapes.add_picture(img, Inches(1.8), Inches(1.9), Inches(9.7))
        elif idx_a == 2:
            img = os.path.join("docs", "img", "matriz_confusion_dark.png")
            if os.path.exists(img):
                s_anx.shapes.add_picture(img, Inches(3.6), Inches(1.9), Inches(6.0))
        else:
            tb = s_anx.shapes.add_textbox(Inches(1.2), Inches(2.2), Inches(10.5), Inches(3.5))
            p = tb.text_frame.paragraphs[0]
            r = p.add_run()
            r.text = desc_a
            r.font.name = FONT_FAMILY
            r.font.size = Pt(20)
            r.font.color.rgb = TEXT_WHITE

        add_speaker_notes(s_anx, "Diapositiva oculta reservada para responder preguntas técnicas del jurado.")

    out1 = os.path.join("docs", "PRESENTACION_PROYECTO_CRISP_DM.pptx")
    prs.save(out1)
    # También copia como PARTE1_ANALISIS_SOUNDDATA_V2.pptx
    shutil.copyfile(out1, os.path.join("docs", "PARTE1_ANALISIS_SOUNDDATA_V2.pptx"))
    print(f"Parte 1 guardada en: {out1}")

# ==============================================================================
# CONSTRUCTOR: PARTE 2 — LA APLICACIÓN WEB
# ==============================================================================
def construir_parte2_app():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    # --- D10: Portada Parte 2 ---
    s10 = prs.slides.add_slide(blank)
    set_slide_bg(s10, prs)
    add_card(s10, Inches(0.8), Inches(0.8), Inches(11.733), Inches(5.9), bg_color=CARD_COLOR, border_color=BORDER_COLOR)

    tb_tag = s10.shapes.add_textbox(Inches(1.3), Inches(1.3), Inches(10.5), Inches(0.4))
    r_tag = tb_tag.text_frame.paragraphs[0].add_run()
    r_tag.text = "PARTE 2 · LA APLICACIÓN"
    r_tag.font.name = FONT_FAMILY
    r_tag.font.size = Pt(14)
    r_tag.font.bold = True
    r_tag.font.color.rgb = ACCENT_GREEN

    tb_t = s10.shapes.add_textbox(Inches(1.3), Inches(1.8), Inches(10.5), Inches(1.5))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p = tf_t.paragraphs[0]
    r = p.add_run()
    r.text = "SoundData: la herramienta para decidir con datos"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(40)
    r.font.bold = True
    r.font.color.rgb = TEXT_WHITE

    p2 = tf_t.add_paragraph()
    p2.space_before = Pt(8)
    r2 = p2.add_run()
    r2.text = "Prueba una canción antes de invertir en producirla."
    r2.font.name = FONT_FAMILY
    r2.font.size = Pt(22)
    r2.font.italic = True
    r2.font.color.rgb = TEXT_GRAY

    # Esquema simple de 3 pasos
    flujo = ["Ajustas la canción", "➔", "La herramienta analiza", "➔", "Probabilidad y perfil"]
    tb_flujo = s10.shapes.add_textbox(Inches(1.3), Inches(3.8), Inches(10.5), Inches(0.8))
    p_f = tb_flujo.text_frame.paragraphs[0]
    for item in flujo:
        r = p_f.add_run()
        r.text = f"{item}  "
        r.font.name = FONT_FAMILY
        r.font.size = Pt(19)
        r.font.bold = (item != "➔")
        r.font.color.rgb = ACCENT_GREEN if item != "➔" else TEXT_GRAY

    # 3 Chips inferiores
    chips = ["Respuesta en < 0,25 s", "Guarda tus canciones (SQLite)", "100 % en español"]
    tb_c = s10.shapes.add_textbox(Inches(1.3), Inches(4.9), Inches(10.5), Inches(0.8))
    p_c = tb_c.text_frame.paragraphs[0]
    for c in chips:
        r = p_c.add_run()
        r.text = f"✔ {c}     "
        r.font.name = FONT_FAMILY
        r.font.size = Pt(16)
        r.font.color.rgb = TEXT_WHITE

    add_speaker_notes(s10, "Orador: Vicente Muñoz (0:30 min)\nPara quién es: directores de A&R, productores y analistas de sellos discográficos.")

    # --- Vistas 1 a 4 con capturas de la app ---
    vistas = [
        ("11", "VISTA 1", "¿Quién escucha qué y desde dónde?", "app_vista_1_analisis_oyentes.png", [
            ("841 M de Oyentes", "Métricas acumuladas del catálogo."),
            ("12 Géneros", "Comparativa dinámica en barras."),
            ("Países", "Reparto porcentual de mercado.")
        ], "Vicente Muñoz (0:50 min)", 11),
        ("12", "VISTA 2", "Explora por género, país, año o sonido", "app_vista_2_segmentacion_atributo.png", [
            ("Filtros Instantáneos", "Cambia el atributo y todo se actualiza."),
            ("Tabla de Peso", "Qué parte del total representa cada grupo."),
            ("Exportar JSON", "Descarga el resumen en un clic.")
        ], "Vicente Muñoz (0:40 min)", 12),
        ("13", "VISTA 3", "Ajusta una canción y mira su potencial", "app_vista_3_simulador_ml.png", [
            ("Mueve los Controles", "Ritmo (BPM), energía, bailabilidad y volumen."),
            ("Probabilidad de Éxito", "Diagnóstico del árbol y clúster K-Means."),
            ("Consejo Accionable", "Recomendación estratégica de mercado.")
        ], "Vicente Muñoz (1:10 min con Demo en Vivo)", 13),
        ("14", "VISTA 4", "Guarda y organiza las canciones evaluadas", "app_vista_4_portafolio_crud.png", [
            ("Base de Datos SQLite", "Persistencia permanente de tus maquetas."),
            ("Sin Recargar", "Crear, editar y eliminar en tiempo real."),
            ("Búsqueda Rápida", "Filtra por título, género o diagnóstico.")
        ], "Bastian Parraguez (0:40 min)", 14),
    ]

    for num_d, kick, tit_v, img_nom, globos, orador_info, num_actual in vistas:
        s_v = prs.slides.add_slide(blank)
        set_slide_bg(s_v, prs)
        add_header(s_v, tit_v, kick)
        add_footer(s_v, num_actual - 9, 7)

        # Captura al 65% del ancho
        add_card(s_v, Inches(0.8), Inches(1.7), Inches(7.8), Inches(4.9))
        img_path = os.path.join("docs", "img", img_nom)
        if os.path.exists(img_path):
            s_v.shapes.add_picture(img_path, Inches(0.92), Inches(1.82), Inches(7.55))

        # 3 Globos explicativos a la derecha
        for i_g, (tit_g, desc_g) in enumerate(globos):
            y_g = Inches(1.7 + i_g * 1.65)
            add_card(s_v, Inches(8.8), y_g, Inches(3.7), Inches(1.45))
            tb_g = s_v.shapes.add_textbox(Inches(9.0), y_g + Inches(0.18), Inches(3.3), Inches(1.1))
            tf_g = tb_g.text_frame
            tf_g.word_wrap = True
            
            p = tf_g.paragraphs[0]
            r = p.add_run()
            r.text = f"{tit_g}\n"
            r.font.name = FONT_FAMILY
            r.font.size = Pt(17)
            r.font.bold = True
            r.font.color.rgb = ACCENT_GREEN

            p2 = tf_g.add_paragraph()
            p2.space_before = Pt(3)
            r2 = p2.add_run()
            r2.text = desc_g
            r2.font.name = FONT_FAMILY
            r2.font.size = Pt(14)
            r2.font.color.rgb = TEXT_GRAY

        add_speaker_notes(s_v, f"Orador: {orador_info}")

    # --- D15: Funciona y es confiable ---
    s15 = prs.slides.add_slide(blank)
    set_slide_bg(s15, prs)
    add_header(s15, "La herramienta fue probada y es segura de usar", "CALIDAD")
    add_footer(s15, 6, 7)

    # Hero Izquierda
    add_card(s15, Inches(0.8), Inches(1.7), Inches(4.8), Inches(4.9))
    tb_h15 = s15.shapes.add_textbox(Inches(1.1), Inches(2.2), Inches(4.2), Inches(3.9))
    tf_h15 = tb_h15.text_frame
    tf_h15.word_wrap = True
    p = tf_h15.paragraphs[0]
    r = p.add_run()
    r.text = "17 / 17\n"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(64)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN

    p2 = tf_h15.add_paragraph()
    r2 = p2.add_run()
    r2.text = "pruebas automáticas aprobadas en menos de 3 segundos."
    r2.font.name = FONT_FAMILY
    r2.font.size = Pt(20)
    r2.font.color.rgb = TEXT_WHITE

    # 3 Chips Derecha
    confiabilidad = [
        ("Errores Claros", "Si ingresas un dato inválido, ves un mensaje amigable en español. Cero pantallas de código técnico."),
        ("Disponible en Línea", "Desplegada en Render y sincronizada con GitHub. Acceso directo desde cualquier navegador."),
        ("Video de Respaldo", "Video de 2 minutos grabado para respaldar la presentación ante cortes de red.")
    ]
    for i, (tit_c, desc_c) in enumerate(confiabilidad):
        y_c = Inches(1.7 + i * 1.65)
        add_card(s15, Inches(5.9), y_c, Inches(6.6), Inches(1.45))
        tb_c = s15.shapes.add_textbox(Inches(6.2), y_c + Inches(0.2), Inches(6.0), Inches(1.1))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        
        p = tf_c.paragraphs[0]
        r = p.add_run()
        r.text = f"{tit_c}: "
        r.font.name = FONT_FAMILY
        r.font.size = Pt(17)
        r.font.bold = True
        r.font.color.rgb = TEXT_WHITE

        r2 = p.add_run()
        r2.text = desc_c
        r2.font.name = FONT_FAMILY
        r2.font.size = Pt(14)
        r2.font.color.rgb = TEXT_GRAY

    add_speaker_notes(s15, "Orador: Bastian Parraguez (0:50 min)\nDetalle técnico: pruebas de endpoints, ciclo completo de base de datos, carga e inferencia de modelos; validación con Pydantic; despliegue contenerizable.")

    # --- D16: Cierre ---
    s16 = prs.slides.add_slide(blank)
    set_slide_bg(s16, prs)
    add_card(s16, Inches(0.8), Inches(0.8), Inches(11.733), Inches(5.9), bg_color=CARD_COLOR, border_color=BORDER_COLOR)

    tb_cierre = s16.shapes.add_textbox(Inches(1.2), Inches(1.2), Inches(10.9), Inches(5.0))
    tf_ci = tb_cierre.text_frame
    tf_ci.word_wrap = True

    p = tf_ci.paragraphs[0]
    r = p.add_run()
    r.text = "Los datos no reemplazan al oído, pero ayudan a invertir mejor.\n\n"
    r.font.name = FONT_FAMILY
    r.font.size = Pt(32)
    r.font.bold = True
    r.font.color.rgb = TEXT_WHITE

    p2 = tf_ci.add_paragraph()
    r2 = p2.add_run()
    r2.text = "1.  85.000 canciones analizadas rigurosamente.\n2.  4 perfiles sonoros y 3 hallazgos accionables.\n3.  Una herramienta lista para producción.\n\n"
    r2.font.name = FONT_FAMILY
    r2.font.size = Pt(20)
    r2.font.color.rgb = TEXT_GRAY

    p3 = tf_ci.add_paragraph()
    p3.space_before = Pt(8)
    r3 = p3.add_run()
    r3.text = "¿Preguntas?\n"
    r3.font.name = FONT_FAMILY
    r3.font.size = Pt(46)
    r3.font.bold = True
    r3.font.color.rgb = ACCENT_GREEN

    p4 = tf_ci.add_paragraph()
    r4 = p4.add_run()
    r4.text = "Repositorio: github.com/mkinaa/MineriaDatos  ·  Plataforma: sounddata-analytics.onrender.com"
    r4.font.name = FONT_FAMILY
    r4.font.size = Pt(15)
    r4.font.color.rgb = TEXT_GRAY

    add_speaker_notes(s16, "Orador: Todos (0:30 min)\nAgradecimiento y ronda de preguntas.")

    # Anexo A5 oculto
    s_a5 = prs.slides.add_slide(blank)
    set_slide_bg(s_a5, prs)
    s_a5._element.set('show', '0')
    add_header(s_a5, "ANEXO A5: ARQUITECTURA Y SUITE DE PRUEBAS", "ANEXO TÉCNICO")
    add_card(s_a5, Inches(0.8), Inches(1.7), Inches(11.7), Inches(4.9))
    img_arq = os.path.join("docs", "img", "arquitectura_sistema.png")
    if os.path.exists(img_arq):
        s_a5.shapes.add_picture(img_arq, Inches(2.5), Inches(1.9), Inches(8.3))
    add_speaker_notes(s_a5, "Diapositiva oculta para preguntas sobre FastAPI, SQLite y Pytest.")

    out2 = os.path.join("docs", "PRESENTACION_APLICACION_WEB.pptx")
    prs.save(out2)
    shutil.copyfile(out2, os.path.join("docs", "PARTE2_APLICACION_SOUNDDATA_V2.pptx"))
    print(f"Parte 2 guardada en: {out2}")

if __name__ == "__main__":
    construir_parte1_crisp()
    construir_parte2_app()
