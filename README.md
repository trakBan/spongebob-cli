# spongebob-cli
Watch classic spongebob from the terminal!

![ezgif com-gif-maker](https://user-images.githubusercontent.com/81049050/165950004-a21d0199-79b5-4ebe-b733-94df1fee918e.gif)

## Usage
```
 usage: spongebob-cli [-h] [-p PLAY] [-l] [-r] [-d DOWNLOAD] [-da] [-b] [-vp VIDEO_PLAYER] [-vd VIDEO_DOWNLOADER]

Watch classic spongebob from the terminal!

options:
  -h, --help            show this help message and exit
  -p PLAY, --play PLAY  play the wanted episode without any user interaction
  -l, --list            list episodes and quit
  -r, --random          play random episode and quit
  -d DOWNLOAD, --download DOWNLOAD
                        download the wanted episode
  -da, --download-all   download all episodes
  -b, --binge           play every video
  -vp VIDEO_PLAYER, --video-player VIDEO_PLAYER
                        use another video player [default=mpv]
  -vd VIDEO_DOWNLOADER, --video-downloader VIDEO_DOWNLOADER
                        use another video downloadr [default=wget]
```

## How to install:

## External programs
  - Video player (required) mpv is default, check ```help``` for specifying another video player
  - Downloader (optional) wget is default, check ```help``` for specifying another downloader 

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
git clone https://github.com/trakBan/spongebob-cli.git && cd spongebob-cli && chmod +x spongebob-cli && sudo python setup.py install
```

### Rewrite in rust!
 [Ali-TM-original ](https://github.com/Ali-TM-original) Made [spongebob-cli in rust](https://github.com/Ali-TM-original/SpongbobCli-Rust)
 
## Contributors
<div align="center">
	<a href="https://github.com/trakBan/spongebob-cli/graphs/contributors">
  	<img src="https://contrib.rocks/image?repo=trakBan/spongebob-cli" />
	</a>
</div>
