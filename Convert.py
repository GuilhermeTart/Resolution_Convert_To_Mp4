import subprocess
import os
from colors import colors

print(f"""{colors.red}
          


   ______                           __     __                             __ __
  / ____/___  ____ _   _____  _____/ /_   / /_____       ____ ___  ____  / // /
 / /   / __ \/ __ \ | / / _ \/ ___/ __/  / __/ __ \     / __ `__ \/ __ \/ // /_
/ /___/ /_/ / / / / |/ /  __/ /  / /_   / /_/ /_/ /    / / / / / / /_/ /__  __/
\____/\____/_/ /_/|___/\___/_/   \__/   \__/\____/    /_/ /_/ /_/ .___/  /_/   
                                                               /_/             


        
        
        
        
 {colors.reset}""")





def convert_to_mp4():

    path_movie = input(f'{colors.green}Insert the path video: {colors.reset} ')
    resolution = input(f'{colors.green}Insert the resolution: {colors.reset} ')
    name_movie = input(f'{colors.green}Enter the name of video:  {colors.reset}')


    if not path_movie or not resolution or not name_movie:
        print('Please provide the correct data')
        return



    if not os.path.isfile(path_movie):
        print(f"Files {path_movie} does not exist.")
        return
    
 

    if not resolution.isdigit() or int (resolution) <= 0:
        print("Invalid Resolution")
        return
    
    
    Command = f"ffmpeg -i {path_movie} -vf scale={resolution} {name_movie}"

    subprocess.run(Command,shell=True)
    
convert_to_mp4()
