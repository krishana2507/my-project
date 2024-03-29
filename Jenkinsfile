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
        // Add more steps here for your OpenAPI linting process
      }
    }
    stage('Lint OpenAPI Spec') {
      steps {
        sh './inso lint spec petstore.yaml'
      }
    }
    stage('Generate kong.yaml') {
      steps {
        sh './inso generate config petstore.yaml --type declarative -o kong.yaml'
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
        sh 'jq --version'
       }
     }
    stage('Download yq') {
      steps {
        sh 'yq --version'
        }
      }
    stage('API Versioning') {
      steps {
        script {
          def w = "/default"
          def v = "/v1.1"
          sh "cat ./kong-new.yaml | yq eval '.services[].routes[].paths |= map(\"${w}${v}\" + .)' --prettyPrint > new-api.yaml"
        }
      }
    }
    stage('Check') {
      steps {
        sh 'deck sync -s ./new-api.yaml --kong-addr http://35.154.219.40:8001'
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
   
  
