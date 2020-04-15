import random
import pandas as pd 

class Augmentations:
  def __init__(self):
    # self.df = df 
    return  
  
  def mixup(self, df, label, txtcol, nums, aug_label, ratio=0.5):
    '''
    对训练数据进行随机的混合，生成新的数据
    '''
      if aug_label:
        # 针对某个label进行扩容
        data = df[df[label]==aug_label]
      else:
        data = df 

      gnt_text = []
      gnt_label = []

      if nums > len(data)-1:
        nums = len(data)-1

      for i in range(1, nums):
        text_pre = data.iloc[i][txtcol]
        rand_index = int(len(data) * random.random())-1
        text_latt = data.iloc[rand_index][txtcol]
        new_text = text_pre[: int(len(text_pre)*ratio)] + text_latt[-int(len(text_latt)*ratio):]
        gnt_text.append(new_text) 
        gnt_label.append(data.iloc[i][label])
      
      return pd.DataFrame.from_dict({txtcol: gnt_text,
                                      label: gnt_label})
