#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


p1 = cv2.imread('img1.jpg')
cv2.imshow("photo1", p1)
cv2.waitKey() == 13
cv2.destroyAllWindows()


# In[3]:


p2 = cv2.imread('img2.jpg')
cv2.imshow("photo2", p2)
cv2.waitKey() == 13
cv2.destroyAllWindows()


# In[4]:


p3 = cv2.imread('img3.jpg')
cv2.imshow("photo3", p3)
cv2.waitKey() == 13
cv2.destroyAllWindows()


# In[5]:


p4 = cv2.imread('img4.jpg')
cv2.imshow("photo4", p4)
cv2.waitKey() == 13
cv2.destroyAllWindows()


# In[6]:


import numpy


# In[7]:


p1.shape


# In[8]:


p2.shape


# In[9]:


p3.shape


# In[10]:


p4.shape


# In[11]:


h_photo = numpy.hstack((p1,p2))


# In[12]:


cv2.imshow("photo",h_photo)
cv2.waitKey() ==13
cv2.destroyAllWindows()


# In[13]:


v_photo = numpy.vstack((p4,p3))


# In[14]:


cv2.imshow("photo",v_photo)
cv2.waitKey() ==13
cv2.destroyAllWindows()


# In[15]:


final = numpy.concatenate((h_photo,v_photo),axis=1)


# In[16]:


cv2.imshow("photo",final)
cv2.waitKey() ==13
cv2.destroyAllWindows()


# In[ ]:




