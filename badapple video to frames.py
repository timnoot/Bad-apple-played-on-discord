from moviepy.editor import *

clip = VideoFileClip('frames/badapple.mp4')
clip = clip.set_fps(10)
clip.write_images_sequence(f"frames/frame%d.png", fps=10)
