#!/usr/bin/python

from os import listdir
from os.path import isfile, join, basename, splitext
import csv
import os
import tifffile as tiff
import matplotlib.pyplot as plt
import sys
import glob
from PIL import Image
from subprocess import call



def convert_images(path):
    os.chdir(path)
    print '>> Converting Images to PNG...'
    for file in glob.glob("*.tif"):
        print file
        a = tiff.imread(file)
        tiff.imshow(a)
        plt.savefig(file + '_tmp.png', bbox_inches = 'tight')
        img = Image.open(file + '_tmp.png')
        img2 = img.crop((249, 13, 249+491, 13+491))
        img2.save(file + '.png')
        os.remove(file + '_tmp.png')
        # os.remove(file)
    for file in glob.glob("*.jp2"):
        print file
        call(['sh','-c','convert ' + file + ' ' + file + '_tmp.png'])
        call(['sh','-c','convert ' + file + '_tmp.png ' + file + '.tif'])
        a = tiff.imread(file + '.tif')
        tiff.imshow(a)
        plt.savefig(file + '_tmp2.png', bbox_inches = 'tight')
        img = Image.open(file + '_tmp2.png')
        img2 = img.crop((249, 13, 249+491, 13+491))
        img2.save(file + '.png')
        os.remove(file + '.tif')
        os.remove(file + '_tmp.png')
        os.remove(file + '_tmp2.png')
        # os.remove(file)


convert_images(str(sys.argv[1]))
