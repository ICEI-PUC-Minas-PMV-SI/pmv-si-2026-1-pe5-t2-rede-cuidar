::::: titlepage
:::: center
**PONTIFÍCIA UNIVERSIDADE CATÓLICA DE MINAS GERAIS**\
**SISTEMAS DE INFORMAÇÃO**\
**Projeto de Infraestrutura de Redes:\
Rede Hospitalar Cuidar**\
*Documento de Planejamento e Implementação*\

::: flushleft
**Grupo de Trabalho:**\
Athos Geraldo Salomon Dolabela da Silveira\
Bernardo Elias Renttins Vasconcelos de Sousa\
Fabrício Junio da Silva\
Henrique Fadel Carvalho\
Igor de Oliveira Martins dos Santos\
Pedro Tolentino Gontijo
:::

**Belo Horizonte**\
**2026**
::::
:::::

# Etapa 1 --- Planejamento e Prototipação

## Gestão e Organização do Projeto

### Definição do Tema e Cenário

O projeto foca na **Rede Hospitalar Cuidar**, uma instituição de saúde
com matriz em Belo Horizonte e unidades remotas (Secretaria e três
UPAs). O cenário exige alta disponibilidade e segmentação, dado o
tráfego de dados sensíveis e a necessidade de comunicação ininterrupta
para prontuários eletrônicos.

### Responsabilidades e Colaboração

Para atender à gestão da comunicação e colaboração, o grupo utilizou
ferramentas como Microsoft Teams e WhatsApp para alinhamento síncrono e
assíncrono.

- **Igor e Pedro:** Planejamento de sub-redes (CIDR), NAT e lógica de
  serviços.

- **Henrique:** Implementação técnica e nomenclatura no Cisco Packet
  Tracer.

- **Bernardo e Athos:** Gestão de ativos, custos e planilhas de
  inventário.

- **Fabrício:** Redação técnica e revisão das normas de documentação.

### Cronograma de Dedicação

::: center
  **Data**        **Tarefa**
  --------------- ----------------------------------------------------------------
  09/02 a 28/02   Estudo dos microfundamentos e definição do cenário.
  01/03 a 15/03   Elaboração do inventário detalhado e cálculos de tráfego.
  16/03 a 24/03   Desenvolvimento do protótipo e testes de conectividade (Ping).
  25/03 a 28/03   Ajustes de nomenclatura conforme feedback e entrega final.
:::

## Arquitetura Lógica e Endereçamento

### Divisão por CIDR e NAT

A rede utiliza o bloco privado `10.0.0.0/8`, segmentado para otimizar o
domínio de broadcast e aumentar a segurança.

::: center
  **Unidade**   **Faixa de Rede**   **Gateway**   **Servidor Principal**
  ------------- ------------------- ------------- --------------------------------
  Matriz        10.10.0.0/24        10.10.0.1     SRV-BH-PRONTUARIO (10.10.0.10)
  Secretaria    10.20.0.0/24        10.20.0.1     SRV-SEC-ADMIN (10.20.0.10)
  UPA 1         10.30.0.0/24        10.30.0.1     SRV-UPA1-LOCAL (10.30.0.10)
  UPA 2         10.40.0.0/24        10.40.0.1     SRV-UPA2-LOCAL (10.40.0.10)
  UPA 3         10.50.0.0/24        10.50.0.1     SRV-UPA3-LOCAL (10.50.0.10)
:::

**NAT (Network Address Translation):** Implementado nos roteadores de
borda para mascarar as redes internas e permitir a saída WAN via IPs
públicos simulados, protegendo a integridade da rede hospitalar.

## Justificativa de Recursos

### Inventário de Equipamentos

O inventário foi organizado para equilibrar custo-benefício e robustez.
Na Matriz, optamos por **Switches Cisco Catalyst 9200L** pela capacidade
de empilhamento e **Firewalls FortiGate** para segurança NGFW. O uso de
nobreaks senoidais da APC garante que os sistemas de prontuário não
sofram quedas por oscilações elétricas.

### Cálculo de Links e Tráfego

Conforme a planilha de cálculos, a Matriz possui um link de 152 Mbps,
dimensionado para suportar o tráfego de videoconsultas e sincronização
de banco de dados das filiais, que operam com links de 42.4 Mbps cada.

