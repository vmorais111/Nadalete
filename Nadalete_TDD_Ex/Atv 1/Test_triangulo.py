import pytest
from Triangulo import triangulo

@pytest.mark.parametrize("a,b,c,resultado_esperado", [
    (3, 4, 5, "Escaleno"),      # 1. T. Escaleno válido
    (5, 5, 8, "Isósceles"),     # 2. T. Isósceles válido
    (6, 6, 6, "Equilátero"),    # 3. T. Equilátero válido
    
    (10,10,12, "Isósceles"),     # 4. 3 CT's com Isósceles válido c/permutação    
    (10,12,10, "Isósceles"),
    (12,10,10, "Isósceles"),

    (0, 5, 5, "Inválido"),      # 5. Valor zero
    (-1, 3, 3, "Inválido"),     # 6. Valor negativo
    (2, 3, 5, "Inválido"),      # 7. Soma de dois lado é igual ao terceiro
    
    (2, 3, 5, "Inválido"),      # 8. Permutação de valores
    (2, 5, 3, "Inválido"),
    (5, 3, 2, "Inválido"),

    (2, 3, 6, "Inválido"),      # 9. Soma de dois lados é menor que o terceiro

    (2, 3, 6, "Inválido"),      # 10. Permutação dos casos acima
    (2, 6, 3, "Inválido"),
    (6, 2, 3, "Inválido"),

    (0, 0, 0, "Inválido")       # 11. Todos os valores como zero
])

def test_tipos_triangulo(a, b, c, resultado_esperado):
    test = triangulo(a,b,c)
    assert test.definirTipo() == resultado_esperado
