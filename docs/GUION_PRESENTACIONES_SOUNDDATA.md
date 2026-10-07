# SoundData Analytics — Guion Oficial para la Defensa Oral
**Proyecto de Minería de Datos (IEI-067) — Universidad Santo Tomás**  
**Docentes:** Florentino Vargas y Rosa Rao  
**Grupo 4:** Vicente Muñoz, Juan Ortiz, Jordan Murillo, Jorge Moncada, Jose Mendez, Bastian Parraguez  
**Duración Total Estimada:** 12 a 14 minutos (Parte 1: ~7 min | Parte 2: ~5 min | Demo y Cierre: ~2 min)

---

## 🧭 Recomendaciones Generales para el Equipo antes de Comenzar
1. **Postura y Ritmo:** Hablen con seguridad, proyectando la voz y manteniendo contacto visual con los docentes. No lean las diapositivas al pie de la letra; las diapositivas son su respaldo visual sintético ($\le 40$ palabras).
2. **Coordinación de Diapositivas:** El encargado de pasar las diapositivas debe estar atento a la frase de pase o "cue" de cada compañero.
3. **Manejo de Preguntas Difíciles:** Si el jurado pide profundizar en fórmulas o números finos, no duden en abrir las **diapositivas ocultas de anexo (A1 a A5)** al final de cada presentación.

---

# PARTE 1: EL ANÁLISIS DE DATOS Y METODOLOGÍA CRISP-DM
📁 Archivo: `docs/PARTE1_ANALISIS_SOUNDDATA_V2.pptx`  
⏱️ Duración: 7:00 a 7:30 minutos  
🎯 Objetivo: Demostrar comprensión del negocio, rigor estadístico y los tres hallazgos clave de minería.

---

### Diapositiva 1 (D1) · Portada
👤 **Orador:** Vicente Muñoz  
⏱️ **Tiempo:** 0:00 – 0:30 (30 seg)  
🖥️ **En pantalla:** Título *"De los datos al éxito musical"*, pregunta guía, integrantes y datos institucionales.

> **Guion verbal (Vicente):**  
> "Muy buenos días, profesores Florentino Vargas y Rosa Rao, y compañeros. Hoy el Grupo 4 les presenta **SoundData Analytics**, un proyecto de inteligencia de negocios aplicado a la industria musical mediante la metodología CRISP-DM.  
> 
> Como equipo nos planteamos una pregunta fundamental: *¿Es posible saber, antes de desembolsar millones en producir y promocionar una canción, a qué tipo de oyente le va a gustar y si tiene probabilidades reales de convertirse en un éxito comercial?*  
> 
> Nuestra defensa está dividida en dos partes: primero, les explicaremos qué descubrimos a partir de 85.000 canciones; y luego, les mostraremos la aplicación web que construimos para que cualquier sello discográfico use estos modelos con un solo clic. Comencemos con el problema."

*(Avanzar a D2)*

---

### Diapositiva 2 (D2) · El Problema de Negocio
👤 **Orador:** Vicente Muñoz  
⏱️ **Tiempo:** 0:30 – 1:20 (50 seg)  
🖥️ **En pantalla:** Cifra protagónica *+100.000 canciones al día* y las tres preguntas críticas del negocio.

> **Guion verbal (Vicente):**  
> "En la industria de la música actual existe una saturación sin precedentes: cada día se suben más de 100.000 canciones nuevas a las plataformas de streaming. Históricamente, las casas discográficas y los productores independientes han invertido presupuestos gigantescos basándose únicamente en la intuición o el 'olfato artístico', lo que genera una tasa de fracaso de inversión superior al 80 %.  
> 
> Para mitigar este riesgo financiero, definimos tres objetivos concretos de minería:  
> 1. Primero: Clasificar y predecir si una canción tiene potencial de alto impacto antes de su masterización.  
> 2. Segundo: Identificar qué arquetipo sonoro u oyente objetivo la va a recibir mejor.  
> 3. Y tercero: Descubrir qué combinaciones de género y popularidad generan sinergia real en el mercado.  
> 
> Ahora Juan les explicará los datos que recolectamos para responder estas preguntas."

