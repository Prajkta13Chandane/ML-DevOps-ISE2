```groovy
pipeline {
    agent any

    stages {
        stage('1. Check Tools') {
            steps {
                bat 'python --version'
                bat 'git --version'
            }
        }

        stage('2. Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('3. Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('4. Validate Application') {
            steps {
                bat '''
                    python -c "from app import app; response = app.test_client().get('/'); print(response.status_code); assert response.status_code == 200"
                '''
            }
        }

        stage('5. Health Check') {
            steps {
                bat '''
                    python -c "from app import app; response = app.test_client().get('/health'); print(response.get_data(as_text=True)); assert response.status_code == 200"
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All pipeline stages completed!'
        }
        failure {
            echo 'FAILURE: Check the Console Output for details.'
        }
    }
}
