pipeline {  
  agent any

  stages {
    stage('Install Node.js') {
      steps {
        tool name: 'NodeJS', type: 'jenkins.plugins.nodejs.tools.NodeJSInstallation'
        echo "node Install"
      }
    }
    stage('node OpenAPI Spec') {
      steps {
        sh 'node --version' // Example step using Node.js
        sh 'npm --version'  // Example step using npm
        sh 'yarn --version' // Example step using yarn
        // Add more steps here for your OpenAPI linting process
      }
    }
    stage('Lint OpenAPI Spec') {
      steps {
        sh 'wget https://github.com/Kong/insomnia/releases/download/lib%403.12.0/inso-linux-3.12.0.tar.xz'
        echo "Hello"
        sh 'tar -xf inso-linux-3.12.0.tar.xz'
        sh './inso lint spec petstore.yaml'
      }
    }
  }
}
