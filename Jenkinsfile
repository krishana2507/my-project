pipeline {                                          
  agent any   
  // environment {
  //   FIREBASE_CREDENTIALS = credentials('pipeline-jenkins')
  // }
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
        // Add more steps here for your OpenAPI linting process
      }
    }
    stage('Lint OpenAPI Spec') {
      steps {
        sh './inso lint spec ./petstore.yaml'
        echo "spec"
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
        echo "deck"
      }
    }
    stage('Update') {
      steps {
        sh 'deck convert --from kong-gateway-2.x --to kong-gateway-3.x --input-file ./kong.yaml --output-file ./kong-new.yaml'
        echo "convert"
      }
    }
    stage('Download jq') {
      steps {
        sh 'sudo apt install jq -y'
        sh 'jq --version'
       }
     }
    stage('Download yq') {
      steps {
        sh 'sudo snap install yq'
        sh 'yq --version'
        }
     }
    stage('API Versioning') {
      steps {
        script {
          def w = '/default'
          def v = '/v1.1'
          sh 'cat ./kong-new.yaml | yq \'.services.[].routes.[].paths.[] = env.w + env.v + .services.[].routes.[].paths.[]\' -o yaml > new-api.yaml'
        }
      }
    }
    stage('Check') {
      steps {
        sh 'deck sync -s ./new-api.yaml --kong-addr http://13.233.107.130:8001'
        echo "sync"
      }
    }
    stage('Commit files') {
      steps {
        sh '''
          git config --local user.email "krishna.sharma@neosalpha.com"
          git config --local user.name "krishna2507"
          git add *.yaml
          if [ -z "$(git status --porcelain)" ]; then
            echo "::set-output name=push::false"
          else
            git commit -m "Add changes sd" -a
            echo "::set-output name=push::true"
          fi
        '''
        script {
          if (env.BRANCH_NAME == 'main') {
            // Push changes only for the main branch
            gitPushChanges()
          } else {
            echo 'Skipping push changes as branch is not main.'
          }
        }
      }
    }

    stage('Publish OAS to dev portal') {
      steps {
        script {
          if (env.BRANCH_NAME == 'main') {
            // Publish API to dev portal only for the main branch
            sh 'portal deploy -D default --preserve'
          }
        }
      }
    }
   
   // stage('Deploy to Firebase') {
   //    steps {
   //      withCredentials([file(credentialsId: 'pipeline-jenkins', variable: 'FIREBASE_CREDENTIALS')]) {
   //        dir('/home/ec2-user/firebase.json'){
   //        sh 'firebase deploy --token $FIREBASE_CREDENTIALS'
   //        }
   //      }
   //    }
   // }
  }
}
