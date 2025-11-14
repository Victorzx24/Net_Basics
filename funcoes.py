import subprocess
import re
import time
from colorama import Fore, Style


def ipconfig():
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
    dominio = input(Fore.YELLOW + 'Insira o domínio: ' + Style.RESET_ALL)
    processo = subprocess.run(
        ['powershell', '-Command', f'nslookup {dominio} | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)


def ipconfig_release():
    processo = subprocess.run(
        ['powershell', '-Command', 'ipconfig /release | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)


def ipconfig_renew():
    processo = subprocess.run(
        ['powershell', '-Command', 'ipconfig /renew | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)


def ipconfig_flush_dns():
    processo = subprocess.run(
        ['powershell', '-Command', 'ipconfig /flushdns | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)


def ping():
    
    endereco = input(Fore.YELLOW + 'Digite o endereço para efetuar o ping: ' + Style.RESET_ALL)
    print(Fore.YELLOW + 'Efetuando ping...' + Style.RESET_ALL)
    time.sleep(3)
    processo = subprocess.run(
        ['powershell', '-Command', f'ping {endereco} | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)


def tracert():
    endereco_ip = input(Fore.YELLOW + 'Digite o Endereço IP: ' + Style.RESET_ALL)
    processo = subprocess.run(
        ['powershell', '-Command', f'tracert {endereco_ip} | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)


def pathping():
    endereco_ip = input(Fore.YELLOW + 'Digite o Endereço IP: ' + Style.RESET_ALL)
    processo = subprocess.run(
        ['powershell', '-Command', f'pathping {endereco_ip} | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)


def netstat_an():
    processo = subprocess.run(
        ['powershell', '-Command', 'netstat -an | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)



def arp_a():
    processo = subprocess.run(
        ['powershell', '-Command', 'arp -a | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)


def hostname():
    processo = subprocess.run(
        ['powershell', '-Command', 'hostname | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)


def getmac():
    processo = subprocess.run(
        ['powershell', '-Command', 'getmac | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)


def net_use():
    processo = subprocess.run(
        ['powershell', '-Command', 'net use | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)


def net_share():
    processo = subprocess.run(
        ['powershell', '-Command', 'net share | Format-Table -AutoSize | Out-String -Width 200'],
        capture_output=True, text=True, shell=False )
    print(processo.stdout)