## Plano de Testes e Validação

Para validar o funcionamento, estabelecemos os seguintes testes no
protótipo:

1.  **Teste de Conectividade Interna:** Pings entre PCs da mesma
    sub-rede.

2.  **Teste de Conectividade WAN:** Pings entre a UPA 3 e o
    SRV-BH-PRONTUARIO.

3.  **Validação de Nomenclatura:** Conferência de que todos os
    dispositivos seguem o padrão *Unidade-Setor-ID*.

## Conclusão della Etapa 1

A Etapa 1 conclui-se com um protótipo funcional e uma documentação que
justifica cada ativo escolhido. O projeto está pronto para a próxima
fase, garantindo que a infraestrutura física e lógica atenda às demandas
críticas da Rede Hospitalar Cuidar.

# Etapa 2 --- Preparação do Ambiente em Nuvem e Virtualização Local

## Introdução

A Etapa 2 é marcada pelo mapeamento e implantação dos servidores em
nuvem e *on-premise* para o devido atendimento do planejamento inicial.
Nesta etapa, adaptações e definições de escopo foram realizadas para
garantir a conformidade com o planejamento estabelecido na Etapa 1, bem
como para atender às eventuais necessidades identificadas na fase
anterior.

## Gestão e Organização da Etapa

### Responsabilidades e Colaboração

Para a execução da Etapa 2, as responsabilidades foram distribuídas
entre os membros do grupo de forma a aproveitar as competências
individuais e garantir a entrega dentro do prazo estabelecido.

- **Igor e Pedro:** Configuração das instâncias EC2 na AWS e definição
  da arquitetura da VPC `rede-cuidar-vpc`.

- **Henrique:** Configuração do servidor Ubuntu no Oracle VirtualBox,
  incluindo definição de IP estático via `netplan` e integração com a
  rede local.

- **Bernardo e Athos:** Instalação e validação dos serviços no servidor
  Ubuntu (Apache2, MySQL, BIND9, DHCP e VSFTPD), além do acompanhamento
  de custos da instância AWS.

- **Fabrício:** Configuração do Active Directory, criação das Unidades
  Organizacionais, vinculação de GPO e redação técnica do documento.

## Ambiente em Nuvem --- Amazon Web Services (AWS)

### Escolha da Plataforma

O grupo optou pela utilização do **Amazon EC2** (Elastic Compute Cloud)
como plataforma de nuvem, por ser um dos principais *players* de
mercado, oferecendo alta disponibilidade, escalabilidade e um vasto
ecossistema de serviços gerenciados adequados à infraestrutura
hospitalar da Rede Cuidar.

### Instâncias Configuradas

As instâncias foram criadas conforme o mapeamento de servidores definido
na Etapa 1, seguindo as boas práticas de nomenclatura e endereçamento
estabelecidas. O **Windows Server** foi implantado via instância EC2
para atuar como servidor de aplicação para publicação do back-end
hospitalar.

::: center
  **Campo**             **Informação**
  --------------------- --------------------------------
  Nome da Instância     Rede Cuidar
  ID da Instância       i-03c0d9df7ad6e2f96
  Tipo de Instância     t2.large
  Sistema Operacional   Windows Server 2016 Datacenter
  IP Público            54.80.166.57
  IP Privado            10.0.1.84
  Usuário de Acesso     Administrator
  Método de Acesso      RDP (Área de Trabalho Remota)
  Região                us-east-1 (Norte da Virgínia)
  VPC                   rede-cuidar-vpc (10.0.0.0/16)
  Status                Executando
:::

### Configuração de Segurança --- Acesso Criptografado

O acesso às instâncias é realizado por meio de **SSH com autenticação
por par de chaves pública/privada**, garantindo comunicação totalmente
criptografada entre os administradores e os servidores em nuvem. Essa
abordagem atende às boas práticas de segurança em infraestrutura de
redes e assegura que nenhum acesso não autorizado seja possível sem a
chave privada correspondente.

## Virtualização Local --- Oracle VirtualBox

### Configuração do Servidor On-Premise

Para o mapeamento dos serviços *on-premise*, foi utilizado o **Oracle
VirtualBox** como plataforma de virtualização. O servidor local foi
configurado com o sistema operacional **Ubuntu Server**, representando o
servidor `SRV-BH-PRONTUARIO` da Matriz, conforme planejado na Etapa 1.

