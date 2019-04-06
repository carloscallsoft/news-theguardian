#                  busca informações no jornal the guardian

import requests
import os     as limpa                                                          #Limpar tela
import json
import pandas as pd                            									# trabalhar com excel

limpa.system('cls')

def exportar_csv(titulo,link, nome):                                            #recebe exportar_csv(titulo,link, "Noticias") 
	df = pd.DataFrame({'Titulo': titulo, 'link':link})                              #cria um vetor - grade
	df.to_csv("%s.csv" % nome, index=False, sep=";", encoding='utf-8-sig')      #comando para gerar arquivo em excel 
	print("Arquivo exportado com sucesso para a pasta do projeto ")

def buscar_noticias(dados, tema):												#Função Buscar Noticias
	titulo = []                             									#criando lista vazia
	link   = []                             
	for posicao in dados['response']['results']:         
		if posicao['pillarName'] == tema:
			titulo.append(posicao['webTitle'])
			link.append(posicao['webUrl'])
		elif tema ==  'Todas':
			titulo.append(posicao['webTitle'])
			link.append(posicao['webUrl'])
	if len(titulo) == 0:
		print("nao foi encontrado nenhum post referente ao ", tema)
	else:
		exportar_csv(titulo,link, tema)           						   		 #manda os dados para def export (tit,lin,nome)                    

def main():                                                                     #função chamada de programas
	url = "https://content.guardianapis.com/search?api-key=ee29d74e-e730-4f65-aa97-2bf1e4114153"
	print("Acessando base de dados")
	response = requests.get(url)
	if response.status_code == 200:                                		        #Variavel response
		dados = response.json()
		opcao = 4  
		while opcao  != 0:              										#Dados variavel que vai receber json
			try:
				print("Conseguiu acessar base de dados ...")
				print("	0 - FIM")
				print("	1 - ESPORTE")
				print("	2 - NEWS")
				print("	3 - ARTES")
				print("	4 - TODAS")
				opcao = int(input("Digite a Opçao: "))
			except:
				print("Digite apenas numeros ")
			if opcao > 4 or opcao < 0:
				print("por favor digite numero entre 0 e 4")
			elif opcao == 1:
				tema = 'Sports'
				buscar_noticias(dados, tema)
			elif opcao == 2:
				tema = 'News'
				buscar_noticias(dados, tema)
			elif opcao == 3:
				tema = 'Arts'
				buscar_noticias(dados, tema)
			elif opcao == 4:
				tema = 'Todas'
				buscar_noticias(dados, tema)
			elif opcao == 0:
				print("Fim do programa")
	else:
		print("Não foi possivel acessar base dados..")
if __name__ == "__main__":
	main()

#   index (nao colocar numero colunas index)    sep(separar colunas com ;)     encoding (tabela caracteres alfanumerico)
#	print('Titulo:', dados['response']['results'][5]['webTitle'])    somente a posição 5
#	print(dados['response']['results'][5]['webUrl']):
