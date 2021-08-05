pipeline {
    agent { label 'master' }
    environment {
        PATH = "$PATH:/usr/local/bin/docker-compose"
    }
    stages {
        stage('build') {
            steps {
                sh "cd /var/lib/jenkins/workspace/my-django"
                sh 'docker-compose up -d'
                echo 'it works'
            }
        }
    }
}