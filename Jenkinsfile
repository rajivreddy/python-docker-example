pipeline {
  agent none
  stages {
    stage('run pip install ') {
      agent docker {
            image 'python:3'        }
      steps {
        input(message: 'ready to go', ok: 'Next')
        echo 'Hello'
      }
    }
    // stage('pip install') {
    //   steps {
    //     sh 'pip install --no-cache-dir -r requirements.txt'
    //   }
    // }
    // stage('') {
    //   steps {
    //     sh 'python -m unittest test_app'
    //   }
    // }
  }
}
