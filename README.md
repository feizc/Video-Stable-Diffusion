# Video-Stable-Diffusion
Generate consistent videos with stable diffusion. 

Generally, instead of interpolation with image latents, we use depth estimation to limit the image content structure and inpainting of stable diffusion to make video keep moving.

More encouragingly, our method is compatible with [dreambooth](https://dreambooth.github.io/) or [textual inversion](https://textual-inversion.github.io/) to create a personalized video. 

* Model collection: https://huggingface.co/feizhengcong/video-stable-diffusion
* Gradio Web Demo: [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/feizhengcong/video-stable-diffusion) 
* Diffusers pipeline: [![Diffusers](https://img.shields.io/badge/%F0%9F%A4%97%20Diffusers-blue)](https://github.com/huggingface/diffusers/issues/1962)
* Personalized text-to-video generation

## 1.How it Works? 

This repository compatible with mostly environment equipped with [diffusers](https://github.com/huggingface/diffusers), and can be runned locally with pre-set ckpt.
In particular, we provide mac and linux environement that can run video generation method fluently as reference.


### 1.1 Preparation
Download the checkponit of stable diffusion and depth estimation model following [instruments](https://github.com/feizc/Video-Stable-Diffusion/tree/main/models), and put them to the path ```.\models```.

### 1.2 Running command
Run ```python video_infer.py``` to get the fancy video with corresponding hyper-parameters. 


### 1.3 Running scripts
We also provide a simple scripts to create the video.
Note that hyper-parameter 3-D coordinate corresponds the video moving direction and the value denotes the moving speed. 


```python
from pipeline import VideoStableDiffusionPipeline

models_path = './models'
output_path = './outputs'

# load model
pipe = VideoStableDiffusion(models_path=models_path, output_path=output_path) 


# run pipeline in inference
prompt = "A beautiful painting of street and people, spring festival"
move = {'x': 0.5, 'y':0, 'z':0} # move speed for 3-d direction
num_images = 50 # generated number of sequential images in video

pipe(prompt, move=move, num_images=num_images)
```

As the results contains a sequence of images, you can use the script ```video_formation.py``` to transform images to a video formation. 
Note that hyper-parameter fps is used to determine the updation ratio and we find that 20 is suitable. 


## 2.Examples

We list some generated video examples. More interesting prompts can be found in [lexica art](https://lexica.art/).

prompt: crowds in the street, celebrate china new year, spring festival, digital painting, highly detailed, masterpiece, concept art 

https://user-images.githubusercontent.com/37614046/211445726-9a8efa53-a50b-4c45-a642-e7456c952d7d.mp4

prompt: cliff, travel, highly detailed, masterpiece, beautiful painting, 4k 

https://user-images.githubusercontent.com/37614046/211446043-51dfcf54-69ae-403c-8ce9-8d92cddc971d.mp4

prompt: a portrait of a girl surrounded by delicate feathers, face, intricate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by Krenz Cushart and Artem Demura and alphonse mucha

https://user-images.githubusercontent.com/37614046/213334905-b7c0db57-ae2c-4873-9a00-b4a807bbfff9.mp4


prompt: portrait of Gypsy woman, big eyes, highly detailed, masterpiece, realistic, light

https://user-images.githubusercontent.com/37614046/211446105-e70e4523-01e3-41f1-922d-ed2d8c614900.mp4


## 3.Acknowledgements

This repository is based on [deforum-stable-diffusion](https://github.com/deforum-art/deforum-stable-diffusion), [diffusers](https://github.com/huggingface/diffusers), and [huggingface](https://github.com/huggingface/transformers), thanks for their clear code. 
