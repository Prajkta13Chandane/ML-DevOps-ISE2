pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-prediction-app .'
            }
        }

        stage('Deploy Container') {
            steps {
                bat '''
                    docker rm -f student-app-ci 2>NUL
                    docker run -d --name student-app-ci -p 5001:5000 student-prediction-app
                '''
            }
        }

        stage('Health Check') {
            steps {
                bat 'curl.exe -fsS http://localhost:5001/health'
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}