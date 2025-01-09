import os
from pathlib import Path

Project_Name = "Travel_Classification"
List_Of_Files = [
                    f"{Project_Name}/__init__.py",
                    f"{Project_Name}/Components/__init__.py",
                    f"{Project_Name}/Components/Data_Ingestion.py",
                    f"{Project_Name}/Components/Data_Validation.py",
                    f"{Project_Name}/Components/Data_Transformation.py",
                    f"{Project_Name}/Components/Data_Trainer.py",
                    f"{Project_Name}/Components/Data_Evaluation.py",
                    f"{Project_Name}/Components/Model_Pusher.py",
                    f"{Project_Name}/Configuration/__init__.py",
                    f"{Project_Name}/Constant/__init__.py",
                    f"{Project_Name}/Entity/__init__.py",
                    f"{Project_Name}/Entity/Config_Entity.py",
                    f"{Project_Name}/Entity/Articraft_Entity.py",
                    f"{Project_Name}/Logger/__init__.py",
                    f"{Project_Name}/Pipeline/__init__.py",
                    f"{Project_Name}/Pipeline/Training_Pipe.py",
                    f"{Project_Name}/Pipeline/Prediction.py",
                    f"{Project_Name}/Utils/__init__.py",
                    f"{Project_Name}/Utils/Main_Utils.py",
                    "App.py",
                    "Requirements.txt",
                    "Dockerfile",
                    "Demo.py",
                    "Setup.py",
                    "Config/Model.yaml",
                    "Config/Schema.yaml"
                ]

for Files in List_Of_Files:
    File_Paths = Path(Files)
    Folder, Filename = os.path.split(File_Paths)

    if Folder != "":
        os.makedirs(Folder, exist_ok=True)
    
    if (not os.path.exists(File_Paths)) or (os.path.getsize(File_Paths) == 0):
        with open(File_Paths, "w") as f:
            pass
    else:
        print("File Created Successfully")