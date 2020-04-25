import moviepy.editor
import os
f_path='C:\\ML\\Testing\\'
for filename in os.listdir(f_path):
    if filename.endswith('.mp4'):
        video_clip = moviepy.editor.VideoFileClip(f_path+filename)
        audio = moviepy.editor.AudioFileClip(f_path+filename[0:len(filename)-4]+'.mp3')
        audio_clip = moviepy.editor.CompositeAudioClip([audio])
        video_clip.audio = audio_clip
        video_clip.write_videofile(f_path+filename[0:len(filename)-4]+'_new.mp4')
        video_clip.reader.close()
