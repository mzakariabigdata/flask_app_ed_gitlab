# flask_app_ed
## Démarre flask app 
cd C:\Users\morch\Documents\workspaces\flask_app_ed_gitlab\flask_app_ed
pip install -e .
$env:FLASK_APP = "app"
$env:FLASK_ENV = "development"
flask run
python setup.py sdist
python setup.py install
## artifactory
docker run -d --name artifactory  -p 8081:8081 -p 8082:8082 docker.bintray.io/jfrog/artifactory-oss:latest
Version:  7.25.7
Artifactory Home: '/opt/jfrog/artifactory'
admin Zak_Zak!!01
eyJ2ZXIiOiIyIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYiLCJraWQiOiJjNEJTeHYzSGZNZG1EdXZDUjRIMlVJMTBmQ2E5SWxiZWdRX1hpYW94QnJzIn0.eyJzdWIiOiJqZmZlQDAwMFwvdXNlcnNcL2FkbWluIiwic2NwIjoiYXBwbGllZC1wZXJtaXNzaW9uc1wvYWRtaW4gYXBpOioiLCJhdWQiOiIqQCoiLCJpc3MiOiJqZmZlQDAwMCIsImlhdCI6MTYzMjExODgyNCwianRpIjoiOTJjYmYyNGMtMjc1OC00MzNiLWJmZTMtZTg3MzU0ZTA4ODYwIn0.hH2cb0wsef2PBISfl-FLYcAbPOGjV3eMo65rCAtUjIUA8626ATghmr6DMy3ioE-j_-TJ33_2YkQ8raDDs6ZXNOXkv5FtHel7FHGyjTqSGFFwyZWtQnPYrAeMWY059FihFLCTHTyhe46lwdFT6USRSVN7a3EIXBjV529y5d_oDgbKAkAYi6IeWEPYNWIRRJ1-TbS3NpJ5x4KotTZeJGkEJTssfG_VplbjXmQE9g_Xeug4Lnlb_3F1b7JIy4JGcxpdpZOVRBTPwlQfONS2QD-Wm6jegeQEoQt7Rsfo7cW3D8obz7iK-bpRbRJRBk0cT321E0hwVOSzgNsHDgLD1Qabkg
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
token jenkins-api xMVsWqzwCXXmMBE83ynD
gitlab_root_project CQdgiV2jmPfg78Rxcboy
#### nexus
  docker run -d -p 8081:8081 --name nexus sonatype/nexus3
#### send mail (https://sendgrid.com/)
### install plugin
error : WorkflowScript: 2: Invalid agent type "docker" specified. Must be one of [any, label, none] @ line 2, column 13.
solution :
-   install plugins "docker" + "docker pipeline"