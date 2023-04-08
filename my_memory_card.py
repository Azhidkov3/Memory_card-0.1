#импорты
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *

#скрывание групп
class Question():
    def __init__(self, question_text, right_answer, wrong1, wrong2, wrong3):
        self.question_text = question_text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

q1 = Question('Как называется интернет магазин яндекса?','Я.Маркет','Я.Шоп','Я.Пятёрочка','Я.Магазин')
q2 = Question('Как называется этот проект?','Memory card','momery card','Нету названия','fqajy gznyflwfnm')
q3 = Question('АК-...','105','74','М','СУ')
q4 = Question('Устройства Эпл работают на...','IOS','linux','SteamOS','Windows')
q5 = Questio('Что лучше?', 'балтика 9', 'кола', 'пепси', 'фанта'
question_list = []
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
def next_question():
    Main_win.total +=1
    Cur_question = randint(0, len(question_list) -1)
    q=question_list[Cur_question]
    ask(q)

def show_result():
    answerGrp.hide()
    result_box.show()
    button.setText('Следующий вопрос')
def show_quest1():
    buttongroup.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    buttongroup.setExclusive(True)
    result_box.hide()
    answerGrp.show()
    button.setText('Ответить')
def start_test():
    if button.text() == 'Ответить':
        check_ans()
    else:
        next_question()
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question_text)
    R_A.setText(q.right_answer)
    
    show_quest1()
def check_ans():
    if answers[0].isChecked():
        result_text.setText('правильно')
        show_result()
        Main_win.score += 1
    else:
        result_text.setText('не правильно')
        show_result()
    print('Вопросов правильно:', Main_win.score, 'Всего вопросов:', Main_win.total)
    print('Рейтинг:', Main_win.score / Main_win.total * 100)

#Настройки
app = QApplication([])
Main_win = QWidget()

Main_win.resize(400, 300)
Main_win.setWindowTitle('Memory card')
Main_win.total = 0
Main_win.score = 0
#Виджеты
question = QLabel('Вопрос', alignment = Qt.AlignCenter)
button = QPushButton('Ответить')
answerGrp = QGroupBox('Варианты ответа')
ans1 = QRadioButton('1')
ans2 = QRadioButton('2')
ans3 = QRadioButton('3')
ans4 = QRadioButton('4')
answers = [ans1, ans2, ans3, ans4]
buttongroup = QButtonGroup()
buttongroup.addButton(ans1)
buttongroup.addButton(ans2)
buttongroup.addButton(ans3)
buttongroup.addButton(ans4)
#Нпр.
V1 = QVBoxLayout()
V1.addWidget(ans1)
V1.addWidget(ans3)
V2 = QVBoxLayout()
V2.addWidget(ans2)
V2.addWidget(ans4)
H = QHBoxLayout()
H.addLayout(V1)
H.addLayout(V2)
answerGrp.setLayout(H)
VLine = QVBoxLayout()
VLine.addWidget(question)
VLine.addWidget(answerGrp)
VLine.addWidget(button)
result_box = QGroupBox('Результат')
result_text = QLabel('Правильно')
R_A = QLabel ('')
V3 = QVBoxLayout()
V3.addWidget(result_text)
V3.addWidget(R_A)
result_box.setLayout(V3)
VLine.addWidget(question, alignment = Qt.AlignCenter)
VLine.addWidget(answerGrp)
VLine.addWidget(result_box)
VLine.addWidget(button)
Main_win.setLayout(VLine)
Main_win.show()
#ask('Ютуб до того как стал видеохостингом был...', 'сервисом знакомств', 'Месенджером', 'Онлайн школой','Игрой')
button.clicked.connect(start_test)
next_question()
app.exec_()