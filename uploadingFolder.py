import os
import dropbox
class TransferData:
    def __init__(self,access_token):
        sefl.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for route,dirs,files os.walk(file_from):
            for fileName in files:
                local_path=os.path.join(root,fileName)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                with  open(local_path,'rb')as f :
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode(overWrite))

def main():
    acces_token='5giugDah8NIAAAAAAAAAAXxxlhZrs08uncvp5ghCadzcpMJhrlUhv-azZtIfmGDe'
    transferData=TransferData(access_token)
    file_from=str(input('enter the file path to transfer'))
    file_to=input('enter the full path to upload to the dropbox')
    transferData.upload_file(file_from ,file_to)
    print('file has been moved')
main()    