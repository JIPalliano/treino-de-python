class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.empregados = []
        
    def add_empregado(self, empregado):
        self.empregados.append(empregado)
    
    def remove_empregado(self, empregado):
        if empregado in self.empregados:
            self.empregados.remove(empregado)
            
    def total_salario(self):
        return sum(emp._salario for emp in self.empregados)
    
    @classmethod
    def departamento_avg_salario(cls, departamentos):
        total_salario = 0
        total_empregados = 0
        for dept in departamentos:
            total_salario += dept.total_salario()
            total_empregados += len(dept.empregados)
        if total_empregados == 0:
            return 0.0
        return total_salario / total_empregados