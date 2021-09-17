
properties([pipelineTriggers([githubPush()])])


pipeline {
    agent any
    stages {
        stage('Checkout'){
            steps{
                git branch: 'main', url: 'https://github.com/mzakariabigdata/flask_app_ed'
            }
        }
        
        stage('Build') {
            agent {
                docker { image 'python:3.7.0' }
            }
            steps {
                sh '''
                python --version
                python -m venv venv
                . venv/bin/activate
                which python 
                ls -l
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test'){
            agent {
                docker { image 'python:3.7.0' }
            }
            steps {
                echo 'Test stage'
                sh '''
                . venv/bin/activate
                pip install -r tests/requirements.txt
                python -m pytest tests/ --junitxml=target/tests-report.xml  --cov-report term --cov-report xml:target/coverage-report.xml  --cov=app
                '''
            }
            post {
                always{
                    junit allowEmptyResults: true, testResults:'target/tests-report.xml'
                }
            }
        }
        stage('Quality') {
            agent {
                docker { image 'sonarsource/sonar-scanner-cli' }
            }
            steps {
                script{
                    sh 'sonar-scanner -D"sonar.projectKey=flask_app_ed" -D"sonar.sources=." -D"sonar.host.url=http://172.28.114.195:9000" -D"sonar.login=1f997e8aeffefaa2659eab04955f631960602389"'
                    // def qg = waitForQualityGate()
                    // if (qg.status != 'OK') {
                    //     error "Pipeline aborted due to quality gate failure: ${qg.status}"
                    // }
                }
                
            }
        }
        stage('Package'){
            steps {
                echo 'Test Package'
            }
        }
        stage('Tag'){
            steps {
                echo 'Test Tag'
            }
        }
        stage('Publish'){
            steps {
                echo 'Test Publish'
            }
        }
        stage('Xray'){
            steps {
                echo 'Test Xray'
            }
        }
        stage('Invoke cd'){
            steps {
                echo 'Test Xray'
            }
        }
        
    }
    
        post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}