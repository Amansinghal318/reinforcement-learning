# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:23:03 2018

@author: dell 1
"""

#thompson sampling
#import library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import dataset
dataset=pd.read_csv('Ads_CTR_Optimisation.csv')
#implement thompson
import random
N=10000
d=10
ads_selected=[]
no_of_rewards_1=[0]*d
no_of_rewards_0=[0]*d
total_reward=0
for n in range(0,N):
      ad=0
      max_random=0
      for i in range(0,d):
        random_beta=random.betavariate(no_of_rewards_1[i]+1,no_of_rewards_0[i]+1)
        if random_beta>max_random:
                max_random=random_beta
                ad=i
      ads_selected.append(ad)
      
      reward=dataset.values[n,ad]
      if reward==1:
          no_of_rewards_1[ad]=no_of_rewards_1[ad]+1
      else:
              no_of_rewards_0[ad]=no_of_rewards_0[ad]+1
      total_reward=total_reward+reward
#visualizing the result
plt.hist(ads_selected)
plt.title('histogram of thompson ads selected')
plt.xlabel('ads')
plt.ylabel('no_of_times_each_ads_selected')
plt.show()     
        
        