import os
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

window = Tk()
window.title("Downloader/Converter/Cutter")
window_width = 700
window_height = 350
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
z = int((screen_width / 2) - (window_width) / 2)
y = int((screen_height / 2) - (window_height) / 2)
window.geometry("{}x{}+{}+{}".format(window_width, window_height, z, y))

def buttonconv1_press():
    inputfileconv, outputfileconv = entryconv1.get(),  entryconv2.get()
    try:
        os.system('cmd /c ffmpeg -i "' + (inputfileconv) + '" -codec copy "' + (outputfileconv) +'"')
    except:
        print("could not execute command")
def buttonconv2_press():
    inputfileconv, outputfileconv = entryconv1.get(),  entryconv2.get()
    try:
        os.system('cmd /c ffmpeg -i "' + (inputfileconv) + '" -vn -ar 44100 -ac 2 -ab 128k -f mp3 "' + (outputfileconv) + '.mp3"')
    except:
        print("could not execute command")

def buttoncut_press():
    inputcut, starttime, endtime, outputcut = entrycut1.get(), entrycut2.get(), entrycut3.get(), entrycut4.get()
    try:
        os.system('cmd /c ffmpeg -i "' + (inputcut) + '" -ss ' + (starttime) + ' -to ' + (endtime) + ' "' + (outputcut) + '"')
    except:
        print("could not execute command")

def buttonconcat_press():
    inputfileslist, outputconcat = entryconcat1.get(), entryconcat2.get()
    try:
        os.system('cmd /c ffmpeg -safe 0 -f concat -i "' + (inputfileslist) + '.txt" -c copy "' + (outputconcat) + '"')
    except:
        print("could not execute command")

def buttonytdlp1_press():
    ytdlplink = entryytdlp.get()
    try:
        os.system('cmd /c yt-dlp --merge-output-format mp4 ' + (ytdlplink))
    except:
        print("could not execute command")

def buttonytdlp1sub_press():
    ytdlplink = entryytdlp.get()
    try:
        os.system('cmd /c yt-dlp --merge-output-format mp4 --write-sub --sub-lang en --convert-subs srt ' + (ytdlplink))
    except:
        print("could not execute command")
def buttonytdlp2_press():
    ytdlplink = entryytdlp.get()
    try:
        os.system('cmd /c yt-dlp --cookies netscape-cookies.txt --merge-output-format mp4 ' + (ytdlplink))
    except:
        print("could not execute command")
def buttonytdlp2sub_press():
    ytdlplink = entryytdlp.get()
    try:
        os.system('cmd /c yt-dlp --cookies netscape-cookies.txt --merge-output-format mp4 --write-sub --sub-lang en --convert-subs srt ' + (ytdlplink))
    except:
        print("could not execute command")
def buttonytdlp3_press():
    ytdlplink, inputcookies = entryytdlp.get(), entrycookies.get()
    try:
        os.system('cmd /c yt-dlp --cookies-from-browser ' + (inputcookies) + ' --merge-output-format mp4 ' + (ytdlplink))
    except:
        print("could not execute command")
def buttonytdlp3sub_press():
    ytdlplink, inputcookies = entryytdlp.get(), entrycookies.get()
    try:
        os.system('cmd /c yt-dlp --cookies-from-browser ' + (inputcookies) + ' --merge-output-format mp4 --write-sub --sub-lang en --convert-subs srt ' + (ytdlplink))
    except:
        print("could not execute command")
def buttoncookies_press():
    inputcookies = entrycookies.get()
    try:
        os.system('cmd /c node convert-cookies.js "' + (inputcookies) + '.txt" > netscape-cookies.txt')
    except:
        print("could not execute command")
def buttonytdlpupdate_press():
    inputcookies = entrycookies.get()
    try:
        os.system('cmd /c yt-dlp --update')
    except:
        print("could not execute command")

