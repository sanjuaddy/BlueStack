# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:29:24 2020

@author: skadhikarla
"""
import os
import subprocess

def fileCount(folder):
#count the number of files in a directory plus directories itself

    count = 0

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)

        if os.path.isfile(path):
            count += 1
        elif os.path.isdir(path):
            count += 1

    return count

print(fileCount('D:\\testing'))

 
  
# a function to list the files in 
# the current directory and  
# parse the output. 
def list_command(args = 'l'): 
  
    # the ls command 
    cmd = 'ls'
  
    # using the Popen function to execute the 
    # command and store the result in temp. 
    # it returns a tuple that contains the  
    # data and the error if any. 
    temp = subprocess.Popen([cmd, args], stdout = subprocess.PIPE) 
      
    # we use the communicate function 
    # to fetch the output 
    output = str(temp.communicate()) 
      
    # splitting the output so that 
    # we can parse them line by line 
    output = output.split("\n") 
      
    output = output[0].split('\\') 
  
    # a variable to store the output 
    res = [] 
  
    # iterate through the output 
    # line by line 
    for line in output: 
        res.append(line) 
  
    # print the output 
    for i in range(1, len(res) - 1): 
        print(res[i]) 
  
    return res 

list_command('-al')
