from empregado import Empregado
from departamento import Departamento

#Função principal onde irá executar as funções e métodos das classes
def main():
    emp1 = Empregado('ismael', 23, 1.900)
    emp2 = Empregado('ana', 19, 1.200)
    emp3 = Empregado('felipe', 15, 800)
    
    dept1 = Departamento("RH")
    dept2 = Departamento("TI")
    
    dept1.add_empregado(emp2) #RH
    dept1.add_empregado(emp3) #RH
    dept2.add_empregado(emp1) #TI
    
    print("Exemplos da classe departament: ")
    print(dept1.total_salario())
    print(dept2.total_salario())
    print("Exemplo da classe empregrado: ")
    print(Empregado.avg_salario([emp1, emp2]))
    print(emp1.avg_salario([emp2, emp3]))
    print("Exemplo da função de static: ")
    print(Empregado.maior_de_idade(18))
    print(Empregado.maior_de_idade(17))
    try:
        emp1.salario = -1
    except ValueError as e:
        print(e)
    print("Teste da chamado do salario, atributo da classe:")
    print(emp1)
    
    
if __name__ == '__main__':
    main()