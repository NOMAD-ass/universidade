# Projeto Universidade

Modelagem em Orientação á Objetos
das Entidades Alunos, Cursos e Turma.

## Caso de Uso
```mermaid
flowchart LR
    Usuario([Secretaria])

    UC1((cadastrar Alunos))
    UC2((Editar Alunos))
    UC3((Transferir Alunos))

    Usuario --> UC1
    Usuario --> UC2
    Usuario --> UC3
```

## Diagrama de Classes
```mermaid
classDiagram
    class Aluno{
    -nome
    -email
    -cpf
    -telefone
    -endereço
    -matrcula
    +cadastrar()
    +editar()
    +transferir()
    }

```

## Dependências
- **VSCode**: IDE(Interface de Desenvolvimento)
- **Mermaid**: LInguagem para confecção de Diagramas em documentos MD(Mark Down)
- **Material Icon Theme**: Tema para  Colorir as pasta
- **Git Lens**: Interface Grafica para o versionamento git intregado no VSCode.