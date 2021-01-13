from models.Funcionario import Funcionario

class ControllerFuncionario:
    
    @staticmethod
    def MenuFuncionarios():
        print("1-Cadastrar funcionario")
        print("2-Listar todos os funcionarios")
        print("3-Buscar funcionario")
        print("4-Alterar funcionario")
        print("5-Deletar funcionario")
        print("6-Sair")
        print("Selecione uma opção: ")
        optFuncionario = input()
        return optFuncionario
    
    @staticmethod
    def CadastrarFuncionario():
        cpf = input("Insira o cpf: ")
        nome = input("Insira o nome: ")
        cargo = input("Insira o cargo: ")
        while True:
            print("O funcionario é terceirizado?")
            print("1-Sim")
            print("2-Não")
            terceirizado = input()
            if terceirizado == "2":
                terceirizado = False
                while True:
                    try:
                        salario = float(input("Insira o salário: "))
                        break
                    except:
                        print("Salario inválido!")
                        continue
                break
            elif terceirizado == "1":
                terceirizado = True
                salario = 0.0
                break
            else:
                print("Opção inválida!")
                continue            
        funcionario = Funcionario(cpf,nome,cargo,terceirizado, salario)
        funcionario.insertFuncionario()
    
    @staticmethod
    def ListarFuncionarios():
        lista = Funcionario.selectFuncionario()
        print("+" + 63 * "-" + "+")
        cabecalho = "|{:15s} {:11s} {:13s} {:10s} {:10s}|"
        print(cabecalho.format("CPF","NOME","CARGO", "SALARIO", "TERCEIRIZADO"))
        print("+" + 63 * "-" + "+")
        for i in range(0, len(lista)):
            if lista[i][4]==1:
                seTerceirizado = "SIM"
            else:
                seTerceirizado = "NÃO"
            if lista[i][3] == None:
                salario = 0
            else:
                salario = lista[i][3]  
            stri = "|{:15s} {:11s} {:13s} {:10.2f} {:10s}|"
            print(stri.format(lista[i][0],lista[i][1],lista[i][2],salario,seTerceirizado))
        print("+" + 63 * "-" + "+")

    @staticmethod
    def ListarFuncionariosCpf():
        cpf = input("Insira o cpf:")
        lista = Funcionario.selectFuncionarioByCpf(cpf)
        if lista == []:
            print("Não existe nenhum funcionario cadastrado nesse sistema com esse cpf")
        else:
            print("Funcionario cadastrados:")
            cabecalho = "|{:15s} {:11s} {:13s} {:12s} {:10s}|"
            print(cabecalho.format("CPF","NOME","CARGO", "SALARIO", "TERCEIRIZADO"))
            for i in range(0, len(lista)):
                if lista[i][3] == None:
                    salario = 0
                else:
                    salario = float(lista[i][3])                   
                if lista[i][4]=="1":
                    seTerceirizado = "SIM"
                else:
                    seTerceirizado = "NÃO"
                stri = "|{:15s} {:11s} {:13s} {:10.2f} {:10s}|"
                print(stri.format(lista[i][0],lista[i][1],lista[i][2],salario,seTerceirizado))
    
    @staticmethod
    def AlterarFuncionario():
        while True:
            try:
                sair = ""
                while True:
                    cpf = input("Insira o cpf do Funcionario que deseja alterar:")
                    fun = Funcionario.selectFuncionarioByCpf(cpf)
                    if fun==[]:
                        print("Não há funcionarios cadastrados com esse cpf")
                        sair = input("Insira 0 se quiser sair: ")
                        continue
                    else:
                        break
                if sair == "0":
                    break
                nome = input("Insira o nome: (vazio para não alterar)")
                cargo = input("Insira o cargo: (vazio para não alterar)")
                while True:
                    print("O funcionario é terceirizado? (vazio para não alterar)")
                    print("1-Sim")
                    print("2-Não")
                    terceirizado = input()
                    if terceirizado == "":
                        salario = ""
                        break
                    if terceirizado == "2":
                        terceirizado = False
                        while True:
                            try:
                                salario = float(input("Insira o salário: "))
                                break
                            except:
                                print("Salario inválido!")
                                continue
                        break
                    elif terceirizado == "1":
                        terceirizado = True
                        salario = 0
                        break
                    else:
                        print("4 - Opção inválida!")
                        continue
                Funcionario.updateFuncionario(cpf=cpf,nome=nome,cargo=cargo,terceirizado=terceirizado,salario=salario)
                break
            except:
                print("Algum erro aconteceu")
                continue
        
    @staticmethod
    def DeleteFuncionario():
        cpf = input("Insira o cpf:")
        funcionario = Funcionario.selectFuncionarioByCpf(cpf)
        if funcionario == []:
            print("Esse funcionario não esta cadastrado!")
        else:
            Funcionario.deleteFuncionario(cpf)
            print("Apagado com sucesso")

            