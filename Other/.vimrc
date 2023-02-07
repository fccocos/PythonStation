Vim配置文件(.vimrc)
"" 将<leader>将映射到空格键
let mapleader=" "
" 高亮打开
syntax on

" 显示行号
set nu

" 设置相对行号
set relativenumber

" 关闭相对行号
" set norelativenumber

" 设置游标线
set cursorline
set cursorcolumn

" 设置文字包裹模式，超出窗口宽度自动换行
set wrap

" 在末行模式下，设置tab提示中的提示菜单
set wildmenu

" 设置搜索高亮
set hlsearch
exec "nohlsearch"

" 设置搜索时，边搜索边高亮
set incsearch

" 搜索时忽略大小写
set ignorecase

" 搜索时智能匹配
set smartcase


" 向下兼容VI
set nocompatible
filetype on
filetype indent on
filetype plugin on

" 在可视化下兼容鼠标
set mouse=a

" 将缩进设置为空格
let &t_ut=''
set expandtab

" 将缩进设置为4空格
set tabstop=4

" 在行末尾显示$
set list

" 渲染Tab和空格键
" set listchars=tab:œ\ ,trail:™

" 滚动时保留多行
set scrolloff=10

" 启动退格跨行退格
set backspace=indent,eol,start

" 设置代码折叠
set foldmethod=indent
set foldlevel=99

" 永久保留命令行
set laststatus=2

