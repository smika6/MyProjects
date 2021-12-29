## SE 412/512 Project Code Repository

**Group 1** consisting of Juan Cabanela, Thomas Carriveau, Jacob Hopkins, Reuben Koop, Sam Paquin, and Thomas Schmidt.

Our main project goal is to develop an ML-based classifier that can decide if a particular news website shows a tendency toward questionable journalistic practices. Initially, we want to see if given news articles from selected news websites (across the political spectrum) the classifier can determine if those articles exhibit troubling journalistic practices. Once this information is obtained, we can see if trends exist in these practices that are correlated with political bias.

Our stretch goal would be to see if we can notice trends in journalistic practices over time. This goal may not be possible given the limitation in the number of free sources of old news articles tied to particular websites or news organizations (in the pre-internet times).

This is the code repository for that project.

## Setting up your Environment (a Note from Juan)

If you use a conda installation of python (I use miniconda, https://docs.conda.io/en/latest/miniconda.html), its pretty easy to set up a virtual environment for this software.  

Note that I used conda-forge as my main conda repository to pull from, its much more up-to-date than the main anaconda repo and tends to have many more scientific packages in it.  

Here's a link to conda-forge info and how to config conda for it (https://conda-forge.org/docs/user/introduction.html). As long as you have a recent conda install, its a few command lines to make it your default repo and to force 'strict' priority for it 

> conda config --add channels conda-forge

> conda config --set channel_priority strict

**NOTE** This restriction to using only the conda-forge repo for packages once you start using it is critical. Mixing conda-forge and non-conda-forge packages can cause serious problems with some of the packages.  

Once you have conda-forge as your default conda repo, you can use the `ml_environment.yml` file to this repo that can used to set up a machine learning environment with conda.  Just do a 

> conda env create -f ml_environment.yml

to create the environment.  Then activate it with

> conda activate ml
