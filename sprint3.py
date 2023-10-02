import re


def menu_sair():
    while True:
        escolha_sair = input(
            "RETORNAR AO MENU - 1 | SAIR - 2: ")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        if escolha_sair == "2":
            print("Fechando o programa...")
            exit()
        elif escolha_sair == "1":
            print("Retornando ao menu...")
            break
        else:
            print(
                "Resposta inválida. Digite '1' para retornar ao menu ou '2' para sair.")


def mostrar_topicos():
    print("                        -------------")
    print("1. QUEM SOMOS? -->      |     1     |")
    print("                        -------------")
    print("                        -------------")
    print("2. INUNDAÇÕES  -->      |     2     |")
    print("                        -------------")
    print("                        -------------")
    print("3. APLICATIVO  -->      |     3     |")
    print("                        -------------")
    print("                        -------------")
    print("4. CONFIANÇA   -->      |     4     |")
    print("                        -------------")
    print("                        -------------")
    print("5. CADASTRO    -->      |     5     |")
    print("                        -------------")
    print("                        -------------")
    print("6. LOGIN       -->      |     6     |")
    print("                        -------------")
    print("                        -------------")
    print("7. SAIR        -->      |     7     |")
    print("                        -------------")


def validar_email(email):
    if "@" not in email:
        return False
    return True


def validar_nome(nome):
    return bool(re.search("^[a-zA-Z]+$", nome))


def cadastrar_usuario():
    print("Cadastro de Usuário: \n")
    nome = input("Digite seu nome: ")

    while not validar_nome(nome):
        print("O nome deve conter apenas letras. Tente novamente.")
        nome = input("Digite seu nome novamente: ")

    email = input("Digite seu email: ")

    while not validar_email(email):
        print("Formato de email inválido. Tente novamente.")
        email = input("Digite seu email novamente: ")

    senha = input(
        "Digite sua senha (deve conter pelo menos 4 dígitos, incluindo letras e números): ")
    while not re.search(r"^(?=.*[A-Za-z])(?=.*\d).{4,}$", senha):
        print("A senha deve conter pelo menos 4 dígitos.")
        senha = input("Digite sua senha novamente: ")

    confirma_senha = input("Confirme sua senha: ")
    while senha != confirma_senha:
        print("As senhas não coincidem. Tente novamente.")
        senha = input("Digite sua senha: ")
        confirma_senha = input("Confirme sua senha: ")

    print("Cadastro concluído com sucesso!")
    print("--------------------------------------------------------------")

    usuario = {
        "Nome": nome,
        "Email": email,
        "Senha": senha
    }

    return usuario


print("--------------------------------------------------------------")
print("|                   Bem vindo a SafeFlood!                   |")
print("--------------------------------------------------------------")
print("Estamos aqui para ajudar você a se preparar para as enchentes!")
print("--------------------------------------------------------------")


usuarios = {}

try:
    while True:
        mostrar_topicos()
        escolha_do_usuario = input(
            "Escolha uma opção para prosseguir (1 a 7): ")

        match escolha_do_usuario:
            case "1":
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("QUEM SOMOS?\n")
                print("Nós somos a SafeFlood, Nossa solução é um aplicativo de prevenção de danos causados por enchentes que funciona através de alertas a moradores de casas e estabelecimentos que poderão ser afetados, tudo isso de maneira prévia, operando através de dispositivos conectados nas áreas de início das enchentes, que fazem a leitura da altura do alagamento nesses lugares e notificam através do aplicativo para os usuários, auxiliando-os a se prepararem para o desastre, poupando vidas e danos materiais.")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                menu_sair()
            case "2":
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("INUNDAÇÕES\n")
                print("O Brasil tem 3,9 milhões de pessoas que vivem em 13.297 áreas de risco. Dessas, quatro mil localidades são classificadas como de “risco muito alto”, de deslizamentos e inundações, por exemplo. Já o número de áreas classificadas como de “risco alto” é de 9.291 de acordo com https://agenciabrasil.ebc.com.br/, ou seja, estamos combatendo um grande problema que é recorrente em todo território nacional.")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                menu_sair()
            case "3":
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("APLICATIVO\n")
                print("Criamos um aplicativo focado em alertar os usuários sobre as possíveis cheias baseadas na proximidade da sua moradia/estabelecimento ou em alguma rota diária da ocorrência, diminuindo a possibilidade de afetar suas casas, além de evitar que um trecho alagado atrase seu caminho cotidiano. O app notificará  o possível início do desastre, também aparecerá dados meteorológicos da região e a probabilidade de atingir seu local (baseado na altura da água medida por nossos dispositivos).")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                menu_sair()
            case "4":
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("CONFIANÇA\n")
                print("Nossos dispositivos sensores de água garantem a melhor precisão de dados possível, sendo esses dados visualizáveis por nossos usários dentro do aplicativo, sabemos que a confiança é essencial nesses momentos. O sensor de água fica instalado próximos aos locais iniciais das enchentes, que leva em conta históricos locais das regiões, o dispositivo está conectado ao nosso aplicativo, que considera o raio de risco da enchente, avisando os moradores cadastrados no app o mais rápido possível")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                menu_sair()
            case "5":
                print("--------------------------------------------------------------")
                print("Opção 5 selecionada. Fazer cadastro.")
                print("--------------------------------------------------------------")
                usuario = cadastrar_usuario()
                email_usuario = usuario["Email"]
                usuarios[email_usuario] = usuario
            case "6":
                print("--------------------------------------------------------------")
                print(
                    "Opção 6 selecionada. Fazer login. Não se esqueça que precisa possuir um cadastro para logar.\n")
                escolha_prosseguir = input(
                    "PROSSEGUIR - 1 | VOLTAR E REALIZAR CADASTRO - 2: ")
                print("--------------------------------------------------------------")
                while True:
                    if escolha_prosseguir == "2":
                        print("Voltando...")
                        print("--------------------------------------------------------------")
                        break
                    elif escolha_prosseguir == "1":
                        print("Prosseguindo com login... \n")
                        email_login = input("Digite seu email: ")
                        senha_login = input("Digite sua senha: ")
                        if email_login in usuarios and usuarios[email_login]["Senha"] == senha_login:
                            print(
                        f"Login bem-sucedido! Bem-vindo, {usuarios[email_login]['Nome']}!")
                            menu_sair()
                        else:
                            print("\nEmail ou senha incorretos. Retornando para o menu...")
                            break
                    else:
                        print(
                            "Resposta inválida. Digite '1' para retornar ao menu ou '2' para sair.")

            case "7":
                escolha_sair = input("Deseja realmente sair? (S/N): ")
                if escolha_sair.lower() == "s":
                    print("Fechando o programa...")
                    print("Opção 7 selecionada. Até logo, foi um prazer!")
                    break
                elif escolha_sair.lower() == "n":
                    continue
                else:
                    print(
                        "Resposta inválida. Digite 'S' para sair ou 'N' para continuar.")
            case _:
                print("\n\nEscolha uma opção válida (1 a 7).")

except ValueError:
    print("Valor Inválido, tente novamente.")
