## Introduction

Control raspi GPIO pin from webpage(home-automation-php).

## Requirement

 - Raspberry PI 3(tested on 3, should be working also on 2)
 - Pyhton 2.7
 - Pubnub >= 3 < 4 python SDK
 - Raspian OS
 - Simple PHP page (must using pubnub Javascript SDK - main.js) run on local or online web server
 - RPi.GPIO library
 - Internet connectivity(connect raspi to any wifi)
 - Pubnub account

## Usage
 - PIN 16 = Lamp
 - PIN 04 = Fan
 - Channels = "pub-nub-channel" 
 
 
## Run script

```
<sudo> python main.py // ctrl + C to terminate script
```

## Make script autostart on startup

- Install supervisor
- Make supervisor command available on systemd(startup)

For all follwing command please run as `root` not `sudo` group. To make this happen, we can install supervisor using this command :

```
pip install supervisor
```

After finish, create `supervisord.conf` file:

```
mkdir -p /etc/supervisor
echo_supervisord_conf > /etc/supervisor/supervisord.conf. // This won’t work if you do not have root access.
```

And put following content:

```
[program:home-automate]
command=/usr/bin/python /path/to/the/pyhton/main/file/main.py e.g: /home/pi/home-automate/main.py
directory=/paht/to/the/root/pyhton/project e.g: /home/pi/home-automate
autostart=true
autorestart=true
startretries=3
stderr_logfile=/paht/to/the/root/pyhton/project/error.log e.g: /home/pi/home-automate/error.log
stdout_logfile=/paht/to/the/root/pyhton/project/out.log e.g: /home/pi/home-automate/out.log
user=root
```

Create supervisor service file to enable startup service:

```
touch /etc/systemd/system/supervisord.service
```

And put following content:

```
[Unit]
Description=Supervisor daemon

[Service]
Type=forking
ExecStart=/usr/local/bin/supervisord -c /etc/supervisor/supervisord.conf
ExecStop=/usr/local/bin/supervisorctl $OPTIONS shutdown
ExecReload=/usr/local/bin/supervisorctl $OPTIONS reload
KillMode=process
Restart=always
RestartSec=42s
User=root
Group=root

[Install]
WantedBy=multi-user.target
```

And finally enable those service:

```
systemctl daemon-reload

systemctl enable supervisord.service

systemctl start supervisord.service
```
















