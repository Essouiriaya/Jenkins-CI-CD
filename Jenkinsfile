pipeline {
    agent any

    environment {
        HOST = '0.0.0.0'
        PORT = '5000'
        APP_MODULE = 'app:app'
    }

    stages {

        // 1. Recuperation du code source depuis GitHub
        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-token',
                    url: 'https://github.com/Essouiriaya/Jenkins-CI-CD.git'
            }
        }

        // Declenchement automatique toutes les 5 minutes
        triggers {
            cron('H/5 * * * *')
        }

        // 2. Preparation de l'environnement Python
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        // 3. Execution des tests
        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --cov
                '''
            }
        }

        // 4. Deploiement de l'application Flask
        stage('Deploy Application') {
            steps {
                sh '''
                    . venv/bin/activate

                    # Arreter une ancienne instance si elle existe
                    pkill -f gunicorn || true

                    # Lancer l'application en arriere-plan
                    gunicorn --bind ${HOST}:${PORT} ${APP_MODULE} \
                        --daemon \
                        --access-logfile gunicorn.log \
                        --error-logfile gunicorn.log
                '''
            }
        }
    }
}
