    sudo apt install fail2ban

    sudo systemctl start fail2ban ; sudo systemctl enable fail2ban
    
Create file called /etc/fail2ban/jail.local
    
    [sshd]
    enabled = true
    port = 22
    filter = sshd
    logpath = /var/log/auth.log
    maxretry = 3

Unbanning procedure:

    sudo fail2ban-client set sshd unbanip IP_ADDRESS
    
    
