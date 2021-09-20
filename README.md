# flask_app_ed
## Démarre app 
cd C:\Users\morch\Documents\workspaces\flask_app_ed_gitlab\flask_app_ed
pip install -e .
$env:FLASK_APP = "app"
$env:FLASK_ENV = "development"
flask run
python setup.py sdist
python setup.py install
## Démarrage jenkins (agent Docker)
### Commande to boot toolchain
#### vagrant
##### upgrade vbguest
vagrant plugin update vagrant-vbguest
vagrant reload
install docker (doc https://docs.docker.com/engine/install/centos/)
sudo  yum install ifconfig
#### Jenkins (mount docker socket)
    docker run -d --name jenkins -u root -p 8080:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker -v /home/jenkins_home:/var/jenkins_home jenkins/jenkins
#### SonarQube
    docker run -d --name sonarqube -p 9000:9000 
    admin root
    admin 08d9a207237e3b9422bd076c94896b739bb78017
#### Gitlab https://docs.gitlab.com/ee/install/docker.html
export GITLAB_HOME=$HOME/gitlab
sudo docker run --detach \
  --hostname 172.28.114.195 \
  --publish 443:443 --publish 80:80 --publish 23:22 \
  --name gitlab \
  --restart always \
  --volume $GITLAB_HOME/config:/etc/gitlab \
  --volume $GITLAB_HOME/logs:/var/log/gitlab \
  --volume $GITLAB_HOME/data:/var/opt/gitlab \
  gitlab/gitlab-ee:latest
root ZSJ/OvZAPShCXTUHFKmmor19++bCFf6D56FAnBg9dLk=
token jenkins-api CrbfPrx-d6icPho7t_e5
#### nexus
  docker run -d -p 8081:8081 --name nexus sonatype/nexus3
#### send mail (https://sendgrid.com/)
### install plugin
error : WorkflowScript: 2: Invalid agent type "docker" specified. Must be one of [any, label, none] @ line 2, column 13.
solution :
-   install plugins "docker" + "docker pipeline"