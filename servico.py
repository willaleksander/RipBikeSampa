import urllib2
from bike_itau_model import *
import unicodedata

	
if __name__ == '__main__':
	response = urllib2.urlopen('http://ww2.mobilicidade.com.br/bikesampa/mapaestacao.asp')
	html = response.readlines()
	
	s = session()

	for i in range(len(html)):
		if 'exibirEstacaMapa(\"' in html[i]:
			estacao = EstacaoBikeItau()
			movimentacao = MovimentacaoBikeItau()
			
			estacao.latitude = float(html[i][18:-4])
			estacao.longitude = float(html[i+1][1:-4])
			#estacao.icone = html[i+2][1:-4]
			estacao.nome = html[i+3][1:-4].decode('latin_1')
			estacao.idEstacao = int(html[i+4][1:-4])
			movimentacao.statusOnline = html[i+5][1:-4]
			movimentacao.statusOperacao = html[i+6][1:-4]
			movimentacao.vagasOcupadas = int(html[i+7][1:-4])
			estacao.numBicicletas = int(html[i+8][1:-4])
			estacao.endereco = html[i+9][1:-4].decode('latin_1')
			
			movimentacao.vagasDisponiveis = estacao.numBicicletas - movimentacao.vagasOcupadas
			movimentacao.idEstacao = estacao.idEstacao
			s.merge(estacao)
			s.merge(movimentacao)

	s.commit()
	s.close()
	

