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
        echo "yarn"
        sh './inso --version'
//         sh './inso lint spec ./petstore.yaml'
        // Add more steps here for your OpenAPI linting process
      }
    }
    stage('Lint OpenAPI Spec') {
      steps {
        sh './inso lint spec ./petstore.yaml'
    }
    }
    stage('Generate kong.yaml') {
      steps {
        sh './inso generate config ./petstore.yaml --type declarative -o ./kong.yaml'
      }
    }
    stage('Check deck version') {
      steps {
        sh 'deck version'
      }
    }
     stage('Update') {
      steps {
        sh 'deck convert --from kong-gateway-2.x --to kong-gateway-3.x --input-file kong.yaml --output-file new-kong.yaml'
      }
    }
     stage('Check') {
      steps {
        sh 'deck sync -s new-kong.yaml --kong-addr http://13.233.109.117:8001'
      }
    }
  }
}