def buttontwtcst_press():
    useragent, twclink, twtoutput = entrytwtcst1.get(), entrytwtcst2.get(), entrytwtcst3.get()
    try:
        os.system('cmd /c ffmpeg.exe -protocol_whitelist file,http,https,tcp,tls,crypto -user_agent "' + (useragent) + '" -headers "Origin: https://twitcasting.tv/" -i "' + (twclink) + '" -c copy "' + (twtoutput) + '.mp4"')
    except:
        print("could not execute command")

def buttonstrlnk1_press():
    strlnklink = entrystrlnk2.get()
    try:
        os.system('cmd /c streamlink --player "C:\Program Files\VideoLAN\VLC\\vlc.exe" ' + (strlnklink) + ' 1080p')
    except:
        print("could not execute command")
def buttonstrlnk2_press():
    strlnklink = entrystrlnk2.get()
    try:
        os.system('cmd /c streamlink --player "C:\Program Files (x86)\K-Lite Codec Pack\MPC-HC64\mpc-hc64.exe" ' + (strlnklink) + ' 1080p')
    except:
        print("could not execute command")
def buttonstrlnk3_press():
    strlnklink = entrystrlnk2.get()
    try:
        os.system('cmd /c streamlink --player "C:\Program Files (x86)\K-Lite Codec Pack\MPC-HC\mpc-hc.exe" ' + (strlnklink) + ' 1080p')
    except:
        print("could not execute command")
def buttonstrlnk4_press():
    strlnklink, playerpath = entrystrlnk2.get(), filedialog.askopenfilename()
    try:
        os.system('cmd /c streamlink --player "' + (playerpath) + '" ' + (strlnklink) + ' 1080p')
    except:
        print("could not execute command")
def buttonstrlnk5_press():
    strlnklink, dllocation, filename = entrystrlnk2.get(), filedialog.askdirectory(), entrystrlnk3.get()
    try:
        os.system('cmd /c streamlink -o "' + (dllocation) + "\\"+ (filename) + '" ' + (strlnklink) + ' 1080p')
    except:
        print("could not execute command")
def buttonfanbox1_press():
    sessid, creator = entryfanbox1.get(), entryfanbox2.get()
    try:
        os.system('cmd /c fanbox-dl --sessid ' + (sessid) + ' --save-dir ./content --creator ' + (creator) + ' --all')
    except:
        print("could not execute command")

notebook = ttk.Notebook(window)

tabconv = Frame(notebook, padx=10, pady=10,bg="#696969")
tabcut = Frame(notebook, padx=10, pady=10,bg="#696969")
tabconcat = Frame(notebook, padx=10, pady=10,bg="#696969")
tabytdlp = Frame(notebook, padx=10, pady=10,bg="#696969")
tabtwtcst = Frame(notebook, padx=10, pady=10,bg="#696969")
tabstrlnk = Frame(notebook, padx=10, pady=10,bg="#696969")
tabfanbox = Frame(notebook, padx=10, pady=10,bg="#696969")
info = Frame(notebook, padx=10, pady=10,bg="#696969")

notebook.add(tabconv,text="converter")
notebook.add(tabcut,text="cutter")
notebook.add(tabconcat,text="concatenate")
notebook.add(tabytdlp,text="yt-dlp")
notebook.add(tabtwtcst,text="twitcasting")
notebook.add(tabstrlnk,text="streamlink")
notebook.add(tabfanbox,text="fanbox-dl")
notebook.add(info,text="information")

