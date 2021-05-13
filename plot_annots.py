"""
Author: Gurkirt Singh
Date: 12-05-2021

The purpose of this script is to plot annotation or ROAD dataset.

"""

import json, pdb, argparse
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cm as cmx
import matplotlib.colors as colors
from PIL import Image
import numpy as np
import os

def filter_labels(ids, all_labels, used_labels):
    """Filter the used ids"""
    used_ids = []
    for id in ids:
        label = all_labels[id]
        if label in used_labels:
            used_ids.append(used_labels.index(label))
    
    return used_ids

def main(video_name, final_annots, input_images_dir, output_images_dir=None):

    ## we are only going to show agent classes on the box but other can be print
    ## in place of agent replace it with either of ['agent', 'action', 'location', 'duplex', 'triplet']
    ## these label types can be access through a list given in final_annots['label_types']
    label_types = ['agent', 'action'] # or = final_annots['label_types']
    # cmaps = 
    if input_images_dir is None:
        output_images_dir = '../../road-plotted-images/'
    video_plot_dir = os.path.join(output_images_dir, video_name)
    
    if not os.path.isdir(video_plot_dir):
        os.makedirs(video_plot_dir)

    max_colors = 30
    cNorm  = colors.Normalize(vmin=0, vmax=max_colors)
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap='rainbow')
    tube_uids = {}
    database = final_annots['db'][video_name]
    frames = database['frames']
    frame_nums = [int(f) for f in frames.keys()]
    for frame_num in sorted(frame_nums): #loop from first frame to last
        # frame_num += 5
        if frame_num>=100000:
            break
        frame_id = str(frame_num)
        img_path = input_images_dir + '/{:s}/{:05d}.jpg'.format(video_name, frame_num)
        frame = Image.open(img_path)
        # Create figure and axes
        fig, ax = plt.subplots()
        # Display the image
        ax.imshow(frame)
        w, h = frame.size
        # check if frame is annotated
        if frame_id in frames.keys() and frames[frame_id]['annotated']>0:
            frame_annos = frames[frame_id]['annos']
            for key in frame_annos:
                anno = frame_annos[key]
                box = anno['box']
                box[0] *= w; box[1] *= h; box[2] *= w; box[3] *= h
                labels = []
                
                for idx, label_type in enumerate(label_types):
                    ## Get ids for only the classesbeing used 
                    filtered_ids = filter_labels(anno[label_type+'_ids'], final_annots['all_'+label_type+'_labels'], final_annots[label_type+'_labels'])   
                    classes = final_annots[label_type+'_labels'] ## classes that are being currently used 
                    # all_classes = final_annots['all_'+'agent'+'_labels'] ## All classes of this label type that are annotated
                    for fid in filtered_ids:
                        labels.append(classes[fid])
                # print(anno.keys(), box, labels)
                # Create a Rectangle patch
                x, y = box[0], box[1]
                tube_uid = anno['tube_uid']
                if tube_uid not in tube_uids:
                    tube_uids[tube_uid] = int(np.random.random()*max_colors-0.1)

                colorVal = scalarMap.to_rgba(tube_uids[tube_uid])
                rect = patches.Rectangle((box[0], box[1]), box[2]-box[0], box[3]-box[1], linewidth=1.65, edgecolor=colorVal, facecolor='none')
                # Add the patch to the Axes
                ax.add_patch(rect)
                offf = 31
                offset = offf*(len(labels))+3
                for label in labels:
                    offset -= offf
                    ax.text(x,(y-offset), label, color=colorVal, fontsize=11)
                    # offset -= offf
                
        out_image = video_plot_dir + '/{:05d}.jpg'.format(frame_num)
        # plt.show()
        fig.savefig(out_image)
        plt.close('all')

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='extract frame from videos')
    p.add_argument('data_dir', type=str,
                   help='Video directory where videos are saved.')
    args = p.parse_args()
    input_images_dir = os.path.join(args.data_dir, 'rgb-images')
    video_dirs = os.listdir(input_images_dir)
    video_dirs = [af for af in video_dirs if len(af)>3]
    # output_images_dir = os.path.join(args.data_dir, 'plotted-images')
    output_images_dir = os.path.join('plotted-images')
    print('NUMBER OF VIDEO FILES are:::>', len(video_dirs))

    ## read train and val annotations
    anno_file  = os.path.join(args.data_dir, 'road_trainval_v1.0.json')
    with open(anno_file,'r') as fff:
        final_annots = json.load(fff)

    for video_name in video_dirs:
            print(' Plotting for', video_name, '\n\n')
            main(video_name, final_annots, input_images_dir, output_images_dir)

