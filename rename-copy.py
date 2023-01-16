import os
import shutil

# Set the input and output paths, and the list of allowed extensions
letter = "C"
DIR = "SILT"
input_path = "E:/soilution/january/" + DIR + "/" + letter + "-" + DIR
output_path = 'E:/soilution/january/' + DIR + '/' + DIR
allowed_extensions = ('.jpg', '.jpeg', '.png', '.webp')
# Create the output folder if it doesn't exist
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Get a list of all the files in the input directory
files = os.listdir(input_path)

# Iterate through the files and copy the images
for i, file in enumerate(files):
    # Check if the file has an allowed extension
    if file.endswith(allowed_extensions):
        # Generate the new file name using the alpha numeric format
        new_name = 'image_' + DIR + '_' + letter + '_{:03d}{}'.format(i, os.path.splitext(file)[1])

        # Get the full paths for the old and new names
        old_name = os.path.join(input_path, file)
        new_name = os.path.join(output_path, new_name)

        # Copy the file
        shutil.copy(old_name, new_name)
