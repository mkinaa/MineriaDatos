import os
import json
import joblib
import pandas as pd
from app.main import ejecutar_inferencia, CLUSTER_PROFILES

MODELS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'app', 'models')

def test_existencia_artefactos_modelos():
    assert os.path.exists(os.path.join(MODELS_DIR, 'scaler.joblib'))
    assert os.path.exists(os.path.join(MODELS_DIR, 'modelo_arbol.joblib'))
    assert os.path.exists(os.path.join(MODELS_DIR, 'modelo_kmeans.joblib'))
    assert os.path.exists(os.path.join(MODELS_DIR, 'reglas_apriori.json'))

def test_carga_scaler():
    scaler = joblib.load(os.path.join(MODELS_DIR, 'scaler.joblib'))
    df = pd.DataFrame([{
        'tempo': 120.0,
        'danceability': 0.7,
        'energy': 0.8,
        'loudness': -6.0,
        'instrumentalness': 0.05,
        'explicit': 0
    }])
    transformed = scaler.transform(df)
    assert transformed.shape == (1, 6)

def test_modelo_arbol_decision():
    modelo_arbol = joblib.load(os.path.join(MODELS_DIR, 'modelo_arbol.joblib'))
    df = pd.DataFrame([{
        'tempo': 128.0,
        'danceability': 0.8,
        'energy': 0.85,
        'loudness': -5.0,
        'instrumentalness': 0.0,
        'explicit': 1
    }])
    pred = modelo_arbol.predict(df)
    probs = modelo_arbol.predict_proba(df)
    assert pred[0] in [0, 1]
    assert 0.0 <= probs[0][1] <= 1.0

def test_modelo_kmeans():
    scaler = joblib.load(os.path.join(MODELS_DIR, 'scaler.joblib'))
    modelo_kmeans = joblib.load(os.path.join(MODELS_DIR, 'modelo_kmeans.joblib'))
    df = pd.DataFrame([{
        'tempo': 135.0,
        'danceability': 0.65,
        'energy': 0.9,
        'loudness': -4.0,
        'instrumentalness': 0.1,
        'explicit': 0
    }])
    scaled = scaler.transform(df)
    cluster = modelo_kmeans.predict(scaled)[0]
    assert cluster in [0, 1, 2, 3]
    assert cluster in CLUSTER_PROFILES

def test_reglas_apriori_json():
    with open(os.path.join(MODELS_DIR, 'reglas_apriori.json'), 'r', encoding='utf-8') as f:
        reglas = json.load(f)
    assert isinstance(reglas, list)
    assert len(reglas) >= 3
    for r in reglas:
        assert 'antecedentes' in r
        assert 'consecuentes' in r
        assert 'lift' in r
        assert r['lift'] >= 1.2

def test_ejecutar_inferencia_unificada():
    resultado = ejecutar_inferencia(
        tempo=125.0,
        danceability=0.75,
        energy=0.8,
        loudness=-5.5,
        instrumentalness=0.02,
        explicit=0,
        genre='Pop',
        country='Chile'
    )
    assert resultado['exito'] is True
    assert isinstance(resultado['es_hit'], bool)
    assert 0.0 <= resultado['probabilidad_hit'] <= 100.0
    assert resultado['cluster_id'] in [0, 1, 2, 3]
    assert len(resultado['recomendaciones']) > 0
