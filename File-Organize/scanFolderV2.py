import os
import shutil 
import json
import hashlib
from datetime import datetime

#function baca config.json
def bacaConfig() : 
    with open('config.json', 'r') as file : 
        return json.load(file)

#tambah log semasa
def tulisLog(mesej) : 
    masa = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(config["log_file"] , "a") as isi : 
        isi.write(f"[{masa}] Log : {mesej}\n")

#memilih kategori folder 
def asingKategori(formatFile) : 
    formatFile = formatFile.lower() 
    for folder, formatValid in config["categories"].items() :
        if formatFile in formatValid : 
             return folder
        else : 
            continue # Redundant code dengan senagaja agar lebih mudah dibaca nanti
    return "Other"

# aisngkan yang mana perlu check sama ada duplicate atau dgn dgn check,
#   size berbeza = tak perlu check duplciate atau tak sebab sah "tidak"
def filterHash(fileBaru,folderDestinasi ) : 
    sizeFileBaru = os.path.getsize(fileBaru)
    isiFolder = os.listdir(folderDestinasi)
    for namaFile in isiFolder : 
        fullPath = os.path.join(folderDestinasi, namaFile)
        if os.path.isfile(fullPath) : 
            if sizeFileBaru != os.path.getsize(fullPath) : 
                continue
            else : 
                hashSystemBaru = hashlib.md5()
                with open(fileBaru, "rb") as fs : 
                    while True : 
                        beberapaHash = fs.read(64 * 1024)
                        if not beberapaHash : 
                            break
                        hashSystemBaru.update(beberapaHash)
                    fullHash_UntukFileBaru = hashSystemBaru.hexdigest()
                hashSystemSemasa = hashlib.md5()    
                with open(fullPath, "rb") as fb : 
                    while True : 
                        beberapaHash = fb.read(64 * 1024)
                        if not beberapaHash : 
                            break
                        hashSystemSemasa.update(beberapaHash)
                    fullHash_UntukFileSemasa = hashSystemSemasa.hexdigest()
                if fullHash_UntukFileBaru == fullHash_UntukFileSemasa :
                    return True
    return False
                





config = bacaConfig()

#ABAIKAN CODE DIBAWAH KERANA INI DARI V1. AKAN DIUBAH ,DITMABAH ,DIBUANG NANTI

    
# def folder(folders) : 
#     for folder in folders :
#         organize(folder) 
#     return 'selesai proses'

# def organize(name) :
#     lokasi_fail_sekarang = os.path.join("download_path", name)
#     if os.path.isdir(lokasi_fail_sekarang) : 
#         return 
    
#     nama, format_file = os.path.splitext(name)
#     format_file = format_file.lower()
#     for 

#     check_folder = os.path.join(folder_yang_dituju, folderBetul)
#     os.makedirs(check_folder, exist_ok=True)
#     shutil.move(lokasi_fail_sekarang, check_folder)
#     print(f"file {nama} berjaya di alihkan ke {folderBetul}")

# print(folder(isi_folder_tujuan))