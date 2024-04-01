import os
nome = []
cpf =[]
numeroconta =[]
saldo =[]


def limpar():
    os.system("cls")
def menu():
     print("*****sistema bancário*******")
     print("\n \n criar conta: '1' \n   alterar conta:'2' \n consultar conta:'3'\n excluir conta:'4' \n inserir'5'\n consultar pix'6' ")
   
def criarconta():
    limpar()
    nome.append(input("seu nome:"))
    cpf.append(input("seu cpf:"))
    numeroconta.append(input("o numero da conta:"))
    saldo.append(0)
    limpar()
    menu()

def alterar():
    limpar()
    print("alterarcpf:'1'\n alterarnome:'2'")
    conta = input("Digite o numero da conta:")
    encontrado = False
    
    for i in range(len(numeroconta)):
        if numeroconta[i] == conta:
            print(f"Conta: {numeroconta[i]}\nCPF: {cpf[i]}\nNome: {nome[i]}\nSaldo: {saldo[i]}")
            encontrado = True
            break
    
    if not encontrado:
        print("Esta conta não existe")
    
   
    
    if conta == numeroconta[i]:
        pedido=input("O que voce deseja alterar")
    if pedido == '1':
        cpf[i] = input("Digite seu cpf novo:") 
    elif pedido == '2': 
        nome[i] = input("Digite seu novo nome:")
     
    
    inicio = input("Digite 'sair' para voltar para o início: ")
    if inicio == 'sair':
        limpar()
        menu()  

def consultar():
    limpar()
    conta = input("O número da sua conta: ")
    encontrado = False
    for i in range(len(numeroconta)):
        if numeroconta[i] == conta:
            print(f"Conta: {numeroconta[i]}\nCPF: {cpf[i]}\nNome: {nome[i]}\nSaldo: {saldo[i]}")
            encontrado = True
            break
    if not encontrado:
        print("conta não existe")
       
    voltar =input("Digite 'sair' pra voltar pro inicio")
    if voltar=='sair':
     limpar()
     menu() 

def excluirconta():
    limpar()
    print("Digite o numero da conta para exclui-lá")
    conta=input("digite o numero da conta:")
    encontrado = False
    for i in range(len(numeroconta)):
         if numeroconta[i] == conta:
            print(f"Conta: {numeroconta[i]}\nCPF: {cpf[i]}\nNome: {nome[i]}\nSaldo: {saldo[i]}")
            encontrado = True
            break
    
    if not encontrado:
           print("essa conta não existe")
    
    if conta==numeroconta[i]:
          pedido=input("Voce quer excluir conta?")
    if pedido=="sim":     
          del(cpf[i])
          del(nome[i])
          del(numeroconta[i])
          del(saldo[i])
          print("conta excluída")
    inicio = input("Digite 'sair' para voltar para o início: ")
    if inicio == 'sair':
        limpar()
        menu()  
def depositar():
    limpar()
    print("Digite o numero da conta para depositar")
    valor=int(input("digite o valor a ser depositado:"))
    conta=input("Digite o numero da conta:")
    encontrado = False
    for i in range(len(numeroconta)):
         if numeroconta[i] == conta:
            print(f"Conta: {numeroconta[i]}\nCPF: {cpf[i]}\nNome: {nome[i]}\nSaldo: {saldo[i]}")
            encontrado = True
            break
    
    if not encontrado:
           print("conta não encontrada")
    
    if conta == numeroconta[i]:
         saldo[i]=saldo[i]+valor
    inicio = input("Digite 'sair' para voltar para o início: ")
    if inicio == 'sair':
        limpar()
        menu()
def pix():
     limpar()
     print("Digite o numero da conta para fazer o pix")
     valor=int(input("Qual o valor a transferir?"))
     conta=input("Digite o numero da conta")
     encontrado = False
     for i in range(len(numeroconta)):
         if numeroconta[i] == conta:
            print(f"Conta: {numeroconta[i]}\nCPF: {cpf[i]}\nNome: {nome[i]}\nSaldo: {saldo[i]}")
            encontrado = True
            break
    
     if not encontrado:
           print("conta não encontrada")
    
     if conta == numeroconta[i]:
         saldo[i]=saldo[i]+valor
         saldo[i]=saldo[i]-valor
         print("Pix realizado")
     saida = input("Digite 'sair' para voltar para o início: ")
     if saida == 'sair':
        limpar()
        menu()
def menu():
    print("*****sistema bancário*******")
    print("\n \n criar conta: '1'\n alterar conta:'2' \n consultar conta:'3'\n excluir conta:'4' \n inserir'5'\n consultar pix'6'\n depositar'7'\n fazer pix:'8' ")
    x = input("o que voce quer fazer?")
    
    if x == '1':
      limpar()
      criarconta()

    elif x == '3':
     limpar()
     consultar()
     
    elif x =='2':
       limpar()
       alterar()

    elif x=='4':
       limpar()
       excluirconta()
    elif x=='7':
        limpar()
        depositar()

    elif x=='8':
        limpar()
        pix()
 
menu()