pipeline {
  agent {
    docker {
      image 'python:3'
      args '''-v $PWD:/usr/src/app
-w /app'''
    }

  }
  stages {
    stage('run pip install ') {
      steps {
        input(message: 'ready to go', ok: 'Next')
        echo 'Hello'
      }
    }
    stage('pip install') {
      steps {
        sh 'pip install --no-cache-dir -r requirements.txt'
      }
    }
    stage('') {
      steps {
        sh 'python -m unittest test_app'
      }
    }
  }
}