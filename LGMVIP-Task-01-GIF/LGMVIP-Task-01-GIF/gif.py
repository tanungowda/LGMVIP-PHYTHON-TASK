from moviepy.editor import *

images = ["image1.png", "image2.png","image3.png","image4.png","image5.png"]

clip = ImageSequenceClip(images, fps=30)  

clip.write_gif("jyo.gif")
