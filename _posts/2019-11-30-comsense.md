### using arch to access windows file:
To achieve write permissions for other users than root, you will need to install ntfs-3g, which also will install the fuse package in order to work:
pacman -Sy ntfs-3g

### find
find . -type d -name "chrome*"

### fcitx/ibus win+space doesn't work [cause kRunner's Bug]
first reset KRunner's 快捷键 over Win+spacce after that it's done..



### electron boot automatically

https://www.reddit.com/r/archlinux/comments/7tubn5/everytime_i_boot_electron_automatically_starts/?utm_source=share&utm_medium=web2x

I just move ~/.config/autostart/electron.desktop to electron.desktop_backup 

But.. when i reboot, it's automatically make a electron.desktop again.. I will change its comment etc to see..

还为了找配置信息下了systemdgenie..

### fsl

在manjaro下fsl编译一中午加下午弄完

在Arch下失败.. so 使用aur里的讨论中有说(martin)缺少依赖的(python-xxxx), 也有建议重装fslpy的，但都不起作用，我在github/fsl里makepkg -si时也怀疑会不会是文件夹的问题，甚至认为makepkg只能在～/.cache/yay里使用...

最后是使用aur里的避开策略，忽略check() feat和fsd 的检查，于是将就下下来了，结束的时候需要输密码应该是pacman -U 的一步？

[git clone -> makepkg -si]; [pacman -U (压缩好的aur的tar...包)]; [yay -S xxx] 三种方法

我因为.tar文件下载太慢且老出错就自己下下来考到了fsl的文件夹，～/github/fsl和～/.cache/yay/fsl都试过..不过Cleanbuild的话会删，可以先点cleanbuild在问你是否show different的时候拷贝过去 :-)

如果不cleanbuild会报有些文件夹已经建了的bug, 可以将src文件夹名称改成src_backup :D



下完还没完，得export环境变量和source:

（可能有多余的命令）

export PATH=$PATH:/opt/fsl/bin

export PATH="$PATH:/home/arch/github/fsl/src/fsl/bin"

export FSLDIR=/opt/fsl

source $FSLDIR/etc/fslconf/fsl.sh

反正都放进了~/.zshrc...



ext:

使得刚修改的环境变量生效：source <带环境变量的文件>

查看环境变量： env 或 set 

持久化的环境变量主要存在于这几个文件中：

1. /etc/profile
2. /etc/environment
3. ~/.bash_profile
4. ~/.bashrc

加载优先级是：1->2->3≈4(3和4之间的优先级不大清楚)

其中1和2是系统的全局环境变量，3和4是用户个人的环境变量

 环境变量的写法：

```
#注意引用已经存在的环境变量，以冒号 : 分割两个环境变量，$ 调用已经存在的变量
PATH=$PATH:<PATH 1>:<PATH 2>:<PATH 3>:——:<PATH 3>
#然后启用它，注意：/etc/environment 中无需添加下面这条命令 
export PATH
```

SHELL中设置临时变量：

```
export PATH="$PATH:<PATH 1>:——:<PATH n>"
```



### audio

arch没有声音的问题

于是胡乱下东西：alsamixer; alse-utils; pulseaudio， pavucontrol ..etc..

胡乱改东西：

胡乱试：aplay -l; alsamixer; sudo alsactl store; lspci | grep -i audio; speaker-test -c2 ;

aplay -D plughw:0 /usr/share/sounds/alsa/Noise.wav; pulseaudio --start -> 这个随便--kill还会出点小问题，菜单右下方的声音选项当场不工作

(headphone -> alsamixer里的耳机..)

最后

可以外放了..因为将默认输出从intel 改成了nvidia HDMI （现在用的HDMI 线）

但耳机并不可以.. -> 待解决！

### polipo

### plasma plugins

1. 有的可以直接yay下下来在右键桌面选择add wigets -> local 加上 如latte dock

2. 有的必须得想其他办法  i.e./ e.g. now dock
3. 

### 删除家目录 -> 各文件夹作用

### mount over

### UEFI GRUB 

