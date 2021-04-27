---
layout: page
title: Setup instructions (Linux)
---
## Bash
You should already have bash (or another terminal) installed. If you are not sure how to access it, search for "terminal" on your desktop's application menu.

## Git
You may already have git installed. Check that by typing the command `git --version` on your terminal.
If not, the installation steps depend on the Linux distribution you are using. If you have...

- A Debian based distribution (e.g., Ubuntu, Mint, ...) you can use `apt` : `apt install git`
- A RedHat based distribution (e.g., Fedora, CentOS, ...) you can use `dnf`: `dnf install git`
- OpenSuse you can use zipper: `zypper install git`
- An Arch Linux based distribution (e.g., Manjaro, ...) you can use `pacman`: `pacman -S git`

## Python
{% include python.md os="linux" %}


## Pytest
{% include pytest.md %}

## Optional: VS Code
{% include vscode.md os="linux" %}
