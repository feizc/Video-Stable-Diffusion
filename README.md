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


## 2.Examples

We provide some generated video examples.

https://user-images.githubusercontent.com/37614046/211445726-9a8efa53-a50b-4c45-a642-e7456c952d7d.mp4


https://user-images.githubusercontent.com/37614046/211446043-51dfcf54-69ae-403c-8ce9-8d92cddc971d.mp4


https://user-images.githubusercontent.com/37614046/211446105-e70e4523-01e3-41f1-922d-ed2d8c614900.mp4

## 3.Acknowledgements

This repository is based on [deforum-stable-diffusion](https://github.com/deforum-art/deforum-stable-diffusion) and [huggingface](https://github.com/huggingface/transformers), thanks for their clear code. 
