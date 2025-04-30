All how-to-use information is in the information tab in the tool itself
Download EXE [here](https://github.com/OppaiEcchi/DownloaderConverterCutter/releases/tag/Downloader)


====================================links====================================

ffmpeg:  https://ffmpeg.org/download.html#build-windows
(recommended version: "gyan.dev" "ffmpeg-release-full") get 7zip for that
yt-dlp: https://github.com/yt-dlp/yt-dlp
streamlink: https://streamlink.github.io/
fanbox-dl: https://github.com/hareku/fanbox-dl
mpc: https://codecguide.com/download_k-lite_codec_pack_mega.htm
vlc: https://www.videolan.org/vlc/
cookies converter: https://raw.githubusercontent.com/dandv/convert-chrome-cookies-to-netscape-format/master/convert-cookies.js

=========================preparing required programs=========================

Required programs to use all functions of this tool are:
ffmpeg, yt-dlp, streamlink.
additionally you might want a video player for "streamlink"
if you want to use "VLC" or "MPC" links are above
and remember to install them in default directory

ffmpeg:
1.download and place all three ".exe" files from "bin" folder in:
    "C:\(yourfoldername)"
2.in taskbar searchbar type "path" and hit enter
3.go to "Environment Variables"
4.in "System Variables" select "Path" and click "Edit"
5.add line: "C:\(yourfoldername)"
you can check if it works with cmd line: "ffmpeg -codecs"
ffmpeg is now ready.

yt-dlp:
just download the last version, and place it anywhere you want
but i recommend the same folder as ffmpeg, since the Path is already added
if you want different folder, then do the same path adding as with ffmpeg
and yt-dlp is also ready now.
NOTE: with yt-dlp you can download single video, but also playlist
or even a whole channel, all you need to do is copypaste a link of video
playlist, or channel and download
you can also download videos from different websites
all supported websites are listed in the link below.
https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

streamlink:
download and install the last version, installation should add it to PATH
if it didn't, just add it, if you don't remember where was it installed
then try "C:\Program Files (x86)\Streamlink\bin" or in the non (x86)
now streamlink is ready

fanbox-dl:
download the lastest version of the fanbox-dl, and place it anywhere,
and do the PATH adding process that you should already know,
but and again i recommend the same folder as ffmpeg and yt-dlp
and you can now use fanbox-dl.

============================how to use functions============================

"converter":
uses ffmpeg
for "Video to Video", type in input and output file name(with extension)
for "Video to mp3", do the same with input file
but for the output just type in the name, it will be in mp3 anyway.
NOTE: place input files in the same directory where this tool is

"cutter":
uses ffmpeg
input and output just like in "Video to Video" in "converter"
for start and end times, type in the beginning and the end time of the clip
in format "hh:mm:ss" or "hh:mm:ss:ms"
"hh"=hours, "mm"=minutes, "ss"=seconds, "ms"=milliseconds.
NOTE: place input files in the same directory where this tool is

"concatenate":
uses ffmpeg
merge two or more media files
input file list is name of the .txt file containing the list of input files
example of what the list should look like":
file 'filename.extension' 
file 'filename.extension' 
file 'filename.extension' 
output is similar to output from "converter"
NOTE 1: place input files in the same directory where this tool is
NOTE 2: (.txt list file and all files from the list inside of it)

"yt-dlp":
uses yt-dlp
"(w/ subtitles)" will also download "en" subtitles in ".srt" format
"w/o cookies", just copy paste the link and download
"w/ cookies", for this you need converted cookies in ".txt" file
1.for that first go to this link:
    https://raw.githubusercontent.com/dandv/convert-chrome-cookies-to-netscape-format/master/convert-cookies.js
    right click anywhere on this page and select "save as"
    don't change the name
    save it in the same directory where this tool is
2.open blank .txt file in "notepad", or any txt editor you have
3.in chrome browser go to the website you want the cookies from
    for youtube just go to https://www.youtube.com
4.press "F12" to open "Developer tools"
5.go to "Application" tab(if you don't see it, just press ">>" button)
    under "Storage" expand "Cookies" and select "https://www.youtube.com"
    then select all text in the box on the right
    and copypaste it to the blank .txt file created before
6.save the file as "(yourfilename).txt", in the directory where this tool is
7.copypaste the name of the txt file(without extension) into the "Input File"    and press "Convert", converted cookies file will have the name
  "netscape-cookies.txt" don't change it if you want to use it in this tool
now you can download videos with cookies.

"twitcasting":
uses ffmpeg
1.in chrome browser go to https://www.google.com/ and search for:
    "What is my User Agent"
    and copypaste whole line into the "User Agent" entrybox
2.in chrome browser press F12, go to "console" tab, and run this script:
    let a=[];for(let _ of JSON.parse(document.querySelector("video")["dataset"]["moviePlaylist"])[2])a.push(_.source?.url);console.log(a.join("\n"))
3.in output file just type the name, it will be in mp4 format.

"streamlink":
uses streamlink
"VLC" will open the stream in "VLC" player
location:
"C:\Program Files\VideoLAN\VLC\vlc.exe"
"MPC-64" and "MPC-32" will open the stream in 64 and 32 bit versions of MPC
locations:
"C:\Program Files (x86)\K-Lite Codec Pack\MPC-HC64\mpc-hc64.exe" for 64 bit
"C:\Program Files (x86)\K-Lite Codec Pack\MPC-HC\mpc-hc.exe" for 32 bit
if you have those installed in different directory
or if you want to use different player
use "Different Player" button, it will ask you to pick the ".exe" file
"Download", copypaste the link, type in the output file name(w/ extension)
press the "Download" button, and it will ask you for download location.

"fanbox-dl":
uses fanbox-dl
"Session ID", this is very similar to cookies for yt-dlp but even easier
1.in chrome browser open Fanbox page(remember to log in)
2.open developer tools(F12) and go to "Application" tab
    (use ">>" if you can't find it)
3.in "Storage" section expand "Cookies", and find "https://www.fanbox.cc"
4.in the box on the right-hand side, find "FANBOXSESSID", and use it's value
    (also if you don't fill in that entrybox with a proper session id,
    the downloader will only download the public posts)
"Creator ID", here just paste the name from the Creator fanbox page link
    example: "https://<creator_name>.fanbox.cc/"
now just use "Download" button

=============================================================================
