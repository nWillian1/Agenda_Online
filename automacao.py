import pyautogui # Biblioteca para automação de cliques e teclas
import time # Biblioteca para manipulação do tempo 

pyautogui.PAUSE = 1 # Pausa de 1 segundo entre cada comando do pyautogui

pyautogui.press('win') # Abre o menu iniciar
pyautogui.write('chrome') # Escreve "o navegador padrão"
pyautogui.press('enter') # Abre o navegador padrão

time.sleep(1)

pyautogui.click(x=687, y=63) # Clica na barra de endereços
pyautogui.write('https://agenda-online-nx9c.vercel.app/') # Escreve o endereço do site
pyautogui.press('enter') # Acessa o site

time.sleep(2) # Espera o site carregar

import pandas # Biblioteca para manipulação de tabelas

tabela = pandas.read_csv('telefonica.csv') # Lê a tabela
print(tabela) # Mostra a tabela

for linhas in tabela.index: # Para cada linha na tabela
    pyautogui.click(x=835, y=339) # Clica no campo "NOME"
    nome = tabela.loc[linhas, 'NOME'] # Pega o nome da linha atual
    pyautogui.write(nome) # Escreve o nome
    pyautogui.press('tab') # Vai para o próximo campo
    time.sleep(0.5) # Espera meio segundo para o campo carregar
    telefone = tabela.loc[linhas, 'TELEFONE'] # Pega o telefone da linha atual
    pyautogui.write(telefone) # Escreve o telefone
    pyautogui.press('tab') # Vai para o botão "cadastrar"
    pyautogui.press('enter') # Clica no botão "cadastrar"
    time.sleep(0.5) # Espera meio segundo para o cadastro ser realizado