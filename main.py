from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()

text_edit = QTextEdit()
list_notes_lbl = QLabel("список заміток")
notes_list = QListWidget()
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




window.setLayout(main_line)
window.show()
app.exec()