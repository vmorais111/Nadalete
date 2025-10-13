# Exercícios Práticos de TDD – Testes com Pytest
## Requisitos: 
Python 3.10, pytest 8.4.2.

## Estrutura do projeto

- Atv 1
  - Triangulo.py
  - Test_triangulo.py
- Atv 2
  - Email.py
  - Person.py
  - PersonDAO.py
  - test_person_DAO.py
- Atv 3
  - Calculator.py
  - test_calculator.py
## 1. Clonar o repositório
```
git clone https://github.com/<seu-usuario>/<seu-repo>.git
cd <seu-repo>
```
## 2. Preparar o ambiente
*Usando ambiente virtual (recomendado)*
- Windows (PowerShell)
```
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install pytest
```
## 3. Executar os testes
### 3.1. Todos os testes (a partir da raiz)
```
pytest -v "Atv 1" "Atv 2" "Atv 3"
```
### 3.2. Por atividade
- Atv 1 (Triângulo)
```
pytest -v "Atv 1"
# ou
pytest -v "Atv 1/Test_triangulo.py"
```
- Atv 2 (Person / Email / DAO)
```
pytest -v "Atv 2"
# ou
pytest -v "Atv 2/test_person_DAO.py"
```
- Atv 3 (Calculadora de salário)
```
pytest -v "Atv 3"
# ou
pytest -v "Atv 3/test_calculator.py"
```
### 3.3. Um teste específico
```
pytest -v "Atv 2/test_person_DAO.py::TestPersonDAO::test_valid_person_ok"
```
