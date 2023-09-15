#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 17:57:31 2023

@author: Marina
"""


#%% 

from pdf2image import convert_from_path
import os


a = 2
print(a+222)

# check current directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)

# Set a new working directory
new_directory = "/Users/Marina/AMAYA_UBUNTU/githubpages1/maluque.github.io/images/gallery_picsPDF"
os.chdir(new_directory)

# update the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)


# Output directory for JPG images
input_dir = "/Users/Marina/AMAYA_UBUNTU/githubpages1/maluque.github.io/images/gallery_picsPDF"
output_dir =  "/Users/Marina/AMAYA_UBUNTU/githubpages1/maluque.github.io/images/gallery_picsJPG"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get a list of all files and directories in the specified directory
contents = os.listdir(current_directory)

# Print the list of contents
print(contents)


# Path to your PDF file
pdf_file = 'piecharts.pdf'

# Convert PDF to JPG
images = convert_from_path(pdf_file, dpi=150)  # Adjust dpi for desired quality

# Save the JPG images
for i, image in enumerate(images):
    image.save(os.path.join(output_dir, f'page_{i + 1}.jpg'), 'JPEG')

print('PDF converted to JPG images in the output directory.')

#%% 

from pdf2image import convert_from_path
import os
from PIL import Image

# Output directory for JPG images
input_dir = "/Users/Marina/AMAYA_UBUNTU/githubpages1/maluque.github.io/images/gallery_picsPDF"
output_dir =  "/Users/Marina/AMAYA_UBUNTU/githubpages1/maluque.github.io/images/gallery_picsJPG"


# Set the desired compression level (1-95)
compression_quality = 50  # Adjust this value as needed

# filename="dotplot1.jpg"
# input_path = os.path.join(input_dir, filename)
# print(input_path)
# output_path = os.path.join(output_dir, filename)
# print(output_path)
# img = Image.open(input_path)
# # Save the image with compression
# img.save(output_path, 'JPEG', quality=compression_quality)



compression_quality = 80  # Adjust this value as needed

# Iterate through files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.pdf'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        filename2=filename.replace(".pdf", ".jpg")
        output_path2 = os.path.join(output_dir, filename2)
        
        images = convert_from_path(input_path, dpi=100)  # Adjust dpi for desired quality

        for i, img in enumerate(images):
            img.save(output_path2, 'JPEG', quality=compression_quality)


print('Compression complete.')





# Set a new working directory
new_directory = "/Users/Marina/AMAYA_UBUNTU/githubpages1/maluque.github.io/images/gallery_picsJPG"
os.chdir(new_directory)


for filename in os.listdir(output_dir):
        if filename.endswith('.jpg'):
            image = Image.open(os.path.join(output_dir, filename))
            # Calculate the new dimensions
            width, height = image.size
            
            percentage_reduction = 30000//width
            
            new_width = int((width * percentage_reduction) / 100)
            new_height = int((height * percentage_reduction) / 100)
            #print(new_width, new_height)

            # Resize the image proportionally
            image.thumbnail((new_width, new_height))
            
            # Save the resized image
            image.save("THUMB_" + filename)
            
            # Close the image
            image.close()








    