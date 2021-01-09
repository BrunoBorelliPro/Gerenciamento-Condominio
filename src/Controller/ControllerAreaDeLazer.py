from models.AreaDeLazer import AreaDeLazer
from datetime import datetime
from models.RegistroLazer import RegistroLazer

class ControllerAreaDeLazer:
       
    @staticmethod
    def MenuAreaDeLazer():
        print("1-Cadastrar")
        print("2-Listar")
        print("3-Buscar")
        print("4-Cadastrar novo acesso")
        print("5-Verificar registro de acessos")
        print("6-Sair")
        print("Selecione uma opção: ")
        optAreaLazer = input()
        return optAreaLazer
    
    @staticmethod
    def CadastrarAreaLazer():
        descricao = input("Insira descricao: ")     
        areaLazer = AreaDeLazer(descricao)
        areaLazer.insertAreaDeLazer()
    
    @staticmethod
    def ListarAreaLazer():
        lista = AreaDeLazer.selectAreaDeLazer()
        ControllerAreaDeLazer.imprimeListagemAreas(lista)

    @staticmethod
    def ListarAreaLazerDescricao():
        descricao = input("Insira descrição:")
        lista = AreaDeLazer.selectAreaByDescricao(descricao)
        if lista == []:
            print("Não existe nenhuma área de lazer cadastrado nesse sistema com esse nome")
        else:
            ControllerAreaDeLazer.imprimeListagemAreas(lista)
        
            
    @staticmethod
    def insereRegistroAcesso():
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
        idArea=input("Id da área de lazer")
        registroLazer = RegistroLazer(idArea=idArea,horarioEntrada=horarioEntrada,horarioSaida=horarioSaida)
        registroLazer.insertRegistro()
         
    
    @staticmethod
    def listaRegistroVisita():
        lista = RegistroLazer.selectRegistro()
        ControllerAreaDeLazer.imprimeListagemRegistros(lista)
        

    @staticmethod
    def imprimeListagemAreas(lista):
        print("Área de lazer cadastradas:")
        print("+" + 30 * "-" + "+")
        cabecalho = "|{:15s} {:14s}|"
        print(cabecalho.format("ID ÁREA", "DESCRIÇÃO"))
        print("+" + 30 * "-" + "+")
        for i in range(0, len(lista)):
            stri = "|{:15s} {:14s}|"
            print(stri.format(str(lista[i][0]),lista[i][1]))
        print("+" + 30 * "-" + "+")

    @staticmethod
    def imprimeListagemRegistros(lista):
        print("+" + 67 * "-" + "+")
        cabecalho = "|{:15s} {:19s} {:19s} {:11s}|"
        print(cabecalho.format("ID REGISTRO", "HORÁRIO ENTRADA", "HORÁRIO SAÍDA", "ID AREA"))
        print("+" + 67 * "-" + "+")  
        for item in lista:
            stri = "|{:15s} {:19s} {:19s} {:11s}|"
            print(stri.format(str(item[0]),item[1], item[2], str(item[3])))
        print("+" + 67 * "-" + "+")