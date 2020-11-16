# -*- coding: utf-8 -*-
import arcpy
import glob
import os
from arcpy import env

arcpy.CheckOutExtension('Spatial');
env.workspace = r"D:\arcclip\fpar_huanghuaihai_all";
inputfile = r"D:\arcclip\fpar_huanghuaihai_all";
mask_file = r"D:\arcclip\ceshi_shp_new_all";

tiffs = os.listdir(inputfile);
for tiff in tiffs:
        shpFiles = os.listdir(mask_file);
        for file in shpFiles:
                if file[-4:] == ".shp":
                        outputfilename = tiff[:22]+ 'fpar.' + file[:-4] + ".tif";
                        print(outputfilename)
                        mask = os.path.join(mask_file,file);
                        out_extract = arcpy.sa.ExtractByMask(tiff, mask);
                        out_extract.save(outputfilename);
