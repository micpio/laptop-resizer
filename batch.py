#process a batch of image files by specified width,
#height determined by aspect ratio automatically
import glob
from PIL import Image
import os, sys
#import overide
f = os.getcwd()#+"/workbench/"
fin = f+"/tobe/"
fout = f+"/processed/"
def Batch(f):
    files = (os.listdir(fin))     # Create a list of files to process
    print(".................................")
    print("Height will be determined automatically by aspect ratio")
    new_width = int(input("enter desired width :__"))
    print(".................................")
    
    for file in files :
   
        print("lets resize some images")
        print("folder location   "+fin)
        print("Opening"+ file)
        im = Image.open(fin+file)
        if im.size >= (128,128): 
            aspect_ratio = round((im.height / im.width),2)
            new_height = round(new_width * aspect_ratio)
            sf = os.path.splitext(file)[0] #split file ext
            new = im.resize((new_width ,new_height))
            rf  = fout + "re" +sf +".jpeg"  #format for file sent to processed
            if "re" not in f:
                new.save( rf)    #save
                print(".................................")
                print("resized with new name" )
                print(rf)
                print("originnal size")
                print(im.size ) 
                print("new size")
                print(new.size)
                print(".................................")
                print("Thank You ")
                print(".................................")
                
            else:
                print("Thank You no more files available")
                print(".................................")
                  
#Batch(f)









