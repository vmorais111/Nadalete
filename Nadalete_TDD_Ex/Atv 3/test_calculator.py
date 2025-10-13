import pytest
from Calculator import Calc_Funcionario

@pytest.mark.parametrize(
    "nome,email,salario,cargo,resultado_esperado",
    [
        ("João Silva", "jo.silva@teste.com", 4000.00, "DEV", 4000.00 * 0.80),   # 3200.00
        ("José Silva", "jojo.silva@teste.com", 2900.00, "DEV", 2900.00 * 0.90), # 2610.00
        ("Alberto de Assis", "AlbA@teste.com", 2500.00, "DBA", 2500.00 * 0.75), # 1875.00
        ("Augusto de Assis", "A.Assis@teste.com", 1500.00, "DBA", 1500.00 * 0.85), # 1275.00
        ("Martin Morales", "M.Mo@teste.com", 2500.00, "TES", 2500.00 * 0.75),   # 1875.00
        ("Mateus Manuel", "Mat.Manuel@teste.com", 1500.00, "TES", 1500.00 * 0.85), # 1275.00
        ("Arthur", "Arthur123@teste.com", 5500.00, "GER", 5500.00 * 0.70),      # 3850.00
        ("Heitor Henrique", "Hei.Henri@teste.com", 4500.00, "GER", 4500.00 * 0.80), # 3600.00
    ]
)
def test_sal_liquido(nome, email, salario, cargo, resultado_esperado):
    func = Calc_Funcionario(nome, email, salario, cargo)
    assert func.SalLiquido() == pytest.approx(resultado_esperado, rel=1e-9)