notebook.pack(expand=True,fill="both")
frameconv1 = Frame(tabconv,bg="#696969")
frameconv1.pack(anchor=W)
frameconv2 = Frame(tabconv,bg="#696969")
frameconv2.pack(anchor=W)
frameconv3 = Frame(tabconv,bg="#696969")
frameconv3.pack(anchor=W)
frameconv4 = Frame(tabconv,bg="#696969")
frameconv4.pack(anchor=W)
frameconv5 = Frame(tabconv,bg="#696969")
frameconv5.pack(anchor=W)
frameconv6 = Frame(tabconv,bg="#696969")
frameconv6.pack(anchor=W)
framecut1 = Frame(tabcut,bg="#696969")
framecut1.pack(anchor=W)
framecut2 = Frame(tabcut,bg="#696969")
framecut2.pack(anchor=W)
framecut3 = Frame(tabcut,bg="#696969")
framecut3.pack(anchor=W)
framecut4 = Frame(tabcut,bg="#696969")
framecut4.pack(anchor=W)
framecut5 = Frame(tabcut,bg="#696969")
framecut5.pack(anchor=W)
frameconcat1 = Frame(tabconcat,bg="#696969")
frameconcat1.pack(anchor=W)
frameconcat2 = Frame(tabconcat,bg="#696969")
frameconcat2.pack(anchor=W)
frameconcat3 = Frame(tabconcat,bg="#696969")
frameconcat3.pack(anchor=W)
frameconcat4 = Frame(tabconcat,bg="#696969")
frameconcat4.pack(anchor=W)
frameytdlp1 = Frame(tabytdlp,bg="#696969")
frameytdlp1.pack(anchor=W)
frameytdlp2 = Frame(tabytdlp,bg="#696969")
frameytdlp2.pack(anchor=W)
frameytdlp2sub = Frame(tabytdlp,bg="#696969")
frameytdlp2sub.pack(anchor=W)
frameytdlp3 = Frame(tabytdlp,bg="#696969")
frameytdlp3.pack(anchor=W)
frameytdlp3sub = Frame(tabytdlp,bg="#696969")
frameytdlp3sub.pack(anchor=W)
frameytdlp4 = Frame(tabytdlp,bg="#696969")
frameytdlp4.pack(anchor=W)
frameytdlp4sub = Frame(tabytdlp,bg="#696969")
frameytdlp4sub.pack(anchor=W)
frameytdlp5 = Frame(tabytdlp,bg="#696969")
frameytdlp5.pack(anchor=W)
frameytdlp6 = Frame(tabytdlp,bg="#696969")
frameytdlp6.pack(anchor=W)
frameytdlp7 = Frame(tabytdlp,bg="#696969")
frameytdlp7.pack(anchor=W)
frametwtcst1 = Frame(tabtwtcst,bg="#696969")
frametwtcst1.pack(anchor=W)
frametwtcst2 = Frame(tabtwtcst,bg="#696969")
frametwtcst2.pack(anchor=W)
frametwtcst3 = Frame(tabtwtcst,bg="#696969")
frametwtcst3.pack(anchor=W)
frametwtcst4 = Frame(tabtwtcst,bg="#696969")
frametwtcst4.pack(anchor=W)
framestrlnk2 = Frame(tabstrlnk,bg="#696969")
framestrlnk2.pack(anchor=W)
framestrlnk3 = Frame(tabstrlnk,bg="#696969")
framestrlnk3.pack(anchor=W)
framestrlnk4 = Frame(tabstrlnk,bg="#696969")
framestrlnk4.pack(anchor=W)
framestrlnk5 = Frame(tabstrlnk,bg="#696969")
framestrlnk5.pack(anchor=W)
framestrlnk6 = Frame(tabstrlnk,bg="#696969")
framestrlnk6.pack(anchor=W)
framestrlnk8 = Frame(tabstrlnk,bg="#696969")
framestrlnk8.pack(anchor=W)
framestrlnk7 = Frame(tabstrlnk,bg="#696969")
framestrlnk7.pack(anchor=W)
framefanbox1 = Frame(tabfanbox,bg="#696969")
framefanbox1.pack(anchor=W)
framefanbox2 = Frame(tabfanbox,bg="#696969")
framefanbox2.pack(anchor=W)
framefanbox3 = Frame(tabfanbox,bg="#696969")
framefanbox3.pack(anchor=W)

