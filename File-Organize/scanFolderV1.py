import os
import shutil 

isi_folder_tujuan = os.listdir("/home/hayqal/Downloads")
folder_yang_dituju = "/home/hayqal/Downloads" 



def folder(folders) : 
    for folder in folders :
        organize(folder) 
    return 'selesai proses'

def organize(name) :
    lokasi_fail_sekarang = os.path.join(folder_yang_dituju, name)
    if os.path.isdir(lokasi_fail_sekarang) : 
        return 
    
    nama, format_file = os.path.splitext(name)
    format_file = format_file.lower()
    if format_file in [".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".ico"] :
        folderBetul = "Images"

    elif format_file in [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".txt", ".rtf", ".csv"] : 
        folderBetul = "Documents"

    elif format_file in [".mp4", ".mkv", ".avi", ".mov", ".mp3", ".wav", ".flac"] : 
        folderBetul = "Media"

    elif format_file in [".zip", ".rar", ".7z", ".tar", ".gz"] : 
        folderBetul = "Archives"

    elif format_file in [".iso", ".img", ".ima", ".vmdk", ".vhd", ".vhdx", ".nrg"] : 
        folderBetul = "Iso_Disk"

    elif format_file in [".exe", ".msi", ".deb", ".rpm", ".sh", ".py", ".js", ".html", ".css"] : 
        folderBetul = "Installer-Code"

    else : 
        folderBetul = "Other"

    check_folder = os.path.join(folder_yang_dituju, folderBetul)
    os.makedirs(check_folder, exist_ok=True)
    shutil.move(lokasi_fail_sekarang, check_folder)
    print(f"file {nama} berjaya di alihkan ke {folderBetul}")

print(folder(isi_folder_tujuan))
