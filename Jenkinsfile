pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/iphuoc0309/Adience.git'
            }
        }
        stage('Build') {
            steps {
                // This step should not normally be used in your script. Consult the inline help for details.
                withDockerRegistry(credentialsId: 'adience', url: 'https://index.docker.io/v1/') {
                    sh label: '', script: 'docker build -t iphuoc0309/adience:latest .'
                    sh label: '', script: 'docker push iphuoc0309/adience:latest'
                }
            }
        }
    }
}