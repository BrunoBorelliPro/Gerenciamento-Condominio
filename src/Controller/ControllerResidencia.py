from models.Residencia import Residencia
class ControllerResidencia:

    @staticmethod
    def menuResidencias():
        print("1-Cadastrar residência")
        print("2-Listar todas as residências")
        print("3-Buscar residência")
        print("4-Alterar residência")
        print("5-Deletar residência")
        print("6-sair")
        print("Selecione uma opção: ")
        optResidencia = input()
        return optResidencia

    @staticmethod
    def cadastrarResidencia():
        endereco = input("Insira o endereco: ")
        terreno = float(input("Insira o tamanho do terreno: "))
        preco = float(input("Insira o preco: "))
        cpf = input("Cpf do proprietário: ")
        residencia = Residencia(endereco=endereco,tamanhoDoTerreno=terreno,cpfProprietario=cpf,preco=preco)
        residencia.insertResidencia()
    
    @staticmethod
    def selecionarResidencias():
        lista = Residencia.selectResidencias()
        ControllerResidencia.imprimirListagem(lista)
    
    @staticmethod
    def selecionarResidenciaById():
        idResidencia = input("Insira o idResidencia:")
        lista = Residencia.selectResidenciaByIdResidencia(idResidencia)
        ControllerResidencia.imprimirListagem(lista)
    
    @staticmethod
    def atualizarResidencia():
        idResidencia = input("Insira o id da residência: ")
        try:
            Residencia.selectResidenciaByIdResidencia(idResidencia)
        except:
            print("Id da residencia invalido!")
            return
        endereco = input("Insira o endereco: (Vazio para não alterar o campo)")
        terreno = input("Insira o tamanho do terreno: (Vazio para não alterar o campo)")
        preco = input("Insira o preco: (Vazio para não alterar o campo)")
        cpf = input("Cpf do proprietário: (Vazio para não alterar o campo)")
        Residencia.updateResidencia(idResidencia, endereco=endereco, tamanhoDoTerreno=terreno, preco=preco, cpfProprietario=cpf)
        
    @staticmethod
    def deletarResidencia():
        idResidencia = input("Insira o id da residência: ")
        result = Residencia.selectResidenciaByIdResidencia(idResidencia)
        if result == []:
            Residencia.deleteResidencia(idResidencia)
            print("Deletada")
        else:
            print("Residência não cadastrada")

    @staticmethod
    def imprimirListagem(lista):
        print("+" + 66 * "-" + "+")
        cabecalho = "|{:8s}{:15s} {:11s} {:13s} {:10s}|"
        print(cabecalho.format("ID","ENDEREÇO","TAMANHO","PREÇO", "CPF PROPRIETÁRIO"))
        print("+" + 66 * "-" + "+")
        for i in lista:
            stri = "|{:8s}{:16s}{:11s}{:15s}{:16s}|"
            print(stri.format(str(i[0]),i[1],str(round(i[2],2)),str(round(i[3],2)),i[4]))
        print("+" + 66 * "-" + "+") 