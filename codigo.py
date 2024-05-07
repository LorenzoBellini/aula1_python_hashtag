# Pra Instalar a biblioteca: pip install pyautogui
import pyautogui #Comando para imoprtar a biblioteca de comandos "pyautogui"
import time #Comando para importar a biblioteca de comandos "time"
import pandas as pd #Comando para importar as funcionalidades do pandas 
'''Caso queira importar alguma biblioteca de comandos com nome específico, tem como:
import pyautogui as pa
import pandas as pd
Aí toda vez que for escrever o comando, usar a abreviação de escolha'''

pyautogui.PAUSE = 0.6 #Comando para definir o intervalo de tempo entre uma linha de código e outra

# 1 Comandos para abrir o navegador: 
pyautogui.press("win") #Comando para apertar a tecla window
pyautogui.write("chrome") #Comando para escrever "Chrome"
pyautogui.press("enter")

# 2 Comandos para abrir o site da "empresa":
time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# 3 Comandos para fazer Login no site. !!!!!!!ver o comando auxiliar!!!!!
pyautogui.click(x=510, y=377)
pyautogui.write("login.lorenzo@teste.com")
pyautogui.press("tab")
pyautogui.write("Senha de verdade em")
pyautogui.press("enter")

# 4 Comandos para abrir/ importar a base de dados de produtos. Instalar o Pandas, numpy e openpyxl
tabela = pd.read_csv("produtos.csv") # Abrir o código no mesmo lugar do arquivo de base de dados, caso não faça isso tem que passar o caminho todo do arquivo pra ler

# 5 Comandos para cadastrar um produto

for linha in tabela.index:
    codigo = tabela.loc[linha, coluna]
    pyautogui.click(x=438, y=256)

    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write("Marca")
    pyautogui.press("tab")

    pyautogui.write("Tipo")
    pyautogui.press("tab")

    pyautogui.write("Categoria")
    pyautogui.press("tab")

    pyautogui.write("Preco")
    pyautogui.press("tab")

    pyautogui.write("Custo")
    pyautogui.press("tab")

    pyautogui.write("Obs")
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)

# 6 Comandos para repetir os passos acima até que a lista acabe



