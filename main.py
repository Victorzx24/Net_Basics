import subprocess
import re

lista_opcoes = r"""
 ________   _______  _________  ________  ________  ________     
|\   ___  \|\  ___ \|\___   ___\\   __  \|\   ____\|\   ____\    
\ \  \\ \  \ \   __/\|___ \  \_\ \  \|\ /\ \  \___|\ \  \___|    
 \ \  \\ \  \ \  \_|/__  \ \  \ \ \   __  \ \_____  \ \  \       
  \ \  \\ \  \ \  \_|\ \  \ \  \ \ \  \|\  \|____|\  \ \  \____  
   \ \__\\ \__\ \_______\  \ \__\ \ \_______\____\_\  \ \_______\
    \|__| \|__|\|_______|   \|__|  \|_______|\_________\|_______|
                                            \|_________|         
                                                                 
     ____                       _           __                  
   / __/___  _____   _      __(_)___  ____/ /___ _      _______
  / /_/ __ \/ ___/  | | /| / / / __ \/ __  / __ \ | /| / / ___/
 / __/ /_/ / /      | |/ |/ / / / / / /_/ / /_/ / |/ |/ (__  ) 
/_/  \____/_/       |__/|__/_/_/ /_/\__,_/\____/|__/|__/____/  




[0] Sair                     - Para sair do NetBsc
[1] ipconfig                 - Mostrar configuração de rede
[2] ipconfig /all            - Mostrar informações detalhadas do IP
[3] nslookup [domínio]       - Consultar DNS para detalhes de domínio
[4] ipconfig /release        - Liberar endereço IP
[5] ipconfig /renew          - Renovar endereço IP
[6] ipconfig /flushdns       - Limpar cache de DNS
[7] ping [IP]                - Verificar conexão de rede com um servidor
[8] tracert [IP]             - Rastrear rota até um destino
[9] pathping [IP]            - Combina ping e tracert
[10] netstat -an             - Mostrar conexões de rede ativas
[11] arp -a                  - Mostrar cache ARP
[12] hostname                - Exibir nome do computador
[13] getmac                  - Mostrar endereço MAC dos adaptadores de rede
[14] net use                 - Conectar a um recurso compartilhado
[15] net share               - Listar recursos compartilhados

"""



def executar_powershell(lista_opcoes):
    while True:
        print(lista_opcoes)
        selecao = int(input("Digite a opção [?]: "))
        if selecao == 0:
            exit()
        elif selecao == 1:
            ipconfig_formatado()
        elif selecao == 2:
            ipconfig_all()
        elif selecao == 3:
            nslookup()


def ipconfig_menu():
    processo = subprocess.run(
        ['powershell', '-Command', 'ipconfig | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)

def ipconfig_all():
    processo = subprocess.run(
        ['powershell', '-Command', 'ipconfig /all | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)

def nslookup():
    dominio = input('Insira o domínio: ')
    processo = subprocess.run(
        ['powershell', '-Command', f'nslookup {dominio} | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)


executar_powershell(lista_opcoes)