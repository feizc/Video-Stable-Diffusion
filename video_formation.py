import cv2 
import numpy as np 
import os 
from tqdm import tqdm


def write_video(video_path_out, frames_sequence): 
    if ".mp4" in video_path_out: raise ValueError("[ERROR] This method does not support .mp4; try .avi instead")
    height, width, _ = frames_sequence[0].shape
    # 0 means no preprocesing
    # 1 means  each image will be played with 1 sec delay (1fps)
    out = cv2.VideoWriter(video_path_out,0, 15,(width,height))
    for frame in frames_sequence:
        out.write(frame)
    out.release() 


num_imgs = 200
img_path = './data'
out_video = 'result.avi'


frames_sequence = []
for i in tqdm(range(num_imgs)): 
    t_path = os.path.join(img_path, f'20230107111207_{int(i):05d}.png')
    img = cv2.imread(t_path) 
    frames_sequence.append(img) 

write_video(video_path_out=out_video, frames_sequence=frames_sequence)

