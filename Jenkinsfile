pipeline {  
  agent any

  stages {
    stage('Lint OpenAPI Spec') {
      steps {
        sh 'wget https://github.com/Kong/insomnia/releases/download/lib%403.12.0/inso-linux-3.12.0.tar.xz'
        echo "Hello"
        sh 'tar -xf inso-linux-3.12.0.tar.xz'
        sh './inso lint spec ./petstore.yaml'
      }
    }
  }
}
