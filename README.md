# spongebob-cli
Watch classic spongebob from the terminal!

![image](https://user-images.githubusercontent.com/81049050/150638868-18f6f51b-71e8-4d63-aa4c-2ebc2ec9c322.png)

# Dependecies (all python dependecies will automatically be installed):
1.  mpv player https://mpv.io/
2.  youtube-dl https://github.com/ytdl-org

**Fedora**

```
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install mpv
```

**Debian/Ubuntu**

```
sudo apt install mpv
```

**Arch**

```
sudo pacman -S mpv
```

# Usage:
```
 If the programm was ran without arguments it will ist all the episodes an it will let you play them.
 --download | -d, usage --download {a number of a episode}, This will download that video under a directory the command was run
 --list | -l,     usage --list, this will list all the episodes and then exit the programm
 --list | -l, usage --list {number} this will show the number of episodes with the limit you provided.
 --play | -p      usage --play {a number of a episode}, This will play the episode without listing the episodes
 --help | -h      usage --help this will print what each argument does
```
# How to install:
Download this repository with git or other.

```
cd spongebob-cli
chmod +x spongebob-cli && python setup.py install
```

# Troubleshooting

If setup.py fails try this:

```
pip3 install termcolor beautifulsoup4
```

If video wont play check if you have mpv and youtube-dl installed.
If you dont have youtube-dl but a fork of it, make a alias in your .zshrc or .bashrc and alias it to youtube-dl
