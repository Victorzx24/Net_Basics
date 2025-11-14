Perfeito! Aqui está o **README completo, estilizado, organizado, profissional e pronto para o GitHub**, seguindo o mesmo padrão estético que usamos no seu outro projeto, mas agora adaptado ao **NetBasics**.

---

# 🛰️ **NetBasics — Automação e Estudo de Comandos de Rede (Windows)**

🧠 **NetBasics** é um projeto criado com o objetivo de **fortalecer conhecimentos em Redes de Computadores e Python**, automatizando diversos comandos fundamentais utilizados no diagnóstico e troubleshooting de redes *no Windows*.

O projeto facilita o uso de comandos como `ipconfig`, `ping`, `tracert`, `netstat`, `nslookup` e muitos outros — tudo através de um menu interativo e estilizado com **Colorama**.

---

## 🚀 **Objetivos do Projeto**

✔ Automatizar comandos básicos de rede para Windows
✔ Melhorar entendimento de diagnósticos e troubleshooting
✔ Praticar Python com **subprocess**, **regex**, **colorama**
✔ Tornar a saída dos comandos mais legível
✔ Criar uma ferramenta simples, mas funcional, para estudo contínuo

---

## 🧩 **Tecnologias Utilizadas**

* 🐍 **Python 3**
* 🎨 **Colorama** — estilização do terminal
* ⚙️ **subprocess** — execução de comandos PowerShell
* ⏱️ **time** — simulação de processos
* 🔍 **regex** *(parcialmente, dependendo de futuras melhorias)*
* 🪟 **PowerShell** — estrutura base dos comandos executados

---

## 🖥️ **Menu do NetBasics**

O programa exibe um menu interativo com as opções:

```
[0] Sair
[1] ipconfig
[2] ipconfig /all
[3] nslookup [domínio]
[4] ipconfig /release
[5] ipconfig /renew
[6] ipconfig /flushdns
[7] ping [IP]
[8] tracert [IP]
[9] pathping [IP]
[10] netstat -an
[11] arp -a
[12] hostname
[13] getmac
[14] net use
[15] net share
```

---

## 🧠 **Estrutura Interna do Projeto**

O código foi dividido em:

### 📁 `main.py`

* Exibe o banner
* Exibe o menu
* Recebe a opção do usuário
* Encaminha para a função correspondente

### 📁 `funcoes.py`

Contém todas as funções que executam comandos PowerShell via `subprocess`.

---

## 🛠️ **Tabela Explicativa das Funções**

| Função                 | Comando Executado    | Função na Rede                           |
| ---------------------- | -------------------- | ---------------------------------------- |
| `ipconfig()`           | `ipconfig`           | Mostra a configuração básica de IP       |
| `ipconfig_all()`       | `ipconfig /all`      | Mostra informações detalhadas de rede    |
| `nslookup()`           | `nslookup domínio`   | Consultar DNS de um domínio              |
| `ipconfig_release()`   | `ipconfig /release`  | Libera o endereço IP atual               |
| `ipconfig_renew()`     | `ipconfig /renew`    | Solicita novo IP ao servidor DHCP        |
| `ipconfig_flush_dns()` | `ipconfig /flushdns` | Limpa o cache DNS                        |
| `ping()`               | `ping destino`       | Testa conectividade                      |
| `tracert()`            | `tracert destino`    | Rastreia a rota até o host               |
| `pathping()`           | `pathping destino`   | Combina ping + tracert                   |
| `netstat_an()`         | `netstat -an`        | Lista portas e conexões ativas           |
| `arp_a()`              | `arp -a`             | Exibe cache ARP                          |
| `hostname()`           | `hostname`           | Mostra o nome do computador              |
| `getmac()`             | `getmac`             | Exibe os MACs das interfaces             |
| `net_use()`            | `net use`            | Lista conexões a recursos compartilhados |
| `net_share()`          | `net share`          | Lista recursos compartilhados            |

---

## 🎨 **Por que usar `Format-Table -AutoSize`?**

Todos os comandos utilizam:

```
| Format-Table -AutoSize | Out-String -Width 200
```

Isso foi feito para:

* 📏 melhor formatação
* 📘 colunas visualmente alinhadas
* 🧹 eliminação de textos truncados
* 🖥️ maior legibilidade no terminal Python

---

## 📌 **Possíveis Atualizações Futuras**

🔧 Adicionar logs
📡 Interface gráfica (Tkinter ou PyQt)
📂 Exportar resultados para `.txt`
🧪 Testes automáticos
🧠 Mais comandos avançados (TCPView, Get-NetIPAddress, etc.)

> O projeto foi criado para ser infinito em evolução — quanto mais você aprender, mais ele cresce.

---

## 📜 **Como executar**

```bash
python main.py
```

---