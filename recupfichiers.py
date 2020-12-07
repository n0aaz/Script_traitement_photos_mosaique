import csv
from google_drive_downloader import GoogleDriveDownloader as gdd
import gdown
import os

#gdd.download_file_from_google_drive()
os.chdir("./")
current=os.getcwd().replace('\\', '/')+'/'
entrees=[]
with open('concours.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        entrees.append(row)

for row in entrees[1:]:
    identifiant=(row[2].split('?id='))[1]
    dossier= row[1].replace(":",'-').replace("/","-")
    nom=row[-1]
    #print("dossier= ",dossier)
    #print("identifiant= ",identifiant)
    if not os.path.isdir(current+dossier):
        os.mkdir(dossier)
    if not os.path.isfile(dossier+'/'+nom+'.jpg'): # petite condition pour ne pas tout retélécharger
        gdown.download(row[2].replace("/open?","/uc?"),dossier+'/'+nom+'.jpg')
