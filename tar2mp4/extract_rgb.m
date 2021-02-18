
base_dir = '/mnt/jupiter-alpha/robot_car/';
archive_dir = [base_dir,'archives/'];

gbrg_dir = [base_dir,'temp_gbrg_images/'];
if ~isdir(gbrg_dir)
    mkdir(gbrg_dir)
end
rgb_dir = [base_dir,'rgb-images/'];
if ~isdir(rgb_dir)
    mkdir(rgb_dir)
end

dirname = [archive_dir,'/*.tar'];
list = dir(dirname);
list = sort({list.name});
fprintf('\n\n%d videos to convert\n\n',length(list));
for l = 1 : length(list)
    
    name = list{l};
    fprintf('extracting and converting id:: %03d videoname:: %s\n', l, name)
    dst_dir = [rgb_dir,name(1:end-4),'/'];
    if ~isdir(dst_dir)
        mkdir(dst_dir)
    end
    dirname = [dst_dir,'*.png'];
    imglist_rgb = dir(dirname); 
    imglist_rgb = sort({imglist_rgb.name});
    if length(imglist_rgb)<10

        if ~isdir(gbrg_dir)
            mkdir(gbrg_dir)
        end

        cmd = ['tar -xvf ', archive_dir, name,' -C ', gbrg_dir];
        [~, ~] = system(cmd);
        
        step1 = dir(gbrg_dir);
        step1 = step1(3).name;
        step2 = dir([gbrg_dir,step1]);
        
        cmd = ['mv ',gbrg_dir,step1,'/',step2(4).name, ' ',dst_dir];
        [~, ~] = system(cmd);

        step2 = step2(3).name;
        step3 = dir([gbrg_dir,step1,'/',step2]);
        step3 = step3(3).name;
        gbrg_dir_final = [gbrg_dir,step1,'/',step2,'/',step3,'/'];
        dirname = [gbrg_dir_final,'*.png'];
        imglist = dir(dirname); 
        imglist = sort({imglist.name});
        parfor f = 1 : length(imglist)
            in_img = [gbrg_dir_final,imglist{f}];
            out_img = [dst_dir,imglist{f}];
            img = imread(in_img);
            img = demosaic(img,'gbrg');
            imwrite(img,out_img)
        end
        [~,~] = system(['rm -rf ',gbrg_dir]);
    end
end
extract_rgb;

% d=dir('/mnt/jupiter-alpha/robot_car/archives/2015-02-03-19-43-11/stereo/centre');
% for i= 3: 6002
% s=strcat('/mnt/jupiter-alpha/robot_car/archives/2015-02-03-19-43-11/stereo/centre/',d(i).name);
% A=imread(s);
% A=demosaic(A,'gbrg');
% %imshow(A)
% save=strcat('/mnt/jupiter-alpha/robot_car/rgb-images/2015-02-03-19-43-11_stereo_centre_04/',d(i).name);
% imwrite(A,save)
% end
