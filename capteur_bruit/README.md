# 🎙️ Station de Surveillance Acoustique avec Arduino

> Projet académique — Ingénierie des Réseaux et Radiocommunications  
> **Étudiant :** Njimongba Fochivé Mama Abdourahim  
> **Encadrant :** Dr Nzebop  
> **Établissement :** Sup'PTIC

---

## 📋 Description

Ce projet implémente une **station de surveillance acoustique** capable de détecter, mesurer et analyser en temps réel le bruit généré par une machine. Il illustre l'intégration de concepts clés en systèmes embarqués : acquisition de signal par capteur, traitement sur microcontrôleur, communication série et visualisation informatique.

Le système génère automatiquement une **alerte** lorsque le niveau sonore dépasse un seuil prédéfini, ce qui le rend adapté à une supervision industrielle simplifiée.

---

## 🧰 Matériel requis

| Composant | Rôle |
|-----------|------|
| Arduino UNO | Microcontrôleur central |
| Capteur de son (ex. KY-038) | Acquisition du signal acoustique |
| Écran LCD 16×2 + module I2C | Affichage local en temps réel |
| Breadboard + câbles Dupont | Montage du circuit |
| PC avec port USB | Analyse, visualisation et alertes |

---

## 🗂️ Structure du projet

```
surveillance-acoustique/
│
├── arduino/
│   └── surveillance_acoustique.ino   # Code principal Arduino
│
├── python/
│   └── monitoring_bruit.py           # Script de supervision PC
│
├── docs/
│   ├── rapport.pdf                   # Rapport de projet (PDF)
│   └── rapport.docx                  # Rapport de projet (Word)
│
├── schema/
│   └── branchement.png               # Schéma de câblage
│
└── README.md
```

---

## 🔌 Schéma de branchement

```
Arduino UNO
│
├── 5V  ──────────────── Rail + (breadboard)
├── GND ──────────────── Rail − (breadboard)
│
├── A0  ──────────────── Capteur de son (AO)
├── A4  ──────────────── LCD I2C (SDA)
└── A5  ──────────────── LCD I2C (SCL)

Rail + ──── VCC (Capteur) / VCC (LCD)
Rail − ──── GND (Capteur) / GND (LCD)
```

---

## ⚙️ Installation et utilisation

### 1. Côté Arduino

1. Ouvrir `arduino/surveillance_acoustique.ino` dans l'**IDE Arduino**
2. Installer la bibliothèque LCD I2C si nécessaire :
   - `Sketch` → `Include Library` → `Manage Libraries` → rechercher `LiquidCrystal I2C`
3. Sélectionner la carte `Arduino UNO` et le bon port COM
4. Téléverser le code

### 2. Côté Python

**Prérequis :**

```bash
pip install pyserial matplotlib
```

**Lancement :**

```bash
python python/monitoring_bruit.py
```

> ⚠️ Modifier la variable `PORT` dans le script selon votre configuration (`COM3` sur Windows, `/dev/ttyUSB0` ou `/dev/ttyACM0` sur Linux/macOS).

---

## 🚀 Fonctionnalités

- 📡 **Acquisition** — lecture analogique du capteur de son via la broche A0
- 🖥️ **Affichage LCD** — valeur brute affichée en temps réel sur l'écran local
- 📊 **Graphique dynamique** — visualisation du signal en temps réel sur PC avec Matplotlib
- 📈 **Moyenne glissante** — filtrage des fluctuations pour observer les tendances
- 🚨 **Alerte de seuil** — notification immédiate en cas de dépassement du niveau sonore configuré

---

## 📊 Résultats des tests

| Scénario | Comportement observé | Alerte |
|----------|----------------------|--------|
| Silence | Valeurs stables, faible amplitude | ✅ Non déclenchée |
| Bruit modéré | Augmentation visible sur LCD et graphique | ✅ Non déclenchée |
| Bruit élevé | Dépassement du seuil | 🚨 Déclenchée |

---

## 🔧 Paramètres configurables

Dans `python/monitoring_bruit.py` :

```python
PORT     = "COM3"      # Port série Arduino
BAUDRATE = 9600        # Doit correspondre au code Arduino
SEUIL    = 600         # Seuil d'alerte (valeur analogique 0–1023)
FENETRE  = 20          # Taille de la fenêtre de moyenne glissante
```

---

## 🔭 Perspectives d'évolution

- [ ] Enregistrement automatique des données en CSV pour l'analyse historique
- [ ] Support multi-capteurs pour un suivi acoustique multi-points
- [ ] Seuil dynamique basé sur la moyenne et la variance (détection d'anomalies)
- [ ] Module réseau (Wi-Fi / Ethernet) pour supervision à distance via interface web

---

## 📚 Concepts mobilisés

| Domaine | Concepts |
|---------|----------|
| Systèmes embarqués | Microcontrôleur, capteur analogique, bus I2C |
| Communication | Liaison série UART, protocole USB-Serial |
| Traitement du signal | Moyenne glissante, détection de seuil |
| Supervision industrielle | Acquisition temps réel, gestion des alertes |

---

## 👤 Auteur

**Njimongba Fochivé Mama Abdourahim**  
Filière : Ingénierie des Réseaux et Radiocommunications — Sup'PTIC  
Encadrant : Dr Nzebop

---

*Projet réalisé dans le cadre de la formation en systèmes embarqués et télécommunications.*
