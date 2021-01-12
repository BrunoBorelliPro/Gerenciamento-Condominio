from models.Funcionario import Funcionario
from models.Residencia import Residencia
from models.Morador import Morador
from Controller.ControllerFuncionario import ControllerFuncionario
from Controller.ControllerResidencia import ControllerResidencia
from Controller.ControllerMoradores import ControllerMoradores
from Controller.ControllerVisitantes import ControllerVisitantes
from Controller.ControllerAreaDeLazer import ControllerAreaDeLazer

while True:
    print("1-Gerenciar Funcionarios")
    print("2-Gerenciar Residencias")
    print("3-Gerenciar Moradores")
    print("4-Gerenciar Visitantes")
    print("5-Areas de Lazer")
    print("6-Sair")
    print("Selecione uma opção: ")
    optMenu = input()

    if optMenu == "1":
        optFuncionario = ControllerFuncionario.MenuFuncionarios()
        if optFuncionario == "1":
            ControllerFuncionario.CadastrarFuncionario()
        elif optFuncionario == "2":
            ControllerFuncionario.ListarFuncionarios()
        elif optFuncionario == "3":
            ControllerFuncionario.ListarFuncionariosCpf()
        elif optFuncionario == "4":
            ControllerFuncionario.AlterarFuncionario()
        elif optFuncionario == "5":
            ControllerFuncionario.DeleteFuncionario()
        elif optFuncionario == "6":
            print("Saindo")
            break
        else:
            print("Opção invalida")
        
    elif optMenu == "2":
        optResidencia = ControllerResidencia.menuResidencias()
        if optResidencia == "1":
            ControllerResidencia.cadastrarResidencia()
        elif optResidencia == "2":
            ControllerResidencia.selecionarResidencias()    
        elif optResidencia == "3":
            ControllerResidencia.selecionarResidenciaById()
        elif optResidencia == "4":
           ControllerResidencia.atualizarResidencia()
        elif optResidencia == "5":
            ControllerResidencia.deletarResidencia()
        elif optResidencia == "6":
            print("Saindo")
            break
        else:
            print("Opção inválida")
            continue
    
    elif optMenu == "3":
        optMorador = ControllerMoradores.menuMorador()
        if optMorador == "1":
            ControllerMoradores.cadastrarMorador()
        elif optMorador == "2":
            ControllerMoradores.selecionarMoradores()
        elif optMorador == "3":
            ControllerMoradores.selecionaMoradorByCpf()
        elif optMorador == "4":
            ControllerMoradores.atualizarMorador()
        elif optMorador == "5":
            ControllerMoradores.deletarMorador()
        elif optMorador == "6":
            print("Saindo")
            break
        else:
            print("Opção inválida!")
    
    elif optMenu == "4":
        optVisitante = ControllerVisitantes.MenuVisitantes()
        if optVisitante == "1":
            ControllerVisitantes.CadastrarVisitantes()
        elif optVisitante == "2":
            ControllerVisitantes.ListarVisitantes()
        elif optVisitante == "3":
            ControllerVisitantes.ListarVisitantesCpf()
        elif optVisitante == "4":
            ControllerVisitantes.AlterarVisitante()
        elif optVisitante == "5":
            ControllerVisitantes.deleteVisitantes()
        elif optVisitante == "6":
            ControllerVisitantes.listaRegistroVisita()
        elif optVisitante == "7":
            ControllerVisitantes.insereRegistroVisita()
        elif optVisitante == "8":
            print("Saindo")            
        else:
            print("Opção inválida!")

    elif optMenu == "5":
        optAreaLazer = ControllerAreaDeLazer.MenuAreaDeLazer()
        if optAreaLazer == "1":
            ControllerAreaDeLazer.CadastrarAreaLazer()        
        elif optAreaLazer == "2":
            ControllerAreaDeLazer.ListarAreaLazer()
        elif optAreaLazer == "3":
            ControllerAreaDeLazer.ListarAreaLazerDescricao()
        elif optAreaLazer == "4":
            ControllerAreaDeLazer.insereRegistroAcesso()
        elif optAreaLazer == "5":
            ControllerAreaDeLazer.listaRegistroVisita()
        elif optAreaLazer == "6":
            print("Saindo")            
        else:
            print("Opção Inválida!")
            

    elif optMenu == "6":
        print("Encerrando")
        break
    else:
        print("Opção inválida")
        break