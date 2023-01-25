# Refactored branch
This branch will slowly replace main branch

## Download
```
git clone -b refactored https://github.com/trakBan/spongebob-cli.git
```

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

# spongebob-cli
Watch classic spongebob from the terminal!
