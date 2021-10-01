### Vim/Neovim Plugin

curl -v -o ~/.vim/bundle/.vundle/script-names.vim-scripts.org.json https://raw.githubusercontent.com/i-cooltea/resource/master/vim-api_scripts.json 



#### first need to know

- normal set :

  `http://www.ruanyifeng.com/blog/2018/09/vimrc.html`

- vimrc       ---->         ~/.vimrc     /       /etc/vimrc之类
- neovim config file        -------->      /.config/nvim/init.vim

#### Need to do

- junkfile

### find out

#### vundle

1. Vundle is a Plugin manager for vim, so I gonna use it.

   ​	`git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim`

   I changed this command to the following one:  (from gist)

   `git clone https://github.com/VundleVim/Vundle.vim.git ~/.config/nvim/bundle/Vundle.vim`

2. And Vundle's configuration should be changed

   - before changed, vimrc should be like vundle's origin:

     `set rtp+=~/.vim/bundle/Vundle.vim`

   - now it's like that:

     `set rtp+=~/.config/nvim/bundle/Vundle.vim`

   - the other's configuration is in vundle's github

3. Vundle's Usage

   in vim input command:

   ```in vimrc/init.vim
   :PluginInstall
   :PluginSearch vim
   :bdelete # remove cache
   :PluginUpdate
   :PluginList
   :PluginClean
   
   ```

   

4. Bugs

   when you using PluginSearch, it might be error, so I find the solution:

   ```issue
   https://github.com/VundleVim/Vundle.vim/issues/599:
   The root of this problem is that PluginSearch queries http://vim-scripts.org, and this site no longer exists. This is because most vim plugin development and distribution occurs via github/gitlab now.
   
   I recommend searching for plugins directly, or searching for plugins on github. This functionality should be considered dead now.
   
   or use curl or wget to get the file(either is ok, pick one as you like), like:
   
   curl -v -o ~/.vim/bundle/.vundle/script-names.vim-scripts.org.json https://raw.githubusercontent.com/i-cooltea/resource/master/vim-api_scripts.json
   
   or
   
   wget https://raw.githubusercontent.com/i-cooltea/resource/master/vim-api_scripts.json -v -O ~/.vim/bundle/.vundle/script-names.vim-scripts.org.json
   ```

   but the command doesn't work when I chanded ~/.vim to ~/.config/nvim..

   so the bundles will installed in ~/.vim/bundle while Vundle usage in ~/.config/nvim/bundle

   and vim doesn't work now (no Vundle in ~/.vim)

   but nvim might be work .. so just be that.

5. need to know

   when u using :PluginSearch and type i to add the bundle to vim, u will find that lots of bundles are not the offical, so I find out some Plugin and put them into init.vim maually:

   ```plugin
   Plugin 'scrooloose/nerdtree'
   Plugin 'valloric/YouCompleteMe'
   ```

   but YCM still have problems.. and there are two ways to use that

   ```aur
   http://pre.tir.tw/008/blog/output/vim-youcompleteme-on-arch-linux.html:
   1.  aur 
   2.  download clang
   	Plugin 'valloric/YouCompleteMe'
   	:PluginUpdate
   	cd ~/.vim/bundle/YouCompleteMe
   	./install.py --all
   ```

   but it begins to call YCM need python2.0 or something..

   

   

   

   #### bundles

   ```juejin
   https://juejin.im/post/5c696497f265da2db27924bb:
   Ctrlp
   ctrlp.vim 这个插件可以所说是我用的最多的插件，因为它支持模糊搜索查询文件名，只需要ctrl+p就能做到输入自己要跳转的部分文件名。ctrl+j/k进行上线选择然后确定就进行跳转了，非常方便快捷，可以说是居家旅行必备良药。
   
   NERDTree
   它像IDE一样可以得到整个项目的目录树，非常方便切换。每次只需要ctrl+e就可以调出来侧边栏，通过ctrl+w进行切换各个窗口。
   
   ACK
   不仅可以Linux下面进行内容搜索，也能进通过插件的方式在安装在Vim进行。
   
   #### 不一定能用：Plugin 'VundleVim/Vundle.vim'               " requiredPlugin 'scrooloose/nerdtree'                " file/directory treeePlugin 'kien/ctrlp.vim'                     " Fuzzy file, buffer, mru, tag, etc finder
   
   ```

   ```bugs
   https://www.cnblogs.com/muahao/p/6821021.html：
   NERDTree needs :NERDTree to using it, 默认开启，vimrc加入：
   autocmd vimenter * NERDTree
   ```

   for junkfile :

   just add Plugin 'https://github.com/Shougo/junkfile.vim' in vimrc

   

   最后的选择：yay -S neovim-youcompleteme-core-git

   

   
   
   
   
   ​	
   
   