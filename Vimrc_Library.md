# Vim 設定に必要なライブラリ・パッケージ一覧（Ubuntu / AlmaLinux / macOS）

# ✅ 基本前提条件

## ✅ OS別まとめ

### Ubuntu

```
sudo apt install vim nodejs npm clangd git python3-pip
```

### AlmaLinux

```
sudo dnf install vim-enhanced nodejs npm clang-tools-extra git python3-pip
```

### macOS（Homebrew 使用）

```
brew install vim node llvm git python go
```

## ✅ :PlugInstall 実行後に Vim で以下を実行

```
:CocInstall coc-pyright coc-clangd coc-go coc-sh
```


### Vim（バージョン8.1以上推奨）
- `+clipboard`, `+python3` が有効なビルドを推奨

### Node.js（`coc.nvim` に必須）
#### ✅ 推奨インストール方法（全OS共通）:
```bash
# nvmでインストール（推奨）
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc  # or ~/.zshrc
nvm install --lts

# ✅ 各OS別パッケージインストール

```
# Ubuntu
sudo apt install nodejs npm

# AlmaLinux
sudo dnf install epel-release
sudo dnf install nodejs npm

# macOS (Homebrew)
brew install node
```

# ✅ vim-plug のインストール

```
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
     https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

# ✅ coc.nvim に必要な言語サーバ（LSP）


## Python: coc-pyright
```
:CocInstall coc-pyright
pip install pyright
```

## C/C++: coc-clangd

```
:CocInstall coc-clangd
```

### 必要パッケージ

```
# Ubuntu
sudo apt install clangd

# AlmaLinux
sudo dnf install clang-tools-extra

# macOS
brew install llvm
```

# Go: coc-go

```
:CocInstall coc-go
```

## 必要なGoツール

```
go install golang.org/x/tools/gopls@latest
go install golang.org/x/tools/cmd/goimports@latest

# 環境変数に追加
export PATH=$PATH:$(go env GOPATH)/bin

```

### Shell: coc-sh

```
:CocInstall coc-sh
npm install -g bash-language-server
```

# ✅ その他プラグインと要件

```
# git が必要な場合
sudo apt install git       # Ubuntu
sudo dnf install git       # AlmaLinux
brew install git           # macOS
```

# ✅ clipboard 機能の確認（unnamedplus）

```
vim --version | grep clipboard
```

# ✅ 自動フォーマット用ツール（任意）

```
# Python
pip install black

# Shell script
npm install -g shfmt
```

