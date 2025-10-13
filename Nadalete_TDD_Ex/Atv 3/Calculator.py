class Calc_Funcionario:
    def __init__(self, nome: str, email: str, salario: float, cargo:str):
        self.nome = nome
        self.email = email
        self.salario = salario
        self.cargo = cargo

    def SalLiquido (self) -> float:

        salario_pessoa = self.salario
        cargo_pessoa = self.cargo

        match cargo_pessoa:
            case 'DEV':
                if salario_pessoa >= 3000.00:
                    desconto = 0.2
                else:
                    desconto = 0.1     
            case 'DBA':
                if salario_pessoa >= 2000.00:
                    desconto = 0.25
                else:
                    desconto = 0.15
            case 'TES':
                if salario_pessoa >= 2000.00:
                    desconto = 0.25
                else:
                    desconto = 0.15
            case 'GER':
                if salario_pessoa >= 5000.00:
                    desconto = 0.3
                else:
                    desconto = 0.2

        return salario_pessoa * (1 - desconto)