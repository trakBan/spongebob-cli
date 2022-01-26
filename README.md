# spongebob-cli
Watch classic spongebob from the terminal!
Thanks to everyone that is starring, forking, writing issues, pull requesting and just users of spongebob-cli!

![updatedgif45729805790](https://user-images.githubusercontent.com/81049050/150833862-0a828939-f267-4bd2-931f-79df55d51e28.gif)

## Dependecies:
- mpv player https://mpv.io/  (Must be installed through a package manager)

## How to install:

### For UNIX based OS - One Line Execution
Checkout the source code with `git` or download it as a .zip file.
```bash

#Sudo isn't required as long as you're in Root
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

## Arch and arch based distributions
This is not kept up to date regulary.
There is an [AUR](https://aur.archlinux.org/packages/spongebob-cli-git/) package for spongebob-cli mantained by [getchoo](https://github.com/getchoo)

```
yay -S spongebob-cli-git
```

## PackageStatus
[![Packaging status](https://repology.org/badge/vertical-allrepos/spongebob-cli.svg)](https://repology.org/project/spongebob-cli/versions)

## Episodes that are known to not work
- Episode 30

## Troubleshooting

### If setup.py fails try this:
```bash
pip3 install termcolor beautifulsoup4 prettytable halo
```

### If you're getting an error like `sudo: python: command not found`
```bash
git clone https://github.com/trakBan/spongebob-cli.git; cd spongebob-cli; chmod +x spongebob-cli; sudo python3 setup.py install
```

#### Gentoo users:
Run this instead:
```bash
git clone https://github.com/trakBan/spongebob-cli.git; cd spongebob-cli; chmod +x spongebob-cli; python3 setup.py install --user
```

### If the video won't play
- Check if you have mpv and youtube-dl installed.
    - You can also install `youtube-dl` through your package manager if `setup.py` did not install it correctly
- If you don't have youtube-dl but a fork of it, make a alias in your .zshrc or .bashrc for youtube-dl and direct it to your fork.

## Contributors
[yaacornus](https://github.com/yaacornus), 
[redouane](https://github.com/red-elka), 
[totensee](https://github.com/totensee), 
[Kat](https://github.com/TransKat), 
[dev-nolant](https://github.com/dev-nolant)
