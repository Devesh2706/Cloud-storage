import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token= access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)


def main():
    access_token = 'FSKkYUjrSbsAAAAAAAAAAT1sN1mo9n5BcFbxJeZaQLhfUrG2iqAKnOyL_LlEysNQ'
    transferdata = TransferData(access_token)

    file_from = input("Enter the file path to transfer:")
    file_to = "/Resper/testtext.txt"

    transferdata.upload_file(file_from,file_to) 
    print("Done")

main()           