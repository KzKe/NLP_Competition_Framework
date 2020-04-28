import numpy as np
import random
import os
import torch
def seed_torch(seed=1029):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed) # if you are using multi-GPU.
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.enabled = False

seed_torch()


# confusion maxtrix 
from sklearn.metrics import confusion_matrix
import seaborn as sns
cf_matrix = confusion_matrix(t1, o1)
print(cf_matrix)
sns.heatmap(cf_matrix, annot=True)
group_names = ['True Neg','False Pos','False Neg','True Pos']
group_counts = ["{0:0.0f}".format(value) for value in
                cf_matrix.flatten()]
group_percentages = ["{0:.2%}".format(value) for value in
                     cf_matrix.flatten()/np.sum(cf_matrix)]
labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in
          zip(group_names,group_counts,group_percentages)]
labels = np.asarray(labels).reshape(2,2)
sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues')


# pandas columns not equal 
tests.loc[~(tests['sentiment'] == tests['pred'])]

# pandas show all text 
pd.set_option('display.max_colwidth', -1)

# pandas read text file 
sup_test = pd.read_csv('/content/data/imdb_unsup_train.txt',delimiter="\t")

# time difference
import datetime
a = datetime.datetime.now()
b = datetime.datetime.now()
print(b-a)


# rename columns
translated_data = translated_data.rename(columns={'back_tranlated': 'comment'})

# concate
dataset2 = pd.concat([dataset1, new_data, new_data2, new_data3], axis=0).reset_index(drop=True)


# check GPU usage 
from pynvml import *
nvmlInit()
h = nvmlDeviceGetHandleByIndex(0)
info = nvmlDeviceGetMemoryInfo(h)
print(f'total    : {info.total}')
print(f'free     : {info.free}')
print(f'used     : {info.used}')
