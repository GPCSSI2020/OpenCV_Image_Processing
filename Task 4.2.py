#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 


# In[2]:


#read 2 images

p1 = cv2.imread('image3.jpg')
p2 = cv2.imread('img5.jpg')


# In[3]:


p1.shape


# In[4]:


p2.shape


# In[5]:


#show photo1

cv2.imshow("photo",p1)
cv2.waitKey() ==13
cv2.destroyAllWindows()


# In[6]:


#show photo2

cv2.imshow("photo",p2)
cv2.waitKey() ==13
cv2.destroyAllWindows()


# In[7]:


#cropping img1
p3 = p1[1:1024,512:1024]
cv2.imshow("photo",p3)
cv2.waitKey() ==13
cv2.destroyAllWindows()


# In[8]:


#cropping img2
p4 = p2[1:1024,1:513]
cv2.imshow("photo",p4)
cv2.waitKey() ==13
cv2.destroyAllWindows()


# In[9]:


#swap images

p5 = p1[1:1024,512:1024]
p2[1:1024,512:1024] = p5
cv2.imshow("photo",p2)
cv2.waitKey() ==13
cv2.destroyAllWindows()


# In[10]:


#crop Image and convert into Black & White

p6 = p1[1:1024,512:1024]
p6 = cv2.cvtColor(p6,cv2.COLOR_BGR2GRAY)
cv2.imshow("photo",p6)
cv2.waitKey() ==13
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




