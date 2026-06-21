set shell := ["bash", "-c"]
list:
    just --list

build:
    stack build

site:
    stack exec site build

watch:
    stack exec site watch

marimo:
    uv run marimo edit

pluto:
    julia --project -e "using Pluto; Pluto.run()"

uoshell:
    TERM=xterm-256color SSHPASS="$(pass uoregon/shell)" sshpass -e ssh shell.uoregon.edu

upload:
    echo "When at the 'sftp>' prompt, type: `cd public_html; put -r _site/*`"
    sftp tgorordo@sftp.uoregon.edu

    
clean:
    rm -rf _site

wipe:
    just clean
    rm -rf .venv .stack-work _cache

send:
    just site
    sftp sftp.uoregon.edu <<< $'cd public_html\nput -r _site/*'
