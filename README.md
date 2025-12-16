## 🧾 Description du projet

Ce projet est une **application Python avec interface graphique** permettant de **générer des QR codes à partir d’une URL**, de les afficher à l’écran et de les **enregistrer au format PNG**.

L’interface est développée avec **Tkinter**, et la génération du QR code se fait avec la librairie **qrcode**.

---

## 📦 Dépendances

Le projet utilise les bibliothèques suivantes :

* `tkinter` : création de l’interface graphique
* `Pillow (PIL)` : manipulation et affichage des images
* `qrcode` : génération du QR code

Installation des dépendances :

```bash
pip install pillow qrcode
```

> `tkinter` est inclus par défaut avec Python.

---

## 🗂️ Structure du code

Le code est contenu dans un seul fichier :
`genQRcode.py`

Il est organisé autour d’une **classe principale `QRApp`**.

---

## 🧠 Explication du code

### 1️⃣ Initialisation de l’application

```python
class QRApp:
    def __init__(self, root):
```

* Configure la fenêtre principale :

  * Titre
  * Taille (420x520)
  * Fenêtre non redimensionnable
* Applique le thème `clam` de `ttk`
* Crée les éléments de l’interface :

  * Titre
  * Champ de saisie pour l’URL
  * Bouton “Générer”
  * Zone d’affichage du QR code
  * Bouton “Enregistrer le QR”

---

### 2️⃣ Génération du QR Code

```python
def generate_qr(self):
```

Fonction appelée lorsque l’utilisateur clique sur **“Générer”**.

Étapes :

* Récupère l’URL entrée par l’utilisateur
* Vérifie que le champ n’est pas vide
* Crée un QR code avec la librairie `qrcode`
* Génère une image noire sur fond blanc
* Redimensionne l’image pour l’aperçu
* Affiche le QR code dans l’interface

En cas d’erreur (champ vide), une **boîte de dialogue** s’affiche.

---

### 3️⃣ Enregistrement du QR Code

```python
def save_qr(self):
```

Fonction appelée lorsque l’utilisateur clique sur **“Enregistrer le QR”**.

* Vérifie qu’un QR code a bien été généré
* Ouvre une fenêtre de sauvegarde
* Enregistre l’image au format **PNG**
* Affiche un message de confirmation

---

### 4️⃣ Lancement de l’application

```python
if __name__ == "__main__":
```

* Initialise la fenêtre Tkinter
* Lance la boucle principale de l’application

---

## ▶️ Comment exécuter le projet

```bash
python genQRcode.py
```

Une fenêtre s’ouvre :

1. Entrer une URL
2. Cliquer sur **Générer**
3. Enregistrer le QR code si souhaité

---

## ✨ Fonctionnalités

* Interface graphique simple et intuitive
* Génération rapide de QR codes
* Prévisualisation du QR code
* Export en image PNG

---

