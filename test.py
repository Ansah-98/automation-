import webbrowser
import bs4


import requests 

filed  = requests.get('https://youtu.be/hVx49oXgNv8')
filed.raise_for_status()

playfile = open('javascript.mp4','wb')
for chunck in filed.iter_content(1000):
    playfile.write(chunck)
  
playfile.close()
print(playfile)