import os
import sqlite3
import json
from datetime import datetime
from typing import List, Optional, Dict, Any

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'sounddata.db')

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(inferencia_fn=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS canciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        track_name TEXT NOT NULL,
        artist_name TEXT NOT NULL,
        genre TEXT NOT NULL,
        country TEXT NOT NULL,
        tempo REAL NOT NULL,
        danceability REAL NOT NULL,
        energy REAL NOT NULL,
        loudness REAL NOT NULL,
        instrumentalness REAL NOT NULL,
        explicit INTEGER NOT NULL DEFAULT 0,
        es_hit INTEGER NOT NULL DEFAULT 0,
        probabilidad_hit REAL NOT NULL DEFAULT 0.0,
        cluster_id INTEGER NOT NULL DEFAULT 0,
        cluster_nombre TEXT NOT NULL,
        recomendaciones TEXT NOT NULL,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    );
    """)
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM canciones;")
    total = cursor.fetchone()[0]

    if total == 0 and inferencia_fn:
        semillas = [
            {
                "track_name": "Noches de Verano",
                "artist_name": "Valentina Paz",
                "genre": "Pop",
                "country": "Chile",
                "tempo": 124.0,
                "danceability": 0.76,
                "energy": 0.81,
                "loudness": -5.2,
                "instrumentalness": 0.01,
                "explicit": 0
            },
            {
                "track_name": "Perreo 56",
                "artist_name": "El Jordan & FlowCL",
                "genre": "Reggaetón",
                "country": "Chile",
                "tempo": 98.0,
                "danceability": 0.88,
                "energy": 0.84,
                "loudness": -4.1,
                "instrumentalness": 0.0,
                "explicit": 1
            },
            {
                "track_name": "Niebla en los Cerros",
                "artist_name": "Cuarteto Cordillera",
                "genre": "Folk",
                "country": "Chile",
                "tempo": 105.0,
                "danceability": 0.42,
                "energy": 0.35,
                "loudness": -15.4,
                "instrumentalness": 0.72,
                "explicit": 0
            },
            {
                "track_name": "Hyperdrive Overload",
                "artist_name": "CyberPulse",
                "genre": "EDM",
                "country": "Estados Unidos",
                "tempo": 136.0,
                "danceability": 0.69,
                "energy": 0.94,
                "loudness": -3.8,
                "instrumentalness": 0.18,
                "explicit": 0
            }
        ]

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for s in semillas:
            ml_res = inferencia_fn(
                tempo=s["tempo"],
                danceability=s["danceability"],
                energy=s["energy"],
                loudness=s["loudness"],
                instrumentalness=s["instrumentalness"],
                explicit=s["explicit"],
                genre=s["genre"],
                country=s["country"]
            )
            cursor.execute("""
            INSERT INTO canciones (
                track_name, artist_name, genre, country,
                tempo, danceability, energy, loudness, instrumentalness, explicit,
                es_hit, probabilidad_hit, cluster_id, cluster_nombre, recomendaciones,
                created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, (
                s["track_name"], s["artist_name"], s["genre"], s["country"],
                s["tempo"], s["danceability"], s["energy"], s["loudness"], s["instrumentalness"], s["explicit"],
                1 if ml_res["es_hit"] else 0, ml_res["probabilidad_hit"], ml_res["cluster_id"], ml_res["cluster_nombre"],
                json.dumps(ml_res["recomendaciones"], ensure_ascii=False),
                now, now
            ))
        conn.commit()

    conn.close()

def listar_canciones(
    filtro_q: Optional[str] = None,
    filtro_hit: Optional[int] = None,
    filtro_genero: Optional[str] = None
) -> List[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM canciones WHERE 1=1"
    params = []

    if filtro_q:
        query += " AND (track_name LIKE ? OR artist_name LIKE ?)"
        term = f"%{filtro_q.strip()}%"
        params.extend([term, term])

    if filtro_hit is not None:
        query += " AND es_hit = ?"
        params.append(filtro_hit)

    if filtro_genero and filtro_genero.strip() != "":
        query += " AND genre = ?"
        params.append(filtro_genero.strip())

    query += " ORDER BY id DESC;"
    cursor.execute(query, params)
    rows = cursor.fetchall()

    resultado = []
    for r in rows:
        d = dict(r)
        try:
            d["recomendaciones"] = json.loads(d["recomendaciones"])
        except Exception:
            d["recomendaciones"] = []
        d["es_hit"] = bool(d["es_hit"] == 1)
        resultado.append(d)

    conn.close()
    return resultado

def obtener_cancion(cancion_id: int) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM canciones WHERE id = ?;", (cancion_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return None
    d = dict(row)
    try:
        d["recomendaciones"] = json.loads(d["recomendaciones"])
    except Exception:
        d["recomendaciones"] = []
    d["es_hit"] = bool(d["es_hit"] == 1)
    return d

def crear_cancion(datos: Dict[str, Any], ml_res: Dict[str, Any]) -> Dict[str, Any]:
    conn = get_connection()
    cursor = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO canciones (
        track_name, artist_name, genre, country,
        tempo, danceability, energy, loudness, instrumentalness, explicit,
        es_hit, probabilidad_hit, cluster_id, cluster_nombre, recomendaciones,
        created_at, updated_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, (
        datos["track_name"], datos["artist_name"], datos["genre"], datos["country"],
        datos["tempo"], datos["danceability"], datos["energy"], datos["loudness"], datos["instrumentalness"], datos["explicit"],
        1 if ml_res["es_hit"] else 0, ml_res["probabilidad_hit"], ml_res["cluster_id"], ml_res["cluster_nombre"],
        json.dumps(ml_res["recomendaciones"], ensure_ascii=False),
        now, now
    ))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return obtener_cancion(new_id)

def actualizar_cancion(cancion_id: int, datos: Dict[str, Any], ml_res: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    UPDATE canciones SET
        track_name = ?, artist_name = ?, genre = ?, country = ?,
        tempo = ?, danceability = ?, energy = ?, loudness = ?, instrumentalness = ?, explicit = ?,
        es_hit = ?, probabilidad_hit = ?, cluster_id = ?, cluster_nombre = ?, recomendaciones = ?,
        updated_at = ?
    WHERE id = ?;
    """, (
        datos["track_name"], datos["artist_name"], datos["genre"], datos["country"],
        datos["tempo"], datos["danceability"], datos["energy"], datos["loudness"], datos["instrumentalness"], datos["explicit"],
        1 if ml_res["es_hit"] else 0, ml_res["probabilidad_hit"], ml_res["cluster_id"], ml_res["cluster_nombre"],
        json.dumps(ml_res["recomendaciones"], ensure_ascii=False),
        now, cancion_id
    ))
    conn.commit()
    conn.close()

    return obtener_cancion(cancion_id)

def eliminar_cancion(cancion_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM canciones WHERE id = ?;", (cancion_id,))
    conn.commit()
    eliminados = cursor.rowcount
    conn.close()
    return eliminados > 0
