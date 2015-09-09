import os
import datetime
import tkFileDialog
from matplotlib.pyplot import imshow, show
import numpy as np
from scipy import misc

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

# get the time each image was created, and determine group membership
img_times = []
group = []
group_id = 0
for img in img_names:
    img_times.append(datetime.datetime.fromtimestamp(os.path.getctime(img)))
    if not group:
        group.extend([group_id])
    elif img_times[-1] - img_times[-2] <= time_threshold:
        group.extend([group_id])
    else:
        group_id += 1
        group.extend([group_id])

# Now do binary choice on each group
deletes = np.zeros((len(group),))
for g in set(group):
    indices = [i for (i,gr) in zip(np.arange(len(group)),group) if gr==g]
    if len(indices) > 1:
        choice = np.random.choice(indices, 2)

        ims = []
        ims.append(misc.imread(img_names[choice[0]]))
        ims.append(misc.imread(img_names[choice[1]]))
        
        h0 = imshow(ims[0])
        h1 = imshow(ims[1])
        show()

        if g > 1:
            break

