class Empregado:
    
    #Construtor da classe, aqui estará os atributos da classe.
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self._salario = salario
    
    #Método que irá retornar uma String para o objeto.
    def __str__(self):
        return f'Nome do funcionário: {self.nome} \n Idade do funcionário: {self.idade} \n Salário do funcionário: {self._salario:.3f}'
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, value):
        if value >= 0:
            self._salario = value
        else:
            raise ValueError("Salário não pode ser negativo, por favor inserir um valor positivo válido!")
            
    @classmethod
    def avg_salario(cls, empregados):
        if not empregados:
            return 0.0
        total_salario = sum(emp.salario for emp in empregados)
        return total_salario / len(empregados)
    
    @staticmethod
    def maior_de_idade(idade):
        if idade >= 18:
            return f'Você é maior de idade. \n Idade fornecida: {idade}'
        else:
            return f'Você é menor de idade. \n Idade fornecida: {idade}'
    
    
    