*(Avanzar a D3)*

---

### Diapositiva 3 (D3) · Los Datos y la Asimetría del Éxito
👤 **Orador:** Juan Ortiz  
⏱️ **Tiempo:** 1:20 – 2:10 (50 seg)  
🖥️ **En pantalla:** Cifra *25 % → 68 % de streams* y gráfico de distribución en modo oscuro.

> **Guion verbal (Juan):**  
> "Gracias, Vicente. Para este estudio analizamos un catálogo masivo de **85.000 canciones de Spotify**, abarcando una década completa, entre 2015 y 2025, con 17 atributos acústicos y de mercado en 12 géneros musicales.  
> 
> Al realizar el análisis exploratorio, nos encontramos con la realidad brutal del mercado musical que ven en el gráfico de la derecha: una distribución fuertemente asimétrica. Un pequeño grupo de canciones acapara la gran mayoría del tráfico. Específicamente, **el 25 % superior de las canciones concentra el 68 % de todas las reproducciones mundiales**.  
> 
> Por esta razón estadística, definimos rigurosamente como **'Éxito Comercial'** a aquellas canciones situadas en el cuartil superior (Q3), es decir, canciones con **85,2 millones de reproducciones o más**. Este es el umbral que el modelo debe predecir."

*(Avanzar a D4)*

---

### Diapositiva 4 (D4) · Preparación de Datos con Rigor
👤 **Orador:** Juan Ortiz  
⏱️ **Tiempo:** 2:10 – 2:50 (40 seg)  
🖥️ **En pantalla:** Cifra *99,8 % conservado* y las 3 tarjetas de preparación.

> **Guion verbal (Juan):**  
> "En minería de datos, la calidad de los resultados depende directamente de la limpieza. De las 85.180 filas originales, descartamos únicamente **180 registros con valores nulos o corruptos**, lo que representa apenas un 0,2 % de pérdida. Es decir, **conservamos el 99,8 % de los datos limpios**.  
> 
> Pero el desafío más importante fue el tratamiento de valores extremos: en música, un tema con millones de reproducciones o con tempo muy acelerado no es un 'error de tipeo', es un megahit. Por lo tanto, no eliminamos los outliers de streams; aplicamos winsorización en percentiles 1 y 99 para ritmos atípicos y estandarizamos todas las variables acústicas con `StandardScaler` para que ninguna variable dominara artificialmente la distancia.  
> 
> Con los datos preparados, Jorge les explicará el primer modelo: la segmentación por K-Means."

*(Avanzar a D5)*

---

### Diapositiva 5 (D5) · Segmentación Acústica (K-Means)
👤 **Orador:** Jorge Moncada  
⏱️ **Tiempo:** 2:50 – 3:50 (1:00 min)  
🖥️ **En pantalla:** 4 perfiles sonoros con sus colores identificadores (Turquesa, Fucsia, Naranja, Púrpura).

> **Guion verbal (Jorge):**  
> "Gracias, Juan. Para entender a qué audiencia pertenece cada canción, aplicamos el algoritmo de agrupamiento no supervisado **K-Means**. Mediante el Método del Codo y el Coeficiente de Silueta, determinamos que **K = 4** es la estructura óptima del catálogo.  
> 
> El modelo descubrió cuatro perfiles acústicos con identidad muy clara:  
> - En **Turquesa (Clúster 0)**: *Chill y Acústico*, dominado por baladas, música clásica y acústica, con baja energía y alto valor instrumental.  
> - En **Fucsia (Clúster 1)**: *Pop Enérgico*, canciones sumamente luminosas, de alta positividad y ritmo comercial.  
> - En **Naranja (Clúster 2)**: *Rock y Sonidos Orgánicos*, temas potentes donde priman guitarras y volumen elevado con baja bailabilidad electrónica.  
> - Y en **Púrpura (Clúster 3)**: *Urbano y Bailable*, el territorio del reggaetón, hip-hop y trap latino, caracterizado por una máxima bailabilidad e intensas frecuencias graves.  
> 
> Esto le permite a un productor saber al instante en qué playlist y nicho de mercado encaja su sonido. Ahora, Jose les mostrará cómo predecimos si será un éxito."

