class triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    
    def verificar (self):
        a, b, c = self.ladoA, self.ladoB, self.ladoC
        return (
            a > 0 and b > 0 and c > 0 and
            a + b > c and
            a + c > b and
            b + c > a
        )

    def definirTipo(self):

        if not self.verificar():
            return 'Inválido'
    
        check = len({self.ladoA, self.ladoB, self.ladoC})
        match check:
            case 3:
                return "Escaleno"
            case 2:
                return "Isósceles"
            case 1:
                return "Equilátero"