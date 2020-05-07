print ("Vamos calcular seu Indíce de Massa Corporea - IMC")
altura = float(input("Digite sua altura em metro\n"))
peso = float(input("Digite seu peso em kilo\n"))

imc = peso/(altura**2)
if imc < 18.5: 
	categoria = ("ABAIXO DO PESO") 
	acao = ("ganhar")
	dif = 18.5*(altura**2)-peso
elif 18.5 <= imc < 25: 
	categoria = ("PESO ADEQUADO") 
elif 25 <= imc < 30: 
	categoria = ("SOBREPESO") 
	acao = ("perder")
	dif = peso-24.9*(altura**2)
else: 
	categoria = ("OBESIDADE") 
	acao = ("perder")
	dif = peso-24.9*(altura**2)

print ("Seu IMC é", round(imc,2), "e, segundo o ministério da saúde, você está na categoria", categoria,".")
if imc < 18.5 or imc >= 25: 
	print ("Se quiser atingir a categoria peso adequado, você precisa",acao,round(dif,2),"kg")
