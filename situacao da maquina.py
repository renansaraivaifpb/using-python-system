import verificar_localhost_internet
import verificar_memoria_cpu

if not verificar_memoria_cpu.verificar_memoria('/') or not verificar_memoria_cpu.verificar_uso_cpu():
    print('Memória ou CPU está com algum problema')
elif verificar_localhost_internet.verificar_localhost() and verificar_localhost_internet.verificar_conexacao_a_internet():
    print('Conexão está ok')
print('Memória e CPU estão oks')
