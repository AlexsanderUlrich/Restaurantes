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
    print('3. Ativar/Inativar restaurante')
    print('4. Excluir restaurante')
    print('5. sair')

def sub_titulo():
    os.system('cls')
    exibir_nome_do_programa()

#listas

restaurantes = [
    {
    'nome': 'Bauru',
    'categoria' : 'Lancheria',
    'status': False
},
    {
    'nome': 'Dinapoli',
    'categoria' : 'Pizzaria',
    'status': False
},
    {
    'nome': 'Arigato',
    'categoria' : 'Sushiria',
    'status': True
}
]


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
    sub_titulo()

    nome = (input('\n\ndigite o nome do restaurante: '))
    categoria = (input('\n\ndigite a categoria do restaurante: '))
    restaurante = {'nome': nome, 'categoria' : categoria, 'status' : False} 
    

    restaurantes.append(restaurante)
    print(f'\nRestaurante {nome} cadsatrado, só agradece!!!')
    voltar_ao_menu()    
       

def listar_restaurantes():   
    sub_titulo()
    print(f'{'NOME DO RESTAURANTE:'.ljust(23)}  {'CATEGORIA:'.ljust(21)}  STATUS:\n')
    for item in restaurantes: 
        nome = item['nome']
        categoria = item['categoria']
        status = 'Ativo' if item['status'] else 'Inativo'

        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {status} \n' ) 

    voltar_ao_menu()


def apenas_listar_restaurantes():    
    print(f'{'NOME DO RESTAURANTE:'.ljust(23)}  {'CATEGORIA:'.ljust(21)}  STATUS:\n')
    for item in restaurantes: 
        nome = item['nome']
        categoria = item['categoria']
        status = 'Ativo' if item['status'] else 'Inativo'

        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {status} \n' ) 


def excluir_restaurantes():
    sub_titulo()

    nome = input('\nDigite qual restaurante deseja excluir: ')
    excluir = {'nome': nome}
    
    restaurantes.remove({'nome': nome})
    print(f'\nJá é, o restaurante {nome} foi de arrasta!')
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
            alterar_status()

        elif opcao_escolhida == 4: 
            excluir_restaurantes()

        elif opcao_escolhida == 5: 
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()


def alterar_status():
    sub_titulo()
    apenas_listar_restaurantes()

    nome = input(f'\nManda pro pai qual restaurente que alterar: ')
    encontrado = False

    for item in restaurantes:
        if nome == item['nome']:
            encontrado = not encontrado
            item['status'] = not item['status']
            mensagem = f'\nFechou, o {nome} tá ativado irmão!!!' if item['status'] else f'\nFechou, o {nome} está inativado Cupinxa!!!'
            print(mensagem)
            voltar_ao_menu()
            
            

    if not encontrado:
        print(f'\n -Digita esse nome direito por favor, olha o jeito que tu escreveu essa merda: {nome}')
        voltar = input('\nQuer tentar de novo, escrevendo direito dessa vez? S/N: ')
        if voltar == 's':
            alterar_status()
        elif voltar == 'S':
            alterar_status()
        elif voltar == '':
            alterar_status()
        else: 
            finalizar_app()


#main

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
