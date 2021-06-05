def entrada(texto):
    print('-=' * 30)
    print(texto)
    print('-=' * 30)
entrada('           SEJA BEM-VINDO AO NOSSO MICROBLOGGING')

def registrarUsuario(lista):
    arquivo = open('usuario.txt', 'w')

    for dados in lista:
        arquivo.write('{}#{}#{}#{}\n'.format(dados['email'], dados['nome'], dados['apelido'], dados['idade']))

    arquivo.close()
def registrarPost(lista):
    arquivo=open('post.txt','w')
    for dado in lista:
        arquivo.write('{}\n'.format(dado['postagem']))
    arquivo.close()

def carregarUsuario():
    lista = []

    try:
        arquivo = open('usuario.txt', 'r')

        for linha in arquivo.readlines():
            coluna = linha.strip().split('#')
            dados = {
                'email': coluna[0],
                'nome': coluna[1],
                'apelido': coluna[2],
                'idade': coluna[3],
                }

            lista.append(dados)

        arquivo.close()
    except FileNotFoundError:
        pass
    
    return lista
def carregarPost(lista):
    try:
        arquivo=open('post.txt','r')
        for linha in arquivo.readlines():
            coluna=linha.strip().split('#')
            dado={'postagem':coluna[0]}
            lista.append(dado)
            arquivo.close()
    except FileNotFoundError:
        pass
    return lista

def existeUsuario(lista, email):
    if len(lista) > 0:
        for dados in lista:
            if dados['email'] == email:
                return True
    return False


def adicionarUsuario(lista):

    while True:
        email = str(input('Email: '))

        if not existeUsuario(lista, email):
            break
        else:
            print('Esse email já existe!')
            print('Por favor, tente novamente.')

    dados = {
        'email': email,
        'nome': str(input('Nome: ')),
        'apelido': str(input('Apelido: ')),
        'idade': int(input('Idade: '))
    }


    lista.append(dados)

    print('O usuário {} foi cadastrado com sucesso!\n '.format(dados['nome']))


def excluirUsuario(lista):
    print('== EXCLUIR USUÁRIO ==')
    if len(lista) > 0:
        email = input('Digite o email do usuário a ser excluído: ')
        if existeUsuario(lista, email):
            for i, dados in enumerate(lista):
                if dados['email'] == email:
                    print('Nome: {}'.format(dados['nome']))
                    print('Apelido: {}'.format(dados['apelido']))
                    print('Idade: {}'.format(dados['idade']))
                    print('-=' * 13)

                    del lista[i]

                    print('O usuário foi apagado com sucesso! ')

        else:
            print('Não existe nenhum usuário cadastrado com esse email {}\n'.format(email))


    else:
        print('Não existe nenhum usuário cadastrado nesse sistema.')


def exibirUsuario(lista):
    print('== LISTA DE USUÁRIOS ==')
    if len(lista) > 0:
        for i, dados in enumerate(lista):
            print('Usuário {}: '.format(i+1))
            print('\tNome: {}'.format(dados['nome']))
            print('\tApelido: {}'.format(dados['apelido']))
            print('\tIdade: {}'.format(dados['idade']))
            print('-=' *13)

        print('O nosso sistema possui {} usuários.'.format(len(lista)))
    else:
        print('Não existe nenhum usuário cadastrado nesse sistema.')
        


def exibirPostagem(lista):
    if len(lista) > 0:
        email = input('Digite o email: ')
        if existeUsuario(lista, email):
            for i,dado in enumerate(lista):
                arquivo=open('post.txt','r')
                ler=arquivo.read()
                print(ler)
                arquivo.close()
            else:
                print('Não há postagens')
def criarPost(lista):
    print('== CRIAR POST ==')
    if len(lista) > 0:
        email = input('Digite o email: ')
        if existeUsuario(lista, email):
            for i,dado in enumerate(lista):
                postagem = input('Digite sua postagem: ')
                while len(postagem) > 120:
                    print('== VOCÊ ULTRAPASSOU O LIMITE DE CARACTERES ==')
                    postagem = input('Digite sua postagem: ')

        else:
            print('Usuário não encontrado. ')
            print('Tente novamente...')
    else:   
        print('Não existe nenhum usuário cadastrado nesse sistema.')
    post={'postagem':postagem}
    
    print('== SUA MENSAGEM FOI SALVA ==')
    lista.append(post)

def exibirDados(lista):
    print('== DADOS DO USUÁRIO ==')
    if len(lista) > 0:
        email = input('Digite o email do usuário a ser encontrado: ')
        if existeUsuario(lista, email):
            if dados['email'] == email:
                print('Nome: {}'.format(dados['nome']))
                print('Apelido: {}'.format(dados['apelido']))
                print('Idade: {}'.format(dados['idade']))
                print('-=' * 13)

        else:
            print('Não existe nenhum usuário cadastrado com esse email {}\n'.format(email))


    else:
        print('Não existe nenhum usuário cadastrado nesse sistema.')



def menuPrincipal():

    lista = carregarUsuario()
    while True:
        print('Digite 1 para cadastrar um novo usuário: ')
        print('Digite 2 para excluir um usuário: ')
        print('Digite 3 para exibir todos os usuários: ')
        print('Digite 4 para buscar e exibir dados de um usuário: ')
        print('Digite 5 para exibir as postagens de um usuário: ')
        print('Digite 6 para criar um novo post com um usuário: ')
        print('Digite 0 para sair: ')
        opcao = int(input('>> '))

        if opcao == 1:
            adicionarUsuario(lista)
            registrarUsuario(lista)
        elif opcao == 2:
            excluirUsuario(lista)
            registrarUsuario(lista)
        elif opcao == 3:
            exibirUsuario(lista)
        elif opcao == 4:
            exibirDados(lista)
        elif opcao == 5:
            carregarPost(lista)
            exibirPostagem(lista)
        elif opcao == 6:
            carregarPost(lista)
            registrarPost(lista)
            criarPost(lista)
        elif opcao == 0:
            print('SAINDO DO PROGRAMA...')
            break
        else:
            print('-=' * 30)
            print(' A opção escolhida é inválida. Por favor, tente novamente!  ')
            print('-=' * 30)

menuPrincipal()