labelconv1 = Label(frameconv1,text="Input File(with extention)",font=("gothic",13),bg="#696969",fg="#000000")
labelconv1.pack(side="right")
entryconv1 = Entry(frameconv1,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entryconv1.pack(side="left")
labelconv2 = Label(frameconv2,text="Output File(with extention)",font=("gothic",13),bg="#696969",fg="#000000")
labelconv2.pack(side="right")
entryconv2 = Entry(frameconv2,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entryconv2.pack(side="left")

labelcut1 = Label(framecut1,text="Input File(with extention)",font=("gothic",13),bg="#696969",fg="#000000")
labelcut1.pack(side="right")
entrycut1 = Entry(framecut1,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entrycut1.pack(side="left")
labelcut2 = Label(framecut2,text="Start Time(in format hh:mm:ss, or hh:mm:ss:ms)",font=("gothic",13),bg="#696969",fg="#000000")
labelcut2.pack(side="right")
entrycut2 = Entry(framecut2,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entrycut2.pack(side="left")
labelcut3 = Label(framecut3,text="End Time(in format hh:mm:ss, or hh:mm:ss:ms)",font=("gothic",13),bg="#696969",fg="#000000")
labelcut3.pack(side="right")
entrycut3 = Entry(framecut3,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entrycut3.pack(side="left")
labelcut4 = Label(framecut4,text="Output File(with extention)",font=("gothic",13),bg="#696969",fg="#000000")
labelcut4.pack(side="right")
entrycut4 = Entry(framecut4,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entrycut4.pack(side="left")

labelconcat1 = Label(frameconcat1,text="Input File List(txt)",font=("gothic",13),bg="#696969",fg="#000000")
labelconcat1.pack(side="right")
entryconcat1 = Entry(frameconcat1,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entryconcat1.pack(side="left")
labelconcat1 = Label(frameconcat2,text="example line for the list (file 'filename.extension' )",font=("gothic",13),bg="#696969",fg="#000000")
labelconcat1.pack(side="right")
labelconcat2 = Label(frameconcat3,text="Output File(with extention)",font=("gothic",13),bg="#696969",fg="#000000")
labelconcat2.pack(side="right")
entryconcat2 = Entry(frameconcat3,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entryconcat2.pack(side="left")

labelytdlp1 = Label(frameytdlp1,text="Video link",font=("gothic",13),bg="#696969",fg="#000000")
labelytdlp1.pack(side="right")
entryytdlp = Entry(frameytdlp1,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entryytdlp.pack(side="left")
labelcookies = Label(frameytdlp5, text="Browser name / Input File(cookies copied to a .txt file)", font=("gothic", 13),bg="#696969",fg="#000000")
labelcookies.pack(side="right")
entrycookies = Entry(frameytdlp5, width=20, font=("gothic", 12),bg="#696969",fg="#000000")
entrycookies.pack(side="left")

labeltwtcst1 = Label(frametwtcst1,text="User_Agent",font=("gothic",13),bg="#696969",fg="#000000")
labeltwtcst1.pack(side="right")
entrytwtcst1 = Entry(frametwtcst1,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entrytwtcst1.pack(side="left")
labeltwtcst2 = Label(frametwtcst2,text="Link",font=("gothic",13),bg="#696969",fg="#000000")
labeltwtcst2.pack(side="right")
entrytwtcst2 = Entry(frametwtcst2,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entrytwtcst2.pack(side="left")
labeltwtcst3 = Label(frametwtcst3,text="Output file name",font=("gothic",13),bg="#696969",fg="#000000")
labeltwtcst3.pack(side="right")
entrytwtcst3 = Entry(frametwtcst3,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entrytwtcst3.pack(side="left")

labelstrlnk2 = Label(framestrlnk2,text="Video Link",font=("gothic",13),bg="#696969",fg="#000000")
labelstrlnk2.pack(side="right")
entrystrlnk2 = Entry(framestrlnk2,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entrystrlnk2.pack(side="left")
labelstrlnk3 = Label(framestrlnk8,text="Download file name(with extention)",font=("gothic",13),bg="#696969",fg="#000000")
labelstrlnk3.pack(side="right")
entrystrlnk3 = Entry(framestrlnk8,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entrystrlnk3.pack(side="left")

labelfanbox1 = Label(framefanbox1,text="Session ID",font=("gothic",13),bg="#696969",fg="#000000")
labelfanbox1.pack(side="right")
entryfanbox1 = Entry(framefanbox1,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entryfanbox1.pack(side="left")
labelfanbox2 = Label(framefanbox2,text="Creator ID",font=("gothic",13),bg="#696969",fg="#000000")
labelfanbox2.pack(side="right")
entryfanbox2 = Entry(framefanbox2,width=20,font=("gothic",12),bg="#696969",fg="#000000")
entryfanbox2.pack(side="left")

labelconv3 = Label(frameconv3,text="Video to Video",font=("gothic",13),bg="#696969",fg="#000000")
labelconv3.pack(side="right")
buttonconv1 = Button(frameconv3,text="Convert",command=buttonconv1_press,font=("gothic",12),width=19,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonconv1.pack(side="left")
labelconv4 = Label(frameconv4,text="Video to mp3(extension not required)",font=("gothic",13),bg="#696969",fg="#000000")
labelconv4.pack(side="right")
buttonconv2 = Button (frameconv4,text="Convert",command=buttonconv2_press,font=("gothic",12),width=19,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonconv2.pack(side="left")

buttoncut = Button (framecut5,text="Cut",command=buttoncut_press,font=("gothic",12),width=19,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttoncut.pack(side="left")

buttonconcat = Button (frameconcat4,text="Concatenate",command=buttonconcat_press,font=("gothic",12),width=19,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonconcat.pack(side="left")

labelytdlp2 = Label(frameytdlp2,text="w/o Cookies",font=("gothic",13),bg="#696969",fg="#000000")
labelytdlp2.pack(side="right")
buttonytdlp1 = Button(frameytdlp2,text="Download",font=("gothic",12),command=buttonytdlp1_press,width=19,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonytdlp1.pack(side="left")
labelytdlp2 = Label(frameytdlp2sub,text="w/o Cookies(w/ subtitles)",font=("gothic",13),bg="#696969",fg="#000000")
labelytdlp2.pack(side="right")
buttonytdlp1 = Button(frameytdlp2sub,text="Download",font=("gothic",12),command=buttonytdlp1sub_press,width=19,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonytdlp1.pack(side="left")
labelytdlp3 = Label(frameytdlp3,text="w/ Cookies (netscape-cookies.txt)",font=("gothic",13),bg="#696969",fg="#000000")
labelytdlp3.pack(side="right")
buttonytdlp2 = Button(frameytdlp3,text="Download",font=("gothic",12),command=buttonytdlp2_press,width=19,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonytdlp2.pack(side="left")
labelytdlp3 = Label(frameytdlp3sub,text="w/ Cookies (netscape-cookies.txt) (w/ subtitles)",font=("gothic",13),bg="#696969",fg="#000000")
labelytdlp3.pack(side="right")
buttonytdlp2 = Button(frameytdlp3sub,text="Download",font=("gothic",12),command=buttonytdlp2sub_press,width=19,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonytdlp2.pack(side="left")
labelytdlp4 = Label(frameytdlp4,text="w/ Cookies (directly from browser)",font=("gothic",13),bg="#696969",fg="#000000")
labelytdlp4.pack(side="right")
buttonytdlp3 = Button(frameytdlp4,text="Download",font=("gothic",12),command=buttonytdlp3_press,width=19,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonytdlp3.pack(side="left")
labelytdlp4 = Label(frameytdlp4sub,text="w/ Cookies (directly from browser) (w/ subtitles)",font=("gothic",13),bg="#696969",fg="#000000")
labelytdlp4.pack(side="right")
buttonytdlp3 = Button(frameytdlp4sub,text="Download",font=("gothic",12),command=buttonytdlp3sub_press,width=19,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonytdlp3.pack(side="left")
labelcookies = Label(frameytdlp6,text="Convert Cookies(convert-cookies.js required)",font=("gothic",13),bg="#696969",fg="#000000")
labelcookies.pack(side="right")
buttoncookies = Button(frameytdlp6,text="Convert",font=("gothic",12),command=buttoncookies_press,width=19,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttoncookies.pack(side="left")
buttonytdlpupdate = Button(frameytdlp7,text="Update yt-dlp",font=("gothic",12),command=buttonytdlpupdate_press,width=19,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonytdlpupdate.pack(side="left")

buttontwtcst = Button(frametwtcst4,text="Download",font=("gothic",12),command=buttontwtcst_press,width=19,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttontwtcst.pack(side="left")

labelstrlnk3 = Label(framestrlnk3,text="VLC",font=("gothic",13),bg="#696969",fg="#000000")
labelstrlnk3.pack(side="right")
buttonstrlnk1 = Button(framestrlnk3,text="Play",font=("gothic",12),width=19,command=buttonstrlnk1_press,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonstrlnk1.pack(side="left")
labelstrlnk4 = Label(framestrlnk4,text="MPC-64bit",font=("gothic",13),bg="#696969",fg="#000000")
labelstrlnk4.pack(side="right")
buttonstrlnk2 = Button(framestrlnk4,text="Play",font=("gothic",12),width=19,command=buttonstrlnk2_press,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonstrlnk2.pack(side="left")
labelstrlnk5 = Label(framestrlnk5,text="MPC-32bit",font=("gothic",13),bg="#696969",fg="#000000")
labelstrlnk5.pack(side="right")
buttonstrlnk3 = Button(framestrlnk5,text="Play",font=("gothic",12),width=19,command=buttonstrlnk3_press,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonstrlnk3.pack(side="left")
labelstrlnk6 = Label(framestrlnk6,text="Different Player",font=("gothic",13),bg="#696969",fg="#000000")
labelstrlnk6.pack(side="right")
buttonstrlnk4 = Button(framestrlnk6,text="Play",font=("gothic",12),width=19,command=buttonstrlnk4_press,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonstrlnk4.pack(side="left")
labelstrlnk7 = Label(framestrlnk7,text="Download Video/Stream while it's live",font=("gothic",13),bg="#696969",fg="#000000")
labelstrlnk7.pack(side="right")
buttonstrlnk5 = Button(framestrlnk7,text="Download",font=("gothic",12),width=19,command=buttonstrlnk5_press,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonstrlnk5.pack(side="left")

labelfanbox3 = Label(framefanbox3,text="All works of mentioned creator",font=("gothic",13),bg="#696969",fg="#000000")
labelfanbox3.pack(side="right")
buttonfanbox1 = Button(framefanbox3,text="Download",command=buttonfanbox1_press,font=("gothic",12),width=19,bg="#696969",fg="#000000",activebackground="#696969",activeforeground="#000000")
buttonfanbox1.pack(side="left")

textinfo = Text(info,font=("gothic",12),bg="#696969",fg="#000000")
textinfo.pack(side=LEFT, fill=BOTH, expand=True)

scrollbarinfo = Scrollbar(textinfo,bg="#696969")
info.grid_rowconfigure(0, weight=1)
info.grid_columnconfigure(0, weight=1)
textinfo.grid(sticky=N + E + S + W)

scrollbarinfo.pack(side=RIGHT, fill=Y)
textinfo.config(yscrollcommand=scrollbarinfo.set)

infotext = "====================================links====================================\n" \
           "\n" \
           "ffmpeg:  https://ffmpeg.org/download.html#build-windows\n" \
           "(recommended version: \"gyan.dev\" \"ffmpeg-release-full\") get 7zip for that\n" \
           "yt-dlp: https://github.com/yt-dlp/yt-dlp\n" \
           "streamlink: https://streamlink.github.io/\n" \
           "fanbox-dl: https://github.com/hareku/fanbox-dl\n" \
           "mpc: https://codecguide.com/download_k-lite_codec_pack_mega.htm\n" \
           "vlc: https://www.videolan.org/vlc/\n" \
           "cookies converter: https://raw.githubusercontent.com/dandv/convert-chrome-cookies-to-netscape-format/master/convert-cookies.js\n" \
           "\n" \
           "=========================preparing required programs=========================\n" \
           "\n" \
           "Required programs to use all functions of this tool are:\n" \
           "ffmpeg, yt-dlp, streamlink.\n" \
           "additionally you might want a video player for \"streamlink\"\n" \
           "if you want to use \"VLC\" or \"MPC\" links are above\n" \
           "and remember to install them in default directory\n" \
           "\n" \
           "ffmpeg:\n" \
           "1.download and place all three \".exe\" files from \"bin\" folder in:\n" \
           "    \"C:\\(yourfoldername)\"\n" \
           "2.in taskbar searchbar type \"path\" and hit enter\n" \
           "3.go to \"Environment Variables\"\n" \
           "4.in \"System Variables\" select \"Path\" and click \"Edit\"\n" \
           "5.add line: \"C:\\(yourfoldername)\"\n" \
           "you can check if it works with cmd line: \"ffmpeg -codecs\"\n" \
           "ffmpeg is now ready.\n" \
           "\n" \
           "yt-dlp:\n" \
           "just download the last version, and place it anywhere you want\n" \
           "but i recommend the same folder as ffmpeg, since the Path is already added\n" \
           "if you want different folder, then do the same path adding as with ffmpeg\n" \
           "and yt-dlp is also ready now.\n" \
           "NOTE: with yt-dlp you can download single video, but also playlist\n" \
           "or even a whole channel, all you need to do is copypaste a link of video\n" \
           "playlist, or channel and download\n" \
           "you can also download videos from different websites\n" \
           "all supported websites are listed in the link below.\n" \
           "https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md\n" \
           "\n" \
           "streamlink:\n" \
           "download and install the last version, installation should add it to PATH\n" \
           "if it didn't, just add it, if you don't remember where was it installed\n" \
           "then try \"C:\Program Files (x86)\Streamlink\\bin\" or in the non (x86)\n" \
           "now streamlink is ready\n" \
           "\n" \
           "fanbox-dl:\n" \
           "download the lastest version of the fanbox-dl, and place it anywhere,\n" \
           "and do the PATH adding process that you should already know,\n" \
           "but and again i recommend the same folder as ffmpeg and yt-dlp\n" \
           "and you can now use fanbox-dl.\n" \
           "\n" \
           "============================how to use functions============================\n" \
           "\n" \
           "\"converter\":\n" \
           "uses ffmpeg\n" \
           "for \"Video to Video\", type in input and output file name(with extension)\n" \
           "for \"Video to mp3\", do the same with input file\n" \
           "but for the output just type in the name, it will be in mp3 anyway.\n" \
           "NOTE: place input files in the same directory where this tool is\n" \
           "\n" \
           "\"cutter\":\n" \
           "uses ffmpeg\n" \
           "input and output just like in \"Video to Video\" in \"converter\"\n" \
           "for start and end times, type in the beginning and the end time of the clip\n" \
           "in format \"hh:mm:ss\" or \"hh:mm:ss:ms\"\n" \
           "\"hh\"=hours, \"mm\"=minutes, \"ss\"=seconds, \"ms\"=milliseconds.\n" \
           "NOTE: place input files in the same directory where this tool is\n" \
           "\n" \
           "\"concatenate\":\n" \
           "uses ffmpeg\n" \
           "merge two or more media files\n" \
           "input file list is name of the .txt file containing the list of input files\n" \
           "example of what the list should look like\":\n" \
           "file 'filename.extension' \n" \
           "file 'filename.extension' \n" \
           "file 'filename.extension' \n" \
           "output is similar to output from \"converter\"\n" \
           "NOTE 1: place input files in the same directory where this tool is\n" \
           "NOTE 2: (.txt list file and all files from the list inside of it)\n" \
           "\n" \
           "\"yt-dlp\":\n" \
           "uses yt-dlp\n" \
           "\"(w/ subtitles)\" will also download \"en\" subtitles in \".srt\" format\n" \
           "\"w/o cookies\", just copy paste the link and download\n" \
           "\"w/ cookies (netscape-cookies.txt)\", for this you need converted cookies in \".txt\" file\n" \
           "1.go to the link below:\n" \
           "    https://raw.githubusercontent.com/dandv/convert-chrome-cookies-to-netscape-format/master/convert-cookies.js\n" \
           "    right click anywhere on this page and select \"save as\"\n" \
           "    don't change the name\n" \
           "    save it in the same directory where this tool is\n" \
           "2.open blank .txt file in \"notepad\", or any txt editor you have\n" \
           "3.in chrome browser go to the website you want the cookies from\n" \
           "    for youtube just go to https://www.youtube.com\n" \
           "4.press \"F12\" to open \"Developer tools\"\n" \
           "5.go to \"Application\" tab(if you don't see it, just press \">>\" button)\n" \
           "    under \"Storage\" expand \"Cookies\" and select \"https://www.youtube.com\"\n" \
           "    then select all text in the box on the right\n" \
           "    and copypaste it to the blank .txt file created before\n" \
           "6.save the file as \"(yourfilename).txt\", in the directory where this tool is\n" \
           "7.copypaste the name of the txt file(without extension) into the \"Input File\"" \
           "    and press \"Convert\", converted cookies file will have the name\n" \
           "    \"netscape-cookies.txt\" don't change it if you want to use it in this tool\n" \
           "    now you can download videos with cookies.\n" \
           "\"w/ cookies (directly from browser)\" - in the \"Browser name / Input File\" type in\n" \
           "    the name of the internet browser where the cookies should be taken from\n" \
           "\"twitcasting\":\n" \
           "uses ffmpeg\n" \
           "1.in chrome browser go to https://www.google.com/ and search for:\n" \
           "    \"What is my User Agent\"\n" \
           "    and copypaste whole line into the \"User Agent\" entrybox\n" \
           "2.in chrome browser press F12, go to \"console\" tab, and run this script:\n" \
           "    let a=[];for(let _ of JSON.parse(document.querySelector(\"video\")[\"dataset\"][\"moviePlaylist\"])[2])a.push(_.source?.url);console.log(a.join(\"\\n\"))\n" \
           "3.in output file just type the name, it will be in mp4 format.\n" \
           "\n" \
           "\"streamlink\":\n" \
           "uses streamlink\n" \
           "\"VLC\" will open the stream in \"VLC\" player\n" \
           "location:\n" \
           "\"C:\Program Files\VideoLAN\VLC\\vlc.exe\"\n" \
           "\"MPC-64\" and \"MPC-32\" will open the stream in 64 and 32 bit versions of MPC\n" \
           "locations:\n" \
           "\"C:\Program Files (x86)\K-Lite Codec Pack\MPC-HC64\mpc-hc64.exe\" for 64 bit\n" \
           "\"C:\Program Files (x86)\K-Lite Codec Pack\MPC-HC\mpc-hc.exe\" for 32 bit\n" \
           "if you have those installed in different directory\n" \
           "or if you want to use different player\n" \
           "use \"Different Player\" button, it will ask you to pick the \".exe\" file\n" \
           "\"Download\", copypaste the link, type in the output file name(w/ extension)\n" \
           "press the \"Download\" button, and it will ask you for download location.\n" \
           "\n" \
           "\"fanbox-dl\":\n" \
           "uses fanbox-dl\n" \
           "\"Session ID\", this is very similar to cookies for yt-dlp but even easier\n" \
           "1.in chrome browser open Fanbox page(remember to log in)\n" \
           "2.open developer tools(F12) and go to \"Application\" tab\n" \
           "    (use \">>\" if you can't find it)\n" \
           "3.in \"Storage\" section expand \"Cookies\", and find \"https://www.fanbox.cc\"\n" \
           "4.in the box on the right-hand side, find \"FANBOXSESSID\", and use it's value\n" \
           "    (also if you don't fill in that entrybox with a proper session id,\n" \
           "    the downloader will only download the public posts)\n" \
           "\"Creator ID\", here just paste the name from the Creator fanbox page link\n" \
           "    example: \"https://<creator_name>.fanbox.cc/\"\n" \
           "now just use \"Download\" button\n" \
           "\n" \
           "=============================================================================" \

textinfo.insert(tkinter.INSERT, infotext)
textinfo.config(state=DISABLED)

window.resizable(False,False)
window.mainloop()