
base_dir = '/mnt/jupiter-beta/robot_car/';

video_dir = [base_dir,'videos/'];
if ~isdir(video_dir)
    mkdir(video_dir)
end
rgb_dir = [base_dir,'rgb-images/'];
if ~isdir(rgb_dir)
    mkdir(rgb_dir)
end
fid = fopen('conversion_log.txt','w');

list = dir(rgb_dir);
list = sort({list.name});
fprintf('\n\n%d videos to convert\n\n',length(list));
for l = 3 : length(list)
    
    name = list{l};
    if name(1) == '.'
        continue;
    end
    
    src_dir = [rgb_dir,name,'/'];
    
    if ~isdir(src_dir)
        mkdir(src_dir)
    end
    
    dirname = [src_dir,'*.png'];
    imglist_rgb = dir(dirname);
    imglist_rgb = sort({imglist_rgb.name});
    
    if length(imglist_rgb)>3
        temp_dir = [base_dir,'temp_rgb_images/'];
        if ~isdir(temp_dir)
            mkdir(temp_dir)
        end
        fprintf('Converting %s to video id=%d\n', name,l);
        fprintf(fid, 'Converting %s to video id=%d\n', name,l);
        for f = 1 : length(imglist_rgb)
            in_img = [src_dir, imglist_rgb{f}];
            out_img = sprintf('%simg%012d.png',temp_dir,f);
            cmd = sprintf('cp %s %s', in_img, out_img);
            [~,~] = system(cmd);
        end
        fprintf('Transfer Done, now converting\n');
        videoname = sprintf('%s%s.mp4', video_dir, name);
        cmd = ['ffmpeg -r 12 -i ',temp_dir,'img%012d.png ',videoname];
        [~,~] =	system(cmd);
        
        fprintf('Converted and stored ::> %s\n\n', videoname)
        new_tmp = [base_dir,'temp_out_rgb_images/'];
        if ~isdir(new_tmp)
            mkdir(new_tmp)
        end
        cmd = ['ffmpeg -i ',videoname,' -r 12 ', new_tmp,'img%012d.png'];
        [~,~] = system(cmd);
        num_rgb = length(dir(temp_dir));
        num_ext = length(dir(new_tmp));
        fprintf('Orginal number of images %d and extracted %d', num_rgb, num_ext);
        fprintf(fid,'Orginal number of images %d and extracted %d\n', num_rgb, num_ext);
        [~,~] = system(['rm -rf ', temp_dir]);
        [~,~] = system(['rm -rf ', new_tmp]);
    end
    
end
