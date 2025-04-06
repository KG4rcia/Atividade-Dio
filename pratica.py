'''
# Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: 
# depósito, saque e extrato. 
# O sistema será desenvolvido para um banco que busca monetizar suas operações. 
# Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as
# operações bancárias. Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e 
# eficientes.
'''

BANCO = 0
LIMITESAQUEDIARIO = 0
LIMITESAQUE = 500
MANTENDOWHILE = 1
EXTRATO = ""

def menu():
    mensagem = input('''

        - > Bem vindo. Por favor, selecione uma opção:

        ====================================
        | [1] - Depositar valor. 
        | [2] - Sacar valor. 
        | [3] - Extrato. 
        | [4] - Sair.
        ====================================
        
        - > Sua escolha: ''')
    return mensagem

def depositar():
    Qtd_Valor = float(input("Digite um valor para deposito: "))
    if Qtd_Valor > 0:
        global BANCO
        BANCO += Qtd_Valor
        global EXTRATO
        EXTRATO += f'''

        Você fez um deposito de {Qtd_Valor:.2F} no banco! 
        
        '''
        
        valorexibir = f'''
                        
        Você tem R$: {BANCO:.2f} em seu banco!'''
        print(valorexibir)
        continuarOuNao = '''

        - > Você deseja continuar?

        ====================================
        | [ Não ]
        | [ Sim ]
        ====================================

        - > Sua resposta: '''

        respostaContinuar = input(continuarOuNao).lower()
        if respostaContinuar == "s" or respostaContinuar == "sim":
            return Qtd_Valor
        
        elif respostaContinuar == "não" or respostaContinuar == "n" or respostaContinuar == "nao":
            respostafinalizada = '''

        ====================================
        | Tudo bem, então vamos finalizar!
        ====================================
        '''
        print(respostafinalizada)
        mantendoWhile
        mantendoWhile -= 2
    else:
        print("Opção inválida. Tente novamente: ")
        return


 # Aqui vamos entrar com um while pra ficar repetindo o menu lá de opções

def sacarValor():
    global LIMITESAQUEDIARIO, BANCO
    if LIMITESAQUEDIARIO > 3:
        return print("O limite de saques diários foi atingido.")
    else:
        saque = int(input('''
                    
        - > Realizando Saque!


        ====================================                |
        | Quanto você deseja sacar?
        ====================================
                    
        - > Sua resposta: '''))
        global EXTRATO
        EXTRATO += f'''

        Você fez um saque de {saque:.2F} no banco! 
        
        '''
        if saque > LIMITESAQUE:
            print(f'''

            ==================
            | O seu limite de saque é {LIMITESAQUEDIARIO:.2f}! Você nâo pode ultrapassar esse valor!                  
            ==================
        ''')
        if saque <= BANCO:
            BANCO = BANCO - saque
            print("O valor foi sacado!")

            print("\n")
            exibirBanco = f'''

        - > Quanto tenho no banco?

        ====================================
        | Agora você tem R$: {BANCO:.2f} em seu banco!
        ====================================
        '''
            print(exibirBanco)
            
            LIMITESAQUEDIARIO += 1
        else:
            print(f'''
                  
        ====================================      
        | Você não tem saldo suficiente para sacar: {saque:.2f}, pois você: {BANCO:.2f} no banco!
        ====================================
        ''')

def exibirExtrato():
    exibindoExtrato = f'''

        ==================
        {EXTRATO}
        ==================

    '''
    print(exibindoExtrato)

while MANTENDOWHILE > 0:
    opcao = menu()
    if opcao == "1":
        # Aqui entra a função de deposito
        depositar()
    elif opcao == "2":
        sacarValor()
    elif opcao == "3":
        if not EXTRATO:
            print('''
            
        Extrato da sua conta!:
     
                  
        ==================
        |Não há nada.
        ==================
                  
                  
                  ''')
        else: 
            exibirExtrato()
    elif opcao == "4":
        # Função pra finalizar o bagulho
        finalizando2 = '''

        Extrato da sua conta!:

        ====================================
        | Entendi, nesse caso: Até logo! 
        ====================================
        
        '''
        print(finalizando2)
        MANTENDOWHILE -= 2

    else:
        print("Digite um valor válido.")