# GUÍA Y ESTRUCTURA DE PRESENTACIÓN ORAL (10 MINUTOS)
## Proyecto Final Minería de Datos (IEI-067): "SoundData Analytics"
### Soporte para Diapositivas (.pptx) y Guión de Defensa

---

**Tiempo Total Asignado:** 10 minutos  
**Estructura:** 10 Diapositivas clave + 2 min de Demostración en Vivo  
**Distribución de Integrantes:** 6 expositores (~1:30 a 1:40 min por persona)

---

## 🕒 Cronograma de Exposición (10 Minutos)

| Diapositiva | Título / Tema | Expositor | Tiempo Estimado |
| :---: | :--- | :--- | :---: |
| **D1** | Portada y Problema de Negocio | **Vicente Muñoz** | 0:00 - 1:15 |
| **D2** | Entendimiento y Exploración de Datos | **Juan Ortiz** | 1:15 - 2:30 |
| **D3** | Preparación de Datos y Filtro IQR | **Juan Ortiz** | 2:30 - 3:30 |
| **D4** | Modelado 1: Reglas de Asociación (Apriori) | **Jordan Murillo** | 3:30 - 4:45 |
| **D5** | Modelado 2: Clustering de Audiencias (K-Means) | **Jorge Moncada** | 4:45 - 6:00 |
| **D6** | Modelado 3: Árbol de Decisión y Matriz de Confusión | **Jose Mendez** | 6:00 - 7:15 |
| **D7** | Evaluación de Modelos y Límites de la Minería | **Jose Mendez** | 7:15 - 8:00 |
| **D8** | Demostración en Vivo de la Aplicación Web | **Vicente Muñoz & Bastian Parraguez** | 8:00 - 9:15 |
| **D9** | Arquitectura Web, SQLite y Calidad de Código | **Bastian Parraguez** | 9:15 - 9:45 |
| **D10** | Conclusiones y Recomendaciones de Negocio | **Vicente Muñoz** | 9:45 - 10:00 |

---

## 📑 Detalle Contenido Diapositiva por Diapositiva

### Diapositiva 1: Portada y Contexto de Negocio
- **Título:** SoundData Analytics — Inteligencia de Datos para la Industria Musical.
- **Subtítulo:** Metodología CRISP-DM sobre 85.000 canciones (2015–2025).
- **Contenido:**
  - Nombres de los 6 integrantes, profesores y fecha.
  - El dolor de la industria: Más de 100.000 lanzamientos diarios; necesidad de pasar de la intuición de A&R a decisiones guiadas por datos.
  - Preguntas clave: ¿Será un éxito comercial? ¿A qué segmento pertenece? ¿Qué combinaciones impulsan su viralidad?

### Diapositiva 2: Comprensión de los Datos (EDA)
- **Título:** Comprensión de los Datos: Catálogo Global de Spotify.
- **Contenido:**
  - 85.000 pistas con 17 atributos (numéricos y categóricos).
  - Variable objetivo: `es_exito` (Corte en Percentil 75: $\ge 85.200.000$ reproducciones).
  - Distribución asimétrica de reproducciones (*right-skewed*): el 25% de canciones concentra el 68% de las escuchas.
  - Correlaciones clave: Energía y Sonoridad ($r = +0.72$); Instrumentalidad vs Popularidad ($r = -0.34$).

### Diapositiva 3: Preparación de Datos (Fase 3 CRISP-DM)
- **Título:** Limpieza Rigurosa, Outliers con IQR y Estandarización.
- **Contenido:**
  - Detección de outliers con **Rango Intercuartílico ($IQR = Q_3 - Q_1$)**:
    - Winsorización controlada en BPM y duración para no perder temas extremos válidos.
    - Conservación justificada de los "Mega-Hits".
  - Tratamiento de nulos (eliminación marginal de $< 0.2\%$).
  - Normalización con `StandardScaler` ($\mu=0, \sigma=1$) para no sesgar las distancias en K-Means.
  - Partición Train/Test 80/20 con estratificación (`stratify=y`) para mantener la proporción de éxitos.

### Diapositiva 4: Minería de Reglas de Asociación (Apriori)
- **Título:** Descubrimiento de Patrones de Consumo con Apriori.
- **Contenido:**
  - Algoritmo Apriori implementado con la librería `mlxtend`.
  - Discretización de variables continuas en canastas transaccionales.
  - **Regla Estrella:**
    $$\{\text{Alto\_Stream}, \text{Gen\_Pop}\} \Longrightarrow \{\text{Alta\_Popularidad}\} \quad (\text{Lift} = 3.40, \; \text{Confianza} = 61.3\%)$$
  - **Impacto en el Negocio:** Un tema Pop con tracción inicial triplica su probabilidad de transformarse en un fenómeno global frente a otros géneros.

