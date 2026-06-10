# Analyse du paysage mondial des centrales électriques avec NumPy, Pandas et Matplotlib

## Introduction

L'objectif de cette étude est d'explorer la base de données mondiale des centrales électriques (*Global Power Plant Database*) afin de mieux comprendre la répartition géographique des installations, les sources d'énergie utilisées et les caractéristiques de production associées.

Pour réaliser cette analyse, trois bibliothèques fondamentales de l'écosystème Python ont été utilisées :

* **Pandas** pour le chargement, le nettoyage et la manipulation des données.
* **NumPy** pour les calculs numériques, les statistiques et les opérations matricielles.
* **Matplotlib** (associé à Seaborn) pour la visualisation des résultats.

L'ensemble de données contient près de 35 000 centrales électriques réparties dans plus de 160 pays.

---

# 1. Importation et nettoyage des données

## Chargement du dataset

Les données ont été importées à l'aide de Pandas :

```python
import pandas as pd

df = pd.read_csv("global_power_plant_database.csv")
```

## Traitement des valeurs manquantes

Une analyse des valeurs manquantes a montré que certaines colonnes relatives à la production annuelle et aux combustibles secondaires étaient fortement incomplètes.

Les principales actions réalisées ont été :

* Identification des valeurs nulles avec `isnull().sum()`.
* Conversion des colonnes numériques à l'aide de `pd.to_numeric()`.
* Suppression des doublons éventuels.
* Conservation des valeurs manquantes dans certaines colonnes non critiques afin d'éviter une perte excessive d'information.

---

# 2. Analyse exploratoire des données

## Structure générale

Le dataset contient :

* 34 936 centrales électriques
* 36 variables
* Des informations sur :

  * la localisation,
  * la capacité installée,
  * le combustible principal,
  * l'année de mise en service,
  * la production annuelle.

## Répartition par type de combustible

L'analyse révèle que les combustibles les plus représentés sont :

| Combustible | Nombre de centrales |
| ----------- | ------------------- |
| Solar       | 10 665              |
| Hydro       | 7 156               |
| Wind        | 5 344               |
| Gas         | 3 998               |
| Coal        | 2 330               |
| Oil         | 2 320               |

Cette distribution montre la forte présence des énergies renouvelables dans la base de données mondiale.

## Répartition géographique

Les pays comptant le plus grand nombre de centrales sont :

| Pays        | Nombre |
| ----------- | ------ |
| États-Unis  | 9 833  |
| Chine       | 4 235  |
| Royaume-Uni | 2 751  |
| Brésil      | 2 360  |
| France      | 2 155  |

Les États-Unis représentent à eux seuls près de 28 % des installations recensées.

---

# 3. Analyse statistique avec NumPy

Afin d'étudier la capacité des centrales selon leur source d'énergie, plusieurs indicateurs statistiques ont été calculés :

```python
np.mean()
np.median()
np.std()
```

## Capacité moyenne par combustible

| Combustible | Capacité moyenne (MW) |
| ----------- | --------------------- |
| Nuclear     | 2091.86               |
| Coal        | 843.58                |
| Gas         | 373.45                |
| Hydro       | 147.17                |
| Wind        | 49.22                 |
| Solar       | 17.66                 |

Les centrales nucléaires possèdent de loin la capacité moyenne la plus élevée.

Les centrales solaires et éoliennes sont beaucoup plus nombreuses mais généralement de plus petite taille.

---

# 4. Test d'hypothèse

Afin de vérifier si les capacités diffèrent réellement selon le combustible utilisé, une ANOVA à un facteur a été réalisée.

## Hypothèses

H₀ : toutes les capacités moyennes sont identiques.

H₁ : au moins une moyenne est différente.

```python
from scipy import stats

stats.f_oneway(*groupes)
```

## Résultat

* Statistique F : 1128.48
* p-value : < 0.001

## Conclusion

L'hypothèse nulle est rejetée.

Il existe une différence statistiquement significative entre les capacités moyennes des centrales selon leur type de combustible.

---

# 5. Analyse temporelle

L'année de mise en service des centrales a permis d'étudier l'évolution des technologies de production électrique.

## Évolution du nombre de centrales

Les données montrent une accélération importante des nouvelles installations à partir des années 2000.

Cette croissance est principalement portée par :

* le solaire,
* l'éolien,
* certaines installations hydroélectriques.

## Évolution des combustibles

Les centrales au charbon dominent historiquement les premières décennies.

À partir des années 2000, on observe :

* une forte progression du solaire ;
* une augmentation rapide de l'éolien ;
* une diversification progressive du mix énergétique mondial.

Cette évolution reflète les politiques de transition énergétique observées dans de nombreux pays.

---

# 6. Visualisations réalisées

Plusieurs graphiques ont été produits :

### Diagramme des combustibles

Permet d'identifier les principales sources d'énergie utilisées dans le monde.

### Répartition des pays

Montre les pays disposant du plus grand nombre d'installations.

### Courbe temporelle

Met en évidence la croissance des nouvelles centrales au cours du temps.

### Carte géographique

À partir des coordonnées GPS (latitude/longitude), les centrales ont été projetées afin d'observer leur répartition mondiale.

Les zones les plus denses sont :

* l'Amérique du Nord,
* l'Europe,
* l'Asie de l'Est.

---

# 7. Opérations matricielles et analyse avancée

NumPy a également été utilisé pour effectuer des opérations matricielles sur les variables quantitatives.

## Matrice de corrélation

Une matrice de corrélation a été construite à partir de :

* capacité (MW),
* latitude,
* longitude,
* année de mise en service.

```python
corr = np.corrcoef(matrix.T)
```

Cette matrice permet d'identifier les relations éventuelles entre les variables.

## Valeurs propres et vecteurs propres

Les valeurs propres et vecteurs propres ont été calculés avec :

```python
np.linalg.eig()
```

Ces outils sont particulièrement utiles pour :

* l'Analyse en Composantes Principales (ACP),
* la réduction de dimension,
* l'identification des facteurs expliquant le plus de variance dans les données.

Dans ce contexte, ils permettent de résumer efficacement les caractéristiques des centrales électriques mondiales.

---

# 8. Intégration de NumPy, Pandas et Matplotlib

Cette étude illustre parfaitement la complémentarité de ces trois bibliothèques.

## Pandas

Utilisé pour :

* charger les données ;
* nettoyer les colonnes ;
* regrouper les observations ;
* produire les statistiques descriptives.

## NumPy

Utilisé pour :

* les calculs statistiques ;
* les filtres complexes ;
* les opérations matricielles ;
* l'analyse de corrélation ;
* les valeurs propres et vecteurs propres.

## Matplotlib / Seaborn

Utilisés pour :

* les graphiques de distribution ;
* les diagrammes en barres ;
* les courbes temporelles ;
* les représentations géographiques.

---

# Conclusion

Cette analyse met en évidence plusieurs tendances importantes du secteur énergétique mondial.

Les principales observations sont :

* Les États-Unis dominent largement le nombre de centrales répertoriées.
* Les énergies renouvelables (solaire, hydroélectricité et éolien) représentent désormais la majorité des installations.
* Les centrales nucléaires possèdent les capacités de production les plus élevées.
* Les capacités varient significativement selon le combustible utilisé.
* Le développement des énergies renouvelables s'est fortement accéléré depuis le début du XXIᵉ siècle.

L'utilisation combinée de Pandas, NumPy et Matplotlib a permis de transformer un vaste ensemble de données en informations exploitables et de mieux comprendre l'évolution du paysage mondial de la production électrique.
