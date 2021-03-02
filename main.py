from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import youtube_dl

Builder.load_file('design.kv')

Window.size = (500, 270)

class MyLayout(GridLayout):
    def check_click(self, instance, value, y):
        if self.ids.link.text != '':
            self.ids.dl.disabled = False
        if y == 'video':
            global options
            options = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': '~/Videos/%(title)s.%(ext)s',
                'mergeoutput': True,
                'ffmpeg_location': 'ffmpeg-win-2.2.2'
            }
            self.ids.ch2.disabled = True
            self.ids.ch1.disabled = False
        elif y == 'audio':
            options = {
                'format': 'bestaudio/best',
                'extractaudio': True,  # extracting audio
                'audioformat': 'mp3',  # file options and format
                'outtmpl': "~/Music/%(title)s.%(ext)s",  # name the file the ID of the video
                'ffmpeg_location': 'ffmpeg-win-2.2.2',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',  # Used ffmpeg for converting the file to mp3
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            }
            self.ids.ch1.disabled = True
            self.ids.ch2.disabled = False

    def download(self):
        link = self.ids.link.text
        self.ids.dl.text = "downloaded"
        self.ids.dl.disabled = True
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([link])  # final downloading

class ytDownld(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    ytDownld().run()
