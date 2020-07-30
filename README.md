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

### Running the Script
Edit [this line](https://github.com/Syzygianinfern0/wallhaven/blob/master/havenscraper.py#L17) to the user you would 
like to "subscribe to". As I am lazy and not in the mood, I'm not setting up any arg parsers. If this helped you and 
you want to contribute back, you are very much welcome to send a PR my way. 

This project can be used in 3 different levels of automation:

#### Level 0 (Any OS)
The python script will populate the downloads directory with the latest 10 images filtering out duplicates.

#### Level 1 (Linux Only)
The bash script will download and set the current wallpaper to the most recent one from the artist. Also, if integrated
properly, pywal can be made to change your entire WM and application theme and achieve a sexy consistent colour palette. 

#### Level 2 (Definitely Linux Only)
Basically for automation of wall switching and downloading, make the `wallhaven.sh` script executable and create a 
cron-tab for the same. 

More information can be found [here](https://wiki.archlinux.org/index.php/cron)