import os, zipfile, re
from pathlib import Path

def backup_to_zip(folder):
    folder = Path(folder).resolve()
    top_dir = Path(folder.name)
    number = 1
    while True:
        zip_filename = Path(folder.name+'_'+str(number)+'.zip')
        print(zip_filename)
        if not zip_filename.exists():
            break;
        number = number + 1

    print(f'Creating {zip_filename} ...')
    skip_dirs = ['.git','.obsidian']
    with zipfile.ZipFile(folder/zip_filename,'w') as backup_zip:
        for folder_name, subfolders, filenames in os.walk(folder):
            subfolders[:] = [d for d in subfolders if d not in skip_dirs]
            folder_name = Path(folder_name)
            rel_folder = folder_name.relative_to(folder)
            print(f'Adding files in folder {folder_name}...')
            for filename in filenames:
                full_path = folder_name/filename
                if rel_folder == Path('.'):
                    cname = top_dir/filename
                else:
                    cname = top_dir /rel_folder/filename
                if filename.endswith('.md'):
                    backup_zip.write(full_path, cname)
    print('Done')

backup_to_zip('D:/github/my-wiki/')
