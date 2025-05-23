
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
RSA_Secure_Messenger/
│
├── rsa_secure_messenger_pyqt6/
│   ├── app/
│   │   ├── icon.ico              # Icône
│   │   └── gui.py                # Interface PyQt6
│   ├── crypto.py                 # Fonctions de chiffrement/déchiffrement
│   ├── keys.py                   # Génération des clés RSA
│
├── keys/
│   ├── private_key.pem           # Clé privée générée
│   └── public_key.pem            # Clé publique générée
│
├── logs/
│   └── history.log               # Historique des actions
│
├── icon.ico                      # Icône
├── main.py                       # Point d’entrée de l'application
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

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

<img width="596" alt="1" src="https://github.com/user-attachments/assets/5bb5b8ae-1314-4cf5-bc2a-c1da88cfc37b" />
<img width="595" alt="2" src="https://github.com/user-attachments/assets/948f4a25-7d74-4975-8b01-893faf92cc41" />
<img width="162" alt="3" src="https://github.com/user-attachments/assets/4f023571-cb37-497a-84f9-9cb1531766ef" />
<img width="575" alt="4" src="https://github.com/user-attachments/assets/52a0e14f-d8a4-420f-9efb-5e68e1ff9aae" />
<img width="594" alt="5" src="https://github.com/user-attachments/assets/0aff5ff6-57ee-454a-8949-974f119787f5" />

https://github.com/user-attachments/assets/80ce1e50-0e87-432b-94aa-1176e51eab9a

<img width="619" alt="6" src="https://github.com/user-attachments/assets/335056d2-5ab1-4402-964b-352396d829dd" />



---

## 📄 Licence

Ce projet est sous licence MIT.

---

## 🤝 Contributions

Les contributions sont les bienvenues ! Vous pouvez proposer des améliorations via issues ou pull requests.
