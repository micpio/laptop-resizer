#process a batch of image files by specified width,
#specified height user must be aware of distorttions
import glob
from PIL import Image
import os, sys
#import overide
f = os.getcwd()#+"/workbench/"
fin = f+"/tobe/"
fout = f+"/processed/"
def Overide(f):
    files = (os.listdir(fin))     # Create a list of files to process
    
    new_width = int(input("enter desired width :__"))
    new_height = int(input("enter desired heigh:__"))
    print(".................................")
    for file in files:
            print("lets resize some images")
            print("folder location   "+fin)
            print("Opening"+ file)
            im = Image.open(fin+file)
            if im.size >= (128,128): #process files that meet ext creds
                aspect_ratio = round((im.height / im.width),2)
                print(".................................")
                print("aspect ratio")
                print(aspect_ratio)
                print(".................................")
                sf = os.path.splitext(file)[0] #split file ext
                new = im.resize((new_width ,new_height))
                rf  = fout + "re" +sf +".jpeg"  #format for file sent to processed
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
           
#Overide(f)


