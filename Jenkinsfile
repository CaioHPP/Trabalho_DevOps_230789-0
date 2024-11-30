pipeline {
    agent any

    environment {
        REPOSITORY_URL = 'git@github.com:CaioHPP/Trabalho_DevOps_230789-0.git'
        BRANCH_NAME = 'dev'
    }

    stages {
        stage('Baixar código do Git') {
            steps {
                // Clonar o repositório do Git
                git branch: "${BRANCH_NAME}", url: "${REPOSITORY_URL}"
            }
        }

        stage('Rodar Testes') {
            steps {
                script {
                    // Rodar os testes com o pytest (ou qualquer outra ferramenta de testes que você esteja utilizando)
                    sh 'pytest --maxfail=1 --disable-warnings -q'
                }
            }
        }

        stage('Build e Deploy') {
            steps {
                script {
                    // Construir as imagens Docker para cada serviço
                    sh '''
                        docker-compose build
                    '''

                    // Subir os containers do Docker com Docker Compose
                    sh '''
                        docker-compose up -d
                    '''

                    // // (Opcional) Realizar o monitoramento e verificação de saúde após o deploy
                    // // Exemplo para verificar se o container Flask está funcionando:
                    // sh '''
                    //     docker ps -q --filter "name=flask"
                    // '''

                // // Verificar logs do Prometheus ou Grafana, caso necessário
                // sh '''
                //     docker logs prometheus
                //     docker logs grafana
                // '''
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executada com sucesso!'
        }
        failure {
            echo 'A pipeline falhou.'
        }
    }
}
