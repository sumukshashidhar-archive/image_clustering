from modules.load_vars import load_env_file
from modules.get_files import get_jpg_files
from modules.no_data_image_removal import check_nodata_image
from time import perf_counter
from tqdm import tqdm
from os import rename
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures


def build_image_full_path(image):
    return env['FILEPATH'] + '/' + image


# define the env file path
env_file = '.ENV'

# load the env file
env = load_env_file(env_file)

# get the list of jpg files
image_list = get_jpg_files(env['FILEPATH'])

# start the timer
start = perf_counter()

# Define the number of workers
num_workers = 8  # or the number of CPU cores you want to use

# loop through the list of JPG files, and check if they are nodata images
dataless_images = set()
with ThreadPoolExecutor(max_workers=num_workers) as executor:
    # Submit tasks to the executor
    futures = {executor.submit(check_nodata_image, build_image_full_path(image)): image for image in image_list}

    # Iterate through the completed tasks and update the dataless_images set
    for future in tqdm(concurrent.futures.as_completed(futures), total=len(image_list)):
        image = futures[future]
        if future.result():
            dataless_images.add(image)

# end the timer
end = perf_counter()

# print the time taken
print(f'Time taken: {end - start} seconds')

# print the number of nodata images
print(f'Number of nodata images: {len(dataless_images)}')

# move the nodata images to a new directory
for image in dataless_images:
    rename(env['FILEPATH'] + '/' + image, env['FILEPATH'] + '/final/' + image)
