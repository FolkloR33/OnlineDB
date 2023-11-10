import os
from bs4 import BeautifulSoup
from tqdm import tqdm
import shutil

def replace_text_in_html(file_path, old_lines, new_lines):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    for i, line in enumerate(content):
        for old_line, new_line in zip(old_lines, new_lines):
            if old_line in line:
                content[i] = line.replace(old_line, new_line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(content)

def process_html_files(directory, old_file_path, new_file_path):
    # Copier les fichiers old et new pour éviter les modifications indésirables
    shutil.copy2(old_file_path, 'old_file_temp.html')
    shutil.copy2(new_file_path, 'new_file_temp.html')

    with open('old_file_temp.html', 'r', encoding='utf-8') as old_file:
        old_lines = old_file.readlines()

    with open('new_file_temp.html', 'r', encoding='utf-8') as new_file:
        new_lines = new_file.readlines()

    file_list = [file for file in os.listdir(directory) if file.endswith('.html')]
    
    for filename in tqdm(file_list, desc='Progress', unit='file'):
        file_path = os.path.join(directory, filename)
        replace_text_in_html(file_path, old_lines, new_lines)

    # Supprimer les fichiers temporaires
    os.remove('old_file_temp.html')
    os.remove('new_file_temp.html')

if __name__ == "__main__":
    root_directory = "Z:/"
    old_file_path = "Z:/old_file.html"
    new_file_path = "Z:/new_file.html"

    process_html_files(root_directory, old_file_path, new_file_path)

    print("La modification a été effectuée avec succès.")
