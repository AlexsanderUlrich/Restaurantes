import os

#nomes utilizando prints


def  exibir_nome_do_programa():
    print("""                                                           
                                            ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
                                            ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
                                            ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
                                            ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
                                            ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
                                            ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Excluir restaurante')
    print('5. sair')


#listas

restaurantes = []


#funções para cadastrar, excluir, listar, finalizar e validar


def voltar_ao_menu(): 
    voltar = input('\ndeseja voltar ao menu? S/N: ')
    if voltar == 's':
        main()
    elif voltar == 'S':
        main()
    elif voltar == '':
        main()
    else: 
        finalizar_app()


def cadastrar_restarante():
    restaurante = (input('\n\ndigite o nome do restaurante: '))
    restaurantes.append(restaurante)
    print(f'\nrestaurante {restaurante} cadsatrado com sucesso!!!')
    voltar_ao_menu()    
       

def listar_restaurantes():
    for item in restaurantes: 
        print(f'\n- {item}')
    voltar_ao_menu()


def excluir_restaurantes():
    excluir = input('\nDigite qual restaurante deseja excluir: ')
    restaurantes.remove(excluir)
    print(f'\nrestaurante {excluir} excluído com sucesso')
    voltar_ao_menu()


def finalizar_app():
    os.system('cls')
    print('\nprograma encerrado')    


def opcao_invalida():
    print('\nOpção Inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()


def escolher_opcao():

    try:
        opcao_escolhida = int( input('\nescolha uma opção: ') )

        if opcao_escolhida == 1: 
            cadastrar_restarante()

        elif opcao_escolhida == 2: 
            listar_restaurantes()

        elif opcao_escolhida == 3: 
            print('Ativar restaurante')

        elif opcao_escolhida == 4: 
            excluir_restaurantes()

        elif opcao_escolhida == 5: 
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()

#main

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
