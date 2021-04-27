---
layout: page
title: Windows
---

## Bash and git
You can either follow this [Video
Tutorial](https://www.youtube.com/watch?v=339AEqk9c-8) or follow the
instructions below:

1. Download the [Git for Windows installer](https://git-for-windows.github.io/).
1. Run the installer and follow the steps below:
   - Click on "Next" four times (two times if you've previously installed Git).
     You don't need to change anything in the Information, location, components,
     and start menu screens.
   - **From the dropdown menu, select “Use the nano editor by default” and click on “Next”.**
   - Ensure that "Git from the command line and also from 3rd-party software" is selected and click on
     "Next".
   - Ensure that "Use the OpenSSL library" is selected and click on "Next".
   - Keep "Checkout Windows-style, commit Unix-style line endings" selected and click on "Next".
   - **Ensure that "Use Windows' default console window" is selected and click on "Next".**
   - Ensure that "Default (fast-forward or merge) is selected and click "Next". 
   - Ensure that the (New!) "Git Credential Manager Core" is selected and click on "Next". 
   - Ensure that "Enable file system caching" is selected and click on "Next". 
   - Experimental features: Keep the default (i.e., nothing selected) - click "Next"
   - Click on "Install".
   - Unselect "View release notes" (unless you are interested), and click on "Next". 

If your "HOME" environment variable is not set (or you don't know what this is): 
   - Open the Windows command prompt (Open Start Menu then type `cmd` and press Enter).
   - Type the following line into the command prompt window exactly as shown:
`setx HOME "%USERPROFILE%"`
   - Press Enter, you should see `SUCCESS: Specified value was saved`. 
   - Quit command prompt by typing exit then pressing Enter.


You should be able to open the git bash terminal by searching "git bash" on your Start Menu. 

Check that your installation has been successful:
1. The window title of the git bash terminal starts with `MINGW64:`. 
1. If you select any text with the mouse, it's pasted on the prompt when you right-click with the mouse. 
1. If you run the command `git --version`, it shows you are using the 2.2831 version of git.  

## Python
{% include python.md os="win" %}


## Pytest
{% include pytest.md %}
