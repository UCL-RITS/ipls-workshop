---
layout: page
title: Using Desktop@UCL
---
At [Desktop@UCL](https://my.desktop.ucl.ac.uk/) you can find Anaconda and a terminal (git bash). If you want to access anaconda from within git bash you'll need to follow these steps:

1. Open git bash 2.22.0 
1. Type `echo $HOME`. If it doesn't show `/n/`, then: 
    1. Create a new file with nano: `nano ~/.bash_profile` 
    1. Add the following content to it:
    ```
    OLDHOME="${HOME}"  
    export HOME="/n/"  
    cd $HOME [[ ! -f OLDHOME/.bash_profile ]] && cp $HOME/.bash_profile $OLDHOME 
    ```
1. Open a new git bash terminal and run: `conda init bash` (this may say that the operation failed, but it's OK) 
1. Open a new terminal again. It may show a bash error at the start, but everything should work fine. 

This checks whether you had created a startup configuration in your home directory and copies to the new home on the n drive.
