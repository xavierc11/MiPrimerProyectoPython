from datetime import datetime


def get_current_date():
    current_date = datetime.now()
    return current_date

def save_file(path_file):
    print("Archivo guardado!.")

def encrypt_text(text):
    print("Texto encriptado!.")