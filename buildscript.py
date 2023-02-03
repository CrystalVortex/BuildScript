import os

import time

import shutil




with open('.buildscript', 'r') as file:
    for line in file:
        if 'GET(' in line:
            contents = line.split('GET(')[1].split(')')[0]
            contents = contents.strip('"')
            import wget
            print("Starting download...")
            wget.download(contents)
            print(f"Download complete @{contents}")
        if 'DIR(' in line:
            dir_ = line.split('DIR(')[1].split(')')[0]
            dir_ =  dir_.strip('""')
            print(f"Creating directory: {dir_}")
            from pathlib import Path
            Path(dir_).mkdir(parents=True,exist_ok=True)
        if 'RUN(' in line:
            run_ = line.split('RUN(')[1].split(')')[0]
            run_ =  run_.strip('""')
            print(f"Attempting to run application {run_}")
            import subprocess
            subprocess.run(run_)
        if 'ECHO(' in line:
            echo_ = line.split('ECHO(')[1].split(')')[0]
            echo_ =  echo_.strip('""')
            print(echo_)
        if 'CWD(' in line:
            cwd_ = line.split('CWD(')[1].split(')')[0]
            cwd_ =  cwd_.strip('""')
            print(f"Directory changed to {cwd_}")
            os.chdir(cwd_)
        if 'UNZIP(' in line:
            unzip_ = line.split('UNZIP(')[1].split(')')[0]
            unzip_ =  unzip_.strip('""')
            shutil.unpack_archive(unzip_)
        if 'SYSTEM(' in line:
            system_ = line.split('CWD(')[1].split(')')[0]
            system_ =  system_.strip('""')
            print("executing command: "+system_)
            os.system(system_)
