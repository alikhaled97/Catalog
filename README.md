# Catalog APP
This is the Second project of the Full Stack Web Developer Nanodegree.

The opject of this project :  is to build a website with Flask, SQLAlchemy, third party OAuths and API endpoints.

## How do u run this project ?

### 1. Download and configure: Virtual Machine & Database

**First step:** Download and install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).

**Second step:** Download the VM configuration from files [HERE](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).

**Third step:** Download the python program (`project`) that i have sent to you. Then, copy it to  the `vagrant/` (one of the folders that you downloaded before in Second step).

**Fourth step:** Open your terminal then run this commands:

```
# Install & Configure VM
# 1.Change the path to vagrant
cd /path/to/vagrant

# Run vagrant up
vagrant up

# note: If this is the first time you run (vagrant up) command, you have to wait for a while.

#  Log into machine
vagrant ssh

# Close the machine
# Ctrl + D

```
### 2. Running myTool

Open your terminal then run:

```
# Launch the machine
# Change direction to vagrant:
cd /path/to/vagrant

# Then run:
vagrant up
vagrant ssh

# Open shared folder:
cd /vagrant 

# Run the program to setup the DataBase:
python database_setup.py 

# Then Run the program to setup some of DataBase categories and items:
python someofcategories.py

# and finally Run the program:
python catalog.py

# Then open your browser and go to (localhost:5000/login) to login to my site.
# You can go to (localhost:5000) without login.
```


## Contacts

- [Facebook](https://www.facebook.com/ali.khaled.71465)
- E-mail: engalikhaled@hotmail.com
