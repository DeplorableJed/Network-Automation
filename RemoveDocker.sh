sudo apt-get purge -y docker.io 
sudo apt-get autoremove -y --purge docker.io
sudo apt-get autoclean
sudo rm -rf /var/lib/docker
sudo rm -rf /etc/docker
sudo rm /etc/apparmor.d/docker
sudo apt-get purge runc containerd docker.io