### Configuração de Rede --- IP Estático

O servidor virtual foi configurado com **endereço IP estático** via
`netplan`, garantindo que o endereço de rede seja fixo e compatível com
o plano de infraestrutura. A configuração foi aplicada no arquivo
`/etc/netplan/50-cloud-init.yaml` com os seguintes parâmetros:

- **Interface:** `enp0s3`

- **Endereço IP:** `192.168.18.75/24`

- **Gateway:** `192.168.18.1`

- **DNS primário:** `8.8.8.8` (Google DNS)

- **DNS secundário:** `8.8.4.4` (Google DNS)

- **DHCP4:** Desabilitado

::: center
    network:
      version: 2
      ethernets:
        enp0s3:
          dhcp4: false
          addresses:
            - 192.168.18.75/24
          routes:
            - to: default
              via: 192.168.18.1
          nameservers:
            addresses:
              - 8.8.8.8
              - 8.8.4.4
:::

### Serviços Instalados

O servidor Ubuntu foi configurado com os seguintes serviços, atendendo
às demandas de infraestrutura hospitalar mapeadas na Etapa 1:

::: center
  **Serviço**   **Função**                                               **Porta Padrão**
  ------------- -------------------------------------------------------- ------------------
  SSH           Acesso remoto seguro e criptografado ao servidor         22
  Apache2       Servidor Web para publicação de aplicações               80/443
  MySQL         Banco de dados relacional para prontuários eletrônicos   3306
  BIND9/named   Servidor DNS para resolução de nomes da rede interna     53
  DHCP          Distribuição automática de endereços IP na rede local    67
  VSFTPD        Servidor FTP para transferência segura de arquivos       21
:::

Todos os serviços foram instalados e configurados conforme as boas
práticas de administração de sistemas Linux, garantindo que o servidor
`SRV-BH-PRONTUARIO` esteja apto a atender as demandas da Matriz da Rede
Hospitalar Cuidar.

## Evidências de Funcionamento

### Servidor Ubuntu (VirtualBox) --- IP Estático

<figure id="fig:ubuntu_ip" data-latex-placement="H">
<img src="./print_ip_estatico.png" />
<figcaption>Servidor Ubuntu On-Premise com IP estático configurado
(<code>192.168.18.75/24</code>)</figcaption>
</figure>

### Servidor Ubuntu (VirtualBox) --- Serviços Ativos

<figure id="fig:ubuntu_servicos" data-latex-placement="H">
<img src="./print_servicos.png" />
<figcaption>Serviços instalados e ativos no servidor Ubuntu
On-Premise</figcaption>
</figure>

### Instância AWS EC2 --- Nuvem

<figure id="fig:aws_instancia" data-latex-placement="H">
<img src="./print_instancia.png" />
<figcaption>Instância EC2 “Rede Cuidar” em execução no painel da
AWS</figcaption>
</figure>

### Windows Server --- Servidor de Aplicação

<figure id="fig:windows_server" data-latex-placement="H">
<img src="./windows_server.png" />
<figcaption>Windows Server 2016 Datacenter em execução na instância
AWS</figcaption>
</figure>

### VPC --- Rede Privada Virtual (AWS)

<figure id="fig:vpc" data-latex-placement="H">
<img src="./print_vpc.png" />
<figcaption>VPC <code>rede-cuidar-vpc</code> configurada na AWS com CIDR
<code>10.0.0.0/16</code></figcaption>
</figure>

### Active Directory --- Estrutura do Domínio

<figure id="fig:ad_estrutura" data-latex-placement="H">
<img src="./ad_print.png" />
<figcaption>Central Administrativa do Active Directory — domínio
<code>minasgerais.net</code></figcaption>
</figure>

### Active Directory --- Unidades Organizacionais (OUs)

<figure id="fig:ad_ous" data-latex-placement="H">
<img src="./subredes_print.png" />
<figcaption>OUs criadas no AD: <code>minas</code> com sub-OUs
<code>belohorizonte</code>, <code>betim</code> e
<code>contagem</code></figcaption>
</figure>

### Política de Grupo (GPO)

