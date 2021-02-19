import  os
import argparse

def main(vidname, videos_dir, outdir):

    base_name = vidname.split('.mp4')[0]
    video_file = os.path.join(videos_dir, vidname)

    images_dir = os.path.join(outdir, base_name)
    
    if not os.path.isdir(images_dir):
        os.makedirs(images_dir)

    imglist = os.listdir(images_dir)
    imglist = [img for img in imglist if img.endswith('.jpg')]

    if len(imglist)<10: # very few or no frames try extracting again
        command = 'ffmpeg  -i {} -q:v 1 {}/%05d.jpg'.format(video_file, images_dir) # extract at very good quality of 1
        print('run', command)
        os.system(command)
    
    imglist = os.listdir(images_dir)
    imglist = [img for img in imglist if img.endswith('.jpg')]
    
    return len(imglist)
    


if __name__ == '__main__':

    p = argparse.ArgumentParser(description='extract frame from videos')
    p.add_argument('data_dir', type=str,
                   help='Video directory where videos are saved.')
    args = p.parse_args()
    videos_dir = os.path.join(args.data_dir, 'videos')
    videofiles = os.listdir(videos_dir)
    videofiles = [af for af in videofiles if af.endswith('.mp4')]
    images_dir = os.path.join(args.data_dir, 'rgb-images')
    print('NUMBER OF VIDEO FILES are:::>', len(videofiles))
    for i, videofile in enumerate(videofiles):
            print('\n %d videofile '%i, videofile, '\n')
            main(videofile, videos_dir, images_dir)

