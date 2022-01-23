import os
import pytube as pt
import moviepy.editor as mp

# Download
url = str(input('URL: '))
stream = pt.YouTube(url).streams.get_audio_only()
stream.download('F:\Programmer\Músicas')
title = str(stream.title)

# Conversão
clip = mp.AudioFileClip('F:\Programmer\Músicas\\' + title + '.mp4')
clip.write_audiofile('F:\Programmer\Músicas\\' + title + '.mp3')

# Deletar mp4
delete = str(input('Deletar mp4? (S/N): '))
if delete in 'Ss':
    os.remove('F:\Programmer\Músicas\\' + title + '.mp4')
    print(".mp4 deletado!")
else:
    print(".mp4 não deletado!")