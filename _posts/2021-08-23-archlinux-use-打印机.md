 

http://[fe80:fa0d:acff:fed8:9cc3%9]:3911/
172.20.165.52



arch: 安装cups. 启动cups服务

sudo pacman -S cups

systemctl start cups

systemctl enable org.cups.cupsd.service

cd /usr/lib/systemd/system/ : 有cups的socket说明没问题

systemctl enable cups

yay -S system-config-printer

然后printer manager可以选择HP, 驱动选名字一样的, 可以不带dw. 于是ok.

okular不能双面, wps可以

cups-pdf: 还没玩明白

