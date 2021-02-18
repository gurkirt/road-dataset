import json, pdb
import  os
import cv2
import subprocess

FONT = cv2.FONT_HERSHEY_SIMPLEX
SAVE = True


base_dir = '/mnt/mercury-alpha/aaa-av/'
videos_dir = base_dir + 'videos/'
outdir = base_dir + 'rgb-images/'


if not os.path.isdir(outdir):
    os.makedirs(outdir)

def main(vidname):

    base_name = vidname.split('.mp4')[0]
    video_file = videos_dir + vidname

    images_dir = outdir+base_name
    
    if not os.path.isdir(images_dir):
        os.makedirs(images_dir)

    imglist = os.listdir(images_dir)
    imglist = [img for img in imglist if img.endswith('.jpg')]

    if len(imglist)<10: # very few or no frames try extracting again
        command = 'ffmpeg -loglevel panic -i {} -q:v 1 {}/%08d.jpg'.format(video_file, images_dir) # extract at very good quality of 1
        print('run', command)
        os.system(command)
    
    imglist = os.listdir(images_dir)
    imglist = [img for img in imglist if img.endswith('.jpg')]
    
    return len(imglist)
    


if __name__ == '__main__':
    videofiles = os.listdir(videos_dir)
    videofiles = [af for af in videofiles if af.endswith('.mp4')]
    
    print('NUMBER OF VIDEO FILES are:::>', len(videofiles))
    for videofile in sorted(videofiles):
            print('\n annofile ', videofile, '\n')
            main(videofile)

