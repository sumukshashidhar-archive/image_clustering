from modules.load_vars import load_env_file
from modules.get_files import get_jpg_files

# define the env file path
env_file = '.ENV'

# load the env file
env = load_env_file(env_file)

# get the list of jpg files
image_list = get_jpg_files(env['FILEPATH'])


print(len(image_list))