"  在重新打开文件后保存光标的位置
au BufReadPost * if line("''\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif

" 设置自动缩进
set autoindent

" 显示输入的命令
set showcmd



""""""""""""""""""""""""""""""
" 快捷键设置
""""""""""""""""""""""""""""""

" noremap 表示不递归映射

" <nop> 没有选项
" 保存文件
nmap S :w<CR>

" 退出VIM
nmap Q :q<CR>

" 重新配置.vimrc
nmap R :source ~/.vimrc<CR>

" 设置复制粘贴到剪切版的快捷键
vnoremap <Leader>y "+y
nmap <Leader>p "+p

" 取消搜索高亮
noremap <Leader><CR> :nohlsearch<CR>

" 设置分屏快捷键
map spl :set splitright<CR>:vsplit<CR> " 向右边分屏
map sph :set nosplitright<CR>:vsplit<CR> " 向左边分屏
map spj :set splitbelow<CR>:split<CR> " 向下边分屏
map spk :set nosplitbelow<CR>:split<CR> " 向上边分屏

" 设置跳转分屏键
map <C-h> <C-w>h
map <C-j> <C-w>j
map <C-k> <C-w>k
map <C-l> <C-w>l

" 调整窗口快捷键
map <Leader>= :vertical resize+5<CR>
map <Leader>- :vertical resize-5<CR>
map <Leader>+ :resize+5<CR>
map <Leader>_ :resize-5<CR>

" 置换窗口
map vh <C-w>t<c-W>H
map hv <C-w>t<c-W>K

" 增加和删除tabe标签
map tu :tabe<CR>
map tc :tabc<CR>
map tp :-tabnext<CR>
map tn :+tabnext<CR>
map tmn :-tabmove<CR>
map tmi :+tabmove<CR>




"""" 快捷见的组合模式 《operation> <motion>
" <operation> 增(y)删(d)改查(f)
" <motion> 上(j)下(k)左(h)右(l)

"""" 快捷键映射语法
" 前缀+map 快捷键 映射结果
" 前缀：n | v | i | c
" nmap 在normal模式下生效
" vmap 在visual模式下生效
" imap 在insert模式下生效
" cmap 在末行模式下生效
" xnoremap x表示n/v/i/c模式，nore表示非递归。例如a->b,b->c <=> a->c（递归）

"""" 特殊按键的写法
" <leader>
" alt组合键  <A-X>   <A-S> -> alt+s
" ctrl组合键 <C-X>   <C-c> -> ctrl+c
" Fn键       <FX>    <F4>  -> F4
" Enter键    <CR>






"""""""""""""""""""""""""""""""""
" vim插件-Plug
""""""""""""""""""""""""""""""""

call plug#begin('~/.vim/plugged')

" 主题插件 vim-snazzy
Plug 'connorholyday/vim-snazzy'
Plug 'mbbill/undotree'
" 文件树
Plug 'https://gitee.com/liquzhi/nerdtree'
Plug 'https://gitee.com/karl1864/vim-airline_vim-airline'
Plug 'preservim/nerdcommenter'
Plug 'https://gitee.com/rulei_mirror/rainbow'
Plug 'https://gitee.com/lordyung/YouCompleteMe'
Plug 'https://gitee.com/snowindz/vim-colors-solarized'
Plug 'https://gitee.com/itl/vim-airline-themes'
call plug#end()


"""""""""""""""""""""""""""""
" vim插件配置
"""""""""""""""""""""""""""""

""" airline
let g:ariline#extensions#tabline#enabled=1
let g:ariline#extensions#tabline#formatter='jsformatter'

""" airline-theme
let g:airline_theme='angr'


"""" vim-snazzy主题配置

" 启动vim-snazzy
colorscheme desert

" https://gitee.com/lordyung/YouCompleteMe

" 将cursorline的样式设置为vim-snazzy主题
 let g:lightline = {
    \ 'colorscheme': 'desert',
    \ }
" 设置背景的透明度
let g:SnazzyTransparent = 0.7

" 启动undotree插件
map <F5> :UndotreeToggle<CR>

" 设置NERDTree快捷键
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>

" 映射切换buffer的键
nnoremap [b :bp<CR>
nnoremap ]b :bn<CR>

" commenter 的快捷键
" <Leader>cc 注释
" <Leader>cu 取消注释

" 配置rainbow
let g:rainbow_active = 1

" 1. vscode defult 2. author defult 3. vscode show
" 'guifgs': ['#B21212', '#1B9CED','#FFFC00'],
" 'guifgs': ['royalblue3', 'darkorange3', 'seagreen3', 'firebrick'],
" 'guifgs': ['#C186BF', '#268EDB','#F79318'],
let g:rainbow_conf = {
\ 'guifgs': ['#C186BF', '#268EDB','#F79318'],
\ 'ctermfgs': ['lightblue', 'lightyellow', 'lightcyan', 'lightmagenta'],
\ 'operators': '_,_',
\ 'parentheses': ['start=/(/ end=/)/ fold', 'start=/\[/ end=/\]/ fold', 'start=/{/ end=/}/ fold'],
\ 'separately': {
\ '*': {},
\ 'tex': {
\ 'parentheses': ['start=/(/ end=/)/', 'start=/\[/ end=/\]/'],
\ },
\ 'lisp': {
\ 'guifgs': ['royalblue3', 'darkorange3', 'seagreen3', 'firebrick', 'darkorchid3'],
\ },
\ 'vim': {
\ 'parentheses': ['start=/(/ end=/)/', 'start=/\[/ end=/\]/', 'start=/{/ end=/}/ fold', 'start=/(/ end=/)/ containedin=vimFuncBody', 'start=/\[/ end=/\]/ containedin=vimFuncBody', 'start=/{/ end=/}/ fold containedin=vimFuncBody'],
\ },
\ 'html': {
\ 'phttps://gitee.com/itl/vim-airline-themesarentheses': ['start=/\v\<((area|base|br|col|embed|hr|img|input|keygen|link|menuitem|meta|param|source|track|wbr)[ >])@!\z([-_:a-zA-Z0-9]+)(\s+[-_:a-zA-Z0-9]+(\=("[^"]*"|'."'".'[^'."'".']*'."'".'|[^ '."'".'"><=`]*))?)*\>/ end=#</\z1># fold'],
\ },
\ 'css': 0,
\ }
\ }
let g:rainbow_active = 1

" 配置YouCompleteMe
let g:ycm_clangd_binary_path = trim(system('brew --prefixllvm')).'/bin/clangd'
