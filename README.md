# wallhaven
📜 Auto-Update your Wallpaper with the Latest Work from your Favourite Artist

## Steps to Use

### Install Requirements
#### 1. Python Packages
```bash
pip3 install -r requirements.txt
```
#### 2. Linux Packages
It's perfectly ok to use the python script as such but to automate, the following packages are necessary
- cronie
- [pywal](https://github.com/dylanaraps/pywal)
If on Arch Linux (and derivatives) this command would do it for you. 
```bash
yay -S cronie python-pywal
```

### Set-Up Env Var (Optional)
For bulk downloads and for NSFW images, create an account at https://wallhaven.cc/ and follow the instructions under
`.sample_env`

### Set-Up Cron-Job
Basically for automation of wall switching and downloading, make the `wallhaven.sh` script executable and create a 
cron-tab for the same. More information can be found [here](https://wiki.archlinux.org/index.php/cron)