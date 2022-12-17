import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QRadioButton
)
from username import usernameGenerator, clearLayout
from qt_material import apply_stylesheet

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Username Generator')
        self.setGeometry(100, 100, 320, 210)

        apply_stylesheet(app, theme='dark_purple.xml')

        self.deleteTextBool = True

        inputFrame = QWidget(self)
        usernameFrame = QWidget(self)
        passwordFrame = QWidget(self)
        deleteTextFrame = QWidget(self)
        themeFrame = QWidget(self)

        self.word1Label = QLabel('Enter the first word: ')
        self.word2Label = QLabel('Enter the second word: ')
        self.word3Label = QLabel('Enter the third word: ')

        self.word1Entry = QLineEdit(self)
        self.word2Entry = QLineEdit(self)
        self.word3Entry = QLineEdit(self)

        #Create button that stores the words
        self.submitButton = QPushButton('Generate Usernames')
        self.submitButton.setChecked(True)
        self.submitButton.clicked.connect(self.buttonClick)

        #Delete Text Buttons
        keepTextButton = QRadioButton('Keep Text', deleteTextFrame)
        keepTextButton.setChecked(False)
        keepTextButton.toggled.connect(self.deleteText)
        deleteTextButton = QRadioButton('Reset Text', deleteTextFrame)
        deleteTextButton.setChecked(True)
        deleteTextButton.toggled.connect(self.deleteText)

        #Theme Buttons
        lightModeButton = QRadioButton('Light mode', themeFrame)
        lightModeButton.setChecked(False)
        lightModeButton.toggled.connect(self.themeUpdate)
        darkModeButton = QRadioButton('Dark mode', themeFrame)
        darkModeButton.setChecked(True)
        darkModeButton.toggled.connect(self.themeUpdate)

        # place the widget on the window
        inputGrid = QGridLayout()
        inputFrame.setLayout(inputGrid)
        inputGrid.addWidget(self.word1Label, 0, 0)
        inputGrid.addWidget(self.word1Entry, 0, 1)
        inputGrid.addWidget(self.word2Label, 1, 0)
        inputGrid.addWidget(self.word2Entry, 1, 1)
        inputGrid.addWidget(self.word3Label, 2, 0)
        inputGrid.addWidget(self.word3Entry, 2, 1)

        self.usernameLayout = QVBoxLayout()
        usernameFrame.setLayout(self.usernameLayout)

        self.passwordLayout = QHBoxLayout()
        passwordFrame.setLayout(self.passwordLayout)

        themeSelectorLayout = QHBoxLayout()
        themeFrame.setLayout(themeSelectorLayout)
        themeSelectorLayout.addWidget(lightModeButton)
        themeSelectorLayout.addWidget(darkModeButton)

        deleteTextLayout = QHBoxLayout()
        deleteTextFrame.setLayout(deleteTextLayout)
        deleteTextLayout.addWidget(keepTextButton)
        deleteTextLayout.addWidget(deleteTextButton)

        self.layout = QGridLayout()
        self.layout.addWidget(inputFrame, 0, 0, 1, 2)
        self.layout.addWidget(self.submitButton, 1, 1)
        self.layout.addWidget(usernameFrame, 0, 2, 7, 2)
        self.layout.addWidget(deleteTextFrame, 1, 0)
        self.layout.addWidget(themeFrame, 3, 0, 2, 1)
        self.layout.addWidget(passwordFrame, 5, 0, 3, 7)
        self.setLayout(self.layout)

        # show the window
        self.show()

    def buttonClick(self):
        word1 = self.word1Entry.text()
        word2 = self.word2Entry.text()
        word3 = self.word3Entry.text()

        words = f'{word1}{word2}{word3}'
        clearLayout(self.usernameLayout)
        clearLayout(self.passwordLayout)
        usernameGenerator(words, self.usernameLayout, self.passwordLayout)

        
        if self.deleteTextBool:
            self.word1Entry.setText('')
            self.word2Entry.setText('')
            self.word3Entry.setText('')
    
    def deleteText(self):
        buttonSignal = self.sender()
        if buttonSignal.text() == 'Keep Text':
            self.deleteTextBool = False
        elif buttonSignal.text() == 'Reset Text':
            self.deleteTextBool = True

    def themeUpdate(self):
        buttonSignal = self.sender()
        if buttonSignal.text() == 'Dark mode':
            apply_stylesheet(app, theme='dark_purple.xml')
        else:
            apply_stylesheet(app, theme='light_purple.xml')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())