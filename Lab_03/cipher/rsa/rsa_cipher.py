import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import requests
from ui_rsa import UI_MainWindow 


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_gen_keys.clicked.connect(self.generatekeys_btn)
        self.ui.btn_encrypt.clicked.connect(self.encrypt_btn)
        self.ui.btn_decrypt.clicked.connect(self.decrypt_btn)
        self.ui.btn_sign.clicked.connect(self.sign_btn)
        self.ui.btn_verify.clicked.connect(self.verify_btn)

    def generatekeys_btn(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                QMessageBox.information(self, "Success", data.get("message", "Keys generated successfully"))
            else:
                QMessageBox.warning(self, "Error", "Failed to generate keys")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request failed: {str(e)}")

    def encrypt_btn(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {"message": self.ui.plaintext_txt.toPlainText(), "key_type": "public"}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.ciphertext_txt.setText(data.get("encrypted_message", ""))
            else:
                QMessageBox.warning(self, "Error", "Encryption failed")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request failed: {str(e)}")

    def decrypt_btn(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {"message": self.ui.ciphertext_txt.toPlainText(), "key_type": "private"}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plaintext_txt.setText(data.get("decrypted_message", ""))
            else:
                QMessageBox.warning(self, "Error", "Decryption failed")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request failed: {str(e)}")

    def sign_btn(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {"message": self.ui.plaintext_txt.toPlainText()}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.signature_txt.setText(data.get("signature", ""))
                QMessageBox.information(self, "Success", "Signed successfully")
            else:
                QMessageBox.warning(self, "Error", "Signing failed")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request failed: {str(e)}")

    def verify_btn(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.information_txt.toPlainText(),
            "signature": self.ui.signature_txt.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Verified successfully")
            else:
                QMessageBox.warning(self, "Error", "Verification failed")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request failed: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
