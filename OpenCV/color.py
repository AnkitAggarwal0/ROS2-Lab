#!/usr/bin/env python
# coding: utf-8

# In[38]:


import cv2
print(cv2.__version__)


# In[39]:


import cv2
import numpy as np


# In[71]:


image=cv2.imread('C:/Users/MAHE/Documents/OpenCV_200929036/GS.png')
cv2.imshow("image", image)
cv2.waitKey(0) 
cv2.destroyAllWindows()


# In[72]:


scale_percent = 100
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
print(dim) 


# In[73]:


# resize image
img = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("image", img)
cv2.waitKey(0) 
cv2.destroyAllWindows()


# In[74]:


def mouse(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        h=hsv[y,x,0]
        s=hsv[y,x,1]
        v=hsv[y,x,2]
        print("H:",h)
        print("S:",s)
        print("V:",v)


# In[75]:


cv2.namedWindow('mouse')
cv2.setMouseCallback('mouse',mouse)
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("mouse", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[76]:


blueLower=(100,180,245)
blueUpper=(110,220,255)
greenLower=(64,60,190)
greenUpper=(74,70,210)
whiteLower=(0,0,245)
whiteUpper=(10,10,255)


# In[77]:


refPt=[(width//2-25, height//2-25),(width//2+25, height//2+25)]
roi = img[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[78]:


hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
havg= np.average(hsv, axis=0)
h_avg = np.average(havg, axis=0)
print(h_avg)


# In[79]:


if (h_avg[0]>=np.array(blueLower[0])) and (h_avg[0]<=np.array(blueUpper[0])) and (h_avg[1]>=np.array(blueLower[1])) and (h_avg[1]<=np.array(blueUpper[1])) and (h_avg[2]>=np.array(blueLower[2])) and (h_avg[2]<=np.array(blueUpper[2])):
    print("Color is Blue")
elif (h_avg[0]>=np.array(greenLower[0])) and (h_avg[0]<=np.array(greenUpper[0])) and (h_avg[1]>=np.array(greenLower[1])) and (h_avg[1]<=np.array(greenUpper[1])) and (h_avg[2]>=np.array(greenLower[2])) and (h_avg[2]<=np.array(greenUpper[2])):
    print("Color is Green")
elif (h_avg[0]>=np.array(whiteLower[0])) and (h_avg[0]<=np.array(whiteUpper[0])) and (h_avg[1]>=np.array(whiteLower[1])) and (h_avg[1]<=np.array(whiteUpper[1])) and (h_avg[2]>=np.array(whiteLower[2])) and (h_avg[2]<=np.array(whiteUpper[2])):
    print("Color is White")    
else:
    print("Color is not Blue, Green or White.")


# In[ ]:




