pipeline {
    agent any

    environment {
        REPOSITORY_URL = 'https://github.com/CaioHPP/Trabalho_DevOps_230789-0'
        BRANCH_NAME = 'main'
    }

    stages {
        stage('Baixar código do Git e Build Containers') {
            steps {
                // Clonar o repositório do Git
                git branch: "${BRANCH_NAME}", url: "${REPOSITORY_URL}"
                sh 'docker-compose down -v'
                sh 'docker-compose build'
            }
        }

        stage('Rodar Testes') {
            steps {
                script {
                    sh 'docker-compose up -d mariadb flask test mysqld_exporter prometheus grafana'
                    sh 'sleep 40'

                    try {
                        sh 'docker-compose run --rm test'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error 'Testes falharam. Pipeline interrompido.'
                    }
                }
            }
        }

        stage('Start Containers') {
                steps {
                    script {
                        sh 'docker-compose up -d mariadb flask test mysqld_exporter prometheus grafana'
                    }
                }
        }
    }

    post {
            failure {
                sh 'docker-compose down -v'
            }
        }
    }
pipeline {
    agent any

    environment {
        REPOSITORY_URL = 'https://github.com/CaioHPP/Trabalho_DevOps_230789-0'
        BRANCH_NAME = 'main'
    }

    stages {
        stage('Baixar código do Git e Build Containers') {
            steps {
                // Clonar o repositório do Git
                git branch: "${BRANCH_NAME}", url: "${REPOSITORY_URL}"
                sh 'docker-compose down'
                sh 'docker-compose build'
            }
        }

        stage('Rodar Testes') {
            steps {
                script {
                    sh 'docker-compose up -d mariadb flask test mysqld_exporter prometheus grafana'
                    sh 'sleep 40'

                    try {
                        sh 'docker-compose run --rm test'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error 'Testes falharam. Pipeline interrompido.'
                    }
                }
            }
        }

        stage('Start Containers') {
                steps {
                    script {
                        sh 'docker-compose up -d mariadb flask test mysqld_exporter prometheus grafana'
                    }
                }
        }
    }

    post {
            failure {
                sh 'docker-compose down'
            }
        }
    }
