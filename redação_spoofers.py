import webbrowser
import time
import sys
import pyautogui 
import keyboard 

def print_s(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)  # Escreve o caractere
        sys.stdout.flush()       # Força a escrita no console
        time.sleep(delay)        # Espera um pouco antes de imprimir o próximo caractere
    print()  # Pula uma linha após a mensagem

print_s("---Seja bem vindo a legião Spoofers---", delay=0.08)
print("█▀▀▀█ █▀▀█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀█ █▀▀")
print("▀▀▀▄▄ █░░█ █░░█ █░░█ █▀▀ █▀▀ █▄▄▀ ▀▀█")
print("█▄▄▄█ █▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀░░ ▀▀▀ ▀░▀▀ ▀▀▀")
print("Created by MrWr3nch")
print_s("AVISO!", delay=0.1)
print_s("Ao terminar de digitar a redação no terminal esteja com o redação paraná aberto, selecione o campo de digitar no redão paraná e espere", delay=0.01)
print_s("Escreva a redação aqui:", delay=0.01)

redação = input("")

print("Executando em 7 segundos...")
time.sleep(7) 
pyautogui.typewrite(redação)


    




