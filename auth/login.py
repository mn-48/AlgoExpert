import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow, QMessageBox, QDesktopWidget
from dashboard import MainWindow

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Form")
        self.setGeometry(100, 100, 300, 150)
        
        # Center the window on the screen
        self.center()

        # Create widgets
        self.label_user = QLabel("Username:")
        self.username = QLineEdit()
        self.label_pass = QLabel("Password:")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Login")

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_user)
        layout.addWidget(self.username)
        layout.addWidget(self.label_pass)
        layout.addWidget(self.password)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

        # Connect button to function
        self.login_button.clicked.connect(self.check_login)

        # Connect the Enter key to submit the form
        self.username.returnPressed.connect(self.check_login)
        self.password.returnPressed.connect(self.check_login)

    def center(self):
        # Get the geometry of the window and the screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def check_login(self):
        # Example credentials
        user = self.username.text()
        passwd = self.password.text()

        if user == "n" and passwd == "x":  # Example validation
            self.open_main_window()
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password")

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    login = LoginForm()
    login.show()

    sys.exit(app.exec_())
