import sys

from PySide6.QtWidgets import QApplication

from resources.data.data_update import update_from_github, data_path, github_data_url

from ui.main_window import MainWindow

if __name__ == "__main__":
    update_from_github(github_data_url, data_path) # Check for hashcat_gpu_benchmarks.csv update
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

