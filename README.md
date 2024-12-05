# Projeto DevOps: Pipeline CI/CD com Docker, Prometheus, Grafana e Jenkins

## **Descrição do Projeto**

Este projeto foi desenvolvido como parte de um trabalho de DevOps, com o objetivo de criar um pipeline CI/CD que automatiza as etapas de desenvolvimento e monitoramento de uma aplicação. O pipeline, configurado no Jenkins, realiza as seguintes etapas:

1. **Baixar Código do Git**: Clona o repositório para iniciar o processo.
2. **Rodar Testes**: Executa testes automatizados para validar a aplicação.
3. **Build e Deploy**: Realiza o build da aplicação, cria imagens Docker e provisiona o ambiente completo.

A aplicação utiliza múltiplos containers Docker, incluindo:
- **MariaDB** para o banco de dados.
- **Flask** para a aplicação web.
- **Prometheus** e **Grafana** para monitoramento e visualização de métricas.


## **Autor**
- **Nome**: Caio Henrique Pedroso Pedro
- **RA**: 230789-0

---

## **Requisitos e Configuração do Ambiente**

### **Ambiente**

Para rodar no Windows, utilizei o WSL com a versão **Ubuntu 22.04.1 LTS**.

### **Instalação do Docker e Docker Compose**

Execute os seguintes comandos:

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \  
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \  
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \  
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo docker run hello-world
sudo apt install docker-compose

sudo chmod 777 /var/run/docker.sock
```

### **Instalação do Jenkins**

Instale o Jenkins e suas dependências:

```bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \  
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \  
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \  
  /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt-get update
sudo apt-get install jenkins

sudo apt update
sudo apt install fontconfig openjdk-17-jre
```

Para rodar o Jenkins:

```bash
jenkins
```

Acesse o Jenkins em: [http://localhost:8080](http://localhost:8080)

> <image src="images/image1.png">

### **Configuração do Pipeline no Jenkins**

1. Crie uma nova tarefa no menu à esquerda e escolha **Pipeline** como tipo.
> <image src="images/image2.png">
2. Configure as opções:
   - **Pipeline Script from SCM**.
   - **SCM**: Git.
   - **Repository URL**: `https://github.com/CaioHPP/Trabalho_DevOps_230789-0.git`.
   - **Branch**: `*/main`. (Atenção: o nome da branch pode variar).
   - **Script Path**: `Jenkinsfile`.
> <image src="images/image3.png">   

3. Salve e inicie o pipeline. Escolha "Construir Agora" para rodar o processo.
> <image src="images/image3.5.png">   

#### **Temporização no Jenkins**

Para configurar a execução automática do pipeline, utilize a opção **Build Triggers** na configuração do pipeline. Escolha "Build periodically" e adicione uma expressão cron, como:

```
H/5 * * * *
```

Essa configuração executará o pipeline a cada 5 minutos. Ajuste conforme necessário.

> <image src="images/image4.png">   

---

## **Endpoints e Funcionalidades**

### **Aplicação Flask**
- URL: [http://localhost:5000](http://localhost:5000)
- Login: `admin` / `admin`
- Funcionalidade: Lista de estudantes gerada pelos testes.

> <image src="images/image5.png">   

### **Prometheus**
- URL: [http://localhost:9090/targets](http://localhost:9090/targets)
- Funcionalidade: Visualizar status dos endpoints monitorados.

> <image src="images/image6.png">   

### **Grafana**
- URL: [http://localhost:3000](http://localhost:3000)
- Login: `admin` / `admin`
- Funcionalidades:
  - **Status do Node**.
  - **Métricas de CPU, memória, tempo de resposta, erros HTTP, entre outras.**

> <image src="images/image7.png"><image src="images/image8.png">  

---

## **Dashboards no Grafana**

> <image src="images/image9.png">
Os dashboards fornecem:
- Status do Node.
- % de CPU utilizada.
- Uso de memória.
- Tempo médio de resposta.
- Taxa de requisições por segundo.
- Taxa de erros.
- Nº de Requests em processo.

---

## **Observações**

>- Caso se depare com o seguinte erro:
><image src="images/image10.png">
>
>Pare o Jenkins, execute o comando abaixo e reinicie o Jenkins:
```bash
sudo chmod 777 /var/run/docker.sock
```

>- Caso se depare com o seguinte erro:
><image src="images/image11.png">
>Pare o serviço do Jenkins e reinicie o Jenkins:

```bash
sudo systemctl stop jenkins
jenkins
```