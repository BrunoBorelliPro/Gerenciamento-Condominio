from models.Visitantes import Visitantes
from models.RegistroVisitas import RegistroVisitas
from datetime import datetime
class ControllerVisitantes:
    
    @staticmethod
    def MenuVisitantes():
        print("1-Cadastrar")
        print("2-Listar todas")
        print("3-Buscar específica")
        print("4-Alterar")
        print("5-Deletar")
        print("6-Visualizar registro de visitas")
        print("7-Registrar Visita")
        print("8-Sair")
        print("Selecione uma opção: ")
        optFuncionario = input()
        return optFuncionario
    
    @staticmethod
    def CadastrarVisitantes():
        cpf = input("Insira o cpf: ")
        nome = input("Insira o nome: ")      
        visitantes = Visitantes(nome,cpf)
        visitantes.insertVisitantes()
    
    @staticmethod
    def ListarVisitantes():
        lista = Visitantes.selectVisitantes()
        ControllerVisitantes.imprimeListagemVisitantes(lista)

    @staticmethod
    def ListarVisitantesCpf():
        cpf = input("Insira o cpf:")
        lista =Visitantes.selectVisitantesByCpf(cpf)
        if lista == []:
            print("Não existe nenhum visitante cadastrado nesse sistema com esse cpf")
        else:
            print("Visitante cadastrados:")
            ControllerVisitantes.imprimeListagemVisitantes(lista)
    
    @staticmethod
    def AlterarVisitante():
        while True:
            try:
                cpf = input("Insira o cpf do Visitante que deseja alterar:")
                fun = Visitantes.selectVisitantesByCpf(cpf)
                if fun==[]:
                    print("Não há visitantes cadastrados com esse cpf")
                    break
                nome = input("Insira o nome: (vazio para não alterar)")
                Visitantes.updateVisitantes(cpf=cpf,nome=nome)
                break
            except:
                print("Algum erro aconteceu")
                continue
        
    @staticmethod
    def deleteVisitantes():
        cpf = input("Insira o cpf:")
        visitantes = Visitantes.selectVisitantesByCpf(cpf)
        if visitantes == []:
            print("Esse funcionario não esta cadastrado!")
        else:
            Visitantes.deleteVisitantes(cpf)
            print("Apagado com sucesso")
            
    @staticmethod
    def insereRegistroVisita():
        placaCarro = input("Placa do carro:")
        while True:
            horarioEntrada = input("Horário entrada: (HH:MM)") 
            try:
                datetime.strptime(horarioEntrada,"%H:%M")
                break
            except:
                print("Horário inválido!")
        while True:
            horarioSaida = input("Horário saida: (HH:MM)") 
            try:
                datetime.strptime(horarioSaida,"%H:%M")
                break
            except:
                print("Horário inválido!")
        cpf=input("insira seu cpf: ")
        registroVisitas = RegistroVisitas(placaCarro=placaCarro,horarioEntrada=horarioEntrada,horarioSaida=horarioSaida,cpf=cpf)
        registroVisitas.insertRegistroVisitas()
         
    
    @staticmethod
    def listaRegistroVisita():
        lista = RegistroVisitas.selectRegistroVisitas()
        ControllerVisitantes.imprimeListagemRegistros(lista)
        

    @staticmethod
    def imprimeListagemVisitantes(lista):
        print("+" + 25 * "-" + "+")
        cabecalho = "|{:11s} {:13s}|"
        print(cabecalho.format("CPF","NOME"))
        print("+" + 25 * "-" + "+")  
        for item in lista:
            stri = "|{:11s} {:13s}|"
            print(stri.format(item[0],item[1]))
        print("+" + 25 * "-" + "+")

    @staticmethod
    def imprimeListagemRegistros(lista):
        print(lista)
        print("+" + 75 * "-" + "+")
        cabecalho = "|{:15s} {:19s} {:13s} {:11s} {:13s}|"
        print(cabecalho.format("ID REGISTRO", "PLACA DO CARRO","ENTRADA", "SAÍDA", "CPF"))
        print("+" + 75 * "-" + "+")
        for item in lista:
            stri = "|{:15s} {:19s} {:13s} {:11s} {:13s}|"
        print(stri.format(str(item[0]),item[1],item[2], item[3], item[4]))
        print("+" + 75 * "-" + "+")


            