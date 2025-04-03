# Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: 
# depósito, saque e extrato. 
# O sistema será desenvolvido para um banco que busca monetizar suas operações. 
# Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as
#  operações bancárias. Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e 
# eficientes.
banco = 0

mantendoWhile = 1

mensagem = '''

    - > Bem vindo. Por favor, selecione uma opção:

    ==================
    | [1] - Depositar valor. 
    | [2] - Sacar valor. 
    | [3] - Extrato. 
    | [4] - Sair.
    ==================
    
    - > Sua escolha: '''

while mantendoWhile > 0:
    menu = input(mensagem).lower()
    if menu == "1":
        Qtd_Valor = float(input("Digite um valor para deposito: ")) 
        banco += Qtd_Valor

        valorexibir = f'''
        
        Você tem R$: {banco:.2f} em seu banco!'''
        print(valorexibir)
        continuarOuNao = '''

        - > Você deseja continuar?

        ==================
        | [ Não ]
        | [ Sim ]
        ==================

        - > Sua resposta: '''

        respostaContinuar = input(continuarOuNao).lower()
        if respostaContinuar == "s" or respostaContinuar == "sim":
            continue
        elif respostaContinuar == "não" or respostaContinuar == "n" or respostaContinuar == "nao":
            respostafinalizada = '''

        ==================
        | Tudo bem, então vamos finalizar!
        ==================

        '''
            print(respostafinalizada)
            mantendoWhile -= 2
        else:
            print("Opção inválida. Tente novamente: ")
            print(respostaContinuar)
    elif menu == "4":
        finalizando2 = '''

        ==================
        | Entendi, nesse caso: Até logo!
        ==================
        
        '''
        print(finalizando2)
        mantendoWhile -= 2