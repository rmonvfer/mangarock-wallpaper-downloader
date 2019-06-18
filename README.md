# Reverse Engineering Manga Rock's Wallpaper API
## This repo
In this repo you can find:
- This readme with detailed instructions and information about how this was done
- The complete ´data.json´ obtained from mangarock servers
- 3 HD manga/anime images chosen from a total of 2200 I downloaded with my script

## Background

##### Historic background

Manga Rock is a web service that allows it's users to seamlessly read Manga Comics and _Japan-related_ graphic material.

Manga Rock launched an Android App about 5 years ago (the oldest APK I could find  was dated on 2014 ), the application uses a proprietary web API in order to communicate with its server to fetch the comic images and other assets requested by the application.

##### Wallpaper feature

Manga Rock added a new feature in the latest update of their application that hugely simplifies the task of searching for manga/anime imagery to use as wallpaper. The point here is that they are not free, to download and use them, one must first pay using the in-app currency (_rocks_).  AFAIK, there's guy who has reversed their reward system and even built a tool to earn an unlimited number of rocks, but as of today, it doesn't work because it uses an outdated version of Manga Rock's API. 

## Tools

- Android Phone running AOSP RR 8.1 
- Parallel Space (64 bits) App
- HttpCanary App
- Manga Rock Definitive App (downloaded from their website)

## Procedure

##### Packet capture

##### Binary file analysis

##### Hacking :)

