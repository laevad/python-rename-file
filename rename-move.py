import os

# Set the input and output paths, and the list of allowed extensions
input_path = "E:\\CROPPED\\cropped clay\\A-CLAY"
output_path = 'E:\\CROPPED\\cropped clay\\test_output'
allowed_extensions = ('.jpg', '.jpeg', '.png', '.webp')

# Get a list of all the files in the input directory
files = os.listdir(input_path)

# Iterate through the files and rename the images
for i, file in enumerate(files):
    # Check if the file has an allowed extension
    if file.endswith(allowed_extensions):
        # Generate the new file name using the alpha numeric format
        new_name = 'image_{:03d}{}'.format(i, os.path.splitext(file)[1])

        # Get the full paths for the old and new names
        old_name = os.path.join(input_path, file)
        new_name = os.path.join(output_path, new_name)

        # Rename the file
        os.rename(old_name, new_name)
