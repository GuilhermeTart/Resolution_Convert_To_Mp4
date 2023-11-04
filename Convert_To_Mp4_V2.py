import subprocess
import os
import re #Verifica expressões regulares
import sys #Para usar o argv
from colors import colors

print(f"""{colors.red}
   ______                           __     __                             __ __
  / ____/___  ____ _   _____  _____/ /_   / /_____       ____ ___  ____  / // /
 / /   / __ \/ __ \ | / / _ \/ ___/ __/  / __/ __ \     / __ `__ \/ __ \/ // /_
/ /___/ /_/ / / / / |/ /  __/ /  / /_   / /_/ /_/ /    / / / / / / /_/ /__  __/
\____/\____/_/ /_/|___/\___/_/   \__/   \__/\____/    /_/ /_/ /_/ .___/  /_/   
                                                               /_/             
 {colors.reset}""")

def convert_to_mp4(path_movie, resolution): #pathMovie):
    if not path_movie or not resolution:
        print('Please provide the correct data')
        return

#Padrão expressão regular,  ^ inicio  /d+ um ou + digitos X caractere literal  
 #$ Especifica que o padrão deve terminar no final da string.
    if not re.match(r'^\d+x\d+$', resolution): 
        print("Invalid Resolution")
        return

    if path_movie == "all":
        path_movie = os.getcwd() # os.getcwd() Usa o diretório  atual como o path dos vídeos
        counter = 1
        for file in os.listdir(path_movie):
            if file.endswith(".mp4"):
                name_movie = f"convert_{counter}.mp4"
                Command = f"ffmpeg -i {file} -vf scale={resolution} {name_movie}"
                subprocess.run(Command,shell=True)
                counter += 1
    else:
        #
        if not os.path.isfile(path_movie):
            print(f"Files {path_movie} does not exist.")
            return
        
    
        nameMovie = f"convert_{os.path.basename(path_movie)}" #Irá colocar o convert_  no output do arquivo ajustado.
        Command = f"ffmpeg -i {path_movie} -vf scale={resolution} {nameMovie}"
        subprocess.run(Command,shell=True)

if __name__ == "__main__":
    convert_to_mp4(sys.argv[1], sys.argv[2])
