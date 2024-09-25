## list the file in the current director ##
'''
PS C:\Users\windows 10\Desktop\Git Hub\Microservices-Docker-Fastapi-Apache-kapka-Even-Driven-Architecture\Poetry>ls \


    Directory: C:\Users\windows 10\Desktop\Git Hub\Microservices-Docker-Fastapi-Apache-kapka-Even-Driven-Architecture\Poetry


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         9/25/2024   3:22 AM           5556 poetry-installation and setup.md 
'''
## Check poetry version ##
PS C:\Users\windows 10\Desktop\Git Hub\Microservices-Docker-Fastapi-Apache-kapka-Even-Driven-Architecture\Poetry> poetry --version \
Poetry (version 1.8.3)
## check the poetry virtual enviroment python version ##
PS C:\Users\windows 10\Desktop\Git Hub\Microservices-Docker-Fastapi-Apache-kapka-Even-Driven-Architecture\Poetry> poetry run python --version \
Poetry could not find a pyproject.toml file in C:\Users\windows 10\Desktop\Git Hub\Microservices-Docker-Fastapi-Apache-kapka-Even-Driven-Architecture\Poetry or its parents

## Create new project in poetry ##
PS C:\Users\windows 10\Desktop\Git Hub\Microservices-Docker-Fastapi-Apache-kapka-Even-Driven-Architecture\Poetry> poetry new project_1 \
INFO: Could not find files for the given pattern(s).
Created package project_1 in project_1

## Change directory to project 1 ##
PS C:\Users\windows 10\Desktop\Git Hub\Microservices-Docker-Fastapi-Apache-kapka-Even-Driven-Architecture\Poetry> cd project_1 \
PS C:\Users\windows 10\Desktop\Git Hub\Microservices-Docker-Fastapi-Apache-kapka-Even-Driven-Architecture\Poetry\project_1>

## Checking files lists in the current directory ##
PS C:\Users\windows 10\Desktop\Git Hub\Microservices-Docker-Fastapi-Apache-kapka-Even-Driven-Architecture\Poetry\project_1> ls \


    Directory: C:\Users\windows 10\Desktop\Git Hub\Microservices-Docker-Fastapi-Apache-kapka-Even-Driven-Architecture\Poetry\project_1


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         9/25/2024   3:56 AM                project_1
d-----         9/25/2024   3:56 AM                tests
-a----         9/25/2024   3:56 AM            276 pyproject.toml
-a----         9/25/2024   3:56 AM              0 README.md

## checking the poetry virtual enviroment python version ##
PS C:\Users\windows 10\Desktop\Git Hub\Microservices-Docker-Fastapi-Apache-kapka-Even-Driven-Architecture\Poetry\project_1> poetry run python --version \
Creating virtualenv project-1-mEEf4pgu-py3.12 in C:\Users\windows 10\AppData\Local\pypoetry\Cache\virtualenvs
Python 3.12.1

## To activate poetry virtual enviroment you must be in the file where pyproject.tomel file is present then type "Poetry Shell in cmd" ##
PS C:\Users\windows 10\Desktop\Git Hub\Microservices-Docker-Fastapi-Apache-kapka-Even-Driven-Architecture\Poetry> cd project_1 \
PS C:\Users\windows 10\Desktop\Git Hub\Microservices-Docker-Fastapi-Apache-kapka-Even-Driven-Architecture\Poetry\project_1> poetry shell \
Spawning shell within C:\Users\windows 10\AppData\Local\pypoetry\Cache\virtualenvs\project-1-mEEf4pgu-py3.12
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.   

Try the new cross-platform PowerShell https://aka.ms/pscore6

(project-1-py3.12) PS C:\Users\windows 10\Desktop\Git Hub\Microservices-Docker-Fastapi-Apache-kapka-Even-Driven-Architecture\Poetry\project_1>

## adding packages to poetry enviroments 

Hub\Microservices-Docker-Fastapi-Apache-kapka-Even-Driven-Architecture\Poetry\project_1>poetry add pandas