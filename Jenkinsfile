pipeline {
    agent any

    environment {
        HOST = '0.0.0.0'
        PORT = '5000'
        APP_MODULE = 'app:app'
    }

    // Declenchement automatique
    triggers {
        githubPush()
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
            parallel {

                stage('Test App 1') {
                    steps {
                        sh '''
                            . venv/bin/activate
                            COVERAGE_FILE=.coverage.app1 pytest --cov -v test_app.py
                        '''
                    }
                }

                stage('Test App 2') {
                    steps {
                        sh '''
                            . venv/bin/activate
                            COVERAGE_FILE=.coverage.app2 pytest --cov -v test_app_2.py
                        '''
                    }
                }
            }
        }

        stage('Generate Coverage Report') {
            steps {
                sh '''
                    . venv/bin/activate
                    coverage combine
                    coverage report
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
