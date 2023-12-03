#Importação da ferramenta para reconhecer a voz
import speech_recognition as sr
#Importação da ferramenta para fazer o processo de automação no windows
import pyautogui as at



#Função que irá capturar o áudio do usuário
def ouvir_microfone():
    #Instanciação do método Recognizer, para reconhecer o áudio
    microfone = sr.Recognizer()
    
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Escolha uma das opção ou fale algo:")
        audio = microfone.listen(source)
        
    try:
        #Configurando para que o programa entenda a língua portuguesa
        frase = microfone.recognize_google(audio, language='pt-BR')
        
        #Mostra o foi dito pelo usuário
        print("Você falou: "+frase)
        
    except sr.UnknownValueError:
        print("Não entendi.")
        
    return frase

#Função que irá executar o Google
def exec_navegador():
    #Inicia o menu iniciar
    at.press('win')
    #Pesquisa o Google no menu iniciar
    at.write('google')
    #Executa o navegador
    at.press('Enter')
    print("Deseja pesquisar sobre o que?")
    frase = ouvir_microfone()
    at.write(frase)
    at.press('Enter')
    
    repete = True
    
    #Aqui no laço de repetição vai servir para que o usuário navegue pelo browser
    while repete:
        print("Quer pesquisar sobre oq na página?")
        frase = ouvir_microfone()
        #Rola o "scroll" baixo
        if "baixo" in frase:
            at.scroll(-300)
        #Rola o "scroll" para cima
        if "cima" in frase:
            at.scroll(300)
        #Pesquisa a opção que o usuário quer com as alternativas que o google sugerir
        if "pesquisar" in frase:
            novamente = True
            at.hotkey('ctrl','f')
            print("Esta procurando sobre o que?")
            frase = ouvir_microfone()
            at.write(frase)
            while novamente:
                print("Encontrou o que procura?")
                frase = ouvir_microfone()
                if "sim" in frase:
                    at.hotkey('ctrl','Enter')
                    novamente = False
                if "não" in frase:
                    at.hotkey('ctrl','g')
                if "sair" in frase:
                    novamente = False
        #Sair do Programa
        if "sair" in frase:
            repete = False

    
#Função que irá executar o Bloco de notas
def exec_bloco_de_notas():
    at.press('win')
    at.write('Bloco de notas')
    at.press('Enter')
    
    print("Deseja escrever algo?")
    frase = ouvir_microfone()
    at.write(frase)
    
    repete = True
    #Laço de repetição irá digitar tudo que o usuário dizer
    while repete:
        print("Quer escrever algo a mais?")
        resposta = ouvir_microfone()
        if "sim" in resposta:
            print("Fale a frase:")
            frase = ouvir_microfone()
            at.write(frase)
        if "não" in resposta:
            repete = False





#inicialização do programa usabilidade do Windows via comando de voz
repete = True
#estrutura de repetição para o usuário escolher sua opção
while repete:
    #prints da escolha do usuário
    print("Escolha uma das opções de navegação:\n 1 - Iniciar o Google \n 2 - Iniciar o bloco de notas \n 3 - Encerrar programa")
    #Função que vai receber o áudio do usuário
    frase = ouvir_microfone()
    #move o mouse no centro para facilitar o uso do "scroll" na página
    at.moveTo(960,540)
    
    
    #Google
    if "navegador" in frase or "1" in frase or "um" in frase:
        #ira executar o google
        exec_navegador()
    #Word
    if "escrever" in frase or "2" in frase or "dois" in frase:
        #ira executar o bloco de notas
        exec_bloco_de_notas()
    if "sair" in frase or "3" in frase or "três" in frase:
        #encerra o programa
        print("Encerrando programa")
        repete = False
