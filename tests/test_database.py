from app.database import (
    init_db,
    crear_cancion,
    obtener_cancion,
    listar_canciones,
    actualizar_cancion,
    eliminar_cancion
)

def test_inicializacion_base_datos():
    init_db()
    canciones = listar_canciones()
    assert isinstance(canciones, list)
    assert len(canciones) >= 1

def test_creacion_y_lectura_cancion():
    datos = {
        "track_name": "Test Song Unitario",
        "artist_name": "Artista Unitario",
        "genre": "Rock",
        "country": "Chile",
        "tempo": 120.0,
        "danceability": 0.65,
        "energy": 0.70,
        "loudness": -7.0,
        "instrumentalness": 0.05,
        "explicit": 0
    }
    ml_res = {
        "es_hit": True,
        "probabilidad_hit": 85.5,
        "cluster_id": 0,
        "cluster_nombre": "Acústico & Melódico Comercial",
        "recomendaciones": ["Afinidad de prueba"]
    }
    nueva = crear_cancion(datos, ml_res)
    assert nueva is not None
    assert nueva["id"] > 0
    assert nueva["track_name"] == "Test Song Unitario"
    assert nueva["es_hit"] is True

    obtenida = obtener_cancion(nueva["id"])
    assert obtenida is not None
    assert obtenida["id"] == nueva["id"]
    assert obtenida["artist_name"] == "Artista Unitario"

    eliminar_cancion(nueva["id"])

def test_listar_con_filtros():
    canciones_todas = listar_canciones()
    canciones_pop = listar_canciones(filtro_genero="Pop")
    canciones_busqueda = listar_canciones(filtro_q="Noches")
    assert isinstance(canciones_todas, list)
    assert isinstance(canciones_pop, list)
    assert isinstance(canciones_busqueda, list)

def test_actualizacion_cancion():
    datos = {
        "track_name": "Cancion Para Actualizar",
        "artist_name": "Artista Mod",
        "genre": "Pop",
        "country": "Chile",
        "tempo": 110.0,
        "danceability": 0.50,
        "energy": 0.60,
        "loudness": -8.0,
        "instrumentalness": 0.0,
        "explicit": 0
    }
    ml_res = {
        "es_hit": False,
        "probabilidad_hit": 30.0,
        "cluster_id": 2,
        "cluster_nombre": "Introspectivo & Chillout",
        "recomendaciones": ["Recomendación 1"]
    }
    creada = crear_cancion(datos, ml_res)
    assert creada is not None

    datos_modificados = dict(datos)
    datos_modificados["track_name"] = "Cancion Actualizada Con Exito"
    datos_modificados["tempo"] = 130.0
    ml_res_mod = dict(ml_res)
    ml_res_mod["probabilidad_hit"] = 75.0
    ml_res_mod["es_hit"] = True

    actualizada = actualizar_cancion(creada["id"], datos_modificados, ml_res_mod)
    assert actualizada is not None
    assert actualizada["track_name"] == "Cancion Actualizada Con Exito"
    assert actualizada["tempo"] == 130.0
    assert actualizada["es_hit"] is True

    eliminar_cancion(creada["id"])

def test_eliminar_cancion():
    datos = {
        "track_name": "Cancion Temporal",
        "artist_name": "Artista Temporal",
        "genre": "Pop",
        "country": "Chile",
        "tempo": 120.0,
        "danceability": 0.5,
        "energy": 0.5,
        "loudness": -6.0,
        "instrumentalness": 0.0,
        "explicit": 0
    }
    ml_res = {
        "es_hit": False,
        "probabilidad_hit": 40.0,
        "cluster_id": 0,
        "cluster_nombre": "Acústico & Melódico",
        "recomendaciones": []
    }
    creada = crear_cancion(datos, ml_res)
    eliminada = eliminar_cancion(creada["id"])
    assert eliminada is True

    buscada = obtener_cancion(creada["id"])
    assert buscada is None
