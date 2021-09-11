# vim-dictcc
Vim plugin for dictionary lookups using [**dict.cc**](https://dict.cc)

## Requirements
vim-dictcc requires python3 support. Check by running
```vim
:echo has('python3')
```
in vim, which should return `1`.
In neovim you can use `:checkhealth provider`, which has a more helpful interface.

Further you need to have the python module [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) installed.
Use your package manager or pip:
```sh
pip install beautifulsoup4
```
Remember to call this with `sudo` to install system-wide.

## Installation
Use your plugin manager of choice:

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/weinshec/vim-dictcc ~/.vim/bundle/vim-dictcc`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'weinshec/vim-dictcc'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'weinshec/vim-dictcc'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'weinshec/vim-dictcc'` to .vimrc
  - Run `:PlugInstall`

## Usage
The plugin supports simple online lookups **ENG <-> DEU** for now and provides a vim-command for querying, e.g.
```vim
:Dict lunch
```
will query for *lunch* and show the results in a newly created buffer.

`DictCur` queries for the word under cursor, which is convenient to map, e.g.
```vim
inoremap <c-s> <Esc>:DictCur<CR>
nnoremap <c-s> :DictCur<CR>
```
Now **Ctrl-s** in `normal` and `insert` mode will query for a translation.

The newly created `dictcc` buffer can be closed by pressing the `q` key.

## Development
vim-dictcc is in an early stage of development and your help is appreciated.
Feel free to create issues and contribute PRs.
