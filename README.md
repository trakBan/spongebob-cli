# spongebob-cli
Watch classic spongebob from the terminal!
Thanks to everyone that is starring, forking, writing issues, pull requesting and just the users of spongebob-cli!

![ezgif com-gif-maker](https://user-images.githubusercontent.com/81049050/165950004-a21d0199-79b5-4ebe-b733-94df1fee918e.gif)

## Dependecies:
- mpv player https://mpv.io/  (Must be installed through a package manager)
- Every other dependendency will get automatticaly installed

## How to install:

### For UNIX based OS - One Line Execution
Checkout the source code with `git` or download it as a .zip file.
```bash

# Root is only required for the last line
git clone https://github.com/trakBan/spongebob-cli.git

cd spongebob-cli
chmod +x spongebob-cli
sudo python setup.py install
```

One line: 
```bash
git clone https://github.com/trakBan/spongebob-cli.git; cd spongebob-cli; chmod +x spongebob-cli; sudo python setup.py install
```

## Usage
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

## Arch and Arch-based distributions
There is an [AUR](https://aur.archlinux.org/packages/spongebob-cli-git/) package for spongebob-cli mantained by [getchoo](https://github.com/getchoo)

```
yay -S spongebob-cli-git
```
## Windows
You need to install mpv through a windows package manager

## Package Status
[![Packaging status](https://repology.org/badge/vertical-allrepos/spongebob-cli.svg)](https://repology.org/project/spongebob-cli/versions)

## Episodes that are known to not work
- Episode 30, - Episode 129

## Troubleshooting

### If setup.py fails try this:
```bash
pip install -r requirements.txt
```

### If you're getting an error like `sudo: python: command not found`
```bash
git clone https://github.com/trakBan/spongebob-cli.git; cd spongebob-cli; chmod +x spongebob-cli; sudo python3 setup.py install
```

#### Gentoo users:
Gentoo users have to add --user when they are installing with setup.py
Run this instead:
```bash
git clone https://github.com/trakBan/spongebob-cli.git; cd spongebob-cli; chmod +x spongebob-cli; python3 setup.py install --user
```

### If the video won't play
- Check if you have mpv and youtube-dl installed.
    - You can also install `youtube-dl` through your package manager if `setup.py` did not install it correctly
- If you don't have youtube-dl but a fork of it, make an alias in your ~./bashrc file and alias it to youtube-dl

## Rewrite in rust!
 [Ali-TM-original ](https://github.com/Ali-TM-original) Made [spongebob-cli in rust](https://github.com/Ali-TM-original/SpongbobCli-Rust)
 
## Contributors
Feel free to add yourself in if you contributed to the project.
<div align="center">
	<a href="https://github.com/trakBan/spongebob-cli/graphs/contributors">
  	<img src="https://contrib.rocks/image?repo=trakBan/spongebob-cli" />
	</a>
</div>
