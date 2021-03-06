# Azure FileShare using Python

## Upload/Download/List/Delete
Codes for azure fileshare integration with Python

## Pre-requisites: Python: 3.7

### For installation of packages: 
```bash
pip3 install -r requirements.txt
```
# Functions
1. Listing all the files
2. Download files from the fileshare directory
3. Upload files to the filshare directory

# Credentials required for access
1. Azure Storage account name
2. Azure Storage account key
3. Fileshare name
4. Fileshare directory names

# To list the files
Steps
1. Add the credentials between the "" in the main method of the code.
2. Under the Caling functions, there is a function call with obj.List_directory(). This functions lists all the files in the 'location: "fileshare_name/fileshare_directory_name_list"

# To Download the files
Steps
1. Add the credentials between the "" in the main method of the code.
2. In the local_download_directory="", specify the local location within the "" as the location of files to be downloaded.
3. Under the Caling functions, there is a function call with obj.Download(). This functions downloads all the files in the 'location: "fileshare_name/fileshare_directory_name_download"

# To Upload the files
Steps
1. Add the credentials between the "" in the main method of the code.
2. In the local_upload_directory="", specify the local location within the "" as the location of files to be uploaded.
3. Under the Caling functions, there is a function call with obj.Download(). This functions downloads all the files in the 'location: "fileshare_name/fileshare_directory_name_upload"

## License of this repository
[MIT](https://choosealicense.com/licenses/mit/)
