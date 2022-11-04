from conta_classes import Conta, ContaEspecial, ContaPoupanca

beatrix = Conta('Beatrix', '030303', 100)
print(beatrix)
beatrix.sacar(90)
print(beatrix)
beatrix.depositar(100)
print(beatrix)

lorelei = ContaPoupanca('Lorelei', '020202', 5000, 3)
print(lorelei)
lorelei.calcularNovoSaldo(0.0036)
print(lorelei)

pandora = ContaEspecial('Pandora', '050505', 100, 50)
print(pandora)
pandora.sacarEspecial(100)
print(pandora)
pandora.sacarEspecial(20)
print(pandora)
pandora.sacarEspecial(30)
print(pandora)
pandora.sacarEspecial(1)

