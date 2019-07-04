import os, sys
from azure.storage.file import FileService, ContentSettings

class Azure:
    def __init__(self, ac, key, fileshare):
        self.account_name = ac
        self.account_key = key
        self.fileshare_name = fileshare

        #Create a FileService that is used to call the File Service for the storage account
        self.file_service = FileService(account_name=ac, account_key=key)
        
        return
    
    def List_directory(self,directory_path):
        self.generator = self.file_service.list_directories_and_files(directory_path)
        print("Files in the directory: "+directory_path)
        for file_or_dir in self.generator:
            print("\t File/Directory name: " +file_or_dir.name)
        return

    
    def Download(self, loc_directory,fileshare_directory_name):
        local_path=os.path.expanduser("~/"+loc_directory)
        print("\nDownloading the following files to " + local_path)
        self.generator = self.file_service.list_directories_and_files(self.fileshare_name+"/"+fileshare_directory_name)
        for file_or_dir in self.generator:
            print("\t File/Directory name: " +file_or_dir.name)
        for file_or_dir in self.generator:
            #full_path_to_file2 = os.path.join(local_path, file_or_dir.name)
            self.file_service.get_file_to_path(self.fileshare_name, fileshare_directory_name, file_or_dir.name, local_path+file_or_dir.name)
        print("\nFiles downloaded to " + local_path)
        return
    
    def Upload(self, loc_directory,fileshare_directory_name):
        local_path=os.path.expanduser("~/"+loc_directory)
        self.generator = self.file_service.list_directories_and_files(self.fileshare_name+"/"+fileshare_directory_name)
        print("\nUploading the following files to " + fileshare_directory_name)
        entries = os.listdir(local_path)
        # for entry in entries:
        #     print(entry)
        for entry in entries:
            self.file_service.create_file_from_path(
            self.fileshare_name, #Fileshare name
            fileshare_directory_name, # We want to create this blob in the root directory, so we specify None for the directory_name
            entry,#name of the file that is created
            local_path+entry,#file that needs to be uploaded
            content_settings=ContentSettings(content_type='application/vnd.ms-excel'))
        print("The followig files have been uploaded")
        #listing the files in the fileshare_name
        obj.List_directory(fileshare_name+"/"+fileshare_directory_name_upload)


# Main method.
if __name__ == "__main__":
    storage_account_name = "ccdmigrationdata"
    storage_account_key = "w1O+O8FFnQbkaDWROQuRya/ywxUfHd+UV646C3NcEqecR6enURy52B5wWJxXCkaSwGifaELW7ErPD0SJt222Sw=="
    fileshare_name = "recurringintegrationtest"
    fileshare_directory_name_download="Inbound"
    fileshare_directory_name_upload="Outbound"
    obj = Azure(storage_account_name ,storage_account_key ,fileshare_name)

    #requirement from NGO location
    fileshare_directory_name_spec="Retail Sales Transactions"

    #Calling functions
    
    #listing the files in the fileshare_name
    obj.List_directory(fileshare_name+"/"+fileshare_directory_name_upload)
    #obj.List_directory(fileshare_name)
    
    #Download the files to the given directory
    #local_download_directory= "Work/ccd/azure_fileshare/downloaded_files/"
    #obj.Download(local_download_directory,fileshare_directory_name_download)


    #Download the files to the given directory
    #local_spec_directory= "Work/CCD/spec_files/"
    #obj.Download(local_spec_directory,fileshare_directory_name_spec)

	#Upload files in the document
    #local_upload_directory= "Work/ccd/azure_fileshare/upload_files/"
    #obj.Upload(local_upload_directory,fileshare_directory_name_upload)
