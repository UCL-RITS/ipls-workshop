{%- capture vscode_install_link -%}
{%- if include.os == "win" -%}
https://code.visualstudio.com/docs/setup/windows
{%- elsif include.os == "linux" -%}
https://code.visualstudio.com/docs/setup/linux
{%- elsif include.os == "mac" -%}
https://code.visualstudio.com/docs/setup/mac
{%- else -%}
https://code.visualstudio.com/docs/setup/setup-overview
{%- endif -%}
{%- endcapture -%}
Whilst the workshop will focus on using tools from the command line, you may also wish to use a code editor or IDE to assist in following along. The instructor will be using Visual Studio Code to help demonstrate and explain the use of git, but you can whichever you prefer (or none at all!)

If you wish to have a similar setup, follow the [VSCode installation instructions]({{ vscode_install_link }}).

VS Code can provide additional functionalities using extensions. They can be searched and installed directly from within VS Code. We recommend the following extensions: 

- [Python extension for Visual Studio Code by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)