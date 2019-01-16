
# coding: utf-8

# In[43]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

r = np.linspace(1,255, 15)
g = np.linspace(1,255, 15)
b = np.linspace(1,255, 15)


# In[45]:


fig = plt.figure('3D surface', figsize=(18,18))
ax = fig.add_subplot(111, projection='3d')

for i in r:
    for j in g:
        for k in b:
            rgb = [i/255, j/255, k/255]
            ax.scatter(i,j,k, s=12, c=rgb, alpha=0.55)
plt.show()

