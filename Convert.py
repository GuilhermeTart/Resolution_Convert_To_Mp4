import subprocess

path_movie = input('Insert the path video: ')
resolution = input('Insert the resolution: ')


Command = f"ffmpeg -i {path_movie} -vf scale={resolution} Movie_convert.mp4"

subprocess.run(Command,shell=True)
