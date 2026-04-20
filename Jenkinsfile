pipeline {
    agent any

    options {
        skipDefaultCheckout()
    }

    stages {
        stage('Clonar repositorio') {
            steps {
                checkout scm
            }
        }

        stage('Construir imagen Docker') {
            steps {
                dir('app') {
                    sh 'docker build -t flask_app .'
                }
            }
        }

        stage('Detener contenedor anterior') {
            steps {
                sh 'docker stop flask_app || true'
                sh 'docker rm flask_app || true'
            }
        }

        stage('Desplegar contenedor') {
            steps {
                sh 'docker run -d --name flask_app -p 5000:5000 flask_app'
            }
        }
    }
}