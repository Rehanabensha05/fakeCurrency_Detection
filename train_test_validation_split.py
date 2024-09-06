import os
import shutil
import tensorflow as tf
import matplotlib as plt
from sklearn.model_selection import train_test_split

# Paths
real = r'D:\deeplearning_je\images_je\real_indian rupee'
fake = r'D:\deeplearning_je\images_je\fake indian currency notes'
train = r'D:\deeplearning_je\train'
test = r'D:\deeplearning_je\test'
validation = r'D:\deeplearning_je\validation'

# Create destination directories
for path in [train, test, validation]:
    os.makedirs(os.path.join(path, 'real'), exist_ok=True)
    os.makedirs(os.path.join(path, 'fake'), exist_ok=True)

def split_and_move(src, train_dst, test_dst, val_dst):
    files = os.listdir(src)
    train_files, temp_files = train_test_split(files, test_size=0.2, random_state=42)
    val_files, test_files = train_test_split(temp_files, test_size=0.25, random_state=42)
    
    for file in train_files:
        shutil.move(os.path.join(src, file), os.path.join(train_dst, file))
    for file in val_files:
        shutil.move(os.path.join(src, file), os.path.join(val_dst, file))
    for file in test_files:
        shutil.move(os.path.join(src, file), os.path.join(test_dst, file))

split_and_move(real, os.path.join(train, 'real'), os.path.join(test, 'real'), os.path.join(validation, 'real'))
split_and_move(fake, os.path.join(train, 'fake'), os.path.join(test, 'fake'), os.path.join(validation, 'fake'))




