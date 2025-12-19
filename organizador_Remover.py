import gspread
from google.oauth2.service_account import Credentials as cr

scopes = ["https://www.googleapis.com/auth/spreadsheets"]

creds = cr.from_service_account_file(
    "credentials.json", scopes=scopes
)
client = gspread.authorize(creds)

planilha = client.open_by_key("1miANfO48_yZh8T-wX7LFO7Eg7y7STk0KyBG_uob5oQU")
linha = planilha.sheet1

nome_procurado = input("Informe o nome do documento a remover: ")

dados = linha.get_all_values()

for i, row in enumerate(dados[1:], start=2):
    if row[0] == nome_procurado:  
        linha.delete_rows(i)
        print("Documento removido com sucesso!")
        break
else:
    print("Documento não encontrado.")
