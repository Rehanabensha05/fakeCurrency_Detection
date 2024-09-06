import os 
#library for data augmentation
from tensorflow.keras.preprocessing.image import ImageDataGenerator,img_to_array,array_to_img,load_img
#augmentation
data=ImageDataGenerator(rotation_range=40,width_shift_range=0.2,height_shift_range=0.2,shear_range=0.2,zoom_range=0.2,horizontal_flip=True,fill_mode='nearest')
img=load_img(r"D:\deeplearning_je\images_je\fake indian currency notes\fun fake indian currency notes\Image_61.jpg")
y=img_to_array(img)
y=y.reshape((1,)+ y.shape)
i=0
for batch in data.flow(y,batch_size=10,save_to_dir = r'D:\deeplearning_je\images_je\fake indian currency notes',save_prefix='currencyfake',save_format='jpg'):
    i+=1
    if i>20:
        break