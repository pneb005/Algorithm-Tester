import sys
sys.path.insert(0,'c:\python310\lib\site-packages')
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QObject, pyqtSignal
from faker import Faker
import random
import timeit
fake = Faker()
random.seed(42)

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')

class Backend(QObject):
    updated = pyqtSignal(str, arguments=['text'])
    error = pyqtSignal(str, arguments=['text'])

    def __init__(self):
        super().__init__()
    
    def reset(self):
        clear = ""
        self.error.emit(clear)

    def setErrorMessage(self, message):
        errorMessage = message
        self.error.emit(errorMessage)

    def setProgramText(self, path):
        program = open(path, "r")
        program = program.read()
        text = f"""{program}"""
        self.updated.emit(text)
        
backend = Backend()
win = engine.rootObjects()[0].setProperty('backend', backend)
inputs = engine.rootObjects()[0]
button = inputs.findChild(QObject, "enter")
program = inputs.findChild(QObject, "userInput")  
fileName = inputs.findChild(QObject, "filename")
nameNumber = inputs.findChild(QObject, "nameCount")
submitNames  = inputs.findChild(QObject, "submitButton")
errorLabel = inputs.findChild(QObject, "errorLabel")
loopCount = inputs.findChild(QObject, "loopCount")

def speedTest(script, names, repeats):
    text = f"""
names = {names}
{script}
"""
    programTime = timeit.timeit(text, number=repeats)
    print(f"\n> Program took:\n {programTime} seconds to sort {len(names)} names {repeats} times\n")

nameCount = 0

def setNameCount():
    temp = nameNumber.property("text")
    
def setText():
    text = str(fileName.property("currentFile"))
    text = text.replace("PyQt6.QtCore.QUrl('", "")
    text = text.replace("file:///", "")
    text = text.replace("')", "")
    if len(text)>0:
        backend.setProgramText(text)
        setNameCount()
    else:
        backend.setErrorMessage("Please choose a file")

def diagnose():
    genNames = nameNumber.property("text")
    loops = loopCount.property("text")
    try:
        nameCount = int(genNames)
    except ValueError:
        backend.setErrorMessage("Try to input a number")
        return None

    if (len(genNames) or len(loops)) == 0:
        backend.setErrorMessage("Please input a value")
        return None

    try:
        genNames = int(genNames)
        loops = int(loops)
    except ValueError:
        backend.setErrorMessage("Please input an integer")

    
    if (genNames or loops) == 0:
        backend.setErrorMessage('Non-zero input required')
    else:
        script = program.property('text')
        names = [fake.name() for _ in range(genNames)]
        speedTest(script, names, loops)
    
button.clicked.connect(diagnose)
fileName.accepted.connect(setText)

sys.exit(app.exec())