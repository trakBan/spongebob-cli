# spongebob-cli
Watch classic spongebob from the terminal!
Thanks to everyone that is starring, forking, writing issues, pull requesting and just users of spongebob-cli!

![updatedgif45729805790](https://user-images.githubusercontent.com/81049050/150833862-0a828939-f267-4bd2-931f-79df55d51e28.gif)

# Dependecies (all Python dependecies will automatically be installed):
1.  mpv player https://mpv.io/  (Must be installed through a package manager)
2.  youtube-dl https://github.com/ytdl-org  (Python dependency)

# How to install:

## To download with and install with git:
#### For UNIX based OS - One Line Execution
```bash
#Sudo isn't required as long as you're not in Root
git clone https://github.com/trakBan/spongebob-cli.git
cd spongebob-cli
sudo chmod +x spongebob-cli
sudo python setup.py install
```
One line: 
```bash
git clone https://github.com/trakBan/spongebob-cli.git; cd spongebob-cli; sudo chmod +x spongebob-cli; sudo python setup.py install
```

<!---
#### For Windows OS
```bash
# NOTE: !LAUNCH YOUR CMD AS ADMIN!
git clone https://github.com/trakBan/spongebob-cli.git
cd spongebob-cli
python setup.py install
```
--->
## To install manually - UNIX OS
```bash
# Assuming you already have the Master downloaded
cd spongebob-cli
sudo chmod +x spongebob-cli; sudo python setup.py install
```
One line: 
```bash
cd spongebob-cli; sudo chmod +x spongebob-cli; sudo python setup.py install
```
# Usage:
```
 If the programm was ran without arguments it will list all the episodes and it will let you play them.
 --download | -d, usage --download {a number of a episode}, This will download that video under a directory the command was run.
 --download-all | -da, usage --download-all, This will download every spongebob video it scrapes.
 --binge | -b , usage spongebob-cli --binge, This is used to start the first episode and play until the last episode.
 --list | -l,     usage --list, this will list all the episodes and then exit the program.
 --list | -l, usage --list {number} this will show the number of episodes with the limit you provided.
 --play | -p      usage --play {a number of a episode}, This will play the episode without listing the episodes.
 --random | -r, usage spongebob-cli --random, This will play a random episode.
 --help | -h      usage --help this will print what each argument does.
```
## Arch and arch based distributions
There is an [AUR](https://aur.archlinux.org/packages/spongebob-cli-git/) package for spongebob-cli mantained by [getchoo](https://github.com/getchoo)
```
yay -S spongebob-cli-git
```
# Episodes that are known to not work
Episode: 30, 

# Troubleshooting

- If setup.py fails try this:
  - ```bash
    pip3 install termcolor beautifulsoup4 prettytable halo
    ```

- If you're getting an error like <code>`sudo: python: command not found`</code>
   - ```bash
     git clone https://github.com/trakBan/spongebob-cli.git; cd spongebob-cli; sudo chmod +x spongebob-cli; sudo python3 setup.py install
     ```
   - Use python3 instead of python


- Gentoo users will have to add --user at the end of that line of code

- If the video won't play check if you have mpv and youtube-dl installed.
- If you don't have youtube-dl but a fork of it, make a alias in your .zshrc or .bashrc and alias it to youtube-dl

# Contributors
[yaacornus](https://github.com/yaacornus), 
[redouane](https://github.com/red-elka), 
[totensee](https://github.com/totensee), 
[Kat](https://github.com/TransKat), 
[dev-nolant](https://github.com/dev-nolant)