*(Avanzar a D6)*

---

### Diapositiva 6 (D6) · Modelo Predictivo (Árbol de Decisión)
👤 **Orador:** Jose Mendez  
⏱️ **Tiempo:** 3:50 – 4:50 (1:00 min)  
🖥️ **En pantalla:** Métrica *74 % de precisión en descarte* y gráfico simplificado del árbol con 8 caminos.

> **Guion verbal (Jose):**  
> "Gracias, Jorge. Para predecir el éxito comercial entrenamos un **Árbol de Decisión**. Decidimos acotar intencionalmente la profundidad máxima a `max_depth = 3`. ¿Por qué? Porque un árbol de solo 8 caminos posibles es interpretable para los ejecutivos de un sello discográfico y previene que el modelo memorice el ruido del dataset.  
> 
> El árbol demostró que los factores decisivos para escalar a las grandes ligas son el volumen sonoro medio (loudness), la energía y la bailabilidad.  
> 
> Pero lo más valioso para el negocio es su rol como **filtro de descarte**: cuando el árbol clasifica una pista como 'No Éxito', **acierta el 74 % de las veces**. En la industria, evitar gastar cientos de miles de dólares en promocionar canciones inviables genera más ahorro y rentabilidad que intentar adivinar un golpe de suerte.  
> 
> A continuación, Jordan les presentará las reglas de asociación que completan este análisis."

*(Avanzar a D7)*

---

### Diapositiva 7 (D7) · Reglas de Asociación (Algoritmo Apriori)
👤 **Orador:** Jordan Murillo  
⏱️ **Tiempo:** 4:50 – 5:40 (50 seg)  
🖥️ **En pantalla:** Métrica protagonista *Lift 3,40* y tarjetas con las 3 reglas comerciales.

> **Guion verbal (Jordan):**  
> "Gracias, Jose. Mientras los modelos anteriores analizan el sonido de forma individual, con el algoritmo **Apriori** buscamos qué combinaciones de género, popularidad y presencia en el catálogo ocurren juntas de manera recurrente.  
> 
> Minamos cientos de reglas con `mlxtend` y filtramos aquellas con verdadero impacto comercial:  
> - La regla reina nos reveló un **Lift de 3,40 y 61,3 % de confianza**: indica que cuando una pista del género Pop logra alta exposición, su probabilidad de alcanzar popularidad masiva es **3,4 veces superior a lo esperable por azar**.  
> - La segunda regla demostró que la música Urbana con alta bailabilidad mantiene una confianza sostenida sobre el 58 % en listas de éxitos.  
> - Y la tercera regla nos advierte que los temas instrumentales rara vez traspasan al top 25 % masivo, requiriendo estrategias de marketing de nicho.  
> 
> Ahora Vicente sintetizará el impacto financiero de estos tres hallazgos."

*(Avanzar a D8)*

---

### Diapositiva 8 (D8) · Impacto en el Negocio y Retorno de Inversión
👤 **Orador:** Vicente Muñoz  
⏱️ **Tiempo:** 5:40 – 6:20 (40 seg)  
🖥️ **En pantalla:** Los tres pilares de impacto financiero (Filtrar antes de producir, pauta dirigida, colaboraciones estratégicas).

