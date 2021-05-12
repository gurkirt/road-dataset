import json, pdb, argparse
import cv2, os
base_dir = './'

FONT = cv2.FONT_HERSHEY_SIMPLEX

SAVE = True


def main(video_name, input_images_dir, output_images_dir):

    
    video_plot_dir = os.path.join(output_images_dir, video_name)
    
    if not os.path.isdir(video_plot_dir):
        os.makedirs(video_plot_dir)
    
    color = (0,0,255)
    color1 = (255,0,5)
    frames = db['frames']

    for f in sorted(frames.keys()):
        in_id = int(f)
        # input_image_path = '{:s}/{:05d}.png'.format(imagedir, 3*(in_id-1)+1)

        color = (0, 0, 255)
        color1 = (255, 0, 5)

        flag, frame = video_handle.retrive()
        
        for i in range(3):
            _, _ = video_handle.retrive()

        annots = frames[f]
        for anno in annots:
            width = anno['width']
            height = anno['height']
            box = anno['box']
            tags = anno['tags']

            pt = [int(box['x1']), int(box['y1']),int(box['x2']),int(box['y2'])]
            cv2.rectangle(frame, (pt[0], pt[1]), (pt[2], pt[3]), color, 2)
            offset = 0
            for tag in tags:
                cv2.putText(frame, tag, (int(pt[0]) , int(pt[1]) + offset), FONT, 1, color, 1, cv2.LINE_AA)
                offset += 21
        out_image = '{:s}/{:05d}.png'.format(outdir, in_id)
        cv2.imwrite(out_image,frame)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='extract frame from videos')
    p.add_argument('data_dir', type=str,
                   help='Video directory where videos are saved.')
    args = p.parse_args()
    input_images_dir = os.path.join(args.data_dir, 'rgb-images')
    video_dirs = os.listdir(input_images_dir)
    video_dirs = [af for af in video_dirs if len(af)>3]
    output_images_dir = os.path.join(args.data_dir, 'plotted-images')
    print('NUMBER OF VIDEO FILES are:::>', len(video_dirs))


    for video_name in video_dirs:
            print('\n\n\n\n\n annofile ', video_name, '\n\n\n\n\n\n')
            main(video_name, input_images_dir, output_images_dir)

