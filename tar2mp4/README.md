
## Pre-processing videos

Here we provide two Matlab scripts for pre-processing videos provided by [OxRD](https://robotcar-dataset.robots.ox.ac.uk/about/).

`extract_rgb.` is used for `demosaic`ing original binary files into `rgb` images. You can run it on full dataset after downloading. 

`convert2video.m` is used to put extracted videos in `.mp4` video format. Here we first put the `.png` images extracted by `extract_rgb.m` in to `.mp4` then re-extract them into `.png` images at fixed frame-rate of `12`. Finally, re-extracted images are put into `.mp4` video.

We provide videos with these two steps pre-performed on [Google-Drive](https://drive.google.com/drive/folders/1hCLlgRqsJBONHgwGPvVu8VWXxlyYKCq-?usp=sharing). Which is also lined in main [README](../README.md). 