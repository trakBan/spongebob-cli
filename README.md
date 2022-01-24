# spongebob-cli
Watch classic spongebob from the terminal!
Thanks to everyone that is starring, forking, writing issues, pull requesting and just users of spongebob-cli!

![updatedgif](https://user-images.githubusercontent.com/81049050/150698534-03b2361d-8f62-437b-8eab-776b9b045377.gif)


# Dependecies (all python dependecies will automatically be installed):
1.  mpv player https://mpv.io/  (Must be installed through a package manager)
2.  youtube-dl https://github.com/ytdl-org  (Python dependency)

# Usage:
```
 If the programm was ran without arguments it will ist all the episodes an it will let you play them.
 --download | -d, usage --download {a number of a episode}, This will download that video under a directory the command was run
 --list | -l,     usage --list, this will list all the episodes and then exit the programm
 --list | -l, usage --list {number} this will show the number of episodes with the limit you provided.
 --play | -p      usage --play {a number of a episode}, This will play the episode without listing the episodes
 --random | -r, usage spongebob-cli --random, This will play a random episode
 --help | -h      usage --help this will print what each argument does
```
# How to install:
Download this repository with git or other.
```
cd spongebob-cli
sudo chmod +x spongebob-cli; sudo python setup.py install
```
## Arch and arch based distributions
There is an [AUR](https://aur.archlinux.org/packages/spongebob-cli-git/) package for spongebob-cli mantained by [getchoo](https://github.com/getchoo)
```
yay -S spongebob-cli-git
```
# Troubleshooting

If setup.py fails try this:
```
pip3 install termcolor beautifulsoup4 prettytable
```
If video wont play check if you have mpv and youtube-dl installed.
If you dont have youtube-dl but a fork of it, make a alias in your .zshrc or .bashrc and alias it to youtube-dl
