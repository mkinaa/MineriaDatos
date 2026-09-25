# Segmentación de Audiencias Musicales y Predicción de Éxito
> **Metodología:** CRISP-DM (Fases 1 y 2: Comprensión del Negocio y de los Datos)  
> **Asignatura:** Minería de Datos (IEI-067)  
> **Dataset:** `spotify_2015_2025_85k.csv` (85.000 canciones)

---

| Problema Central | 📊 Base de Datos | 🌐 Solución Web |
| :--- | :--- | :--- |
| **Incertidumbre en lanzamientos:** Alto riesgo financiero y marketing genérico sin segmentar a los oyentes por contexto o estado anímico. | **85.000 canciones reales (2015-2025):** 19 atributos, 10 mercados globales y 12 géneros balanceados sin valores nulos. | **Aplicación Interactiva:** Web full-stack que clasifica potencial de Hit, perfila el cluster sonoro y entrega recomendaciones accionables. |

---

## PUNTO 1: Comprensión del Negocio (Business Understanding)

### 1.1 El Problema Real
* **El cambio de paradigma en el consumo:** En la actualidad, el usuario no consume música únicamente por artista; la escucha está guiada por el **contexto y el ritmo cardíaco (BPM)** (ej: 140–160 BPM para entrenamiento/running, 110–128 BPM para fiesta/club, $<90$ BPM para estudio y relajación).
* **El dolor de la industria:** Tanto las grandes discográficas como los artistas independientes invierten millones a ciegas en campañas de publicidad masivas y genéricas, sin conocer con exactitud qué mercados geográficos o nichos de oyentes tienen afinidad acústica con sus producciones.

### 1.2 Lo que Resuelve la Minería de Datos
* **Clustering (`K-Means`):** Segmentación automática de canciones y audiencias en *"Vibras/Moods"* acústicos (ej. *Cluster Cardio/Alta Energía*, *Cluster Mainstream Bailable*, *Cluster Acústico de Estudio*).
* **Clasificación (`Árbol de Decisión`):** Predicción de probabilidad de éxito comercial (**Hit**: Popularidad $\ge 50$ o alto volumen de reproducciones) antes de incurrir en gastos de marketing.
* **Reglas de Asociación (`Apriori`):** Descubrimiento de patrones ocultos entre tempo, procedencia geográfica y tipo de sello discográfico (ej. *Si el BPM es rápido y proviene de sello independiente $\Rightarrow$ ¿qué géneros y países aseguran mayor afinidad?*).
* **Despliegue Web (`FastAPI` + `HTML/Bootstrap/JS`):** Interfaz interactiva donde un productor ingresa los atributos de su pista y el sistema retorna predicción, cluster y recomendaciones en tiempo real.

### 1.3 Metas de Éxito Concretas
* **Exactitud en Clasificación:** Superar el **70% de Accuracy** en el Árbol de Decisión (`DecisionTreeClassifier`), manteniendo control sobre `max_depth` para evitar sobreajuste (*overfitting*).
* **Calidad de Segmentación:** Entre **3 y 5 clusters** acústicos claramente diferenciados, respaldados técnicamente por el **Método del Codo** y el **Coeficiente de Silueta**.
* **Reglas de Negocio Válidas:** Mínimo **3 reglas Apriori** significativas con:
  * $\text{Soporte} \ge 5\%$
  * $\text{Confianza} \ge 60\%$
  * $\text{Lift} > 1.2$

---

## PUNTO 2: Comprensión de los Datos (Data Understanding)

### 2.1 Radiografía del Dataset Seleccionado
* **Archivo fuente:** `spotify_2015_2025_85k.csv` (Kaggle).
* **Volumen:** **85.000 registros** y **19 columnas** (cumple y supera ampliamente el mínimo de 500 filas y 5 atributos).
* **Integridad técnica:** **0 valores nulos** ($100\%$ de completitud) con cobertura temporal ininterrumpida de una década (**2015 a 2025**).

### 2.2 Identificación y Rol de Variables
* **Variable Objetivo (`Class`):** `is_hit` / Éxito Comercial:
  * `1` = Canción con Popularidad $\ge 50$ o alto volumen de streams.
  * `0` = Canción estándar / baja repercusión comercial.
  * *Esta variable será aprendida por el Árbol de Decisión.*
* **Variables Predictoras (`Meta`):**
  * **Atributos acústicos:** `tempo` (BPM), `danceability`, `energy`, `loudness`, `instrumentalness`.
  * **Mercado geográfico:** `country` (10 países globales representados).
  * **Industria discográfica:** `label` (Major vs. Independent).

### 2.3 Resumen Estadístico y Hallazgos para la Exposición

| Variable | Promedio / Mediana | Rango (Mín - Máx) | Interpretación Analítica para el Negocio |
| :--- | :--- | :--- | :--- |
| `stream_count` *(Reproducciones)* | Promedio: ~214k<br>Mediana: 2.000 | 1.000 a 20.000.000 | **Ley de Pareto evidente:** Un porcentaje reducido de pistas concentra millones de reproducciones (mega-hits), mientras la gran mayoría atiende a nichos específicos. |
| `tempo` *(Ritmo en BPM)* | Promedio: 130 BPM<br>Mediana: 130 BPM | 60 a 200 BPM | **Punto de inflexión simétrico:** 130 BPM divide acústicamente la música pausada/relajante de las pistas de entrenamiento, baile y alta energía. |
| `popularity` *(Índice de Éxito)* | Promedio: 48,16<br>Mediana: 47 | 0 a 100 puntos | **Distribución equilibrada y centrada:** Valida técnicamente fijar el umbral de corte de la clase positiva (`Hit`) en los 50 puntos. |
| `genre` *(12 Géneros)* | ~7.080 canciones / género | 12 categorías | **Equilibrio categórico perfecto:** Cero sesgo muestral entre Pop, Rock, Reggaeton, Metal, EDM, Jazz, etc. |
| `country` *(10 Mercados)* | ~8.500 canciones / país | 10 países | **Representatividad global:** Refleja patrones de consumo en EE.UU., México, Brasil, Reino Unido, Japón, Alemania, entre otros. |
