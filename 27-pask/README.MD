# Cheatsheet:
## Basics:
#### How to create virtual environment (windows)

1. Enter folder where you want to create venv.
2. Open terminal and type:
```
py -m venv venv
```
If you got red terminal:
1. Open your powershell as admin and type:
```
Set-ExecutionPolicy unrestricted
```
2. Select "Yes to all [A]"

#### How to activate virtual environment (windows)
1. Enter folder with your virtual environment (venv)
2. Open terminal and type:
```
venv\Scripts\activate
```
If you got red terminal:
1. Open your powershell as admin and type:
```
Set-ExecutionPolicy unrestricted
```
2. Select "Yes to all [A]"

#### How to create requirements.txt (file with all required libraries for project)
1. Activate venv and type:
```
pip freeze > requirements.txt
```

#### How to install all libraries from requirements.txt
1. Activate venv and type:
```
pip install -r requirements.txt
```
<hr>

## Fast api:
#### How to run development server:
1. Activate venv and type:
```
uvicorn main:app --reload
```