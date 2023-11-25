import speech_recognition as sr
import pyautogui as at
import time as sleep

def ouvir_microfone():
    microfone = sr.Recognizer()
    
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Fale algo:")
        audio = microfone.listen(source)
        
    try:
        
        frase = microfone.recognize_google(audio, language='pt-BR')
            
        print("Você falou: "+frase)
        
    except sr.UnknownValueError:
        print("Não entendi.")
        
    return frase

def exec_navegador():
    at.press('win')
    at.write('google')
    at.press('Enter')
    print("Deseja pesquisar sobre o que?")
    frase = ouvir_microfone()
    at.write(frase)
    at.press('Enter')
    
    repete = True
    
    while repete:
        print("Quer pesquisar sobre oq na página?")
        frase = ouvir_microfone()
        if "baixo" in frase:
            at.scroll(-300)
        if "cima" in frase:
            at.scroll(300)
        if "pesquisar" in frase:
            novamente = True
            at.hotkey('ctrl','f')
            print("Oq procura?")
            frase = ouvir_microfone()
            at.write(frase)
            while novamente:
                print("Achou oq procura?")
                frase = ouvir_microfone()
                if "sim" in frase:
                    at.hotkey('ctrl','Enter')
                    novamente = False
                if "não" in frase:
                    at.hotkey('ctrl','g')
                if "sair" in frase:
                    novamente = False
            
        if "sair" in frase:
            repete = False

    
    
def exec_word():
    return print("entrou exec_word")





repete = True
while repete:
    frase = ouvir_microfone()
    at.moveTo(960,540)
    #Google
    if "navegador" in frase:
        exec_navegador()
    #Word
    if "Word" in frase:
        exec_word()
    if "sair" in frase:
        print("Encerrando programa")
        repete = False

#repete = True

#while repete:
    #print("Deseja mais alguma coisa?")
    #frase = ouvir_microfone()
    
    #if "encerrar execução Python" in frase:
        #repete = False