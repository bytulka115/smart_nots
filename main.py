from PyQt6.QtWidgets import *

from file_kaka import write_in_file, read_from_file

notes = read_from_file()
print(notes)



app = QApplication([])
window = QWidget()

text_edit = QTextEdit()
list_notes_lbl = QLabel("список заміток")
notes_list = QListWidget()
notes_list.addItems(notes)
create_note_btn = QPushButton("створити замітку")
delate_note_btn = QPushButton("видалити замітку")
save_note_btn = QPushButton("зберегти замітку")
list_text_lbl = QLabel("список тегів")
write_text_note = QLineEdit()
write_text_note.setPlaceholderText("введіть тег...")
tags_list = QListWidget()
add_note_btn = QPushButton("додати до заміток")
open_note_btn = QPushButton("відкриття заміток")
searche_note_btn = QPushButton("шукати замітки")

main_line = QHBoxLayout()
v1 =QVBoxLayout()
v2 = QHBoxLayout()
v3 = QHBoxLayout()
main_line.addWidget(text_edit)


v1.addWidget(list_notes_lbl)
v1.addWidget(notes_list)
v2.addWidget(create_note_btn)
v2.addWidget(delate_note_btn)
v1.addLayout(v2)
v1.addWidget(save_note_btn)
v1.addWidget(list_text_lbl)
v1.addWidget(tags_list)
v1.addWidget(write_text_note)
v3.addWidget(add_note_btn)
v3.addWidget(open_note_btn)
v1.addLayout(v3)
v1.addWidget(searche_note_btn)
main_line.addLayout(v1)


def show_note():
    key = notes_list.selectedItems()[0].text()
    text_edit.setText(notes[key]['текст'])
    tags_list.clear()
    tags_list.addItems(notes[key]['теги'])



def save_note():
    notes[key] = field_text.toPlainText()
    write_in_file(notes)






notes_list.itemClicked.connect(show_note)
save_note_btn.clicked.connect(save_note)
window.setLayout(main_line)
window.show()
app.exec()