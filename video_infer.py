from sklearn import pipeline
from pipeline import VideoStableDiffusion

models_path = './models'
output_path = './outputs'

pipe = VideoStableDiffusion(models_path=models_path, output_path=output_path) 

prompt = "A beautiful painting of street and people, spring festival"
move = {'x': 0.5, 'y':0, 'z':0} 
num_images = 50 

pipe(prompt, move=move, num_images=num_images)
