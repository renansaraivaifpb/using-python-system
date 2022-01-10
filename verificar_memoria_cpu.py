# verificação de momória do disk da máquina e o uso porcentagem da CPU durante um inttervalo de 1 segundo
import shutil
import psutil
def verificar_memoria(disk):
    disco = shutil.disk_usage(disk)
    livre = disco.free / disco.total * 100
    return livre > 10
def verificar_uso_cpu():
    usando = psutil.cpu_percent(1)
    return usando < 75


