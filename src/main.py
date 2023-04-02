from modules.load_vars import load_env_file
from modules.get_files import get_jpg_files
from modules.no_data_image_removal import check_nodata_image
from time import perf_counter
from tqdm import tqdm
from os import rename
# define the env file path
env_file = '.ENV'

# load the env file
env = load_env_file(env_file)

# get the list of jpg files
image_list = get_jpg_files(env['FILEPATH'])



# start the timer
start = perf_counter()


# loop through the list of JPG files, and check if they are nodata images
dataless_images = set()
for image in tqdm(image_list):
    # check if the image is a nodata image
    if check_nodata_image(env['FILEPATH'] + '/' + image):
        # if it is, append it to the dataless_images list
        dataless_images.add(image)

# end the timer
end = perf_counter()

# print the time taken
print(f'Time taken: {end - start} seconds')


# print the number of nodata images
print(f'Number of nodata images: {len(dataless_images)}')

# move the nodata images to a new directory
for image in dataless_images:
    rename(env['FILEPATH'] + '/' + image, env['FILEPATH'] + '/nodata/' + image)