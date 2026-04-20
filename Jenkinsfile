pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/cygnux33/mi-repositorio-devops.git'
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
