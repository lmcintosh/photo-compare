import os
import datetime
import tkFileDialog

root = os.path.expanduser("~/")
new_path = tkFileDialog.askdirectory(initialdir=root, title='Please select a directory')

print('Analyzing folder %s' %(new_path))

# allowable image extensions
img_exts = ['png', 'PNG', 'jpg', 'JPG']

# get all photos in directories and subdirectories of new_path
img_names = []
for (dirpath, dirnames, filenames) in os.walk(new_path):
    img_names.extend([f for f in filenames if f[-3:] in img_exts])

