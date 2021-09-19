@Library("shared-lib") _

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
        stage('Scan Sonar') {
            agent {
                docker { image 'sonarsource/sonar-scanner-cli' }
            }
            steps {
                
                script{
                    echo 'Test Quality'
                    withSonarQubeEnv(installationName: 'sq1'){
                            sh '/opt/sonar-scanner/bin/sonar-scanner  -D"sonar.sources=."'
                    }
                    // sh 'echo $PATH'
                    // sh 'which sonar-scanner'
                    // sh 'sonar-scanner -D"sonar.projectKey=flask_app_ed_gitlab" -D"sonar.sources=." -D"sonar.host.url=http://172.26.229.230:9000" -D"sonar.login=1f997e8aeffefaa2659eab04955f631960602389"'
                    
                    // timeout(time: 3, unit: 'MINUTES'){
                    //     waitForQualityGate abortPipeline: true
                    // }
                // def qg = waitForQualityGate()
                    // if (qg.status != 'OK') {
                    //     error "Pipeline aborted due to quality gate failure: ${qg.status}"
                    // }
                }
                
            }
        }
        // stage('Quality Gate'){
        //     steps {
        //         timeout(time: 3, unit: 'MINUTES'){
        //             waitForQualityGate abortPipeline: true
        //         }
        //     }
        // }
        stage('Package'){
            steps {
                echo 'Test Package'
            }
        }
        stage('Tag'){
            steps {
                echo 'Test Tag 1'

            }
        }
        stage('Shared lib'){
            steps {
                helloWorld(dayOfWeek: "Mardi", name: "Zakaria")
            }
        }
        stage('for the test branch'){
            when {
                branch 'test_*'
            }
            steps {
                echo 'this only runs for test branch'
            }
        }
        stage('for the main branch'){
            when {
                branch 'main'
            }
            steps {
                echo 'this only runs for test branch'
            }
        }
        stage('nexus Publish'){

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