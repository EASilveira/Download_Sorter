#! python3
# moves files from downloads folder into categorized subfolders.

import shutil, os, time
from pathlib import Path
arrow = ' --> '
moved = 0
# Apps = ' Applications'
# Docs = ' Docs'
# Other = ' Other'
# AV = ' Audio-Visual'
# Slides = ' Slides'

fileTypes = {'00_Applications' : ['EXE'],
             '01_PythonFiles': ['PY'],
             '02_Videos': ['MP4', 'MOV'],
             '03_Pictures': ['JPG','JPEG', 'PNG', 'BMP'],
             '04_Audio': ['MP3', 'WAV'],
             '05_Documents': ['PDF', 'DOCX', 'TXT', 'XLSX', 'DOC'],
             '06_Slides' : ['PPTX'],
             '07_Other': ['ZIP']}

""" Path to Downloads Folder """
###########################################
downloadPath = f'{str(os.path.join(Path.home()))}\Downloads'
###########################################

try:
    os.chdir(downloadPath)
except FileNotFoundError:
    print(f'Path to file "{downloadPath}" not found.')
    exit()

for filename in os.listdir():
    filename = filename.upper()
    print(filename)
    moved = 0
    ### Find files and move to folder (make folder if not found)
    for folder, extensions in fileTypes.items():
        for ext in extensions:
            if filename.endswith(f'.{ext}'):
                if os.path.isdir(f'{os.getcwd()}\\{folder}'):
                    try:
                        shutil.move(f'{os.getcwd()}\\{filename.title()}', f'{os.getcwd()}\\{folder}')
                        print(f'{filename:<50}{arrow:^5}{folder}\n')
                        moved = 1
                    except shutil.Error:
                        newFilename, ext = filename.split('.')
                        newFilename = f'{new_filename.title()}_{round(time.time())}.{ext}'
                        os.rename(filename, newFilename)

                        shutil.move(f'{os.getcws()}\\{newFilename}', f'{os.getcwd()}\\{folder}')
                        print(f'{filename:<50}{arrow:^5}{folder}\n')
                        moved = 1
                else:
                    os.mkdir(folder)
                    shutil.move(f'{os.getcwd()}\\{filename.title()}', f'{os.getcwd()}\\{folder}')
                    print(f'{filename:<50}{arrow:^5}{folder}\n')
                    moved = 1

    if moved == 0 and os.path.isfile(f'{os.getcwd()}\\{filename.title()}'):
        shutil.move(f'{os.getcwd()}\\{filename.title()}', f'{os.getcwd()}\\07_Other')
        print(f'{filename:<50}{arrow:^5}07_Other\n')

print('done')



    # if os.path.isfile(f'C:\\Users\\sg1si\\Downloads\\{filename}'):
    #     if filename.endswith('.exe') or filename.endswith('.xlsx'):
    #         print(f'{filename:<50}{arrow:^5}{Apps}\n')
    #         shutil.move(f'C:\\Users\\sg1si\\Downloads\\{filename}', 'C:\\Users\\sg1si\\Downloads\\Applications')
    #     elif filename.endswith('.pptx'):
    #         print(f'{filename:<50}{arrow:^5}{Slides}\n')
    #         shutil.move(f'C:\\Users\\sg1si\\Downloads\\{filename}', 'C:\\Users\\sg1si\\Downloads\\Slides')
    #     elif filename.endswith('.txt') or filename.endswith('.docx') or filename.endswith('.pdf') or filename.endswith('.pages'):
    #         print(f'{filename:<50}{arrow:^5}{Docs}\n')
    #         shutil.move(f'C:\\Users\\sg1si\\Downloads\\{filename}', 'C:\\Users\\sg1si\\Downloads\\Docs')
    #     elif filename.endswith('.mp3') or filename.endswith('.mp4') or filename.endswith('.avi') or filename.endswith('.jpg') or filename.endswith('.png'):
    #         print(f'{filename:<50}{arrow:^5}{AV}\n')
    #         shutil.move(f'C:\\Users\\sg1si\\Downloads\\{filename}', 'C:\\Users\\sg1si\\Downloads\\Audio-Visual')
    #     else:
    #         print(f'{filename:<50}{arrow:^5}{Other}\n')
    #         shutil.move(f'C:\\Users\\sg1si\\Downloads\\{filename}', 'C:\\Users\\sg1si\\Downloads\\Other')
