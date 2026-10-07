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

# Configuración oscura idéntica a la especificación de la sección 7.3
DARK_CARD = "#181818"
plt.rcParams.update({
    "figure.facecolor": DARK_CARD,
    "axes.facecolor": DARK_CARD,
    "savefig.facecolor": DARK_CARD,
    "axes.edgecolor": "#2A2A2A",
    "axes.labelcolor": "#B3B3B3",
    "text.color": "#FFFFFF",
    "xtick.color": "#B3B3B3",
    "ytick.color": "#B3B3B3",
    "grid.color": "#2A2A2A",
    "font.size": 14,
    "axes.titlesize": 16,
    "axes.titleweight": "bold",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "font.sans-serif": ["Segoe UI", "Calibri", "Arial", "sans-serif"]
})

# 1. Gráfico de distribución de streams estilo oscuro (cola verde destacada)
print("Generando distribucion_streams_dark.png...")
df = pd.read_csv(os.path.join("data", "spotify_2015_2025_85k.csv"))

fig, ax = plt.subplots(figsize=(7, 5))
streams_m = df['stream_count'] / 1e6
p75 = streams_m.quantile(0.75)

n, bins, patches = ax.hist(streams_m, bins=35, color='#333333', edgecolor='#181818')
# Pintar en verde la cola derecha (éxito >= p75)
for patch, bin_left in zip(patches, bins[:-1]):
    if bin_left >= p75:
        patch.set_facecolor('#1DB954')

ax.axvline(p75, color='#FFFFFF', linestyle='--', linewidth=2, label=f'Corte Éxito (85,2 M)')
ax.set_title("25% de las canciones concentra el 68% de streams", pad=12)
ax.set_xlabel("Millones de Reproducciones")
ax.set_ylabel("N° de Canciones")
ax.legend(facecolor='#222222', edgecolor='#333333', labelcolor='#FFFFFF')
plt.tight_layout()
fig.savefig(os.path.join("docs", "img", "distribucion_streams_dark.png"), dpi=200, bbox_inches="tight")
plt.close(fig)

# 2. Codo y Silueta estilo oscuro
print("Generando metodo_codo_silueta_dark.png...")
scaler = joblib.load(os.path.join("app", "models", "scaler.joblib"))
features = ['tempo', 'danceability', 'energy', 'loudness', 'instrumentalness', 'explicit']
X_scaled = scaler.transform(df[features].sample(n=8000, random_state=42))

k_valores = list(range(2, 8))
inercia = []
siluetas = []
for k in k_valores:
    km = KMeans(n_clusters=k, random_state=42, n_init=5)
    labels = km.fit_predict(X_scaled)
    inercia.append(km.inertia_)
    siluetas.append(silhouette_score(X_scaled, labels))

fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))

axes[0].plot(k_valores, inercia, marker='o', linewidth=2.5, color='#3B82F6', markersize=8)
axes[0].axvline(4, color='#1DB954', linestyle='--', linewidth=2.5, label='K = 4 (Punto Óptimo)')
axes[0].set_title("Método del Codo (Inercia)")
axes[0].set_xlabel("N° de Clústeres (K)")
axes[0].set_ylabel("Inercia")
axes[0].legend(facecolor='#222222', edgecolor='#333333', labelcolor='#FFFFFF')

axes[1].plot(k_valores, siluetas, marker='s', linewidth=2.5, color='#1DB954', markersize=8)
axes[1].axvline(4, color='#1DB954', linestyle='--', linewidth=2.5, label='K = 4 (Silueta ≈ 0,38)')
axes[1].set_title("Coeficiente de Silueta")
axes[1].set_xlabel("N° de Clústeres (K)")
axes[1].set_ylabel("Puntaje de Silueta")
axes[1].legend(facecolor='#222222', edgecolor='#333333', labelcolor='#FFFFFF')

plt.tight_layout()
fig.savefig(os.path.join("docs", "img", "metodo_codo_silueta_dark.png"), dpi=200, bbox_inches="tight")
plt.close(fig)

# 3. Árbol de decisión gráfico estilo oscuro
print("Generando arbol_decision_grafico_dark.png...")
arbol = joblib.load(os.path.join("app", "models", "modelo_arbol.joblib"))

fig, ax = plt.subplots(figsize=(16, 7.5))
fig.patch.set_facecolor(DARK_CARD)
ax.set_facecolor(DARK_CARD)

plot_tree(
    arbol,
    feature_names=['BPM', 'Bailabilidad', 'Energía', 'Sonoridad', 'Instrumental', 'Explícito'],
    class_names=['Estándar', 'Éxito'],
    filled=True,
    rounded=True,
    fontsize=10,
    ax=ax
)
ax.set_title("Árbol de Decisión: 3 Niveles de Preguntas (8 Caminos)", color="#FFFFFF", fontsize=16, fontweight='bold', pad=15)
plt.tight_layout()
fig.savefig(os.path.join("docs", "img", "arbol_decision_grafico_dark.png"), dpi=200, bbox_inches="tight")
plt.close(fig)

# 4. Matriz de confusión oscura
print("Generando matriz_confusion_dark.png...")
cm = np.array([[8253, 4268], [2881, 1598]])
fig, ax = plt.subplots(figsize=(6, 4.5))

sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', cbar=False, ax=ax,
            annot_kws={"size": 14, "weight": "bold", "color": "#FFFFFF"})

ax.set_title("Matriz de Confusión (17.000 Canciones)", color="#FFFFFF", pad=12)
ax.set_xlabel("Predicción del Modelo", color="#B3B3B3", fontweight="bold")
ax.set_ylabel("Realidad del Dataset", color="#B3B3B3", fontweight="bold")
ax.set_xticklabels(['No Éxito (0)', 'Éxito (1)'], color="#FFFFFF")
ax.set_yticklabels(['No Éxito (0)', 'Éxito (1)'], color="#FFFFFF")
plt.tight_layout()
fig.savefig(os.path.join("docs", "img", "matriz_confusion_dark.png"), dpi=200, bbox_inches="tight")
plt.close(fig)

print("¡Gráficos oscuros generados con éxito!")
