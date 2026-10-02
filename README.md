# SoundData Analytics: Segmentación de Audiencias Musicales y Predicción de Éxito
> **Metodología:** CRISP-DM | **Asignatura:** Minería de Datos (IEI-067) — Santo Tomás  
> **Dataset Base:** `spotify_2015_2025_85k.csv` (85.000 canciones, 19 atributos, 10 países y 12 géneros)

---

## 👥 Integrantes del Equipo y Distribución de Roles

| Integrante | Rol / Especialidad | Módulo CRISP-DM | Entregables Clave |
| :--- | :--- | :--- | :--- |
| **Juan Ortiz** | Líder de Datos y Preprocesamiento | **Fase 3: Preparación** | Limpieza de outliers con **IQR**, escalado `StandardScaler`, One-Hot Encoding y partición Train/Test (80/20). |
| **Jordan Murillo** | Modelado de Clasificación | **Fase 4A: Árbol de Decisión** | Entrenamiento de `DecisionTreeClassifier`, optimización de `max_depth` (evitar overfitting), matriz de confusión y exportación de `modelo_arbol.joblib`. |
| **Jorge Moncada** | Modelado de Clustering | **Fase 4B: K-Means** | Aplicación de K-Means, justificación de $K$ (Método del Codo y Silueta), caracterización de clusters y exportación de `modelo_kmeans.joblib`. |
| **Jose Mendez** | Reglas de Asociación | **Fase 4C: Apriori** | Discretización de variables acústicas (BPM), ejecución de Apriori con `mlxtend`, reporte de reglas ($Lift > 1.2$, $Conf \ge 60\%$) y `reglas_apriori.json`. |
| **Bastian Parraguez**| Desarrollador Backend | **Fase 6: API con FastAPI** | Servidor `app/main.py`, endpoints `/api/predecir` y `/api/segmentar`, validación de datos con Pydantic y configuración para Render (`Procfile`). |
| **Vicente Muñoz** | Desarrollador Frontend | **Fase 6: UI con Bootstrap 5** | Interfaz web interactiva en modo oscuro (Bootstrap 5 Dark), conexión cliente-servidor con `fetch()`, gráficos Chart.js y Mockup de Semana 2. |

---

## 📊 Diagrama 1: Flujo de Trabajo del Equipo (CRISP-DM + FullStack)

```mermaid
flowchart TD
    subgraph DS["📓 CIENCIA DE DATOS Y MODELADO (Notebook / Colab)"]
        P1["👤 Juan Ortiz<br><b>Fase 3: Preparación de Datos</b><br>• Outliers IQR (obligatorio)<br>• StandardScaler<br>• One-Hot Encoding<br>• Train/Test Split (80/20)"]
        P2["👤 Jordan Murillo<br><b>Fase 4A: Clasificación</b><br>• DecisionTreeClassifier<br>• Optimización max_depth<br>• Matriz de Confusión<br>• Visualización plot_tree"]
        P3["👤 Jorge Moncada<br><b>Fase 4B: Clustering</b><br>• K-Means con scikit-learn<br>• Método del Codo y Silueta<br>• Justificación de K (3-5)<br>• Perfilado de Clusters"]
        P4["👤 Jose Mendez<br><b>Fase 4C: Reglas de Asociación</b><br>• Apriori con mlxtend<br>• Discretización de BPM/audio<br>• Reglas: Soporte, Confianza, Lift<br>• Interpretación de Negocio"]
    end

    subgraph WEB["🚀 DESARROLLO Y DESPLIEGUE WEB (FastAPI + Bootstrap 5)"]
        P5["👤 Bastian Parraguez<br><b>Fase 6: Backend & API</b><br>• Servidor FastAPI (main.py)<br>• Endpoints /predecir y /segmentar<br>• Carga de modelos (.joblib)<br>• Despliegue en Render"]
        P6["👤 Vicente Muñoz<br><b>Fase 6: Frontend & Mockup</b><br>• Interfaz Bootstrap 5 Dark<br>• Consumo de API con fetch()<br>• Gráficos dinámicos (Chart.js)<br>• Capturas Mockup Semana 2"]
    end

    P1 --> P2
    P1 --> P3
    P1 --> P4
    P2 --> P5
    P3 --> P5
    P4 --> P5
    P5 <--> P6
```

---

## 🏗️ Diagrama 2: Arquitectura del Sistema y Comunicación de Datos

```mermaid
sequenceDiagram
    autonumber
    actor Usuario as 👤 Usuario / Analista
    participant UI as 🖥️ Frontend (HTML + Bootstrap 5 Dark)
    participant API as ⚙️ Backend (FastAPI / Uvicorn)
    participant Modelo as 🧠 Modelos Serializados (.joblib)

    Note over Usuario,UI: 1. Interacción del Usuario
    Usuario->>UI: Ingresa BPM, Energía, País y Género
    Usuario->>UI: Clic en "Analizar Canción / Segmentar"

    Note over UI,API: 2. Comunicación Asíncrona (JSON)
    UI->>API: POST /api/predecir {tempo, energy, country, genre}
    
    Note over API,Modelo: 3. Inferencia de Machine Learning
    API->>API: Valida datos (Pydantic, sin trazas de error)
    API->>Modelo: Escala variables con scaler.joblib
    API->>Modelo: Ejecuta modelo_arbol.predict() y modelo_kmeans.predict()
    Modelo-->>API: Retorna: Hit = Sí (78%) | Cluster = "Cardio / Alta Intensidad"
    API->>API: Cruza con reglas_apriori.json (afinidades de mercado)

    Note over API,UI: 4. Respuesta al Cliente
    API-->>UI: JSON {es_hit: true, probabilidad: 0.78, cluster: "Cardio", recomendaciones: [...]}
    UI->>Usuario: Actualiza tarjetas KPI, gráficos Chart.js y recomendaciones
```

---

## 📁 Estructura del Repositorio

```text
Proyecto-Mineria_Datos/
├── app/                                # Código de la aplicación web
│   ├── main.py                         # Servidor FastAPI y endpoints
│   ├── models/                         # Modelos entrenados (.joblib)
│   ├── static/                         # Estilos CSS y JavaScript
│   └── templates/                      # Plantilla HTML (Bootstrap 5 Dark)
├── data/                               # Dataset del proyecto
│   └── spotify_2015_2025_85k.csv       # 85.000 registros limpios en UTF-8
├── notebook/                           # Cuadernos Google Colab
│   └── Proyecto_Mineria_Datos.ipynb    # Código ejecutable con fases CRISP-DM
├── docs/                               # Documentación y pautas
│   └── Proyecto_MineriaDatos.pdf       # Pauta oficial de la asignatura
├── .gitignore                          # Exclusión de archivos temporales
├── requirements.txt                    # Dependencias Python
├── Procfile                            # Archivo de arranque para Render
└── README.md                           # Documentación central del proyecto
```

---

## 🎯 Resumen de Metas de Éxito de Machine Learning
* **Clasificación (Árbol de Decisión):** Accuracy $\ge 70\%$ con control de `max_depth` para prevenir sobreajuste (*overfitting*).
* **Clustering (K-Means):** Entre 3 y 5 grupos justificados mediante el Método del Codo y Coeficiente de Silueta.
* **Reglas de Asociación (Apriori):** Mínimo 3 reglas de negocio con Soporte $\ge 5\%$, Confianza $\ge 60\%$ y Lift $> 1.2$.
* **Despliegue Web:** Aplicación accesible 24/7 en Render con respuesta menor a 2 segundos y tolerancia a errores de entrada.