> **Guion verbal (Vicente):**  
> "En resumen, integrar minería de datos transforma la toma de decisiones en tres niveles:  
> 1. **Optimización de Presupuesto:** Usar el árbol como filtro de entrada reduce drásticamente las pérdidas en canciones sin tracción acústica.  
> 2. **Segmentación de Audiencia:** Asignar cada tema a uno de los 4 clústeres permite dirigir la pauta publicitaria en TikTok y Spotify Ads exactamente al público objetivo.  
> 3. **Estrategia de Lanzamientos:** Utilizar las reglas de asociación para juntar artistas urbanos y pop maximiza el retorno publicitario.  
> 
> Pero estos modelos no podían quedarse en un Jupyter Notebook. Para que un equipo de marketing o un productor los utilice en su día a día, construimos una solución accesible."

*(Avanzar a D9)*

---

### Diapositiva 9 (D9) · Transición a la Aplicación Web
👤 **Orador:** Vicente Muñoz  
⏱️ **Tiempo:** 6:20 – 6:50 (30 seg)  
🖥️ **En pantalla:** Tarjeta de transición con el logo de SoundData y puente hacia la Parte 2.

> **Guion verbal (Vicente):**  
> "Y es así como nace **SoundData Analytics Web**: un sistema full-stack donde cualquier usuario, sin saber de código ni de estadística, puede interactuar con el catálogo, simular canciones en vivo y gestionar su propio portafolio.  
> 
> Damos paso a la Parte 2, donde Bastian y el equipo les presentarán el funcionamiento de la herramienta."

*(Cambio a la presentación PARTE 2 · Diapositiva 10)*

---

# PARTE 2: LA APLICACIÓN WEB Y DEMO EN VIVO
📁 Archivo: `docs/PARTE2_APLICACION_SOUNDDATA_V2.pptx`  
⏱️ Duración: 5:00 a 6:00 minutos  
🎯 Objetivo: Demostrar arquitectura, usabilidad, robustez de software y funcionamiento en tiempo real.

---

### Diapositiva 10 (D10) · Portada de la Aplicación y Arquitectura
👤 **Orador:** Bastian Parraguez  
⏱️ **Tiempo:** 6:50 – 7:35 (45 seg)  
🖥️ **En pantalla:** Diagrama en 3 pasos (Ajustas → Analiza → Decides) y credenciales técnicas (<0,25s, SQLite, 100 % en español).

> **Guion verbal (Bastian):**  
> "Muchas gracias, Vicente. Bienvenidos a la Parte 2. **SoundData Web** fue diseñada con un principio fundamental: *complejidad en los modelos, simplicidad absoluta para el usuario final*.  
> 
> Su arquitectura está montada sobre **FastAPI en Python**, lo que nos permite tiempos de respuesta menores a 250 milisegundos por inferencia. Para la persistencia creamos una base de datos **SQLite transaccional**, y en el frontend utilizamos una interfaz oscura moderna, responsiva y completamente en español.  
> 
> A continuación, revisaremos las cuatro vistas principales que componen el sistema."

*(Avanzar a D11)*

---

### Diapositiva 11 (D11) · Vista 1: Análisis de Oyentes
👤 **Orador:** Jordan Murillo  
⏱️ **Tiempo:** 7:35 – 8:20 (45 seg)  
🖥️ **En pantalla:** Captura grande de la Vista 1 con los 3 globos destacados.

> **Guion verbal (Jordan):**  
> "La primera pantalla es la **Vista de Análisis de Oyentes**. Su propósito es ofrecer una radiografía ejecutiva inmediata del mercado.  
> 
> En la parte superior encontramos cuatro indicadores clave que resumen más de 841 millones de oyentes acumulados. Debajo, un gráfico dinámico de barras compara el volumen de reproducciones entre los 12 géneros musicales, evidenciando el dominio del Pop y lo Urbano; y a la derecha, un gráfico de dona desglosa el reparto geográfico entre los principales mercados mundiales.  
> 
> Todo el módulo se alimenta directamente de la API REST de forma fluida."

*(Avanzar a D12)*

---

