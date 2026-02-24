from modules.mysql import MySQL

from modules.aluno import Aluno

import sys


from PySide6.QtWidgets import  (
   QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)
def cadastrar():
    pessoa = Aluno(
        campo_nome.text(),
        campo_email.text(),
        campo_cpf.text(),
        campo_telefone.text(),
        campo_endereço.text()
    )

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle("Cadastro aluno")
janela.resize(1200,600)

layout = QVBoxLayout()

#Componetes
label_nome= QLabel("Digite seu nome")
campo_nome = QLineEdit("")

label_email= QLabel("Digite seu email")
campo_email = QLineEdit("")

label_cpf= QLabel("Digite seu cpf")
campo_cpf = QLineEdit("")

label_telefone= QLabel("Digite seu telefone")
campo_telefone = QLineEdit("")



label_endereço= QLabel("Digite seu endereço")
campo_endereço = QLineEdit("")


botao = QPushButton("Cadastrar")


# Adicionar comppnetes a janela
layout.addWidget(label_nome)
layout.addWidget(campo_nome)

layout.addWidget(label_email)
layout.addWidget(campo_email)

layout.addWidget(label_cpf)
layout.addWidget(campo_cpf)

layout.addWidget(label_telefone)
layout.addWidget(campo_telefone)

layout.addWidget(label_endereço)
layout.addWidget(label_endereço)


layout.addWidget(botao)

janela.setLayout(layout)

botao.clicked.connect(cadastrar)

janela.show()


sys.exit(app.exec())

