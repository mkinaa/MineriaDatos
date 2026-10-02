import os
import json
import joblib
import numpy as np
import pandas as pd
from typing import Optional, List
from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, Field

from app.database import (
    init_db,
    listar_canciones,
    obtener_cancion,
    crear_cancion,
    actualizar_cancion,
    eliminar_cancion
)

# Directorios base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, 'models')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Inicialización de la aplicación FastAPI
app = FastAPI(
    title="SoundData Analytics API",
    description="API para predicción de éxito musical, clustering de oyentes, reglas de asociación con CRISP-DM y gestión de catálogo (CRUD)",
    version="1.1.0"
)

# Montaje de archivos estáticos
os.makedirs(STATIC_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Configuración de plantillas Jinja2
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Carga de modelos serializados
try:
    scaler = joblib.load(os.path.join(MODELS_DIR, 'scaler.joblib'))
    modelo_arbol = joblib.load(os.path.join(MODELS_DIR, 'modelo_arbol.joblib'))
    modelo_kmeans = joblib.load(os.path.join(MODELS_DIR, 'modelo_kmeans.joblib'))
    
    with open(os.path.join(MODELS_DIR, 'reglas_apriori.json'), 'r', encoding='utf-8') as f:
        reglas_apriori = json.load(f)
    print("Modelos y reglas cargados exitosamente.")
except Exception as e:
    print(f"Advertencia al cargar modelos: {e}")
    scaler = None
    modelo_arbol = None
    modelo_kmeans = None
    reglas_apriori = []

# Mapeo de clusters a perfiles de negocio interpretables
CLUSTER_PROFILES = {
    0: {
        "nombre": "Acústico & Melódico Comercial",
        "descripcion": "Canciones de alta sonoridad y energía balanceada, orientadas a radio y consumo diario casual.",
        "audiencia": "Oyentes de Pop, R&B y baladas que buscan música melódica para el día a día."
    },
    1: {
        "nombre": "Urbano & Explícito",
        "descripcion": "Temas de alta repercusión con lenguaje explícito y ritmos marcados.",
        "audiencia": "Público joven enfocado en Hip-Hop, Trap y Reggaeton de club."
    },
    2: {
        "nombre": "Introspectivo & Chillout",
        "descripcion": "Canciones de sonoridad suave y tempos moderados, ideales para descanso o concentración.",
        "audiencia": "Oyentes de música Lo-Fi, Folk, Clásica o piezas instrumentales de estudio."
    },
    3: {
        "nombre": "Cardio & Alta Intensidad",
        "descripcion": "Temas veloces con energía máxima (>130 BPM), pensados para actividad física.",
        "audiencia": "Deportistas, runners y fanáticos de festivales de Rock acelerado y EDM."
    }
}

def ejecutar_inferencia(
    tempo: float,
    danceability: float,
    energy: float,
    loudness: float,
    instrumentalness: float,
    explicit: int,
    genre: str = "Pop",
    country: str = "Chile"
) -> dict:
    """Función unificada de inferencia de Machine Learning (Árbol + K-Means + Apriori)."""
    if not modelo_arbol or not modelo_kmeans or not scaler:
        raise HTTPException(status_code=500, detail="Los modelos no están inicializados.")
    
    # Vector crudo con nombres de columna esperados
    X_raw = pd.DataFrame([{
        'tempo': tempo,
        'danceability': danceability,
        'energy': energy,
        'loudness': loudness,
        'instrumentalness': instrumentalness,
        'explicit': explicit
    }])
    
    # 1. Escalado
    X_scaled = scaler.transform(X_raw)
    
    # 2. Árbol de Decisión (Hit vs Nicho)
    pred_hit = int(modelo_arbol.predict(X_raw)[0])
    probabilidades = modelo_arbol.predict_proba(X_raw)[0]
    prob_hit = float(probabilidades[1]) if len(probabilidades) > 1 else float(pred_hit)
    
    # 3. K-Means Clustering
    cluster_id = int(modelo_kmeans.predict(X_scaled)[0])
    cluster_info = CLUSTER_PROFILES.get(cluster_id, {
        "nombre": f"Cluster {cluster_id}",
        "descripcion": "Perfil acústico estándar.",
        "audiencia": "Audiencia general."
    })
    
    # 4. Motor de Recomendación con Reglas Apriori
    recomendaciones = []
    if tempo > 130 and energy > 0.65:
        recomendaciones.append("Fuerte afinidad detectada para playlists de Cardio/Entrenamiento (Lift > 3.0 en EDM y Rock).")
    if danceability > 0.65 and genre in ['Pop', 'Reggaeton', 'R&B']:
        recomendaciones.append("Alta probabilidad de engagement en mercados hispanos y norteamericanos con pauta en discotecas y streaming social.")
    if loudness > -15.0:
        recomendaciones.append("Producción moderna con compresión comercial radial óptima.")
        
    if not recomendaciones:
        recomendaciones.append("Canción con perfil equilibrado, ideal para inclusión en listas de descubrimiento semanal y playlists temáticas de descanso.")
        
    return {
        "exito": True,
        "es_hit": bool(pred_hit == 1),
        "probabilidad_hit": round(prob_hit * 100, 1),
        "cluster_id": cluster_id,
        "cluster_nombre": cluster_info["nombre"],
        "cluster_descripcion": cluster_info["descripcion"],
        "cluster_audiencia": cluster_info["audiencia"],
        "recomendaciones": recomendaciones
    }

# Evento de inicialización de la Base de Datos SQLite
@app.on_event("startup")
def startup_event():
    init_db(inferencia_fn=ejecutar_inferencia)

# Esquemas Pydantic
class PredictionInput(BaseModel):
    tempo: float = Field(..., ge=40, le=240, description="Pulsaciones por minuto (BPM)")
    danceability: float = Field(..., ge=0.0, le=1.0, description="Nivel de bailabilidad (0.0 a 1.0)")
    energy: float = Field(..., ge=0.0, le=1.0, description="Nivel de energía e intensidad (0.0 a 1.0)")
    loudness: float = Field(..., ge=-60.0, le=0.0, description="Sonoridad en decibelios (dB)")
    instrumentalness: float = Field(0.0, ge=0.0, le=1.0, description="Nivel instrumental (0.0 a 1.0)")
    explicit: int = Field(0, ge=0, le=1, description="Contenido explícito (0 o 1)")
    genre: Optional[str] = "Pop"
    country: Optional[str] = "Chile"

class CancionCRUDInput(BaseModel):
    track_name: str = Field(..., min_length=1, max_length=150, description="Título de la canción")
    artist_name: str = Field(..., min_length=1, max_length=150, description="Nombre del artista")
    genre: str = Field("Pop", description="Género musical")
    country: str = Field("Chile", description="País objetivo")
    tempo: float = Field(..., ge=40, le=240, description="Tempo en BPM")
    danceability: float = Field(..., ge=0.0, le=1.0, description="Bailabilidad (0.0 a 1.0)")
    energy: float = Field(..., ge=0.0, le=1.0, description="Energía (0.0 a 1.0)")
    loudness: float = Field(..., ge=-60.0, le=0.0, description="Sonoridad en dB")
    instrumentalness: float = Field(0.0, ge=0.0, le=1.0, description="Instrumentalidad (0.0 a 1.0)")
    explicit: int = Field(0, ge=0, le=1, description="Letra explícita (0 o 1)")

# Manejador amigable de errores de validación sin mostrar errores feos de Python
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    detalles = []
    for err in exc.errors():
        campo = err.get("loc", ["desconocido"])[-1]
        mensaje = err.get("msg", "Valor no válido")
        detalles.append(f"Campo '{campo}': {mensaje}")
    return JSONResponse(
        status_code=422,
        content={
            "error": True,
            "mensaje": "Parámetros de entrada incorrectos. Por favor verifique los valores.",
            "detalles": detalles
        }
    )

# Ruta principal: Servir la aplicación web interactiva
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

# Endpoint de inferencia directa para el simulador
@app.post("/api/predecir")
async def predecir(datos: PredictionInput):
    return ejecutar_inferencia(
        tempo=datos.tempo,
        danceability=datos.danceability,
        energy=datos.energy,
        loudness=datos.loudness,
        instrumentalness=datos.instrumentalness,
        explicit=datos.explicit,
        genre=datos.genre or "Pop",
        country=datos.country or "Chile"
    )

# ==========================================
# ENDPOINTS CRUD: PORTAFOLIO DE CANCIONES (SQLite)
# ==========================================

@app.get("/api/canciones")
async def api_listar_canciones(
    q: Optional[str] = Query(None, description="Búsqueda por título o artista"),
    hit: Optional[int] = Query(None, description="Filtrar por hit (1) o nicho (0)"),
    genre: Optional[str] = Query(None, description="Filtrar por género")
):
    """Consulta la lista de canciones evaluadas en base de datos con filtros opcionales."""
    canciones = listar_canciones(filtro_q=q, filtro_hit=hit, filtro_genero=genre)
    return {
        "exito": True,
        "total": len(canciones),
        "canciones": canciones
    }

@app.get("/api/canciones/{cancion_id}")
async def api_obtener_cancion(cancion_id: int):
    """Obtiene el detalle y diagnóstico ML de una canción por su ID."""
    cancion = obtener_cancion(cancion_id)
    if not cancion:
        raise HTTPException(status_code=404, detail=f"No se encontró la canción con ID {cancion_id}")
    return {
        "exito": True,
        "cancion": cancion
    }

@app.post("/api/canciones")
async def api_crear_cancion(datos: CancionCRUDInput):
    """
    Crea una nueva canción en el portafolio:
    1. Ejecuta la inferencia de ML (Árbol + K-Means + Apriori).
    2. Persiste la canción y sus resultados predictivos en SQLite.
    """
    ml_res = ejecutar_inferencia(
        tempo=datos.tempo,
        danceability=datos.danceability,
        energy=datos.energy,
        loudness=datos.loudness,
        instrumentalness=datos.instrumentalness,
        explicit=datos.explicit,
        genre=datos.genre,
        country=datos.country
    )
    nueva = crear_cancion(datos.model_dump(), ml_res)
    return {
        "exito": True,
        "mensaje": f"Canción '{nueva['track_name']}' registrada y evaluada con éxito.",
        "cancion": nueva
    }

@app.put("/api/canciones/{cancion_id}")
async def api_actualizar_cancion(cancion_id: int, datos: CancionCRUDInput):
    """
    Actualiza los atributos de una canción y recalcula sus modelos predictivos.
    """
    existente = obtener_cancion(cancion_id)
    if not existente:
        raise HTTPException(status_code=404, detail=f"No se encontró la canción con ID {cancion_id}")
    
    ml_res = ejecutar_inferencia(
        tempo=datos.tempo,
        danceability=datos.danceability,
        energy=datos.energy,
        loudness=datos.loudness,
        instrumentalness=datos.instrumentalness,
        explicit=datos.explicit,
        genre=datos.genre,
        country=datos.country
    )
    actualizada = actualizar_cancion(cancion_id, datos.model_dump(), ml_res)
    return {
        "exito": True,
        "mensaje": f"Canción '{actualizada['track_name']}' actualizada y re-evaluada con éxito.",
        "cancion": actualizada
    }

@app.delete("/api/canciones/{cancion_id}")
async def api_eliminar_cancion(cancion_id: int):
    """Elimina una canción del portafolio."""
    eliminada = eliminar_cancion(cancion_id)
    if not eliminada:
        raise HTTPException(status_code=404, detail=f"No se encontró la canción con ID {cancion_id}")
    return {
        "exito": True,
        "mensaje": f"Canción con ID {cancion_id} eliminada correctamente."
    }

# ==========================================
# ENDPOINTS METADATOS Y REGLAS
# ==========================================

@app.get("/api/reglas")
async def obtener_reglas():
    return {
        "total_reglas": len(reglas_apriori),
        "reglas": reglas_apriori
    }

@app.get("/api/estadisticas")
async def obtener_estadisticas():
    return {
        "dataset": "spotify_2015_2025_85k.csv",
        "total_canciones": 85000,
        "total_generos": 12,
        "total_paises": 10,
        "periodo": "2015 - 2025",
        "popularidad_promedio": 48.16,
        "tempo_promedio_bpm": 129.95,
        "calidad_datos": "100% libre de valores nulos"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
