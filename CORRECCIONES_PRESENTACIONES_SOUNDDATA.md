# SoundData Analytics — Auditoría y plan de corrección de las presentaciones

> **Para la IA que ejecute este documento:** este archivo contiene (1) la auditoría de diseño, (2) el sistema de diseño que debes aplicar, (3) la especificación diapositiva por diapositiva de las dos presentaciones corregidas y (4) las reglas de calidad. Genera **dos archivos .pptx nuevos** siguiendo la sección 6. No inventes cifras: todas las cifras permitidas están en este documento.

---

## 1. Contexto

| Dato | Valor |
|---|---|
| Proyecto | SoundData Analytics — Minería de Datos (IEI-067), Universidad Santo Tomás |
| Grupo | Grupo 4: Vicente Muñoz, Juan Ortiz, Jordan Murillo, Jorge Moncada, Jose Mendez, Bastian Parraguez |
| Docentes | Florentino Vargas y Rosa Rao |
| Archivos de origen | `PRESENTACION_PROYECTO_CRISP_DM.pptx` (8 diapositivas), `PRESENTACION_APLICACION_WEB.pptx` (7 diapositivas), `INFORME_TECNICO_FINAL_ACTUALIZADO.docx`, captura de la app `1.PNG` |
| Duración objetivo | **12 a 14 minutos en total** (más 2 minutos de demo en vivo opcional) |
| Público | Docentes y compañeros: personas que quieren entender **qué se hizo, qué se encontró y para qué sirve**, no cómo está programado |
| Formato | 16:9 (13,333" × 7,5"), idioma español de Chile |

**Cambio de enfoque pedido:** menos técnico, más claro. Lo técnico (fórmulas, nombres de librerías, archivos de test) pasa a notas del orador y a un anexo. En pantalla solo queda lo que un lector necesita retener.

---

## 2. Auditoría visual

### 2.1 Lo que funciona (conservar)
- Tema oscuro: coincide con el espíritu de la app.
- Estructura repetible: etiqueta de sección arriba, título, contenido.
- Capturas reales de la app en la presentación web.
- El verde como color de marca.

### 2.2 Problemas encontrados

