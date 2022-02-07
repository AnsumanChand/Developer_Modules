import os
import shutil

##### This is a Demo !!

def make_folder(path):
    os.makedirs(path)

class FolderMaker():
    
    def __init__(self,root_location,folder_name):
        self.folder_name =  folder_name
        self.folder_location = root_location
        self.sub_folder = ["Data","Codes","Models","Results"]
    
        
    def create_folder(self):
        self.full_path = os.path.join(self.folder_location,self.folder_name)
        if os.path.exists(self.full_path):
            print(" {} folder already exists".format(self.folder_name))
        else:
            make_folder(self.full_path)
    
    def create_project(self):
        
        for subf in self.sub_folder:
            full_project_path = os.path.join(self.folder_location,self.folder_name,subf)
            if os.path.exists(full_project_path):
                print(" {} {} folder already exists".format(self.folder_name,subf))
            else:
                make_folder(full_project_path)


                