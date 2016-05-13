# coding=utf-8

teto_salarial = 21613.05

import csv 
# Opens the csv file
with open('../salarios.csv', 'rb') as csvfile:
	planilha = csv.reader(csvfile, delimiter=';', quotechar='|')
	
	# Traduz os dados da planilha para o dicionário
	salarios = {}
	print "Pessoas que possuem dupla matrícula:"
	for row in planilha: 
		if row[0] in salarios:
			print row[0]			
			salarios[row[0]] += float(row[1])
		else:
			salarios[row[0]] = float(row[1])

	#  Separa super salários (acima de R$21.613,05)
	supersalarios = {}
	for nome in salarios:
		if salarios[nome] > teto_salarial:
			supersalarios[nome] = salarios[nome]

	# Soma o excedente dos  super salários
	excedente_supersalarios = 0
	for nome in supersalarios:
		excedente_supersalarios += supersalarios[nome] - teto_salarial

	# Relatório
	print "Funcionários na folha de pagamento: %d" % len(salarios)
	print "Funcionários com super-salários (acima de R$21.613,05): %d (%.1f%%)" % (float(len(supersalarios)), float(len(supersalarios))/float(len(salarios))*100)
	print "Excedente dos super-salários: R$%.2f/mês | R$%.2f/ano" % (excedente_supersalarios, excedente_supersalarios*12)