| # | Problema | Dónde | Gravedad | Corrección |
|---|---|---|---|---|
| V1 | **Texto demasiado pequeño para proyectar.** Casi todo el cuerpo está entre 11 y 13 pt (≈1.090 de los caracteres en 12,5 pt); lo más grande es el título de portada con 34–36 pt. | Ambas, todas las diapositivas | Alta | Cuerpo mínimo 20 pt, apoyos mínimo 14 pt, títulos 36–40 pt. Nada por debajo de 14 pt. |
| V2 | **Paleta distinta a la de la app.** La app usa negro puro y grises neutros con verde Spotify; las presentaciones usan azul marino con borde de 4 colores (verde, celeste, morado, ámbar). | Ambas | Alta | Adoptar la paleta de la app (sección 3). El verde es el único color de acento; los demás colores solo para categorías de datos. |
| V3 | **Arcoíris decorativo.** Cada tarjeta lleva un borde de color distinto sin significado. Confunde: ¿qué significa el morado frente al ámbar? | Todas las de 3 tarjetas | Media | Tarjetas grises (#181818) sin borde de color. El color solo identifica categorías (por ejemplo, un clúster) y siempre el mismo. |
| V4 | **Exceso de texto por diapositiva.** Entre 60 y 110 palabras en las diapositivas 3 y 7/8 (tres columnas con tres viñetas “✔” cada una). | CRISP 3, 4, 8; Web 7 | Alta | Máximo 40 palabras por diapositiva. Una idea por diapositiva, una cifra protagonista. |
| V5 | **Lenguaje técnico en pantalla:** IQR, winsorización, StandardScaler, Z, Lift, Soporte, ASGI, Uvicorn, Pydantic, Chart.js, `test_api.py`, `sounddata.db`. | CRISP 3, 4; Web 4, 6, 7 | Alta | Traducir a beneficio (ver sección 5). Lo técnico va a notas del orador o anexo. |
| V6 | **Imágenes con fondo blanco sobre tema oscuro** (arquitectura, distribución de streams, codo/silueta, árbol, matriz de confusión). Rompen la coherencia y se ven como “pegadas”. | CRISP 2, 5, 6, 7; Web 2 | Alta | Regenerar los gráficos en estilo oscuro con la paleta (snippet en sección 7) o, como mínimo, montarlos sobre una tarjeta blanca con esquinas redondeadas y margen interno. |
| V7 | **Capturas de la app demasiado pequeñas.** Ocupan ~60 % del ancho dentro de un marco con mucho aire; el texto de la interfaz es ilegible. | Web 3, 4, 5, 6 | Alta | Captura al 62–66 % del ancho, recortada a la zona relevante, con 1–3 globos numerados en verde que remiten al texto. |
| V8 | **Texto superpuesto sobre una imagen** (“Control de Sobreajuste” sobre la esquina del árbol). | CRISP 6 | Media | Separar: imagen a un lado, texto a otro, sin solapamiento. |
| V9 | **Emojis como íconos** (🎯 ⚡ 💾 🧪 🛡️ ☁️ 🧠 🎛️ 🧘 🚀). Se ven distinto según el equipo y no son profesionales. | Web 2, 5, 7; CRISP 3, 8 | Media | Íconos de línea (estilo Lucide/Feather) en verde #1DB954 dentro de un chip cuadrado tintado, igual que los íconos de las tarjetas KPI de la app. |
| V10 | **Tarjetas con mucho espacio vacío** abajo (la mitad inferior de las columnas queda vacía mientras el texto es diminuto). | CRISP 3, 8; Web 7 | Media | Tarjetas de altura ajustada al contenido, o contenido más grande para llenarlas. |
| V11 | **Portada pobre:** recuadro grande con texto pequeño, sin logo, integrantes en 11 pt. | Ambas portadas | Media | Portada con logo SoundData (el ícono verde de la app), título 54 pt, subtítulo 24 pt, integrantes en 16 pt. |
| V12 | **Sin numeración, sin pie, sin notas del orador.** Ninguna de las dos tiene notas (0 de 15 diapositivas). | Ambas | Media | Pie fijo en el patrón: “SoundData Analytics · Grupo 4” a la izquierda, número a la derecha. Notas del orador en cada diapositiva. |
| V13 | **Sin cierre.** Ninguna termina con “Gracias / Preguntas”, ni con un mensaje final memorable. La web termina en una lista de pruebas unitarias. | Ambas | Media | Cierre con mensaje único + contacto/URL + “Preguntas”. |
| V14 | **Etiqueta superior (kicker) diminuta** (11 pt) y de color cambiante (verde, ámbar, morado según la diapositiva). | Todas | Baja | 14 pt, mayúsculas, siempre verde, formato “PARTE 1 · 03/09”. |
| V15 | **Dos presentaciones sin hilo conductor.** No se anuncia que son dos partes ni cómo se conectan. | Ambas | Media | Marcarlas como Parte 1 (el análisis) y Parte 2 (la aplicación), con una diapositiva puente. |
| V16 | **Formato numérico inconsistente:** “61,33 %” (coma) junto a “85.2M”, “0.65”, “841.0 M” (punto). | Ambas y app | Baja | Estándar chileno: coma decimal, punto de miles: 85,2 M · 0,65 · 841 M · 85.000. |

### 2.3 Hallazgos sobre la propia aplicación (captura `1.PNG`)
Se ven en la captura que usarán en la demo; conviene arreglarlos o preparar respuesta.

| # | Hallazgo | Sugerencia |
|---|---|---|
| A1 | El panel dice “Dataset conectado: 85,000 canciones”, pero la tarjeta principal dice “Calculado sobre **200 canciones**” y muestra 841 M de oyentes. Un docente lo notará. | Verificar con el equipo qué base alimenta el panel. Si es una muestra, decirlo (“muestra de 200 canciones”). Si no, corregir el texto. |
| A2 | El menú “Ordenar por Oyentes” está seleccionado, pero las barras **no están ordenadas** (Indie, Jazz, Metal, Folk, Clásica…). | Ordenar de mayor a menor al cargar; así “Clásica” se ve como líder. |
| A3 | El eje vertical muestra 0–100 sin unidad, aunque el título habla de “volumen de oyentes” (las tarjetas indican millones). | Rotular el eje “Millones de oyentes”. |
| A4 | El gráfico de dona no tiene leyenda: no se ve qué color es qué país. | Agregar leyenda con nombres y porcentaje. |
| A5 | Todas las barras son del mismo verde; el líder no destaca. | Barra líder en verde #1DB954 y el resto en verde atenuado (#1DB954 al 45 %). |
| A6 | En el menú lateral, “Análisis de Oyentes” está alineado a la izquierda y los otros tres están centrados. | Alinear los cuatro a la izquierda con ícono. |
| A7 | Formato “85,000” y “841.0 M” usa punto decimal. | Aplicar formato es-CL. |
| A8 | “Popularidad promedio 57/100” difiere del 54,2 del informe (probablemente por ser muestra). | Mismo punto que A1. |

---

## 3. Sistema de diseño (derivado de la captura de la app)

Colores medidos directamente en la captura:

| Rol | Hex | Uso |
|---|---|---|
| Fondo de diapositiva | `#0A0A0A` | Fondo general (en la app es #000000; se usa #0A0A0A para evitar bandas en proyectores) |
| Superficie 1 | `#121212` | Franjas, barra lateral |
| Superficie 2 (tarjetas) | `#181818` | Tarjetas, cajas de captura |
| Borde | `#2A2A2A` | Línea de 1 pt, solo si hace falta |
| **Acento principal** | `#1DB954` | Cifras protagonistas, íconos, globos numerados, barras destacadas |
| Texto principal | `#FFFFFF` | Títulos y cifras |
| Texto secundario | `#B3B3B3` | Apoyos y pies (nunca bajo 14 pt) |
| Azul de datos | `#3B82F6` | Solo categorías de datos |
| Morado de datos | `#A855F7` | Solo categorías de datos |
| Ámbar de datos / advertencia | `#F59E0B` | Limitaciones y cautelas |
| Rosa de datos | `#EC4899` | Solo categorías de datos |
| Turquesa de datos | `#14B8A6` | Solo categorías de datos |
| Naranja de datos | `#F97316` | Solo categorías de datos |

**Asignación fija de color a los 4 clústeres** (usar siempre la misma en todas las diapositivas y gráficos):

| Clúster | Nombre sencillo | Color |
|---|---|---|
| 0 | Chill / Instrumental | `#14B8A6` turquesa |
| 1 | Pop Comercial | `#EC4899` rosa |
| 2 | Rock y Fiesta | `#F97316` naranja |
| 3 | Urbano | `#A855F7` morado |

**Tipografía** (una sola familia en dos pesos): *Inter* o, si no está instalada, *Segoe UI*/*Calibri*.

| Elemento | Tamaño | Peso |
|---|---|---|
| Título de diapositiva (es el mensaje, no el tema) | 36–40 pt | Negrita, blanco |
| Cifra protagonista | 72–96 pt | Negrita, verde |
| Cuerpo | 20–24 pt | Normal, blanco |
| Apoyo / pie de cifra | 14–16 pt | Normal, #B3B3B3 |
| Etiqueta superior | 14 pt | Negrita, verde, MAYÚSCULAS |
| Portada: título | 54 pt | Negrita |

**Grilla y componentes**
- Márgenes de 0,6" en los cuatro lados. Título arriba a la izquierda (y = 0,55").
- Pie fijo en la capa maestra: “SoundData Analytics · Grupo 4” (12 pt, gris) a la izquierda y número de diapositiva a la derecha.
- Tarjeta: fondo `#181818`, esquina redondeada pequeña (radio ≈ 0,12"), **sin borde de color**. Opcional: franja vertical de 0,06" en verde a la izquierda.
- Chip de ícono: cuadrado redondeado 0,6", fondo verde al 15 % de opacidad, ícono de línea verde (idéntico a las tarjetas KPI de la app).
- Capturas: marco tipo navegador (barra superior gris con 3 puntos), sombra suave, globos numerados verdes de 0,35".
- Animaciones: ninguna salvo aparición simple. Sin transiciones llamativas.
- Reglas de oro: **un mensaje por diapositiva · máximo 40 palabras · una cifra protagonista · nada bajo 14 pt**.

Construir con **tema y capa maestra** (colores y tipografía definidos una vez), con secciones “Parte 1” y “Parte 2”, y cada elemento con nombre. Gráficos nativos editables cuando sea posible.

---

## 4. Auditoría de contenido

### 4.1 Incoherencias a corregir

| # | Problema | Dónde | Corrección |
|---|---|---|---|
| C1 | “**Eliminación de 180 registros** incompletos” y a la vez “**Preservación íntegra de 85.000 pistas**”: se contradicen. Además el informe divide 68.000/17.000 (suma 85.000), lo que tampoco cuadra con haber eliminado 180. | CRISP 3; informe 3.1 y 3.5 | En la presentación: “Descartamos solo 180 canciones con datos incompletos (0,2 %)”. Pedir al equipo confirmar las cifras exactas del conjunto de prueba (17.000 vs. ≈16.964) y corregir el informe. |
| C2 | “**7 selectores dinámicos**” pero la lista nombra 6 (Género, País, Año, Popularidad, Bailabilidad, Energía). | Web 4 | Verificar en la app el número real. Mientras tanto, decir “Filtros por género, país, año y sonido”. |
| C3 | “**Acceso público 24/7**” contradice el informe (7.5): Render gratuito reinicia los contenedores y puede dormir la app. | Web 7 | Decir “Disponible en línea” y llevar una demo local o el video de respaldo. Agregar URL. |
| C4 | “**Cero pantallas de error**” es una afirmación absoluta difícil de sostener. | Web 7 | “Mensajes de error claros y en español”. |
| C5 | “**99,8 % de calidad**”: ambiguo (la calidad no es lo mismo que lo conservado). | CRISP 3 | “99,8 % de los datos se conservó”. |
| C6 | “**Predicción de Hit**” suena más seguro de lo que el modelo es (acierta 58 % en general; de los que marca como éxito, solo 27 % lo son). | Web 5; CRISP 7 | Hablar de “probabilidad estimada” y “filtro de preselección”, no de “predicción certera”. Ser honestos: es una brújula, no un oráculo. |
| C7 | “**Triple de probabilidad frente al resto**”: el Lift de 3,40 dice “3,4 veces más que el azar” dentro de esa combinación, no “frente al resto del catálogo” en general. | CRISP 4 | “Más de 3 veces más probable que al azar”. |
| C8 | “**3 modelos de Machine Learning**” (Web 2): Apriori es minería de reglas, no un modelo predictivo. | Web 2 | “3 técnicas de minería de datos”. |
| C9 | Formato numérico mezclado (ver V16). | Ambas | Aplicar es-CL. |

### 4.2 Contenido a simplificar (qué se dice y cómo)

| Tecnicismo actual | Cómo decirlo en pantalla |
|---|---|
| IQR, límites Q1 − 1,5 × IQR… | “Revisamos los valores extremos y **conservamos los grandes éxitos**, porque son justo lo que buscamos.” |
| Winsorización 1 %/99 % | (solo nota del orador) “Acotamos los valores muy raros de ritmo.” |
| StandardScaler / puntaje Z | “Pusimos todos los atributos en la **misma escala** para compararlos de forma justa.” |
| Split estratificado 80/20 | “Entrenamos con 80 % y **probamos con 20 % de canciones que el modelo nunca vio**.” |
| Soporte 1,21 %, Confianza 61,33 %, Lift 3,40 | “6 de cada 10 canciones Pop con muchas reproducciones llegan a alta popularidad: **más de 3 veces más que al azar**.” |
| K-Means, método del codo, silueta | “El computador agrupó las canciones en **4 perfiles de escucha**.” (codo y silueta al anexo) |
| Árbol de decisión, max_depth = 3, overfitting | “Un árbol de **preguntas sencillas** (8 caminos posibles) que cualquier productor puede leer. Lo mantuvimos simple a propósito para que **no memorice**.” |
| Matriz de confusión, TN/FP/FN/TP | “Cuando descarta una canción, **acierta 3 de cada 4 veces**.” (matriz completa al anexo) |
| FastAPI, Uvicorn, ASGI, Pydantic | “Programada en Python; responde en **menos de un cuarto de segundo**.” |
| 17 pruebas unitarias, nombres de archivos | “**17 de 17 pruebas automáticas aprobadas**.” (nombres de archivos solo en notas) |

---

## 5. Estructura de tiempo propuesta (≈ 13 minutos + demo opcional)

Narrativa: **Problema → Datos → Tres hallazgos → Cuánto confiar → Qué hacer → La herramienta → Cierre.**

### Parte 1 — El análisis (CRISP-DM contado como historia) · 9 diapositivas · ≈ 7:40

| N.° | Diapositiva | Min | Orador sugerido (según roles del informe) |
|---|---|---|---|
| 1 | Portada | 0:30 | Vicente |
| 2 | El problema: invertir sin saber | 0:50 | Vicente |
| 3 | Los datos: 85.000 canciones | 0:50 | Juan |
| 4 | Preparamos los datos con cuidado | 0:40 | Juan |
| 5 | Hallazgo 1: qué combinaciones funcionan | 1:00 | Jordan |
| 6 | Hallazgo 2: 4 perfiles de canciones | 1:00 | Jorge |
| 7 | Hallazgo 3: un árbol de decisiones simple | 1:00 | Jose |
| 8 | ¿Cuánto podemos confiar? | 1:00 | Jose |
| 9 | Qué recomendamos hacer + puente a la app | 0:50 | Vicente |

### Parte 2 — La aplicación · 7 diapositivas · ≈ 5:10 (+ 2:00 de demo en vivo si hay tiempo)

| N.° | Diapositiva | Min | Orador sugerido |
|---|---|---|---|
| 10 | De los datos a una herramienta (portada de Parte 2) | 0:30 | Vicente |
| 11 | Vista 1: ¿Quién escucha qué? | 0:50 | Vicente |
| 12 | Vista 2: Explora por atributo | 0:40 | Vicente |
| 13 | Vista 3: El simulador | 1:10 | Vicente (demo) |
| 14 | Vista 4: Tu portafolio | 0:40 | Bastian |
| 15 | Funciona y es confiable | 0:50 | Bastian |
| 16 | Cierre y preguntas | 0:30 | Todos |

**Anexo (no se presenta, solo para preguntas):** A1 Preparación en detalle · A2 Método del codo y silueta · A3 Matriz de confusión y métricas completas · A4 Reglas de asociación (Soporte/Confianza/Lift) · A5 Arquitectura y pruebas.

---

## 6. Especificación diapositiva por diapositiva

Convenciones: **[T]** título · **[K]** etiqueta superior · **[HERO]** cifra protagonista · **[V]** visual · **[N]** nota del orador (se guarda en las notas de PowerPoint, no en pantalla).

### PARTE 1 — EL ANÁLISIS

**D1 · Portada**
- Fondo `#0A0A0A`. Logo SoundData (ícono verde de gráfico de línea en círculo) arriba a la izquierda.
- [T] **De los datos al éxito musical**
- Subtítulo (24 pt): *¿Podemos saber, antes de lanzar una canción, a quién le va a gustar y si tiene opciones de ser un éxito?*
- Línea (16 pt, gris): SoundData Analytics · 85.000 canciones de Spotify (2015–2025)
- Integrantes en 16 pt, una línea por pareja; docentes y “Universidad Santo Tomás · Minería de Datos (IEI-067)” en 14 pt.
- Etiqueta: **PARTE 1 · EL ANÁLISIS**
- [N] Presentarse y anunciar el recorrido: “Primero les contamos qué descubrimos, después les mostramos la herramienta que construimos.”

**D2 · El problema**
- [K] EL PROBLEMA · [T] **Las discográficas invierten millones sin saber qué canción funcionará**
- [HERO] **+100.000** *lanzamientos nuevos cada día en el mundo*
- Tres tarjetas con ícono y una pregunta cada una:
  1. ¿Esta canción puede ser un éxito?
  2. ¿Qué tipo de oyente la va a escuchar?
  3. ¿Qué combinaciones suelen funcionar?
- [N] “Hoy muchas decisiones se toman por intuición. Nosotros usamos datos para responder tres preguntas.”

**D3 · Los datos**
- [K] LOS DATOS · [T] **Pocas canciones se llevan casi todo**
- [HERO] **25 % → 68 %** *El 25 % de las canciones concentra el 68 % de las reproducciones*
- Datos de apoyo (una línea, 16 pt): 85.000 canciones · 2015–2025 · 17 atributos (ritmo, energía, país, género…)
- [V] Gráfico de distribución de streams en estilo oscuro (a la derecha, 50 % del ancho), con la cola derecha en verde.
- Cuadro pequeño: “Definimos **éxito** = estar en el 25 % más escuchado (desde 85,2 M de reproducciones).”
- [N] Explicar la fuerte asimetría; por eso se eligió el percentil 75 como umbral.

**D4 · Preparación**
- [K] PREPARACIÓN · [T] **Cuidamos los datos antes de analizarlos**
- [HERO] **99,8 %** *de las canciones se conservó*
- Tres tarjetas con ícono (una frase cada una):
  1. **Limpiamos:** descartamos solo 180 canciones con datos incompletos.
  2. **Protegimos los grandes éxitos:** los valores extremos no se eliminan, son justo lo que buscamos.
  3. **Probamos con canciones nuevas:** 80 % para aprender, 20 % para comprobar.
- [N] Aquí van los detalles técnicos hablados: IQR y límites 1,5 × IQR, winsorización en 1 %/99 % para ritmo, estandarización (media 0, varianza 1) y split estratificado con semilla 42.

**D5 · Hallazgo 1 — Qué combinaciones funcionan**
- [K] HALLAZGO 1 · [T] **Pop y R&B con buen arranque se vuelven populares más fácil**
- [HERO] **6 de cada 10** *canciones Pop con muchas reproducciones alcanzan alta popularidad*
- [V] Dos tarjetas: **Pop** `61 %` · **R&B** `60 %`, cada una con “más de 3 veces más probable que al azar”.
- Conclusión (24 pt): *Impulsar el arranque de una canción Pop o R&B vale la pena.*
- [N] Soporte 1,21 % (≈1.020 canciones), Confianza 61,33 %, Lift 3,40; R&B: 60,03 % y Lift 3,33. Decir que es asociación, no causalidad.

**D6 · Hallazgo 2 — 4 perfiles**
- [K] HALLAZGO 2 · [T] **Las canciones se agrupan en 4 perfiles de escucha**
- [V] Cuatro tarjetas en fila, cada una con el color fijo de su clúster (sección 3), ícono, nombre y una línea:
  - 🟦 *(turquesa)* **Chill / Instrumental** — estudio, concentración y sueño.
  - *(rosa)* **Pop Comercial** — radio y listas masivas.
  - *(naranja)* **Rock y Fiesta** — deporte y festivales.
  - *(morado)* **Urbano** — ritmo marcado, público joven (Gen Z).
- [N] K-Means con K = 4 sobre 6 atributos; el codo y la silueta (≈ 0,38) justifican K = 4 (están en el anexo A2).

**D7 · Hallazgo 3 — Árbol simple**
- [K] HALLAZGO 3 · [T] **Un árbol de preguntas sencillas estima si una canción tiene potencial**
- [V] Imagen del árbol regenerada en estilo oscuro, a la izquierda (≈ 60 % del ancho), sin texto encima.
- A la derecha, tres puntos de 20 pt:
  - Solo **3 niveles de preguntas** → 8 caminos posibles.
  - Lo mantuvimos simple **a propósito**: con más niveles memorizaba y fallaba con canciones nuevas.
  - Cualquier productor puede leerlo.
- [N] max_depth = 3, criterio Gini; con ≥ 8 niveles el entrenamiento llegaba a 84 % pero en validación caía bajo 52 % (sobreajuste).

**D8 · ¿Cuánto podemos confiar?**
- [K] EVALUACIÓN · [T] **Es muy bueno descartando, y una orientación prudente para elegir ganadoras**
- Dos cifras protagonistas lado a lado:
  - **3 de 4** *veces acierta cuando dice “no tiene potencial”* (74 %)
  - **58 %** *de acierto general en 17.000 canciones nuevas*
- Tarjeta ámbar (cautela): *El éxito depende también de marketing, redes sociales y seguidores. Usar como **filtro de preselección**, no como garantía.*
- [N] Preparar la pregunta previsible: ver sección 8, P1 y P2.

**D9 · Recomendaciones + puente**
- [K] QUÉ HACER · [T] **Tres decisiones que los datos respaldan**
- Tres tarjetas con ícono:
  1. **Pop y Urbano:** concentrar publicidad en canciones muy bailables (> 0,65) y enérgicas (> 0,60), con videos verticales en TikTok/Reels para 16–24 años.
  2. **Chill / Instrumental:** evitar radio comercial y apuntar a playlists de estudio y sueño.
  3. **Usar la herramienta:** simular una canción antes de invertir.
- Franja inferior (verde): **→ A continuación: la herramienta que construimos.**
- [N] Cerrar la parte 1 y pasar la palabra.

### PARTE 2 — LA APLICACIÓN

**D10 · Portada de Parte 2**
- Etiqueta **PARTE 2 · LA APLICACIÓN**. [T] **SoundData: la herramienta para decidir con datos**
- Subtítulo: *Prueba una canción antes de invertir en producirla.*
- [V] Esquema simple de 3 cajas con flechas (reemplaza el diagrama de arquitectura): **Tú ajustas la canción → La herramienta la analiza → Obtienes probabilidad y perfil.** Debajo, en 14 pt gris: *Hecha con Python (FastAPI), base de datos SQLite.*
- Tres chips: ⚡ Respuesta en menos de 0,25 s · 💾 Guarda tus canciones · 🇨🇱 100 % en español (usar íconos de línea).
- [N] Para quién es: directores de A&R, productores, analistas de sellos.

**D11 · Vista 1 — Análisis de oyentes**
- [K] VISTA 1 · [T] **¿Quién escucha qué y desde dónde?**
- [V] Captura `app_vista_1_analisis_oyentes.png` al 64 % del ancho, con 3 globos: ① 4 indicadores clave, ② barras por género, ③ dona por país.
- Texto lateral (20 pt): ① **841 M** de oyentes · ② **12 géneros** comparables · ③ Reparto por **países**.
- [N] Antes de la demo: confirmar A1–A5 de la sección 2.3 (200 vs 85.000, orden de barras, unidad del eje, leyenda de la dona).

**D12 · Vista 2 — Segmentación por atributo**
- [K] VISTA 2 · [T] **Explora el catálogo por género, país, año o sonido**
- [V] Captura `app_vista_2_segmentacion_atributo.png`, 3 globos: ① filtros, ② tabla de peso por segmento, ③ botón de descarga.
- Texto: ① Cambia el filtro y todo se actualiza · ② Qué parte del total representa cada grupo · ③ Descarga el resumen con un clic.
- [N] No afirmar “7 selectores” hasta verificar (C2).

**D13 · Vista 3 — Simulador**
- [K] VISTA 3 · [T] **Ajusta una canción y mira su potencial al instante**
- [V] Captura `app_vista_3_simulador_ml.png` grande (≥ 66 % del ancho), 3 globos: ① controles deslizantes (ritmo, energía, volumen, bailabilidad), ② probabilidad de éxito, ③ perfil de la canción y consejo.
- Texto: Mueve los controles → obtienes **probabilidad de éxito**, **perfil** (uno de los 4) y **consejos** de negocio → guárdala con un clic.
- Marca visual **“▶ Demo en vivo”** (chip verde) si se hará demostración.
- [N] Demo sugerida (≈ 2 min): subir bailabilidad y energía de una canción “chill” y ver cómo cambian la probabilidad y el perfil; guardar en portafolio. Si falla internet, usar el video de respaldo de 2 minutos.

**D14 · Vista 4 — Portafolio**
- [K] VISTA 4 · [T] **Guarda y organiza las canciones que evaluaste**
- [V] Captura `app_vista_4_portafolio_crud.png`, 3 globos: ① crear/editar, ② buscar y filtrar, ③ eliminar.
- Texto: Crear, editar, buscar y eliminar canciones, **sin recargar la página**. Los datos quedan guardados.
- [N] Mencionar auto-semillado de 6 canciones de ejemplo (para que nunca aparezca vacía en la nube).

**D15 · Funciona y es confiable**
- [K] CALIDAD · [T] **La herramienta fue probada y es segura de usar**
- [HERO] **17 / 17** *pruebas automáticas aprobadas*
- Tres chips con ícono (una línea cada uno):
  - **Errores claros:** si ingresas un dato inválido, ves un mensaje en español.
  - **En línea:** disponible en la nube (Render). URL visible en 20 pt + código QR.
  - **Respaldo:** video de 2 minutos de la demo.
- [N] Detalle técnico: pruebas de endpoints, ciclo completo de base de datos, carga e inferencia de modelos; validación con Pydantic; despliegue contenerizable con integración continua desde GitHub.

**D16 · Cierre**
- [T] **Los datos no reemplazan al oído, pero ayudan a invertir mejor**
- Tres frases de 24 pt (una por línea, con la cifra en verde):
  1. 85.000 canciones analizadas.
  2. 4 perfiles y 3 hallazgos accionables.
  3. Una herramienta lista para usar.
- “**¿Preguntas?**” en 54 pt. Logo, URL del repositorio `github.com/mkinaa/MineriaDatos` y URL de la app (14–16 pt).

### ANEXO (diapositivas ocultas, solo para preguntas)
- **A1 Preparación en detalle:** IQR, winsorización, estandarización, split.
- **A2 Codo y silueta:** gráficos regenerados en estilo oscuro; K = 4 marcado en verde.
- **A3 Matriz de confusión y tabla de métricas** (precisión, sensibilidad, F1 por clase).
- **A4 Reglas Apriori:** tabla de las 3 reglas con soporte, confianza y Lift.
- **A5 Arquitectura y lista de pruebas.**

---

## 7. Instrucciones de ejecución para la IA

### 7.1 Entregables
1. `PARTE1_ANALISIS_SOUNDDATA_V2.pptx` → diapositivas D1–D9 + anexo A1–A4 (ocultas).
2. `PARTE2_APLICACION_SOUNDDATA_V2.pptx` → diapositivas D10–D16 + A5 (oculta).
   *(Alternativa: un único archivo de 16 diapositivas con dos secciones; usar la opción que prefiera el equipo.)*
3. Notas del orador en cada diapositiva con el texto de [N] y el tiempo objetivo.

### 7.2 Reglas obligatorias
- 16:9, 13,333" × 7,5". Aplicar la paleta y tipografía de la sección 3 mediante **tema/maestra**, no a mano en cada cuadro.
- **No usar emojis** como íconos: íconos de línea en verde dentro de chip tintado.
- **Máximo 40 palabras visibles por diapositiva** (sin contar etiquetas, pie ni números).
- **Nada por debajo de 14 pt.** Cuerpo ≥ 20 pt.
- **Sin texto sobre imágenes.** Sin imágenes con fondo blanco desnudo.
- Todo número con formato es-CL: coma decimal, punto de miles.
- Usar solo las cifras de este documento. Si falta un dato, dejarlo marcado como `[VERIFICAR]` y no inventarlo.
- Los tecnicismos (sección 4.2) solo en notas y anexo.
- Reutilizar las imágenes existentes: `app_vista_1_analisis_oyentes.png`, `app_vista_2_segmentacion_atributo.png`, `app_vista_3_simulador_ml.png`, `app_vista_4_portafolio_crud.png`, `distribucion_streams.png`, `metodo_codo_silueta.png`, `arbol_decision_grafico.png`, `matriz_confusion.png`. Recortarlas según se indica; **no deformar proporciones**.

### 7.3 Snippet para regenerar los gráficos en estilo oscuro (matplotlib)

```python
import matplotlib.pyplot as plt
plt.rcParams.update({
    "figure.facecolor": "#181818", "axes.facecolor": "#181818", "savefig.facecolor": "#181818",
    "axes.edgecolor": "#2A2A2A", "axes.labelcolor": "#B3B3B3", "text.color": "#FFFFFF",
    "xtick.color": "#B3B3B3", "ytick.color": "#B3B3B3", "grid.color": "#2A2A2A",
    "font.size": 16, "axes.titlesize": 20, "axes.titleweight": "bold",
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.prop_cycle": plt.cycler(color=["#1DB954","#3B82F6","#A855F7","#F59E0B","#EC4899","#14B8A6","#F97316"]),
})
# Clústeres: 0 #14B8A6 · 1 #EC4899 · 2 #F97316 · 3 #A855F7
# Guardar con dpi=200 y bbox_inches="tight".
```

### 7.4 Control de calidad antes de entregar
- [ ] Ninguna diapositiva supera 40 palabras ni baja de 14 pt.
- [ ] Todos los títulos expresan un mensaje (no solo un tema).
- [ ] Los clústeres usan siempre el mismo color.
- [ ] Todas las cifras coinciden con este documento.
- [ ] No quedan textos sobre imágenes, ni emojis, ni fondos blancos sueltos.
- [ ] Hay pie con número en todas las diapositivas salvo portadas.
- [ ] Hay notas del orador con tiempos; la suma da 12–14 min.
- [ ] Renderizar a imágenes y revisar cada diapositiva (desbordes, solapamientos, alineación).

---

## 8. Preguntas previsibles del jurado (preparar respuesta)

| # | Pregunta | Respuesta sugerida |
|---|---|---|
| P1 | “El 58 % de acierto es bajo; ¿no sería mejor decir siempre ‘no es éxito’?” | Si dijera siempre “no éxito” acertaría ≈ 74 % solo porque el 75 % de las canciones no lo es, pero **no detectaría ningún éxito**. Nuestro árbol detecta el 36 % de los éxitos reales y, como cuando descarta acierta 74 %, sirve para filtrar. La exactitud sola engaña con clases desbalanceadas. |
| P2 | “Solo el 27 % de lo que marca como éxito lo es.” | Correcto, por eso lo presentamos como **filtro de preselección** y no como garantía. Las limitaciones están declaradas: no hay datos de marketing ni redes. |
| P3 | “¿Por qué un árbol tan simple?” | Para que sea interpretable y no memorice; con mayor profundidad el rendimiento en datos nuevos bajaba bajo 52 %. Además, la rúbrica excluye ensambles complejos. |
| P4 | “¿Asociación significa causalidad?” | No. Indica que ciertas combinaciones aparecen juntas más de lo esperable por azar. |
| P5 | “¿Por qué K = 4?” | El codo y la silueta (≈ 0,38) coinciden en 4, y los 4 grupos son interpretables para el negocio. |
| P6 | “¿Por qué la app muestra 200 canciones y dice 85.000?” | Responder según lo que se verifique (ver A1). Tener la respuesta lista antes de presentar. |
| P7 | “¿Qué harían con más tiempo?” | Incorporar datos de marketing, estudiar cómo decaen las reproducciones en el tiempo y reentrenar los modelos de forma automática. |

---

## 9. Observaciones menores para el informe técnico (no afectan la presentación, pero conviene alinear)
- Reconciliar 85.000 registros con la eliminación de 180 (secciones 3.1 y 3.5): las particiones 68.000/17.000 deberían ser ≈ 67.856/16.964, o aclarar que los 85.000 son el total tras la limpieza.
- La Regla N.° 1 (confianza 6,69 %) y la N.° 2 (61,33 %) tienen el mismo soporte y Lift con antecedente y consecuente invertidos; aclarar en una frase que se presenta la dirección más útil para el negocio.
- Agregar al informe una línea sobre la exactitud de referencia (≈ 74 % si siempre se predice “no éxito”) para anticipar la crítica P1.
- Unificar el formato numérico (coma decimal) en tablas y texto.