### Diapositiva 12 (D12) · Vista 2: Segmentación por Atributo
👤 **Orador:** Jorge Moncada  
⏱️ **Tiempo:** 8:20 – 9:05 (45 seg)  
🖥️ **En pantalla:** Captura de la Vista 2, filtros interactivos y botón de exportación.

> **Guion verbal (Jorge):**  
> "La segunda pantalla es la **Vista de Segmentación**. Esta herramienta permite al analista explorar interactivamente el catálogo completo según cualquier dimensión: por género, país, año de lanzamiento o clúster acústico.  
> 
> Al cambiar los selectores, la tabla recalcula al instante qué porcentaje del catálogo representa ese segmento y su nivel medio de streams. Además, cuenta con un botón de exportación directa que genera un reporte descargable para presentaciones de directorio."

*(Avanzar a D13)*

---

### Diapositiva 13 (D13) · Vista 3: Simulador Predictivo (DEMO EN VIVO)
👤 **Orador:** Jose Mendez  
⏱️ **Tiempo:** 9:05 – 10:20 (1:15 min)  
🖥️ **En pantalla:** Captura de la Vista 3 / Pantalla en vivo de la aplicación en `http://127.0.0.1:8000`.

> **Guion verbal (Jose):**  
> "Llegamos al corazón de la plataforma: el **Simulador Predictivo de Inteligencia Artificial**.  
> 
> *(Si se hace demo en vivo, cambiar a la ventana del navegador; si no, señalar la diapositiva)*  
> 
> Aquí un productor puede ingresar las características de una canción antes de lanzarla: ajustamos el tempo en BPM, la energía, el volumen y la bailabilidad mediante estos controles deslizantes.  
> 
> Al hacer clic en *'Evaluar Potencial'*, en menos de un cuarto de segundo la API normaliza los valores y consulta nuestros tres modelos en paralelo:  
> 1. El velocímetro nos indica la **probabilidad de éxito** según el árbol de decisión.  
> 2. El badge nos asigna automáticamente a cuál de los **4 clústeres sonoros** pertenece.  
> 3. Y en la tarjeta inferior recibimos **consejos de negocio personalizados** derivados de las reglas de asociación.  
> 
> Con el botón inferior, podemos guardar esta evaluación directamente en nuestro portafolio sin recargar la página."

*(Avanzar a D14)*

---

### Diapositiva 14 (D14) · Vista 4: Portafolio y Gestión CRUD
👤 **Orador:** Juan Ortiz  
⏱️ **Tiempo:** 10:20 – 11:05 (45 seg)  
🖥️ **En pantalla:** Captura de la tabla de portafolio con acciones Crear, Editar, Buscar y Eliminar.

> **Guion verbal (Juan):**  
> "La cuarta pantalla es la **Gestión del Portafolio**. Aquí implementamos un ciclo CRUD completo conectado a SQLite:  
> - El analista puede registrar nuevas canciones evaluadas.  
> - Puede editar sus parámetros acústicos si el productor modificó la mezcla en el estudio.  
> - Cuenta con un buscador en tiempo real por título o artista.  
> - Y puede eliminar pistas descartadas con confirmación de seguridad.  
> 
> Para garantizar que la aplicación nunca se vea vacía en la nube, el sistema incluye un mecanismo de auto-semillado que inicializa seis canciones de referencia en la base de datos."

*(Avanzar a D15)*

---

### Diapositiva 15 (D15) · Calidad, Validación y Pruebas
👤 **Orador:** Bastian Parraguez  
⏱️ **Tiempo:** 11:05 – 11:50 (45 seg)  
🖥️ **En pantalla:** Métrica *17 / 17 pruebas aprobadas*, validación Pydantic y despliegue.

