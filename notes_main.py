#начни тут создавать приложение с умными заметками
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QTextEdit,QLineEdit, QPushButton,QApplication, QInputDialog
import json
'''notes = {'Добро пожаловать':
            {'текст':'В этом приложении можно создавать заметки с тегами','теги':
            ['умные заметки','инструкция']}}
with open ('notes.json', 'w') as file:
    json.dump(notes,file)'''
app = QApplication([])
main_win = QWidget()
zam = QTextEdit()#поле дял ввода заметки
zamsp = QListWidget()#Список заметок
teg_line = QListWidget()#Список тегов
addzam = QPushButton("Создать заметку")# кнопка "создать заметку"
delzam = QPushButton("Удалить заметку")#кнопка""удалить заметку"
savezam = QPushButton('Сохранить заметку')# Кнопка сохранить заметку
addkzam = QPushButton('Добавить к заметке')
otkzam = QPushButton('Открепить от заметки')
foundzam = QPushButton('Найти заметку по тегу')
teg = QLineEdit()
tegt= QLabel('Список тегов')
zamt = QLabel('Список заметок')
teg.setPlaceholderText('Введите тег...')
glav = QHBoxLayout()
vert1 = QVBoxLayout()
vert2 = QVBoxLayout()
zamtl = QHBoxLayout()#линия для надписи список заметок
zaml = QHBoxLayout()#Л для списка заметок 
del_add = QHBoxLayout()#создать\удалить заметку
save = QHBoxLayout()# сохранит заметку
taglistt = QHBoxLayout()# текст список тегов
taglist = QHBoxLayout()# список тегов
add_del_tag =  QHBoxLayout()# добавить к заметке открепить
add_teg_text = QHBoxLayout()# введите тег
foundteg = QHBoxLayout()# искать заметки по тегу
zamtl.addWidget(zamt)
taglistt.addWidget(tegt)
zaml.addWidget(zamsp)
del_add.addWidget(addzam)
del_add.addWidget(delzam)
save.addWidget(savezam)
add_teg_text.addWidget(teg)
taglist.addWidget(teg_line)
add_del_tag.addWidget(addkzam)
add_del_tag.addWidget(otkzam)
foundteg.addWidget(foundzam)



vert1.addLayout(zamtl)
vert1.addLayout(zaml)
vert1.addLayout(del_add)
vert1.addLayout(save)
vert1.addLayout(taglistt)
vert1.addLayout(taglist)
vert1.addLayout(add_teg_text)
vert1.addLayout(add_del_tag)
vert1.addLayout(foundteg)


vert2.addWidget(zam)

glav.addLayout(vert2)
glav.addLayout(vert1)

main_win.setLayout(glav)

def show_note():
    name= zamsp.selectedItems()[0].text()
    zam.setText(notes[name]['текст'])
    teg_line.clear()
    teg_line.addItems(notes[name]['теги'])

def add_note():
    note_name,result = QInputDialog.getText(main_win,'Добавить заметку', 'Название заметки:')
    notes[note_name] ={'текст':'','теги':[]}
    zamsp.addItem(note_name)
    teg_line.addItems(notes[note_name]['теги'])

def del_note():
    if zamsp.selectedItems():
        key = zamsp.selectedItems()[0].text()
        del notes[key]
        zamsp.clear()
        teg_line.clear()
        zam.clear()
        zamsp.addItems(notes)
        with open('notes.json', 'w')as file:
            json.dump(notes,file)

def save_note():
    if zamsp.selectedItems():
        note_text = zam.toPlainText()
        name= zamsp.selectedItems()[0].text()
        notes[name]['текст'] = note_text
        with open('notes.json','w')as file:
            json.dump(notes,file)
        
def add_tag():
    if zamsp.selectedItems():
        name= zamsp.selectedItems()[0].text()
        teg_text = teg.text()
        if not teg_text in notes[name]['теги']:
            notes[name]['теги'].append(teg_text)
            teg_line.addItem(teg_text)
            teg.clear()
            with open('notes.json','w')as file:
                json.dump(notes,file)

def del_teg():
    if zamsp.selectedItems():
        name= zamsp.selectedItems()[0].text()
        name_teg = teg_line.selectedItems()[0].text()
        notes[name]['теги'].remove(name_teg)
        teg_line.clear()
        teg_line.addItems(notes[name]['теги'])
        with open('notes.json','w')as file:
            json.dump(notes,file)

def search_tag():
    if foundzam.text() == "Найти заметку по тегу":
        list_notes = dict()
        tag_text = teg.text()
        for note in notes:
            if tag_text in notes[note]['теги']:
                list_notes[note]=notes[note]
        foundzam.setText('Сбросить поиск')
        
        teg.clear()
        zamsp.clear()
        zamsp.addItems(list_notes)
        print (notes)
    elif foundzam.text() == 'Сбросить поиск':
        teg.clear()
        zamsp.addItems(notes)
        foundzam.setText('Найти заметку по тегу')


        

with open('notes.json', 'r')as file:
    notes= json.load(file)
zamsp.addItems(notes)

zamsp.itemClicked.connect(show_note)
addzam.clicked.connect(add_note)
delzam.clicked.connect(del_note)
savezam.clicked.connect(save_note)
addkzam.clicked.connect(add_tag)
otkzam.clicked.connect(del_teg)
foundzam.clicked.connect(search_tag)

main_win.show()
app.exec_()