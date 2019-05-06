
### ubuntu mirror instructions  
Install ubuntu 18.04 desktop 

sudo su ; apt update ; apt upgrade  

apt install apt-mirror  

Pick a mirror from Ubuntu mirrors: e.g. us.archive.ubuntu.com  


Edit /etc/apt/mirror.list (for bionic 18.04) as so:   

deb http://us.archive.ubuntu.com/ubuntu bionic main restricted universe multiverse   

deb-i386 http://us.archive.ubuntu.com/ubuntu bionic main restricted universe multiverse  

...bionic-updates... ...bionic-security...  

Install apache2, net-tools (for ifconfig)   

apt install apache2 net-tools  

cd /var/www/html   

ln -s /var/spool/apt-mirror/mirror/us.archive.ubuntu.com/ubuntu ubuntu  
