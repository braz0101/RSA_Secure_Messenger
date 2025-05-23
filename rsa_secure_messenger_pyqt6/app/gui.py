from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QTextEdit, QFileDialog, QMessageBox, QTextBrowser, QHBoxLayout, QStatusBar
)
from PyQt6.QtGui import QFont, QIcon
import sys
import os
from datetime import datetime

from rsa_secure_messenger_pyqt6.keys import generate_keys
from rsa_secure_messenger_pyqt6.crypto import load_key, encrypt_message, decrypt_message

# Fonction pour obtenir le bon chemin de l'icône
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Fonction pour logger dans un fichier texte
def log_action(message):
    os.makedirs("logs", exist_ok=True)
    with open("logs/history.log", "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.write(f"{timestamp} {message}\n")

def launch_app():
    app = QApplication(sys.argv)

    ICON_PATH = resource_path("icon.ico")
    app.setWindowIcon(QIcon(ICON_PATH))  # icône pour la barre des tâches

    window = QWidget()
    window.setWindowTitle("RSA Secure Messenger")
    window.setWindowIcon(QIcon(ICON_PATH))  # icône pour la fenêtre
    window.setGeometry(100, 100, 800, 600)

    main_layout = QVBoxLayout()

    label = QLabel("🔐 RSA Secure Messenger")
    label.setFont(QFont("Arial", 16))
    main_layout.addWidget(label)

    layout = QHBoxLayout()
    main_layout.addLayout(layout)

    input_text = QTextEdit()
    input_text.setPlaceholderText("Entrez votre message ici...")
    layout.addWidget(input_text)

    output_text = QTextEdit()
    output_text.setPlaceholderText("Résultat...")
    output_text.setReadOnly(True)
    layout.addWidget(output_text)

    log_browser = QTextBrowser()
    log_browser.setPlaceholderText("Historique des actions...")
    main_layout.addWidget(log_browser)

    status_bar = QStatusBar()
    main_layout.addWidget(status_bar)

    def show_status(msg):
        status_bar.showMessage(msg)
        log_browser.append(msg)
        log_action(msg)

    def on_generate_keys():
        try:
            message = generate_keys()
            show_status(message)
            QMessageBox.information(window, "Clés RSA", message)
        except Exception as e:
            show_status(f"Erreur lors de la génération des clés : {e}")
            QMessageBox.critical(window, "Erreur", str(e))

    def on_encrypt():
        plain = input_text.toPlainText()
        if not plain.strip():
            show_status("Erreur : champ de texte vide.")
            QMessageBox.warning(window, "Attention", "Veuillez entrer un message à chiffrer.")
            return
        try:
            pub_key = load_key("keys/public_key.pem")
            encrypted = encrypt_message(pub_key, plain)
            output_text.setPlainText(encrypted.hex())
            show_status("Message chiffré avec la clé par défaut.")
        except Exception as e:
            show_status(f"Erreur de chiffrement : {e}")
            QMessageBox.critical(window, "Erreur", str(e))

    def on_decrypt():
        try:
            priv_key = load_key("keys/private_key.pem", private=True)
            ciphertext = bytes.fromhex(input_text.toPlainText())
            decrypted = decrypt_message(priv_key, ciphertext)
            output_text.setPlainText(decrypted)
            show_status("Message déchiffré avec la clé par défaut.")
        except Exception as e:
            show_status(f"Erreur de déchiffrement : {e}")
            QMessageBox.critical(window, "Erreur", str(e))

    def on_load_pub_key():
        path, _ = QFileDialog.getOpenFileName(window, "Charger une clé publique", "", "Fichiers PEM (*.pem)")
        if path:
            try:
                pub_key = load_key(path)
                encrypted = encrypt_message(pub_key, input_text.toPlainText())
                output_text.setPlainText(encrypted.hex())
                show_status(f"Message chiffré avec la clé : {os.path.basename(path)}")
            except Exception as e:
                show_status(f"Erreur avec la clé publique : {e}")
                QMessageBox.critical(window, "Erreur", str(e))

    def on_load_priv_key():
        path, _ = QFileDialog.getOpenFileName(window, "Charger une clé privée", "", "Fichiers PEM (*.pem)")
        if path:
            try:
                priv_key = load_key(path, private=True)
                decrypted = decrypt_message(priv_key, bytes.fromhex(input_text.toPlainText()))
                output_text.setPlainText(decrypted)
                show_status(f"Message déchiffré avec la clé : {os.path.basename(path)}")
            except Exception as e:
                show_status(f"Erreur avec la clé privée : {e}")
                QMessageBox.critical(window, "Erreur", str(e))

    # Afficher la clé publique dans une boîte de dialogue
    def on_show_public_key():
        try:
            with open("keys/public_key.pem", "r", encoding="utf-8") as f:
                public_key_text = f.read()
            dlg = QMessageBox(window)
            dlg.setWindowTitle("Clé Publique RSA")
            dlg.setText("Voici votre clé publique :")
            dlg.setDetailedText(public_key_text)
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.exec()
            show_status("Clé publique affichée.")
        except FileNotFoundError:
            show_status("Clé publique introuvable. Veuillez générer les clés d'abord.")
            QMessageBox.warning(window, "Erreur", "Aucune clé publique trouvée.")
        except Exception as e:
            show_status(f"Erreur en lisant la clé publique : {e}")
            QMessageBox.critical(window, "Erreur", str(e))

    main_layout.addWidget(QLabel("🔧 Actions :"))

    btn_generate = QPushButton("🛠 Générer les clés")
    btn_generate.clicked.connect(on_generate_keys)
    main_layout.addWidget(btn_generate)

    btn_encrypt = QPushButton("🔒 Chiffrer (clé par défaut)")
    btn_encrypt.clicked.connect(on_encrypt)
    main_layout.addWidget(btn_encrypt)

    btn_decrypt = QPushButton("🔓 Déchiffrer (clé par défaut)")
    btn_decrypt.clicked.connect(on_decrypt)
    main_layout.addWidget(btn_decrypt)

    btn_custom_pub = QPushButton("📂 Chiffrer avec une clé publique externe")
    btn_custom_pub.clicked.connect(on_load_pub_key)
    main_layout.addWidget(btn_custom_pub)

    btn_custom_priv = QPushButton("📂 Déchiffrer avec une clé privée externe")
    btn_custom_priv.clicked.connect(on_load_priv_key)
    main_layout.addWidget(btn_custom_priv)

    btn_show_pubkey = QPushButton("📄 Voir la clé publique")
    btn_show_pubkey.clicked.connect(on_show_public_key)
    main_layout.addWidget(btn_show_pubkey)

    window.setLayout(main_layout)
    window.show()
    sys.exit(app.exec())
