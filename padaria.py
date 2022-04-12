lista_clientes = [];
lista_funcionarios = [];
lista_produtos = [];
faturamento = 0

class Sacola():
    def __init__(self, Produto, quantidade):
        self.Produto = Produto
        self.quantidade = quantidade
        
class Cliente():
    def __init__(self, nome, cpf, email, celular):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.celular = celular

class Funcionario():
    def __init__(self, nome, cargo, matricula, cpf, email, celular):
        self.nome = nome
        self.cargo = cargo
        self.matricula = matricula
        self.cpf = cpf
        self.email = email
        self.celular = celular

class Produto():
    def __init__(self, nome, preco, validade, estoque, tipo, descricao, data_de_fabricacao):
        self.nome = nome
        self.preco = preco
        self.validade = validade
        self.estoque = estoque
        self.tipo = tipo
        self.descricao = descricao
        self.data_de_fabricacao = data_de_fabricacao
        
def cadastrar_novo_cliente(lista_cliente, Cliente):
    nome_novo_cliente = input("Digite seu nome: ")
    cpf_novo_cliente = input("Digite seu CPF: ")
    email_novo_cliente = input("Digite seu email: ")
    celular_novo_cliente = input("Digite seu celular: ")
        
    novo_cliente = Cliente(nome_novo_cliente, cpf_novo_cliente, email_novo_cliente, celular_novo_cliente)
    lista_cliente.append(novo_cliente)
        
    print("Cadastro feito com sucesso")
    print(novo_cliente)

def cadastrar_novo_produto(Produto):
    print("Digite o nome do produto: ")
    novo_produto = input("Nome: ")
    novo_produto_preco = input("Preço: ")
    novo_produto_validade = input("Validade: ")
    novo_produto_estoque = input("Estoque: ")
    novo_produto_tipo = input("Tipo: ")
    novo_produto_descricao = input("Descrição: ")
    novo_produto_data_de_fabricacao = input("Data de Fabricacao: ")

    novo_produto = Produto(novo_produto,
                        novo_produto_preco,
                        novo_produto_validade,
                        novo_produto_estoque,
                        novo_produto_tipo,
                        novo_produto_descricao,
                        novo_produto_data_de_fabricacao)    
    
    lista_produtos.append(novo_produto)
    print("\nProduto cadastrado com sucesso o/")
       

pao = Produto("pao", 1.0, "03/13", 5, "frances", "feito de trigo quentinho", "12/12")
lista_produtos.append(pao)

queijo = Produto("queijo prato", 2.0, "04/12", 5, "queijo prato da casa", "da fazendo do seu joão", "07/12")
lista_produtos.append(queijo)

quindim = Produto("quindim", 3.0, "04/12", 5, "doce", "açucar, coco ralado, manteiga e ovo", "07/12")
lista_produtos.append(quindim)

claudio = Cliente("claudio", "123", "email@gmail.com", "9999.9999")
lista_clientes.append(claudio)

anderson = Funcionario("Anderson", "gerente", "121", "2222222", " email@email.email", "8888.8888")
lista_funcionarios.append(anderson)

while True:
    print("---------------------PADARIA DOS CRIA---------------------")
    print("\n Você é cliente ou trabalha aqui meu rei?")

    cliente_ou_funcionario = input("1- Cliente\n2- Funcionário\n")

    if cliente_ou_funcionario == "1" or cliente_ou_funcionario.lower() == "cliente":
        cadastro = input("Você possui cadastro?\n1- Sim\n2- Não\n")
        
        if cadastro == "1":
            cpf = input("Digite seu CPF: ")
            cpf_errado = True
            
            for cliente in lista_clientes:
                
                if cliente.cpf == cpf:
                    carrinho = []
                    cpf_errado = False
                    
                    print("Bem vindo " + cliente.nome)
                    print("\nAcessar padaria?\n1- Sim\n2- Não")
                    
                    pre_menu = int(input(""))
                    while pre_menu == 1:
                        
                        for produto in lista_produtos:
                            print(f"{ lista_produtos.index(produto) + 1 }- {produto.nome}")
                            
                        print("0- Caso tenha finalizado sua compra :)")    
                        menu = int(input("digite uma opção: "))
                        
                        if menu != 0 and menu <= len(lista_produtos):
                            quantidade = int(input("\nDigite a quantidade: "))
                            sacola = Sacola(lista_produtos[menu - 1], quantidade)
                            carrinho.append(sacola)                    
    
                        elif menu >= len(lista_produtos):
                            print("Digite um produto válido")
                            
                        else:
                            total_compra = 0
                            teste = 0
                            
                            for sacola in carrinho:
                                print(f"quantidade: {sacola.quantidade} | preco: {sacola.Produto.preco}")
                                teste = sacola.quantidade * sacola.Produto.preco
                                total_compra = total_compra + teste
                                
                            print(f"O valor total de sua compra é de R${total_compra:.2f}")
                            faturamento = faturamento + total_compra
                            break
            if cpf_errado:
                print("Cpf ínvalido :(")
                
        else :
            cadastrar_novo_cliente(lista_clientes, Cliente)
            
    elif cliente_ou_funcionario == "2" or cliente_ou_funcionario.lower == "funcionario":
        matricula = input("Digite sua matricula: ")
        
        for funcionario in lista_funcionarios:
            
            if funcionario.matricula == matricula:
                print("Bem-vindo " + funcionario.nome);         
                print("Modificar padaria?\n1- Sim\n2- Não")
                preAdm = int(input(""))
                
                while preAdm == 1:
                    print("----Menu----\n1- Adicionar produtos\n2- Modificar produtos\n3- Visualizar faturamento\n0- Sair")
                    menuAdm = int(input(""))
                    
                    if menuAdm == 1:
                        cadastrar_novo_produto(Produto)
                        
                    if menuAdm == 2:
                        print(f"\n{funcionario.nome} qual produto você deseja mudar?")
                        
                        for produto in lista_produtos:
                            print(f"{ lista_produtos.index(produto) + 1 }- {produto.nome}")
                        print("0- Caso tenha finalizado sua compra :)") 
                        
                        menu = int(input("Digite uma opção: "))
                        
                        if menu != 0 and menu <= len(lista_produtos):
                            modificacao = input("\n O que você deseja modificar? \n nome \n preco \n estoque \n tipo \n fabricacao")
                            novo_valor = input("Agora qual valor você deseja que tenha?")
                            setattr(lista_produtos[menu - 1], modificacao, novo_valor)
    
                        elif menu >= len(lista_produtos):
                            print("Digite um produto válido :)")
                            
                        else:
                            break
                    elif menuAdm == 3:
                        print(f"Faturamento da Padaria dos Cria:\nR${faturamento:.2f}")      
                                                         
                    else:
                        break    
            else:
                print("matricula invalida!")
                
    else:
        print("Número invalido :p")
