import os
import datetime
import tkFileDialog

# Ask user for which directory to run on
root = os.path.expanduser("~/Dropbox/")
new_path = tkFileDialog.askdirectory(initialdir=root, title='Please select a directory')
print('Analyzing folder %s' %(new_path))

# thresholds for similar images
time_threshold = datetime.timedelta(0.0, 10.0) # seconds

# allowable image extensions
img_exts = ['png', 'PNG', 'jpg', 'JPG']

# get all photos in directories and subdirectories of new_path
img_names = []
for (dirpath, dirnames, filenames) in os.walk(new_path):
    img_names.extend([new_path + '/' + f for f in filenames if f[-3:] in img_exts])

# get the time each image was created
img_times = []
for img in img_names:
    img_times.append(datetime.datetime.fromtimestamp(os.path.getctime(img)))



