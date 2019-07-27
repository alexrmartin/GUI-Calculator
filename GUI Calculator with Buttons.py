import sys
from PyQt5.QtWidgets import *

displayNum = 0
backNum = 0
operation = ''

app = QApplication(sys.argv)
widget = QWidget()
label = QLabel("", widget)

btnAdd = QPushButton("+", widget)
btnSub = QPushButton("-", widget)
btnDiv = QPushButton(u"\u00F7", widget)
btnMul = QPushButton("x", widget)
btnEqual = QPushButton("=", widget)
btnPM = QPushButton(u"\u00B1", widget)
btnAC = QPushButton("AC", widget)
btn0 = QPushButton("0", widget)
btn1 = QPushButton("1", widget)
btn2 = QPushButton("2", widget)
btn3 = QPushButton("3", widget)
btn4 = QPushButton("4", widget)
btn5 = QPushButton("5", widget)
btn6 = QPushButton("6", widget)
btn7 = QPushButton("7", widget)
btn8 = QPushButton("8", widget)
btn9 = QPushButton("9", widget)


def init():
    widget.resize (300, 300)
    widget.move(300, 300)
    widget.setWindowTitle('Calculator')
    widget.show()

    label.setText('0')
    label.resize(100, 100)
    label.move(20, 10)
    label.show()

    displayNum = 0
    backNum = 0
    operation = ''

    btnEqual.move(290, 300)
    btnEqual.clicked.connect(equal)
    btnEqual.show()

    btnAdd.move(290, 250)
    btnAdd.clicked.connect(addition)
    btnAdd.show()

    btnSub.move(290, 200)
    btnSub.clicked.connect(subtraction)
    btnSub.show()

    btnDiv.move(290, 150)
    btnDiv.clicked.connect(division)
    btnDiv.show()

    btnMul.move(290, 200)
    btnMul.clicked.connect(multiplication)
    btnMul.show()

    btnPM.move(110, 300)
    btnPM.clicked.connect(sign)
    btnPM.show()

    btnAC.move(200, 300)
    btnAC.clicked.connect(all_clear)
    btnAC.show()
    
    btn0.move(20, 300)
    btn0.clicked.connect(zero)
    btn0.show()

    btn1.move(20, 250)
    btn1.clicked.connect(one)
    btn1.show()

    btn2.move(110, 250)
    btn2.clicked.connect(two)
    btn2.show()

    btn3.move(200, 250)
    btn3.clicked.connect(three)
    btn3.show()

    btn4.move(20, 200)
    btn4.clicked.connect(four)
    btn4.show()

    btn5.move(110, 200)
    btn5.clicked.connect(five)
    btn5.show()

    btn6.move(200, 200)
    btn6.clicked.connect(six)
    btn6.show()

    btn7.move(20, 150)
    btn7.clicked.connect(seven)
    btn7.show()

    btn8.move(110, 150)
    btn8.clicked.connect(eight)
    btn8.show()

    btn9.move(200, 150)
    btn9.clicked.connect(nine)
    btn9.show()

def equal():
    global displayNum
    global backNum
    global operation
    
    if operation == '':
        return
    elif operation == 'add':
        displayNum += backNum
    elif operation == 'subtract':
        displayNum =  backNum - displayNum
    elif operation == 'multiply':
        displayNum *= backNum
    elif operation == 'divide':
        displayNum = backNum/displayNum
        
    label.setText(str(displayNum))
    operation = ''

def addition():
    global displayNum
    global backNum
    global operation
    
    operation = 'add'
    backNum = displayNum
    displayNum = 0

def subtraction():
    global displayNum
    global backNum
    global operation
    
    operation = 'subtract'
    backNum = displayNum
    displayNum = 0

def multiplication():
    global displayNum
    global backNum
    global operation
    
    operation = 'multiply'
    backNum = displayNum
    displayNum = 0

def division():
    global displayNum
    global backNum
    global operation
    
    operation = 'divide'
    backNum = displayNum
    displayNum = 0

def zero():
    global displayNum
    
    displayNum *= 10
    label.setText(str(displayNum))

def one():
    global displayNum
 
    displayNum = displayNum*10 + 1
    label.setText(str(displayNum))

def two():
    global displayNum
    
    displayNum = displayNum*10 + 2
    label.setText(str(displayNum))

def three():
    global displayNum
    
    displayNum = displayNum*10 + 3
    label.setText(str(displayNum))

def four():
    global displayNum
    
    displayNum = displayNum*10 + 4
    label.setText(str(displayNum))

def five():
    global displayNum
    
    displayNum = displayNum*10 + 5
    label.setText(str(displayNum))

def six():
    global displayNum
    
    displayNum = displayNum*10 + 6
    label.setText(str(displayNum))

def seven():
    global displayNum
    
    displayNum = displayNum*10 + 7
    label.setText(str(displayNum))
    
def eight():
    global displayNum
    
    displayNum = displayNum*10 + 8
    label.setText(str(displayNum))

def nine():
    global displayNum
    
    displayNum = displayNum*10 + 9
    label.setText(str(displayNum))

def sign():
    global displayNum

    displayNum *= -1
    label.setText(str(displayNum))

def all_clear():
    global displayNum
    global backNum
    global operation

    displayNum = 0
    backNum = 0
    operation = ''
    label.setText(str(displayNum))

if __name__== "__main__":
    init()
    
app.exec_()
