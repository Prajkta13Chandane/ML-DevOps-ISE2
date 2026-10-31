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

        stage('2. Check Tools') {
            steps {
                bat 'python --version'
                bat 'git --version'
            }
        }

        stage('3. Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('4. Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('5. Validate Application') {
    steps {
        bat '''
            python -c "from app import app; response = app.test_client().get('/'); print(response.status_code); assert response.status_code == 200"
        '''
    }
}
        stage('6. Health Check') {
    steps {
        bat '''
            python -c "from app import app; response = app.test_client().get('/health'); print(response.get_data(as_text=True)); assert response.status_code == 200"
        '''
    }
}

    post {
        success {
            echo 'SUCCESS: All pipeline stages completed.'
        }

        failure {
            echo 'FAILED: Check Console Output.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}