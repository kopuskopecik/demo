pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                sh "cd /var/lib/jenkins/workspace/my-django"
                sh 'sudo docker-compose up -d'
                echo 'it works'
            }
        }
    }
}