You may already have your own workflow set up on your laptop, in which case you can use that.
If not, we recommend you install python via the Anaconda distribution,
but you are free to choose whichever installation method you prefer

To check that you have Python installed, and what version, run the command `python --version` in a bash terminal.
- If the version displayed is Python 3 (e.g. `Python 3.7.3`), then you are set to go!
- If the version displayed is Python 2 (e.g. `Python 2.7.14`), then try running `python3 --version`.
    - If that succeeds, then you are ready, but your "default" installation is Python 2; during in the workshop, use the command `python3` instead of `python`.
    - If that command fails, you will need to install Python 3 using the instructions below (or another method of your choice).

To install Anaconda, [download the right installer](https://www.anaconda.com/products/individual#Downloads)
for your operating system and follow the steps of the installer. 



{% if include.os == "win" %}
Install Python 3 by running the Anaconda Installer, using all of the defaults for installation except make sure to check Add Anaconda to my PATH environment variable.
{% elsif include.os == "linux" %}
The installation requires using the shell. Navigate to the directory where the installer has been downloaded and execute it typing: `bash Anaconda3-` and press Tab on your keyboard to autocomplete to the full file name. Follow the text-only prompts.
{% elsif include.os == "mac" %}
You don't need to do any extra steps.
{% endif %}

Once Anaconda is installed, if you want it to be always available from your terminal, run 
`conda init bash` {% if include.os != "win" %}(or with the specific terminal you are running, e.g., zsh) {% endif %}.

To check that the installation is successful, run `python --version` in your terminal.
This should show a verion starting with `Python 3`.