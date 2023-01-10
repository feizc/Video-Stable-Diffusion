# Video-Stable-Diffusion
Generate consistent videos with stable diffusion.
Instead of image latents interpolation, we use depth estimation to limit the content structure and inpainting version of stable diffusion to make video keep moving.

## 1.How to use? 

This repository compatible with mostly environment equipped with transformers, and can be runned locally with pre-set ckpt.

In particular, we provide mac and linux environement that can run our method fluently as example.


### 1.1 Preparation
Download the checkponit of stable diffusion and depth estimation model, and put them to the path: models.

### 1.2 Runing
Run infer.py to get the fancy video. 

### 1.3 Scripts
We also provide a simple scripts to create the video.

```python
from pipeline import VideoStableDiffusionPipeline, save_video

device = "cuda"
models_path = './models'

# load model
pipe = VideoStableDiffusionPipeline.from_pretrained(models_path)
pipe= pipe.to(device)

# run pipeline in inference
prompt = "A painting of a squirrel eating a burger"
move = {'x': 0.5, 'y':0, 'z':0} # move for 3-d
num_images = 50 # generated number of images in video
video = pipe([prompt], move=move, num_images=num_images)

# save video
save_video("./outputs", video)
```



## 2.Examples

We provide some generated video examples.

https://user-images.githubusercontent.com/37614046/211445726-9a8efa53-a50b-4c45-a642-e7456c952d7d.mp4


https://user-images.githubusercontent.com/37614046/211446043-51dfcf54-69ae-403c-8ce9-8d92cddc971d.mp4


https://user-images.githubusercontent.com/37614046/211446105-e70e4523-01e3-41f1-922d-ed2d8c614900.mp4

## 3.Acknowledgements

This repository is based on [deforum-stable-diffusion](https://github.com/deforum-art/deforum-stable-diffusion) and [huggingface](https://github.com/huggingface/transformers), thanks for their clear code. 
