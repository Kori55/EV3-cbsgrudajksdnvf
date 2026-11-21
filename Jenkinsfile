
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'a'
            }
        }

        stage('Dependency check') {
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

        stage('OWASP ZAP Security Scan') {
            steps {
                echo 'Iniciando analisis de seguridad con OWASP ZAP...'

                bat '''
                    if not exist "%WORKSPACE%\\reports" mkdir "%WORKSPACE%\\reports"

                    pushd "C:\\Program Files\\ZAP\\Zed Attack Proxy"

                    call zap.bat ^
                        -cmd ^
                        -quickurl "http://127.0.0.1:5005" ^
                        -quickout "%WORKSPACE%\\reports\\zap-report.html" ^
                        -quickprogress

                    set "ZAP_EXIT=%ERRORLEVEL%"
                    popd

                    exit /b %ZAP_EXIT%
                '''
            }

            post {
                always {
                    archiveArtifacts artifacts: 'reports/zap-report.html', allowEmptyArchive: true
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
