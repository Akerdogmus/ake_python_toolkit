from moviepy.editor import VideoFileClip

clip = VideoFileClip("camfitool1.mp4")
clip.write_gif("camfitool1.gif", fps=5)