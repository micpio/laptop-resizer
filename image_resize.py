#!/usr/bin/python3
from PIL import Image
import os, sys

f = os.getcwd()
fi = f+"/tobe/"
fo = f+ "/processed/"
def ProcessOne(f):
    
    # Create a list of files to process
    files = os.listdir(fi)
    new_width = int(input("Enter width desired"))

    for file in files:
            print(f'Opening {fi}'+file)
            im = Image.open(fi + file)
            if im.size >= (250,430): #process files that meet ext creds
                                     #minimum size to begin 300x300
                aspect_ratio = round((im.height / im.width),2)
                print("aspect ratio")
                print(aspect_ratio)
            
                new_height = round(new_width * aspect_ratio)
                new = im.resize((new_width, new_height), Image.LANCZOS)
                new.save(fo + "re" +file )
                nf = fo + "re"+ file 

                print(f)
                print("originnal size")
                print(im.size ) 
                print("resized with new name")
                print(new.size)
                print(nf)
        #if __name__ == '__main__':



ProcessOne(f)


# In[ ]:





# In[ ]:




