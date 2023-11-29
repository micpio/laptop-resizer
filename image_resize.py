#!/usr/bin/env python

import glob
from PIL import Image
import os, sys
f = os.getcwd()#+"/workbench/"
fin = f+"/tobe/"
fout = f+"/processed/"
question = input("Hight by aspect enter y, To overide aspect enter n   ")
if question == "":
    question = input(" need answer!!! Hight by aspect enter y, to overide aspect enter n   ")
elif question == "y":
    from batch import Batch
    Batch(f)
elif question == "n":
   from overide import Overide
   Overide(f)
else:
    question = input("letters y or n only!!! height by aspect enter y to overide aspect enter n   ")
   
   







#if __name__ == '__main__':
                


# In[ ]:





# In[ ]:




