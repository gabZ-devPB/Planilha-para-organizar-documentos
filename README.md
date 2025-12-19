# 📄 Cadastro de Documentos no Google Sheets com Python

Este projeto utiliza **Python** e a **Google Sheets API** para realizar o cadastro automático de documentos em uma planilha do Google Sheets, funcionando como um pequeno banco de dados online.

---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **gspread**
- **google-auth**
- **Google Sheets API**

---

## 📌 Objetivo do Projeto

Permitir que o usuário:
- Insira informações de documentos via terminal
- Armazene esses dados automaticamente em uma planilha do Google Sheets
- Mantenha os registros organizados e prontos para análise ou dashboards

---

## 🧠 Funcionamento do Código

### 1️⃣ Importação das bibliotecas
```python
import gspread
from google.oauth2.service_account import Credentials as cr
