
# 🔐 RSA Secure Messenger (PyQt6)

**RSA Secure Messenger** est une application graphique développée en **Python avec PyQt6** permettant de chiffrer et déchiffrer des messages texte en local à l’aide du chiffrement **RSA**. Elle offre une interface conviviale pour tester, générer des clés et manipuler des messages sécurisés, sans dépendre d'aucun serveur externe.

---

## ✨ Fonctionnalités

- 🔑 **Génération de paires de clés RSA (2048 bits)**
- 🔒 **Chiffrement de message avec clé publique**
- 🔓 **Déchiffrement de message avec clé privée**
- 📂 **Support de clés externes (.pem)**
- 📄 **Affichage de la clé publique**
- 🧾 **Historique des actions enregistrées dans un fichier `logs/history.log`**
- 💻 **Interface graphique intuitive et responsive avec PyQt6**
- 📦 **Installeur Windows disponible via Inno Setup (en option)**

---

## 📦 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/braz0101/RSA_Secure_Messenger.git
cd RSA_Secure_Messenger
```

### 2. Créer un environnement virtuel (optionnel mais recommandé)

```bash
python -m venv venv
source venv/bin/activate    # ou .\venv\Scripts\activate sur Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 🚀 Lancer l’application

```bash
python main.py
```

L’interface graphique devrait apparaître avec toutes les fonctionnalités disponibles.

---

## 📁 Structure du projet
```perl
rsa_secure_messenger_pyqt6/
│
rsa_secure_messenger_pyqt6├── app/
│                         ├── icon.ico         # Icône
│                         └── gui.py           # Interface PyQt6
│                         crypto.py            # Fonctions de chiffrement/déchiffrement
│                         keys.py              # Génération des clés RSA
│
│
keys/
  ├── private_key.pem                          # Clé privée générée (exclue du dépôt)
  └── public_key.pem                           # Clé publique générée (exclue du dépôt)
│
logs/
  └── history.log                              # Historique des actions
│
icon.ico                                       # Icône
main.py                                        # Point d’entrée de l'application
.gitignore
LICENSE
README.md
requirements.txt
```
---

## 📜 Utilisation

- Générer des clés avec le bouton 🛠.
- Saisir un message, puis cliquer sur 🔒 pour le chiffrer.
- Déchiffrer le message chiffré avec 🔓.
- Charger des clés externes avec 📂 pour des tests spécifiques.
- Voir la clé publique 🔑 directement dans l’application.

---

## 🛡️ Sécurité

- Les clés RSA sont générées localement et jamais transmises.
- Aucune connexion réseau ou dépendance à des serveurs tiers.
- L'utilisateur peut remplacer les fichiers .pem s’il dispose de ses propres paires de clés.

---
## 🧪 Démonstration

Voici un aperçu de l’utilisation de RSA Secure Messenger :



---

## 📄 Licence

Ce projet est sous licence MIT.

---

## 🤝 Contributions

Les contributions sont les bienvenues ! Vous pouvez proposer des améliorations via issues ou pull requests.