<figure id="fig:gpo" data-latex-placement="H">
<img src="./gpo_criada.png" />
<figcaption>GPO <code>pgbh</code> vinculada à OU <code>usuarios</code>
em <code>belohorizonte</code></figcaption>
</figure>

## Vídeo Demonstrativo

O vídeo demonstrativo da Etapa 2, exibindo o funcionamento dos ambientes
configurados, está disponível no Microsoft Teams pelo link abaixo:

::: center
**Link:**
<https://sgapucminasbr.sharepoint.com/sites/team_sga_2414_2026_1_7378102/_layouts/15/guestaccess.aspx?share=IQBUD9anyHlnSZGWIaAY6TzEAaYO6do7X8C4R6jARODEzeA&e=qDsxRR>
:::

# Etapa 3 --- Monitoramento Ativo da Infraestrutura de Servidores

## Introdução ao Monitoramento Centralizado

Para garantir os critérios de alta disponibilidade, integridade,
identificação proativa de gargalos e comunicação ininterrupta exigidos
pela **Rede Hospitalar Cuidar**, foi consolidada uma solução de
monitoramento de ativos utilizando a ferramenta corporativa **Zabbix**.

Nesta etapa, a infraestrutura foi integrada de ponta a ponta, permitindo
a coleta de dados de desempenho em tempo real por meio de agentes
dedicados e protocolos de rede. A telemetria abrange o consumo de
hardware (processamento, memória, E/S de disco) e volumetria de tráfego
de dados, fornecendo visibilidade total sobre o ecossistema local e em
nuvem.

## Gestão e Organização da Etapa

### Responsabilidades e Colaboração

As atividades da Etapa 3 foram distribuídas entre os membros do grupo
conforme as competências demonstradas nas etapas anteriores, garantindo
continuidade e coesão na execução do projeto.

- **Igor e Pedro:** Instalação e configuração do Zabbix Appliance como
  plataforma central de monitoramento, incluindo definição de IP
  estático e acesso à interface web.

- **Henrique:** Configuração do protocolo SNMP nos servidores Ubuntu e
  Windows, correção das permissões de acesso no `snmpd.conf` e cadastro
  dos hosts no Zabbix.

- **Bernardo e Athos:** Criação do mapa de rede *Rede Hospitalar Cuidar*
  e configuração do dashboard personalizado com widgets de métricas e
  alertas.

- **Fabrício:** Análise e interpretação dos dados coletados pelo Zabbix,
  documentação dos resultados e redação técnica do capítulo.

## Topologia Lógica e Visões de Gerência

### Mapa de Conectividade da Infraestrutura

Abaixo apresenta-se o mapa de topologia estruturado no painel nativo do
Zabbix (*All maps / Rede Hospitalar Cuidar*), ilustrando as relações de
conectividade e o fluxo saudável de comunicação entre os nós de
gerência.

<figure id="fig:zabbix_mapa" data-latex-placement="H">
<img src="./print_mapa.png" style="width:90.0%" />
<figcaption>Mapa de monitoramento integrado da infraestrutura local e
nuvem no Zabbix</figcaption>
</figure>

### Painel Global de Operações (Dashboard)

O monitoramento centralizado conta com um painel de controle principal
(*Dashboard*), que agrega os principais indicadores de desempenho do
ecossistema hospitalar, facilitando a tomada de decisão em nível de
suporte de infraestrutura.

<figure id="fig:zabbix_dashboard" data-latex-placement="H">
<img src="./dashboard_print.png" />
<figcaption>Dashboard geral do Zabbix exibindo a saúde integrada do
ambiente hospitalar</figcaption>
</figure>

### Inventário de Hosts e Status de Disponibilidade

Como evidenciado no painel de controle, todos os hosts monitorados foram
devidamente parametrizados e encontram-se operando sem a presença de
problemas ou alertas ativos. A integração com o agente Zabbix garante a
confiabilidade dos status apresentados.

<figure id="fig:hosts_operacionais" data-latex-placement="H">
<img src="./hosts_verdes.png" />
<figcaption>Listagem de hosts ativos e com status operacional
estabilizado</figcaption>
</figure>

## Métricas de Performance --- Servidor Local (srv-bh-prontuario)

