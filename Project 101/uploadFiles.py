import os
import dropbox
from dropbox.files import WriteMode
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, fileFrom, fileTo, localPath):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(fileFrom):
            relative_path = os.path.relpath(localPath, fileFrom)
            dropbox_path = os.path.join(fileTo, relative_path)
            with open(localPath, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = "sl.BGXs69WoGBfCE3b4Ee0F-a14jiYAprSyKw9j6tcTZMLEGfgXvBKsJ5fB_vg8A-qOOH8NQg0Vcn7VI75arArlrsQh1fpeMwKBtNYMTcCrHR0ac7nKObJxvh-qHPVWoWnJZBDD5_GFV6g"
    transferData = TransferData(access_token)
    fileFrom = 'file1.txt'
    fileTo = '/Exoticc/file2.txt'
    localPath = 'C:/Users/appro/OneDrive/Desktop/Coding/Project 101'
    transferData.upload_file(fileFrom, fileTo, localPath)
    print('file upload has been successful')

main()