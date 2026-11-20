
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'a'
            }
        }

        stage('Test - Dependency check') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat 'if not exist reports mkdir reports'

                    dependencyCheck(
                        odcInstallation: 'Dependency-Check',
                        nvdCredentialsId: 'nvd-api-keyy',
                        additionalArguments: '--scan . --format HTML --format XML --out reports'
                    )
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'

                    withSonarQubeEnv('SonarQube-Server') {
                        bat """
                            "${scannerHome}\\bin\\sonar-scanner.bat" ^
                            -Dsonar.projectKey=EV3-cbsgrudajksdnvf ^
                            -Dsonar.projectName=EV3-cbsgrudajksdnvf ^
                            -Dsonar.sources=. ^
                            -Dsonar.exclusions=**/reports/**
                        """
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Desplegando'
            }
        }
    }
}
