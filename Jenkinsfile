pipeline {
    agent { label 'main' }
    stages {
        stage('build') {
            steps {
                sh "cd /var/lib/jenkins/workspace/my-django"
                sh '/usr/local/bin/docker-compose down'
                sh '/usr/local/bin/docker-compose up -d --build'
                echo 'it works111'
            }
        }
    }
}
