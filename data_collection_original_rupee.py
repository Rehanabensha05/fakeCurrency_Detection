import os 
#Data collection 
from bing_image_downloader import downloader
#create a directory 
directory="D:\deeplearning_je\images_je"
#download image 
downloader.download("2000 indian rupee hd image",limit=100,output_dir=directory)


