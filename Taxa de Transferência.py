tamanho = float(input('Digite o tamanho do arquivo (em MB): '))
velocidade = float(input('Digite a velocidade de conexão (em Mbps): '))

tamanhoBits = tamanho * 1024 * 1024 * 8
tempoSegundos = tamanhoBits / (velocidade * 1024 * 1024)
tempoMinutos = tempoSegundos / 60

print('Tempo aproximado para o download: {:.2f} minutos'.format(tempoMinutos))