O servidor local virtualizado, responsável pelo banco de dados de
prontuários eletrônicos e serviços internos da Matriz em Belo Horizonte,
teve seu comportamento monitorado e os gráficos gerados comprovam a
conformidade do ambiente.

### Utilização de CPU

O gráfico ilustra a carga de processamento da CPU do servidor Ubuntu.
Nota-se que os níveis operacionais mantêm-se baixos e estáveis,
garantindo ampla margem para picos de requisições concorrentes.

<figure id="fig:cpu_ubuntu" data-latex-placement="H">
<img src="./cpu_utilization_ubuntu.png" style="width:90.0%" />
<figcaption>Métricas de uso de processador (CPU) no servidor Ubuntu
local</figcaption>
</figure>

### Utilização de Memória RAM

A telemetria de memória segmenta o espaço total alocado, identificando a
fatia utilizada, disponível e em cache, atestando que a máquina não
sofre com paginação excessiva em disco.

<figure id="fig:memoria_ubuntu" data-latex-placement="H">
<img src="./memory_utilization_ubuntu.png" style="width:90.0%" />
<figcaption>Análise de alocação e consumo de memória RAM do servidor
local</figcaption>
</figure>

### E/S de Disco (Leitura e Escrita)

Monitorar as operações de entrada e saída por segundo (IOPS) e taxa de
transferência é crucial para o banco de dados MySQL. O gráfico confirma
baixa latência de gravação física.

<figure id="fig:disco_ubuntu" data-latex-placement="H">
<img src="./disco_readwirte_ubuntu.png" style="width:90.0%" />
<figcaption>Estatísticas de leitura e escrita em disco do servidor de
banco de dados</figcaption>
</figure>

### Tráfego de Rede

O volume de dados trafegado pela interface de rede (`enp0s3`) exibe o
fluxo simétrico de dados de entrada (*In*) e saída (*Out*), atestando a
integridade das respostas do Apache2 e DNS BIND9.

<figure id="fig:rede_ubuntu" data-latex-placement="H">
<img src="./network_traffic_ubuntu.png" style="width:90.0%" />
<figcaption>Volume e taxa de transferência de pacotes na interface de
rede local</figcaption>
</figure>

## Métricas de Performance --- Servidor em Nuvem (srv-aws-cuidar)

A instância EC2 alocada na região de Norte da Virgínia (`us-east-1`),
que atua com o papel de controlador de domínio Active Directory e
hospedagem do back-end hospitalar, teve suas métricas consolidadas.

### Utilização de CPU

O monitoramento via contador do Windows Server mapeia as flutuações de
uso do processador da instância `t2.large`. Os dados coletados apontam
para um comportamento saudável e livre de gargalos lógicos de
processamento.

<figure id="fig:cpu_aws" data-latex-placement="H">
<img src="./cpu_utilization_aws.png" style="width:90.0%" />
<figcaption>Métricas de processamento da instância EC2 Windows Server na
AWS</figcaption>
</figure>

### Utilização de Memória RAM

A telemetria exibe o consumo percentual e em bytes da memória do Windows
Server. O gráfico assegura que o Active Directory e as políticas de
grupo (GPO) aplicadas estão rodando de forma otimizada.

<figure id="fig:memoria_aws" data-latex-placement="H">
<img src="./memory_utilization_aws.png" style="width:90.0%" />
<figcaption>Gráfico de uso de memória física na instância de aplicação
em nuvem</figcaption>
</figure>

### Tráfego de Rede na Instância Cloud

Os dados exibem o tráfego que cruza a placa de rede virtual conectada à
VPC. A estabilidade dos gráficos comprova que, após a parametrização
fina dos limiares (*thresholds*) de checagem do Zabbix, a latência
geográfica maior devido à rota internacional foi devidamente mitigada,
não interferindo na qualidade da coleta contínua de dados do agente.

<figure id="fig:rede_aws" data-latex-placement="H">
<img src="./rede_utilization_aws.png" style="width:90.0%" />
<figcaption>Análise de pacotes enviados e recebidos através da interface
WAN da AWS</figcaption>
</figure>

# Etapa 4 --- \[Título a Definir\]

::: center
*Este capítulo será preenchido na entrega da Etapa 4.*
:::

# Etapa 5 --- \[Título a Definir\]

::: center
*Este capítulo será preenchido na entrega da Etapa 5.*
:::
