import os
from PyQt5.QtWidgets import QFileDialog

folder = QFileDialog.getExistingDirectory()
spisok = os.listdir(folder)