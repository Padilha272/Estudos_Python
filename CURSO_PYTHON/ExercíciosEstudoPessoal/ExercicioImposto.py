valor = input("Ganho por hora: ")
valor_float = float(valor)
horas = input("Digite o número de horas trabalhadas: ")
horas_int=int(horas)
salario_bruto=valor_float*horas_int
ir = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05

try:
    print(f"+Salário Bruto = {salario_bruto} R$")
    print(f"-Imposto de renda = {ir}")
    print(f"-Inss = {inss} ")
    print(f"-Sindicato = {sindicato}")
    print(f"Salário líquido = {salario_bruto-ir-inss-sindicato}")
except:
    input("Foram digitados valores inválidos")
