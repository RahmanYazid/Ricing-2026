if status is-interactive
     pokemon-colorscripts --random --no-title

    alias ls="eza --icons"
    alias ll="eza -l --icons"
    alias la="eza -la --icons"

    starship init fish | source
end

if test -f ~/.cache/wal/colors.fish
    source ~/.cache/wal/colors.fish
end

alias steam-alt='firejail --private=$HOME/.steam-alt steam'
alias dotfiles='git --git-dir=/home/zomboid/.dotfiles/ --work-tree=/home/zomboid'
alias dotfiles='git --git-dir=/home/zomboid/.dotfiles/ --work-tree=/home/zomboid'
alias dotfiles='git --git-dir=/home/zomboid/.dotfiles/ --work-tree=/home/zomboid'
alias dotfiles='git --git-dir=/home/zomboid/.dotfiles/ --work-tree=/home/zomboid'
