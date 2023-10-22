import subprocess
import os
from colors import colors


print(f"""{colors.red}
          







                 _ _           __       _        _   _             
  /\/\   ___  __| (_) __ _    /__\ ___ | |_ __ _| |_(_) ___  _ __  
 /    \ / _ \/ _` | |/ _` |  / \/// _ \| __/ _` | __| |/ _ \| '_ \ 
/ /\/\ \  __/ (_| | | (_| | / _  \ (_) | || (_| | |_| | (_) | | | |
\/    \/\___|\__,_|_|\__,_| \/ \_/\___/ \__\__,_|\__|_|\___/|_| |_|





        
        
        
        
 {colors.reset}""")



def rota_tion():
    
    path_media = input(f"{colors.green}Informe o caminho da mídia: {colors.reset} ")
    rotation = input(f"{colors.green}Rotacionar para  [D]ireita ou [E]squerda ? : {colors.reset} ")
    name_media = input(f"{colors.green}Informe o nome de saída da mídia:  {colors.reset}")

    if rotation == 'D' :
        command = f'ffmpeg -i {path_media} -vf "transpose=1" {name_media}'
    elif rotation == 'E':
        command = f'ffmpeg -i {path_media} -vf "transpose=2" {name_media}'

    else:
        print(f"{colors.red} Saindo.. {colors.reset}")
        

    # Execute o comando
    subprocess.run(command, shell=True)

rota_tion()