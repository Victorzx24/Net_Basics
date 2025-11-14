import funcoes
from colorama import Fore, Style

print (Fore.GREEN + r"""
 ________   _______  _________        ________  ________  ________  ___  ________  ________      
|\   ___  \|\  ___ \|\___   ___\     |\   __  \|\   __  \|\   ____\|\  \|\   ____\|\   ____\     
\ \  \\ \  \ \   __/\|___ \  \_|     \ \  \|\ /\ \  \|\  \ \  \___|\ \  \ \  \___|\ \  \___|_    
 \ \  \\ \  \ \  \_|/__  \ \  \       \ \   __  \ \   __  \ \_____  \ \  \ \  \    \ \_____  \   
  \ \  \\ \  \ \  \_|\ \  \ \  \       \ \  \|\  \ \  \ \  \|____|\  \ \  \ \  \____\|____|\  \  
   \ \__\\ \__\ \_______\  \ \__\       \ \_______\ \__\ \__\____\_\  \ \__\ \_______\____\_\  \ 
    \|__| \|__|\|_______|   \|__|        \|_______|\|__|\|__|\_________\|__|\|_______|\_________\
                                                            \|_________|             \|_________|
                                                                                                                                                                                                                                                         
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

""" + Style.RESET_ALL)

def opcoes():
    while True:

        selecao = int(input(Fore.YELLOW + "Digite a opção [?]: " + Style.RESET_ALL))

        if selecao == 0:
            print("Saindo...")
            funcoes.time.sleep(0.5)
            exit()

        elif selecao == 1:
            funcoes.ipconfig()

        elif selecao == 2:
            funcoes.ipconfig_all()

        elif selecao == 3:
            funcoes.nslookup()

        elif selecao == 4:
            funcoes.ipconfig_release()

        elif selecao == 5:
            funcoes.ipconfig_renew()

        elif selecao == 6:
            funcoes.ipconfig_flush_dns()
        
        elif selecao == 7:
            funcoes.ping()

        elif selecao == 8:
            funcoes.tracert()

        elif selecao == 9:
            funcoes.pathping()

        elif selecao == 10:
            funcoes.netstat_an()
        
        elif selecao == 11:
            funcoes.arp_a()

        elif selecao == 12:
            funcoes.hostname()

        elif selecao == 13:
            funcoes.getmac()

        elif selecao == 14:
            funcoes.net_use()

        elif selecao == 15:
            funcoes.net_share()

            
opcoes()