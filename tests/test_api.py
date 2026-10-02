from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_endpoint_raiz():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "SoundData" in response.text

def test_endpoint_estadisticas():
    response = client.get("/api/estadisticas")
    assert response.status_code == 200
    data = response.json()
    assert data["total_canciones"] == 85000
    assert "periodo" in data

def test_endpoint_reglas():
    response = client.get("/api/reglas")
    assert response.status_code == 200
    data = response.json()
    assert "total_reglas" in data
    assert data["total_reglas"] > 0
    assert isinstance(data["reglas"], list)

def test_endpoint_predecir_valido():
    payload = {
        "tempo": 128.0,
        "danceability": 0.70,
        "energy": 0.85,
        "loudness": -5.0,
        "instrumentalness": 0.02,
        "explicit": 1,
        "genre": "Pop",
        "country": "Chile"
    }
    response = client.post("/api/predecir", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["exito"] is True
    assert isinstance(data["es_hit"], bool)
    assert isinstance(data["probabilidad_hit"], (int, float))
    assert data["cluster_id"] in [0, 1, 2, 3]
    assert len(data["recomendaciones"]) > 0

def test_endpoint_predecir_invalido_amigable():
    payload = {
        "tempo": -10.0,
        "danceability": 2.5,
        "energy": 0.5,
        "loudness": 10.0,
        "instrumentalness": 0.0,
        "explicit": 5
    }
    response = client.post("/api/predecir", json=payload)
    assert response.status_code == 422
    data = response.json()
    assert data["error"] is True
    assert "mensaje" in data
    assert isinstance(data["detalles"], list)

def test_endpoints_crud_flujo_completo():
    payload_creacion = {
        "track_name": "API Test Hit",
        "artist_name": "Artista API",
        "genre": "Reggaetón",
        "country": "Chile",
        "tempo": 95.0,
        "danceability": 0.85,
        "energy": 0.80,
        "loudness": -4.5,
        "instrumentalness": 0.0,
        "explicit": 1
    }
    res_crear = client.post("/api/canciones", json=payload_creacion)
    assert res_crear.status_code == 200
    data_crear = res_crear.json()
    assert data_crear["exito"] is True
    cancion_id = data_crear["cancion"]["id"]
    assert cancion_id > 0

    res_obtener = client.get(f"/api/canciones/{cancion_id}")
    assert res_obtener.status_code == 200
    assert res_obtener.json()["cancion"]["track_name"] == "API Test Hit"

    payload_actualizacion = dict(payload_creacion)
    payload_actualizacion["track_name"] = "API Test Hit Modificado"
    payload_actualizacion["tempo"] = 100.0
    res_actualizar = client.put(f"/api/canciones/{cancion_id}", json=payload_actualizacion)
    assert res_actualizar.status_code == 200
    assert res_actualizar.json()["cancion"]["track_name"] == "API Test Hit Modificado"

    res_listar = client.get("/api/canciones?q=API Test Hit")
    assert res_listar.status_code == 200
    assert res_listar.json()["total"] >= 1

    res_eliminar = client.delete(f"/api/canciones/{cancion_id}")
    assert res_eliminar.status_code == 200
    assert res_eliminar.json()["exito"] is True

    res_no_encontrado = client.get(f"/api/canciones/{cancion_id}")
    assert res_no_encontrado.status_code == 404
