pipeline{
    agent {
        node{
            label 'docker-agent-node'
        }
    }
    stages{
        stage('Add .env'){
            steps{
            sh ''' 
            rm -rf *.tar.gz
            echo SECRET_KEY=${emailbotSECRET_KEY} > .env
            echo EMAIL_HOST=${EMAIL_HOST} >> .env
            echo EMAIL_HOST_USER=${EMAIL_HOST_USER} >> .env
            echo EMAIL_HOST_PASSWORD=${EMAIL_HOST_PASSWORD} >> .env
            echo DEFAULT_FROM_EMAIL=${DEFAULT_FROM_EMAIL} >> .env
            echo CELERY_BROKER_URL=${CELERY_BROKER_URL} >> .env
            '''
            }
        }
        stage('Package'){
            steps{
                sh '''
                tar czf emailbot-$BUILD_NUMBER.tar.gz .env emailscheduler static staticfiles templates Procfile celerybeat-schedule.bak celerybeat-schedule.dat celerybeat-schedule.dir db.sqlite3 manage.py requirements.txt runtime.txt deploy.sh
                '''
            }
        }
        stage('Deploy'){
            steps{
                sshPublisher(
                    publishers: [
                    sshPublisherDesc(
                    configName: 'portfolio', 
                    transfers: [sshTransfer(
                    cleanRemote: false, excludes: '', 
                    execCommand: '''sudo rm -rf /var/www/emailbot/emailbot-*.tar.gz 
                    sudo mv /home/ubuntu/emailbot-*.tar.gz /var/www/emailbot/;
                    cd /var/www/emailbot/;
                    sudo tar -xf emailbot-*.tar.gz;
                    sudo chmod +x deploy.sh;
                    ./deploy.sh; 
                    ''', 
                    execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, 
                    patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', 
                    sourceFiles: '**/*.gz')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: true)
                    ]
                )
            }
        }
    }
}