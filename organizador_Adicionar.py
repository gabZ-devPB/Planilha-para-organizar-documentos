import gspread
from google.oauth2.service_account import Credentials as cr

scopes = ["https://www.googleapis.com/auth/spreadsheets"]

creds = cr.from_service_account_file(
    "credentials.json", scopes=scopes
)
client = gspread.authorize(creds)

planilha = client.open_by_key("1miANfO48_yZh8T-wX7LFO7Eg7y7STk0KyBG_uob5oQU")
linha = planilha.sheet1

nome_documento = input("Informe o Nome do Documento: ")
tipo_documento = input("Qual o tipo do Documento:  ")
link = input("Informe o link do Documento: ")
autor = input("Informe o autor do Documento: ")

linha.append_row([
    nome_documento,
    tipo_documento,
    link,
    autor
])

print("Dados adicionados com sucesso!")
