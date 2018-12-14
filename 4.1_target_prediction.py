#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
from subprocess import Popen, PIPE, call
lb = 'iwgsc_10_12_18'
path_target_finder = '/home/juan/Desktop/juan/bio/mrcv/sw/TargetFinder/targetfinder.pl'
target_seqs = 'data/res/DEG-cdna.csv'


# In[13]:


df = pd.read_csv('data/res/sRNA_DEG_mirbase.csv', sep='\t')
df.head()


# In[14]:


#search targets
out_file = open("data/res/targets_cdna.csv","w") 
out_total = ''
total = len(df.index)
count = 0
print(total)
for k,v in df.iterrows():  
    count += 1
    print("%i / %i" % (count, total))
    if 'N' in v.MajorRNA:
        continue
    cmd_list = ['perl', path_target_finder,'-s',v.MajorRNA,'-q',v.Gene,'-d',target_seqs,'-p','table']
    print(' '.join(cmd_list))
    pro = Popen(cmd_list, stdout=PIPE, stderr=PIPE)
    out,err = pro.communicate()
    print(out,err)
    out_total += out.decode("utf-8") 
out_file.write(out_total)
out_file.close()
#os.system('grep -v "No results for" targets.csv > targets.clean.csv')


# In[ ]:



