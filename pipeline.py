import sys, time, gc
sys.path.extend([
        'deforum-stable-diffusion/',
        'deforum-stable-diffusion/src',
    ])

import torch
import random
import clip
#from IPython import display
from types import SimpleNamespace
from helpers.save_images import get_output_folder
from helpers.settings import load_args
from helpers.render import render_animation, render_input_video, render_image_batch, render_interpolation
from helpers.model_load import make_linear_decode, load_model, get_model_output_paths
from helpers.aesthetics import load_aesthetics_model

from configuration import Root, DeforumAnimArgs, DeforumArgs 


class VideoStableDiffusion():
    def __init__(self, models_path='models', output_path='outputs'):
        root = Root() 
        root = SimpleNamespace(**root)
        root.models_path = models_path 
        root.output_path = output_path
        root.models_path, root.output_path = get_model_output_paths(root)
        root.model, root.device = load_model(root,load_on_run_all=True, check_sha256=False) 

        args_dict = DeforumArgs()
        anim_args_dict = DeforumAnimArgs()
        args = SimpleNamespace(**args_dict)
        anim_args = SimpleNamespace(**anim_args_dict)
        args.outdir = get_output_folder(root.output_path, args.batch_name)
        args.timestring = time.strftime('%Y%m%d%H%M%S')
        args.strength = max(0.0, min(1.0, args.strength)) 

        if (args.clip_scale > 0) or (args.aesthetics_scale > 0):
            root.clip_model = clip.load(args.clip_name, jit=False)[0].eval().requires_grad_(False).to(root.device)
            if (args.aesthetics_scale > 0):
                root.aesthetics_model = load_aesthetics_model(args, root)
        if args.seed == -1:
            args.seed = random.randint(0, 2**32 - 1)
        if not args.use_init:
            args.init_image = None
        if args.sampler == 'plms' and (args.use_init or anim_args.animation_mode != 'None'):
            print(f"Init images aren't supported with PLMS yet, switching to KLMS")
            args.sampler = 'klms'
        if args.sampler != 'ddim':
            args.ddim_eta = 0

        if anim_args.animation_mode == 'None':
            anim_args.max_frames = 1
        elif anim_args.animation_mode == 'Video Input':
            args.use_init = True
        
        self.root = root 
        self.args = args
        self.anim_args = anim_args

    def __call__(self, prompt, move, num_images=200): 
        prompt_dict = self.__prompt_formulation__(prompt, num_images) 
        self.__move_formulation__(move)
        render_animation(self.args, self.anim_args, prompt_dict, self.root)
        

    def __prompt_formulation__(self, prompt, num_images):
        idx = 0 
        prompt_dict = {}
        step = int(num_images/50)
        for i in range(step):
            prompt_dict[str(idx)] = prompt 
            idx += 50 
        return prompt_dict

    def __move_formulation__(self, move):
        self.anim_args.translation_x = "0:(" + str(move['x']) + ")"
        self.anim_args.translation_y = "0:(" + str(move['y']) + ")"
        self.anim_args.translation_z = "0:(" + str(move['z']) + ")"

