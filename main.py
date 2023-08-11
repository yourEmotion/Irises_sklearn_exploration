import sys

from PyQt5.QtWidgets import QApplication

from src.Windows.windows import MainMenu

NIGHT_MODE_ON = False

curr_user_name = ""
curr_password = ""
first_usage = False


def launch_app():
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    launch_app()

