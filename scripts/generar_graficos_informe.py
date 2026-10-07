import os
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import plot_tree
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

os.makedirs(os.path.join("docs", "img"), exist_ok=True)
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# 1. GRÁFICO DE DISTRIBUCIÓN (FASE 2)
print("Generando distribucion_streams.png...")
df = pd.read_csv(os.path.join("data", "spotify_2015_2025_85k.csv"))

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Subplot 1: Stream count con percentil 75
sns.histplot(df['stream_count'] / 1e6, bins=40, kde=True, ax=axes[0], color='#1DB954')
p75 = df['stream_count'].quantile(0.75) / 1e6
axes[0].axvline(p75, color='#DC2626', linestyle='--', linewidth=2, label=f'Percentil 75 (Corte Éxito: {p75:.1f}M)')
axes[0].set_title("Distribución Asimétrica de Reproducciones (Streams)", fontsize=12, fontweight='bold', pad=10)
axes[0].set_xlabel("Millones de Reproducciones", fontsize=10)
axes[0].set_ylabel("Frecuencia (N° de Canciones)", fontsize=10)
axes[0].legend(frameon=True, facecolor='white', framealpha=0.9)

# Subplot 2: Dispersión Energía vs Bailabilidad por Popularidad
sample_df = df.sample(n=2500, random_state=42)
scatter = axes[1].scatter(sample_df['danceability'], sample_df['energy'], c=sample_df['popularity'], cmap='viridis', alpha=0.6, s=20)
cbar = plt.colorbar(scatter, ax=axes[1])
cbar.set_label("Índice de Popularidad (0-100)", fontsize=10)
axes[1].set_title("Espacio Acústico: Bailabilidad vs. Energía", fontsize=12, fontweight='bold', pad=10)
axes[1].set_xlabel("Bailabilidad (Danceability)", fontsize=10)
axes[1].set_ylabel("Energía (Energy)", fontsize=10)

plt.tight_layout()
fig.savefig(os.path.join("docs", "img", "distribucion_streams.png"), dpi=200)
plt.close(fig)

# 2. MÉTODO DEL CODO Y SILUETA (FASE 4B: K-MEANS)
print("Generando metodo_codo_silueta.png...")
scaler = joblib.load(os.path.join("app", "models", "scaler.joblib"))
features = ['tempo', 'danceability', 'energy', 'loudness', 'instrumentalness', 'explicit']
X_scaled = scaler.transform(df[features].sample(n=10000, random_state=42))

k_valores = list(range(2, 9))
inercia = []
siluetas = []

for k in k_valores:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X_scaled)
    inercia.append(km.inertia_)
    siluetas.append(silhouette_score(X_scaled, labels))

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Inercia (Codo)
axes[0].plot(k_valores, inercia, marker='o', linewidth=2.5, color='#2563EB', markersize=7)
axes[0].axvline(4, color='#DC2626', linestyle='--', linewidth=2, label='K Seleccionado (K=4)')
axes[0].set_title("Método del Codo (Inercia vs K)", fontsize=12, fontweight='bold', pad=10)
axes[0].set_xlabel("Número de Clústeres (K)", fontsize=10)
axes[0].set_ylabel("Suma de Errores al Cuadrado (Inercia)", fontsize=10)
axes[0].legend(frameon=True)

# Silueta
axes[1].plot(k_valores, siluetas, marker='s', linewidth=2.5, color='#16A34A', markersize=7)
axes[1].axvline(4, color='#DC2626', linestyle='--', linewidth=2, label='K Óptimo de Cohesión (K=4)')
axes[1].set_title("Coeficiente de Silueta Promedio vs K", fontsize=12, fontweight='bold', pad=10)
axes[1].set_xlabel("Número de Clústeres (K)", fontsize=10)
axes[1].set_ylabel("Puntuación de Silueta", fontsize=10)
axes[1].legend(frameon=True)

plt.tight_layout()
fig.savefig(os.path.join("docs", "img", "metodo_codo_silueta.png"), dpi=200)
plt.close(fig)

# 3. ÁRBOL DE DECISIÓN GRÁFICO (FASE 4C)
print("Generando arbol_decision_grafico.png...")
arbol = joblib.load(os.path.join("app", "models", "modelo_arbol.joblib"))

fig, ax = plt.subplots(figsize=(18, 9))
plot_tree(
    arbol,
    feature_names=['BPM', 'Bailabilidad', 'Energía', 'Sonoridad', 'Instrumental', 'Explícito'],
    class_names=['Estándar', 'Éxito'],
    filled=True,
    rounded=True,
    fontsize=9,
    ax=ax
)
ax.set_title("Estructura Jerárquica del Árbol de Decisión (Profundidad Máxima = 3)", fontsize=14, fontweight='bold', pad=12)
plt.tight_layout()
fig.savefig(os.path.join("docs", "img", "arbol_decision_grafico.png"), dpi=200)
plt.close(fig)

