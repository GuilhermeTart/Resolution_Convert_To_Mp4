import subprocess
from colors import colors

print(f"""{colors.red}
          


   ______                           __     __                             __ __
  / ____/___  ____ _   _____  _____/ /_   / /_____       ____ ___  ____  / // /
 / /   / __ \/ __ \ | / / _ \/ ___/ __/  / __/ __ \     / __ `__ \/ __ \/ // /_
/ /___/ /_/ / / / / |/ /  __/ /  / /_   / /_/ /_/ /    / / / / / / /_/ /__  __/
\____/\____/_/ /_/|___/\___/_/   \__/   \__/\____/    /_/ /_/ /_/ .___/  /_/   
                                                               /_/             


        
        
        
        
 {colors.reset}""")







path_movie = input(f'{colors.green}Insert the path video: {colors.reset} ')
resolution = input(f'{colors.green}Insert the resolution: {colors.reset} ')
name_movie = input(f'{colors.green}Enter the name of video:  {colors.reset}')



def convert_to_mp4():
    Command = f"ffmpeg -i {path_movie} -vf scale={resolution} {name_movie}"

    subprocess.run(Command,shell=True)


convert_to_mp4()
