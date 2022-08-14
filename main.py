
from PIL import Image
from pytesseract import pytesseract
from moviepy.editor import *
import moviepy as mp
import moviepy.editor as mp
from gtts import gTTS
import random
import praw
import requests
#reddit imige grabbing
reddit = praw.Reddit(client_id="3BPKsmDeLHUwHbUYNIJmeA",
                        client_secret="UYluUprtlM9fryKw1KMv7g6WoTwnPg",
                        user_agent="scraperbot")
sub = reddit.subreddit("greentext")
for post in sub.top(limit=1,time_filter="hour"):
    URL = (post.url)
response = requests.get(URL)
open("greentext/greentext.jpg", "wb").write(response.content)
#text reading
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"C:\Users\user\Desktop\Youtube shorts bot project\greentext\greentext.jpg"
img = Image.open(image_path)
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(img)
lines = (text[:-1])
print("Text reading done...")
#text processing
lines = lines.partition(">")[2]
lines = lines.replace("\n", "")
lines = lines.replace("|", "")
lines = lines.replace(">", ",")
#tts
tts = gTTS(text=f"{lines}", lang='en')
tts.save("speech.mp3")
print("Crappy tts done...")
#video editing framewrok
from mutagen.mp3 import MP3
audio = MP3('speech.mp3')
audiolen =  (audio.info.length)
audiolen = str(audiolen)
audiolen = audiolen[:audiolen.index(".")]
audiolen = int(audiolen)
print("Video prep done...")
#video editing (hell)
splice = random.randint(10,43)
endsplice = splice + audiolen
clip = VideoFileClip("background.mp4").subclip(splice, endsplice)
myclip = ImageClip("logo.jpg")

final = CompositeVideoClip([myclip.set_position("center")], clip)
final.write_videofile("test.mp4")
print('Video editing done...')