> **Guion verbal (Bastian):**  
> "Como futuros ingenieros, la robustez del software era fundamental. La aplicación no solo se ve bien, sino que está respaldada por una suite rigurosa de calidad:  
> - Contamos con **17 pruebas unitarias automatizadas con Pytest**, todas aprobadas al 100 %, verificando los endpoints HTTP, el ciclo CRUD de la base de datos y la inferencia de los modelos serializados.  
> - Cada entrada de usuario está protegida por esquemas tipados con **Pydantic**; si alguien introduce un BPM negativo o texto en un campo numérico, el sistema responde con mensajes de error claros en español, sin romperse.  
> - Además, la plataforma está configurada y lista para despliegue en la nube mediante un archivo `Procfile` contenerizable."

*(Avanzar a D16)*

---

### Diapositiva 16 (D16) · Conclusiones y Cierre
👤 **Orador:** Vicente Muñoz (con todo el equipo al frente)  
⏱️ **Tiempo:** 11:50 – 12:30 (40 seg)  
🖥️ **En pantalla:** Título *"Los datos no reemplazan al oído, pero ayudan a invertir mejor"*, tres conclusiones finales y agradecimiento.

> **Guion verbal (Vicente):**  
> "Para concluir: los datos y los algoritmos jamás van a reemplazar la creatividad ni la sensibilidad de un músico o productor. Sin embargo, en una industria donde se lanzan cien mil temas diarios, **la minería de datos permite transformar la incertidumbre en una ventaja estratégica medible**.  
> 
> Hoy les demostramos que con rigor metodológico CRISP-DM y buenas prácticas de ingeniería de software, es posible pasar desde un conjunto de 85.000 filas hasta una herramienta productiva, confiable y con valor comercial real.  
> 
> Agradecemos sinceramente su atención y quedamos a total disposición de la comisión para responder sus preguntas."

---

## 🛡️ GUÍA RÁPIDA PARA LA RONDA DE PREGUNTAS (ANEXOS OCULTOS)

Si los profesores hacen preguntas técnicas específicas, pueden presionar el número de la diapositiva oculta o navegar hasta el anexo:

| Pregunta Típica del Profesor | Diapositiva de Respaldo | Quién Responde | Respuesta Clave |
|---|:---:|:---:|---|
| *“¿Cómo validaron que K=4 era el número correcto y no K=3 o K=5?”* | **A2** (o A4 en Parte 1) | **Jorge** | "Evaluamos el coeficiente de silueta entre K=2 y K=8. Aunque K=2 daba una silueta ligeramente mayor, solo dividía canciones lentas de rápidas sin valor de negocio. **K=4 logró una silueta sólida de 0,22** separando los cuatro nichos acústicos reales que exige la industria." |
| *“El árbol tiene 58 % de exactitud global, ¿por qué dicen que es un buen modelo?”* | **A3** (Matriz de confusión) | **Jose** | "Porque en una distribución desbalanceada (75/25), el costo de un Falso Positivo es perder dinero produciendo un fracaso. Nuestro árbol tiene un **74 % de precisión en la clase mayoritaria (No Éxito)**, funcionando exactamente como un filtro conservador de descarte de riesgos." |
| *“¿Por qué el Lift de 3,40 es significativo en las reglas Apriori?”* | **A4** (Reglas completas) | **Jordan** | "Un Lift igual a 1 significa independencia estadística. Un **Lift de 3,40** demuestra matemáticamente que la conjunción de género Pop con alta rotación es **3,4 veces más frecuente que si ambos eventos ocurrieran al azar** en el catálogo." |
| *“¿Por qué eligieron SQLite y no PostgreSQL o MySQL?”* | **A5** (Arquitectura y BD) | **Bastian** | "Para este alcance y despliegue liviano, SQLite opera como una base de datos embebida de cero latencia de red, garantizando transaccionalidad ACID completa sin requerir un servidor dedicado adicional." |
| *“¿Qué tratamiento le dieron a los missing values?”* | **A1** (Preparación de datos) | **Juan** | "Se detectaron 180 filas con campos nulos en atributos secundarios sobre 85.180 registros (0,21 %). Al ser una fracción insignificante, eliminarlas preservó el 99,8 % del dataset sin sesgar la muestra con imputaciones artificiales." |
