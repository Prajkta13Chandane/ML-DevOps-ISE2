```groovy
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {

        stage('1. Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('2. Check Python') {
            steps {
                bat 'python --version'
                bat 'git --version'
            }
        }

        stage('3. Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m pip install pytest'
            }
        }

        stage('4. Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('5. Validate Flask Application') {
            steps {
                bat '''
                    python -c "from app import app; client = app.test_client(); response = client.get('/health'); print(response.get_data(as_text=True)); assert response.status_code == 200"
                '''
            }
        }

        stage('6. Deployment Information') {
            steps {
                echo 'Application tests passed.'
                echo 'Flask application is ready to run.'
            }
        }

        stage('7. Health Monitoring') {
            steps {
                bat '''
                    python -c "from app import app; response = app.test_client().get('/health'); assert response.status_code == 200; print('Health Check: PASSED')"
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: CI/CD pipeline completed successfully.'
        }

        failure {
            echo 'FAILED: Check Console Output for errors.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
```