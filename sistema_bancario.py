# Operações a fazer:
# Separar funções existentes de saque, deposito e extrato em funções
# Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária

from datetime import datetime

## Função para exibir o menu de operações
def menu():
    menu = """\n

    Seja muito bem-vindo ao Banco DevBrito.py!

    ========= MENU DE OPERAÇÕES =========
    Por favor, selecione a operação desejada:
    [c]\t Cadastrar usuário
    [a]\t Cadastrar conta bancária
    [l]\t Listar usuários
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [q]\t Sair
    => """
    
    return input(menu).lower()

# Decorador de log para data e hora
def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        if func.__name__ in ["depositar", "sacar"]:
            if resultado is not None:
                print(f"Transação de {func.__name__} realizada em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print(f"Tentativa de {func.__name__} falha em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        elif func.__name__ == "exibir_extrato":
            print(f"Extrato atualizado desde de: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        elif func.__name__ in ["cadastrar_usuario", "cadastrar_conta"]:
            if resultado is not None:
                print(f"Operação de {func.__name__} realizada em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print(f"Tentativa de {func.__name__} falha em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return resultado
    return envelope

# ---------------------------------------
# Funções de Cadastro de Usuário e Conta Bancária e Listagem de Usuários
# ---------------------------------------
# Cadastrar usuário
@log_transacao # Decorador de log aplicado à função cadastrar_usuario, para registrar a data e hora da transação
def cadastrar_usuario(dic_usuarios, /):
    cpf = input("Informe o CPF (somente números): ")
    # Validando o CPF
    if not validar_cpf(cpf):
        return
    # Validando se o usuário já existe no dicionário de usuários
    if verificar_usuario(dic_usuarios, cpf):
        print("Já existe um usuário cadastrado com esse CPF.")
        return
    # Coletando os dados do usuário para cadastro
    nome = input("Informe o nome completo: ")
    # Validando o nome
    if not validar_nome(nome):
        return
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    # Validando a data de nascimento
    if not validar_data_nascimento(data_nascimento):
        return
    endereco = input("Informe o endereço (rua, número - bairro - cidade/sigla do estado): ")
    if endereco.strip() == "":
        print("Endereço inválido. O endereço não pode estar vazio.")
        return
    
    # Armazenando os dados no dicionário de usuários
    dic_usuarios[cpf] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "contas": []
    }
    # Mensagem de sucesso no cadastro, incluindo o nome do usuário
    print(f"\nUsuário {nome} cadastrado com sucesso! Seja bem-vindo ao Banco DevBrito.py!")
# Cadastrar conta bancária
@log_transacao # Decorador de log aplicado à função cadastrar_conta, para registrar a data e hora da transação
def cadastrar_conta(dic_usuarios, dic_contas_bancarias, N_AGENCIA, /):
    cpf = input("Informe o CPF do usuário desejado: ")

    if not verificar_usuario(dic_usuarios, cpf):
        print("Usuário não encontrado. Cadastre o usuário antes.")
        return

    numero_conta = len(dic_contas_bancarias) + 1

    nova_conta = {
        "agencia": N_AGENCIA,
        "numero_conta": numero_conta,
        "titular": dic_usuarios[cpf]["nome"]
    }

    dic_contas_bancarias[numero_conta] = nova_conta
    dic_usuarios[cpf]["contas"].append(numero_conta)

    print("\nConta criada com sucesso!")
    print(f"Agência: {nova_conta['agencia']}")
    print(f"Número da Conta: {nova_conta['numero_conta']}")
    print(f"Titular: {nova_conta['titular']}")
# Listar usuários e suas contas bancárias
def listar_usuarios(dic_usuarios, dic_contas_bancarias, /):
    if not dic_usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    for cpf, dados in dic_usuarios.items():
        print(f"CPF: {cpf}")
        print(f"  Nome: {dados['nome']}")
        print(f"  Data de Nascimento: {dados['data_nascimento']}")
        print(f"  Endereço: {dados['endereco']}")

        if "contas" in dados and dados["contas"]:
            print("  Contas:")
            for numero in dados["contas"]:
                conta = dic_contas_bancarias[numero]
                print(f"    Agência: {conta['agencia']} | Conta: {conta['numero_conta']}")
        else:
            print("  Não possui conta cadastrada.")

        print("-----------------------------------")

# ---------------------------------------
# Funções de Validação de Dados
# ---------------------------------------
# Verificar se o usuário já existe no dicionário de usuários
def verificar_usuario(dic_usuarios, cpf):
    return cpf in dic_usuarios
# Validar o CPF
def validar_cpf(cpf):
    if not cpf.isdigit() or len(cpf) != 11:
        print("O CPF digitado está inválido. Deve conter 11 números.")
        return False
    return True
# Validar o nome
def validar_nome(nome):
    if nome.strip() == "" or any(char.isdigit() for char in nome):
        print("Nome inválido.")
        return False
    return True
# Validar a data de nascimento
def validar_data_nascimento(data_nascimento):
    if len(data_nascimento) != 10 or data_nascimento[2] != "/" or data_nascimento[5] != "/":
        print("Formato inválido. Use DD/MM/AAAA.")
        return False

    dia, mes, ano = data_nascimento.split("/")
    if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
        print("Data inválida.")
        return False

    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    if not (1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 2024):
        print("Data inválida.")
        return False

    return True

# ---------------------------------------
# Funções de Operações Bancárias
# ---------------------------------------
# Realizar depósitos com os argumentos posicionais valor, saldo e extrato por isso a barra
@log_transacao # Decorador de log aplicado à função depositar, para registrar a data e hora da transação
def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t R$ {valor:.2f}\n"
        print("Depósito efetuado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
        return
    return saldo, extrato
# Realizar saques com os argumentos por nome valor, saldo, extrato, limite, numero_saques e LIMITE_SAQUES, por isso o asterisco no início pois tudo após dele são argumentos nomeados
@log_transacao # Decorador de log aplicado à função sacar, para registrar a data e hora da transação
def sacar(*, p_valor, p_saldo, p_extrato, p_limite, p_numero_saques, p_LIMITE_SAQUES):
    # Validações com variáveis booleanas
    excedeu_saldo = p_valor > p_saldo
    excedeu_limite = p_valor > p_limite
    excedeu_saques = p_numero_saques >= p_LIMITE_SAQUES 
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif p_valor > 0:
        p_saldo -= p_valor
        p_extrato += f"Saque:\t\t R$ {p_valor:.2f}\n"
        p_numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    return p_saldo, p_extrato, p_numero_saques
# Exibir o extrato e o saldo atual com os argumentos por posição e por nome saldo e extrato, respectivamente. Por isso a barra e o asterisco entre eles. Apenas o saldo é obrigatório ser posicional.
@log_transacao # Decorador de log aplicado à função exibir_extrato, para registrar a data e hora da transação
def exibir_extrato(saldo, /, *, p_extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not p_extrato else p_extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

## Função principal do sistema bancário
def main():
    # Definindo constantes
    LIMITE_SAQUES = 3
    N_AGENCIA = "0001"

    # Declarando variáveis iniciais
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    dic_usuarios = {}
    dic_contas_bancarias = {}
    
    # Loop principal do sistema bancário
    while True:
        # Exibe o menu e solicita a opção do usuário
        opcao = menu()

        if opcao == "d":
            # Pede o valor do depósito ao usuário
            valor = float(input("Informe o valor do depósito: "))
            # Chama a função depositar e atualiza os valores de saldo e extrato e valida se houve retorno
            if returns := depositar(valor, saldo, extrato):
                saldo, extrato = returns
            else:
                continue

        elif opcao == "s":
            # Pede o valor do saque ao usuário
            valor = float(input("Informe o valor do saque: "))
            # Chama a função sacar e atualiza os valores de saldo, extrato e numero_saques
            saldo, extrato, numero_saques = sacar(
                p_valor=valor,
                p_saldo=saldo,
                p_extrato=extrato,
                p_limite=limite,
                p_numero_saques=numero_saques,
                p_LIMITE_SAQUES=LIMITE_SAQUES,
            )  

        elif opcao == "e":
            # Chama a função extrato para exibir o extrato e o saldo atual
            exibir_extrato(saldo, p_extrato = extrato)

        elif opcao == "c":
            cadastrar_usuario(dic_usuarios)
        
        elif opcao == "l":
            listar_usuarios(dic_usuarios, dic_contas_bancarias)
            
        elif opcao == "a":
            cadastrar_conta(dic_usuarios, dic_contas_bancarias, N_AGENCIA)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
            
main()