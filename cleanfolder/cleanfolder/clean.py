import os
from pathlib import Path
import shutil
import sys


#---------------функція----normalize-------------------------------------------------------------
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ0987654321"

TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j",
                "k", "l", "m", "n", "o", "p", "r", "s", "t", "u","f",
                "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu",
                 "ya", "je", "i", "ji", "g", "_", "_", "_", "_", "_",
                 "_", "_", "_", "_", "_", "_")

TRANS = {}
    
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(name):
    tr = name.translate(TRANS)
    tr = str(tr)
    
    return tr

#------------------------------------------------------------------------------------------------




#--функція--створення--папок--для--сортування--і--переміщення--файлів----------------------------
def move_files_to_new_folder(file, path_sort, move_to):
    
    if not os.path.exists(move_to):
        
        os.mkdir(move_to)
        shutil.move(os.path.join(path_sort, file), move_to )
    else:
        shutil.move(os.path.join(path_sort, file), move_to )
        

#----------------щлях--до--папки--яку--сортуємо--------------------------------------------------

path = Path(os.getcwd())

#------------------розширення--файлів------------------------------------------------------------

documents_suffix = ['.txt', '.doc', '.docx', '.pdf', '.xlsx', '.pptx']
audio_suffix = ['.mp3', '.ogg', '.wav', '.amr']
video_suffix = ['.avi', '.mp4', '.mov', '.mkv']
picture_suffix = ['.jpeg', '.png', '.jpg', '.svg']
archive_suffix = ['.zip', '.gz', '.tar']


#----------кінцеві--папки------------------------------------------------------------------------
documents = os.path.join(path / 'documents')
audio = os.path.join(path /'audio')
video = os.path.join(path /'video')
picture = os.path.join(path /'picture')
archive = os.path.join(path /'archive')
my_other = os.path.join(path /'my_other')

#--множина--для--зберігання--розширень-----------------------------------------------------------
ext_documents = set()
ext_audio = set()
ext_video = set()
ext_picture = set()
ext_archive = set()
ext_my_other = set()

#------------------------------------------------------------------------------------------------

folder_catalog = ['documents', 'audio', 'video', 'picture', 'archive', 'my_other']

#------------------------------------------------------------------------------------------------

def sort(path):
    
    for el in path.iterdir():
        
        if el.name in folder_catalog:
            continue

        elif el.is_dir():
           sort(el)
           handle_folder(el)
        
        else:
            
            if el.suffix in documents_suffix:
                ext_documents.add(el.suffix)
                move_files_to_new_folder(el, path, documents)
                
            
            elif el.suffix in audio_suffix:
                ext_audio.add(el.suffix)
                
                move_files_to_new_folder(el, path, audio)
            
            elif el.suffix in video_suffix:
                ext_video.add(el.suffix)
                
                move_files_to_new_folder(el, path, video)
            
            elif el.suffix in picture_suffix:
                ext_picture.add(el.suffix)
                
                move_files_to_new_folder(el, path, picture)
            
            elif el.suffix in archive_suffix:
                ext_archive.add(el.suffix)
                
                move_files_to_new_folder(el, path, archive)
                #shutil.unpack_archive(el,f'{el.parent} {el.stem}')

            else:
                ext_my_other.add(el.suffix)
                move_files_to_new_folder(el, path, my_other)
                


#-------------розпаковка--архіву-----------------------------------------------------------------
def unpack_sort_archives(archive):

    if archive:
        for file in os.listdir(archive):
            file_name = Path(file)
            shutil.unpack_archive(f'{os.path.join(archive, file)}',f'{os.path.join(archive, normalize(file_name.stem))}')

    else:
        print('You not have archives')


#---функція--видалення--пустих--папок-----------------------------------------------------------
def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Sorry, we can not delete the folder: {folder}')


#---print--info--for--file--and--extension------------------------------------------------------
def print_info(ext_suffix, folder_file_after_sort):
    folder = Path(folder_file_after_sort)

    if folder:
        print('=' *88, '\n' * 2)
        print(f'We have extension in {folder.name}: {ext_suffix}')
        print('-' * 88, '\n')
        
        for file in os.listdir(folder_file_after_sort):
            print(f'{folder.name} file: {file}')
    else:
        print(f'Not have folder with {folder_file_after_sort}')


def clean():
    sort(path)
    unpack_sort_archives(archive)
    print('\n','         INFO AFTER WORK SORT.PY   ','\n')
    print_info(ext_documents, documents)
    print_info(ext_audio, audio)
    print_info(ext_video, video)
    print_info(ext_picture, picture)
    print_info(ext_archive, archive)
    print( '\n'* 3,'      EXTENSIONS UNKNOWN TO THE SCRIPT  ','\n')
    print_info(ext_my_other, my_other)


#=======================MAIN====================================================================

if __name__ == '__main__':
        
    clean()