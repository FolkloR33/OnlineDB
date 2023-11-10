import os
from tqdm import tqdm

def replace_text_in_html(file_path, old_text, new_text):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remplace l'ancien texte par le nouveau texte dans le contenu
    modified_content = content.replace(old_text, new_text)

    # Écrit le contenu modifié dans le fichier
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

def process_html_files(directory, old_file_path, new_file_path):
    # Lit les anciens et nouveaux textes depuis les fichiers
    with open(old_file_path, 'r', encoding='utf-8') as old_file:
        old_text = old_file.read()

    with open(new_file_path, 'r', encoding='utf-8') as new_file:
        new_text = new_file.read()

    # Obtient la liste de tous les fichiers HTML dans le répertoire et ses sous-répertoires
    html_files = find_html_files(directory)
    total_files = len(html_files)

    # Initialise la barre de progression
    progress_bar = tqdm(total=total_files, desc='Progress', unit='file')

    # Parcours tous les fichiers HTML
    for file_path in html_files:
        replace_text_in_html(file_path, old_text, new_text)
        # Met à jour la barre de progression
        progress_bar.update(1)

    # Ferme la barre de progression
    progress_bar.close()

def find_html_files(directory):
    html_files = []
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.html'):
                html_files.append(os.path.join(foldername, filename))
    return html_files

if __name__ == "__main__":
    root_directory = "Z:/OnlineDB/fr/"
    old_file_path = "Z:/OnlineDB/fr/old_file.html"
    new_file_path = "Z:/OnlineDB/fr/new_file.html"

    process_html_files(root_directory, old_file_path, new_file_path)

    print("La modification a été effectuée avec succès.")