### Diapositiva 5: Clustering de Canciones (K-Means)
- **Título:** Segmentación No Supervisada del Catálogo Musical.
- **Contenido:**
  - Justificación cuantitativa del número de clústeres:
    - **Método del Codo (Elbow):** Inflexión de inercia clara en $K=4$.
    - **Coeficiente de Silueta:** Máxima cohesión interna y separación en $K=4$.
  - Los 4 arquetipos identificados:
    1. *Cluster 0 — Acústico, Instrumental & Chill:* Listas de concentración y estudio.
    2. *Cluster 1 — Pop Comercial & Radio:* Gran consumo y alta rotación.
    3. *Cluster 2 — Rock & Fiesta (Alta Energía):* Entrenamientos y festivales.
    4. *Cluster 3 — Urbano, Trap & Explícito:* Audiencia juvenil (Gen Z).

### Diapositiva 6: Clasificación Supervisada (Árbol de Decisión)
- **Título:** Predicción de Éxito Comercial con Árbol de Decisión.
- **Contenido:**
  - `DecisionTreeClassifier` con regularización de hiperparámetros.
  - Control de sobreajuste:
    - Demostración gráfica: $\text{max\_depth} \ge 8$ provocaba *overfitting* severo (train 84% vs test 51%).
    - Se seleccionó $\text{max\_depth} = 3$ para mantener interpretabilidad de negocio.
  - Matriz de Confusión en conjunto de prueba independiente (17.000 canciones):
    - 8.253 Verdaderos Negativos, 1.598 Verdaderos Positivos.

### Diapositiva 7: Evaluación Comparativa y Límites del Modelo
- **Título:** Evaluación y Realidad del Fenómeno Musical.
- **Contenido:**
  - Exactitud global (Accuracy): $57.95\%$ con precisión del $74\%$ en la clase de temas estándar.
  - ¿Por qué el modelo de audio tiene un techo natural?
    - La música es un fenómeno multifactorial: el presupuesto de marketing, la viralización en redes sociales y la base de fans del artista determinan gran parte del éxito.
    - El árbol actúa como un excelente **filtro de preselección técnica de maquetas** para sellos discográficos.

### Diapositiva 8: Demostración en Vivo de la Aplicación Web
- **Título:** Aplicación Web "SoundData Analytics" en Acción.
- **Contenido:**
  - **Pestaña 1 (Análisis de Oyentes):** KPIs en tiempo real, distribución de streams por país y género.
  - **Pestaña 2 (Segmentación):** Exploración por atributos acústicos (100% en español).
  - **Pestaña 3 (Simulador ML):** Inferencia en tiempo real moviendo deslizadores de BPM, energía y bailabilidad.
  - **Pestaña 4 (Portafolio SQLite):** Registro, edición y eliminación de canciones en vivo.
  *(En caso de fallo de internet, se reproduce el Video de Respaldo de 2 minutos).*

### Diapositiva 9: Arquitectura Web, Persistencia y Calidad de Software
- **Título:** Arquitectura Full-Stack, Pruebas y Despliegue.
- **Contenido:**
  - **Backend:** FastAPI con ASGI Uvicorn y modelos Pydantic (validación amigable de errores sin mostrar tracebacks de Python).
  - **Frontend:** Bootstrap 5 Dark, Chart.js y Fetch API nativa (sin frameworks pesados, cumpliendo la rúbrica).
  - **Persistencia:** SQLite 3 transaccional con auto-semillado demostrativo.
  - **Calidad:** Suite automatizada de **17 pruebas unitarias con `pytest`** cubriendo API, base de datos e inferencia.

### Diapositiva 10: Conclusiones y Recomendaciones de Negocio
- **Título:** Conclusiones y Estrategia Accionable de Negocio.
- **Contenido:**
  - Asignación de presupuestos según el clúster (concentrar pauta en Pop/Urbano y ubicar en playlists funcionales los temas acústicos).
  - La importancia del proceso CRISP-DM completo: desde los datos crudos hasta una herramienta operativa de software.
  - Agradecimientos y apertura de la ronda de preguntas.

---

## 🎬 Guión Rápido para el Video de Respaldo (2 Minutos)

Si la comisión solicita el video o si el servicio gratuito de Render experimenta demora de inicio en frío:
1. **0:00 - 0:25:** Mostrar la pantalla de inicio con los KPIs y los gráficos de barras por mercado y género.
2. **0:25 - 0:50:** Cambiar a la pestaña "Segmentación por Atributo" y mostrar los filtros interactivos.
3. **0:50 - 1:25:** Ir al "Simulador ML", ajustar los deslizadores (Tempo: 125 BPM, Bailabilidad: 0.85, Energía: 0.80) y hacer clic en *"Evaluar Potencial de Canción"*. Mostrar cómo aparecen la probabilidad de éxito (ej. 75%), el Cluster 1 (Pop Radio) y las recomendaciones.
4. **1:25 - 1:55:** Hacer clic en *"Guardar Canción en Portafolio"*, ir a la pestaña "Portafolio & CRUD (SQLite)", mostrar la nueva fila creada, editar un campo y eliminar un registro de prueba.
5. **1:55 - 2:00:** Mostrar la terminal ejecutando `pytest -v` con los 17 tests pasando en verde.
