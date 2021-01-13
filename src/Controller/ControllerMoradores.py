from models.Morador import Morador
from models.Residencia import Residencia

class ControllerMoradores:

    @staticmethod
    def menuMorador():
        print("1-Cadastrar morador")
        print("2-Listar todos os morador")
        print("3-Buscar morador")
        print("4-Alterar morador")
        print("5-Deletar morador")
        print("6-Sair")
        print("Selecione uma opção: ")
        optMorador = input()
        return optMorador

    @staticmethod
    def cadastrarMorador():
        nome = input("Insira o nome: ")
        cpf = input("Insira o cpf: ")
        idResidencia = input("Inisra o id da residencia:")
        residencia = Residencia.selectResidenciaByIdResidencia(idResidencia)
        if residencia == []:
            print("Essa residência não está cadastrada!")
            return
        morador = Morador(nome, cpf, idResidencia)
        morador.insertMorador()
        print("Inserido!")
        
    @staticmethod
    def selecionarMoradores():
        lista=Morador.selectMoradores()
        ControllerMoradores.imprimirListagem(lista)
    
    @staticmethod
    def selecionaMoradorByCpf():
        cpf = input("Insira o cpf: ")
        lista=Morador.selectMoradorByCpf(cpf)
        ControllerMoradores.imprimirListagem(lista)
        
    @staticmethod
    def atualizarMorador():
        cpf = input("Insira o cpf: ")
        morador = Morador.selectMoradorByCpf(cpf)
        if morador == []:
            print("Morador não cadastrado!")
            return
        nome = input("Insira o nome: (Vazio para não alterar)")
        idResidencia = input("Insira o id da residencia: (Vazio para não alterar)")
        if not idResidencia == "":
            residencia = Residencia.selectResidenciaByIdResidencia(idResidencia)
            if residencia == []:
                print("Essa residência não está cadastrada!")
                return 
        Morador.updateMorador(cpf, nome, idResidencia)
        print("Atualizado!")

    @staticmethod
    def deletarMorador():
        cpf = input("Insira o cpf:")
        morador = Morador.selectMoradorByCpf(cpf)
        if morador == []:
            Morador.deleteMorador(cpf)
            print("Apagado com sucesso")
        else:
            print("Cpf não encontrado!")

    @staticmethod
    def imprimirListagem(lista):
        print("+" + 53 * "-" + "+")
        cabecalho ="|{:15s} {:17s} {:19s}|"
        print(cabecalho.format("CPF", "NOME", "IDRESIDENCIA"))
        print("+" + 53 * "-" + "+")
        for i in range(0,len(lista)):
            stri = "|{:15s} {:17s} {:18s} |"
            print(stri.format(str(lista[i][0]),lista[i][1],str(lista[i][2])))
        print("+" + 53 * "-" + "+")

