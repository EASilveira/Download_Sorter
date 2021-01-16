#! python3
# moves files from downloads folder into categorized subfolders.

import shutil, os, time
arrow = ' --> '
Apps = ' Applications'
Docs = ' Docs'
Other = ' Other'
AV = ' Audio-Visual'

for files in os.walk('C:\\Users\\sg1si\\Downloads'):
    lst = files[2]
    break
for filename in lst:
    if os.path.isfile(f'C:\\Users\\sg1si\\Downloads\\{filename}'):
        if filename.endswith('.exe'):
            print(f'{filename:<50}{arrow:^5}{Apps}\n')
            shutil.move(f'C:\\Users\\sg1si\\Downloads\\{filename}', 'C:\\Users\\sg1si\\Downloads\\Applications')
        elif filename.endswith('.txt') or filename.endswith('.docx') or filename.endswith('.pdf') or filename.endswith('.pages'):
            print(f'{filename:<50}{arrow:^5}{Docs}\n')
            shutil.move(f'C:\\Users\\sg1si\\Downloads\\{filename}', 'C:\\Users\\sg1si\\Downloads\\Docs')
        elif filename.endswith('.mp3') or filename.endswith('.mp4') or filename.endswith('.avi') or filename.endswith('.jpg') or filename.endswith('.png'):
            print(f'{filename:<50}{arrow:^5}{AV}\n')
            shutil.move(f'C:\\Users\\sg1si\\Downloads\\{filename}', 'C:\\Users\\sg1si\\Downloads\\Audio-Visual')
        else:
            print(f'{filename:<50}{arrow:^5}{Other}\n')
            shutil.move(f'C:\\Users\\sg1si\\Downloads\\{filename}', 'C:\\Users\\sg1si\\Downloads\\Other')