# 4. MATRIZ DE CONFUSIÓN (FASE 4C / FASE 5)
print("Generando matriz_confusion.png...")
cm = np.array([[8253, 4268], [2881, 1598]])
fig, ax = plt.subplots(figsize=(6.5, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, ax=ax, annot_kws={"size": 13, "weight": "bold"})
ax.set_title("Matriz de Confusión en Prueba (17.000 Canciones)", fontsize=12, fontweight='bold', pad=10)
ax.set_xlabel("Clase Predicha por el Modelo", fontsize=11, fontweight='bold')
ax.set_ylabel("Clase Real del Dataset", fontsize=11, fontweight='bold')
ax.set_xticklabels(['No Éxito (0)', 'Éxito (1)'], fontsize=10)
ax.set_yticklabels(['No Éxito (0)', 'Éxito (1)'], fontsize=10)

plt.tight_layout()
fig.savefig(os.path.join("docs", "img", "matriz_confusion.png"), dpi=200)
plt.close(fig)

# 5. DIAGRAMA DE ARQUITECTURA VISUAL (FASE 5.7)
print("Generando arquitectura_sistema.png...")
fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('off')

# Cajas de arquitectura
cajas = [
    (0.08, 0.5, 0.22, 0.35, "CLIENTE WEB\n(Frontend)\n• HTML5 + Bootstrap 5\n• Chart.js\n• Fetch API Asíncrona", "#E0F2FE", "#0284C7"),
    (0.39, 0.5, 0.22, 0.35, "API REST\n(Backend FastAPI)\n• Servidor Uvicorn\n• Pydantic Validators\n• Rutas CRUD y Predict", "#FEF3C7", "#D97706"),
    (0.70, 0.70, 0.24, 0.26, "MODELOS ML\n(Joblib Serializados)\n• StandardScaler\n• DecisionTree (max_depth=3)\n• K-Means (K=4)\n• Reglas Apriori (JSON)", "#DCFCE7", "#16A34A"),
    (0.70, 0.30, 0.24, 0.26, "PERSISTENCIA\n(Base de Datos SQLite)\n• Tabla 'canciones'\n• Historial y Portafolio\n• Auto-semillado inicial", "#F3E8FF", "#9333EA"),
]

from matplotlib.patches import FancyBboxPatch

for x, y, w, h, texto, bg, border in cajas:
    rect = FancyBboxPatch((x, y - h/2), w, h, boxstyle="round,pad=0.02,rounding_size=0.03", facecolor=bg, edgecolor=border, linewidth=2)
    ax.add_patch(rect)
    ax.text(x + w/2, y, texto, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1E293B')

# Flechas de conexión
ax.annotate("", xy=(0.39, 0.53), xytext=(0.30, 0.53), arrowprops=dict(arrowstyle="->", lw=2.5, color="#0F172A"))
ax.text(0.345, 0.56, "HTTP JSON", ha='center', fontsize=8.5, fontweight='bold')

ax.annotate("", xy=(0.30, 0.47), xytext=(0.39, 0.47), arrowprops=dict(arrowstyle="->", lw=2.5, color="#0F172A"))
ax.text(0.345, 0.42, "200 OK", ha='center', fontsize=8.5, fontweight='bold')

ax.annotate("", xy=(0.70, 0.70), xytext=(0.61, 0.58), arrowprops=dict(arrowstyle="->", lw=2, color="#16A34A"))
ax.annotate("", xy=(0.61, 0.52), xytext=(0.70, 0.65), arrowprops=dict(arrowstyle="->", lw=2, color="#16A34A"))

ax.annotate("", xy=(0.70, 0.32), xytext=(0.61, 0.45), arrowprops=dict(arrowstyle="->", lw=2, color="#9333EA"))
ax.annotate("", xy=(0.61, 0.40), xytext=(0.70, 0.28), arrowprops=dict(arrowstyle="->", lw=2, color="#9333EA"))

ax.set_title("Diagrama de Arquitectura de la Plataforma SoundData Analytics", fontsize=13, fontweight='bold', pad=15)
plt.tight_layout()
fig.savefig(os.path.join("docs", "img", "arquitectura_sistema.png"), dpi=200)
plt.close(fig)

print("¡Todas las imágenes generadas con éxito en docs/img/!")
