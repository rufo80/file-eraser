import os
import datetime

class FileEraser:
    def __init__(self, extension, days):
        self.extension = extension.lower()  # Estensione del file (in minuscolo)
        self.days = days  # Numero di giorni

    def remove_files(self, folder_path):
        try:
            # Ottenere la data attuale
            current_date = datetime.datetime.now()

            # Scorrere i file nella cartella
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                
                # Verificare se il file è un file e ha l'estensione specificata
                if os.path.isfile(file_path) and file_name.lower().endswith(f".{self.extension}"):
                    # Calcolare la data di creazione del file
                    creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))

                    # Calcolare la differenza tra la data attuale e la data di creazione
                    difference = current_date - creation_date

                    # Eliminare il file se è più vecchio del numero di giorni specificato
                    if difference.days > self.days:
                        os.remove(file_path)
                        print(f"File eliminato: {file_name}")
        
        except Exception as e:
            print(f"Si è verificato un errore: {str(e)}")