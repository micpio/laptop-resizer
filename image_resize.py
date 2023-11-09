#!/usr/bin/env python
# coding: utf-8

# In[66]:


import os
cwd = os.getcwd()
print(cwd)

import glob
from PIL import Image
import os, sys

fi = os.getcwd()+"/processed/"
print(fi)
def ProcessOne(f):
    files = (os.listdir(fi))
    # Create a list of files to process
    files = [f for f in glob.glob("*.jpeg")]
    print("......................................................................")
    new_width = int(input("enter width desired"))
    print("......................................................................")
    for f in files:
            print("lets resize some images")
            print(f'Opening {f}')
            im = Image.open(f)
            if im.size >= (50,50): #process files that meet ext creds
                                     #minimum size to begin 300x300
                aspect_ratio = round((im.height / im.width),2)
                print("......................................................................")
                print("aspect ratio")
                print(aspect_ratio)
                print("......................................................................")
                new_height = round(new_width * aspect_ratio)
                new = im.resize((new_width, new_height))
                rf  =fi+ "re"+f #format for file sent to processed
                if "re" not in f:
                    print("......................................................................")
                    new.save( rf)    #save
                    print(f)
                    print("originnal size")
                    print(im.size ) 
                    print("......................................................................")
                    print("resized with new name" )
                    print(rf)
                    print("new size")
                    print(new.size)
                    print("......................................................................")
                    print("Thank You ")
                    print("......................................................................")                
                else:
                    print("Thank You no more files available")
                    print("......................................................................")
                    
#if __name__ == '__main__':
                


ProcessOne(fi)


# In[ ]:





# In[ ]:




