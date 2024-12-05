pipeline {
    agent any

    environment {
        REPOSITORY_URL = 'https://github.com/CaioHPP/Trabalho_DevOps_230789-0'
        BRANCH_NAME = 'main'
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

                    echo 'Testes antes do deploys!'
                }
            }
        }

        stage('Build e Deploy') {
            steps {
                script {
                    sh '''
                     docker compose build
                    '''

                    sh '''
                        docker compose up -d
                    '''
                }
            }
        }
        stage('Rodar Testes depois do deploy') {
            steps {
                script {
                    // Rodar os testes com o pytest (ou qualquer outra ferramenta de testes que você esteja utilizando)
                    sh 'sleep 50' // Esperar 50 segundos para o container subir
                    sh 'docker compose run --rm test'
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
