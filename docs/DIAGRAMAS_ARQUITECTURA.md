# Documentación de Arquitectura y Diagramas de Flujo
**Proyecto:** SoundData Analytics — Segmentación de Audiencias y Predicción de Éxito  
**Metodología:** CRISP-DM | **Semana 2: Prototipo y Modelado**

---

## 1. Diagrama de Arquitectura de la Aplicación (Frontend <-> Backend <-> Modelos)

Este diagrama responde formalmente al requerimiento de la **Sección 5.7** y la **Rúbrica de la Semana 2**:

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

## 2. Diagrama de Distribución de Trabajo del Equipo (6 Personas)

Garantiza que cada uno de los 6 integrantes tenga responsabilidades aisladas, entregables claros y commits verificables en GitHub:

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
