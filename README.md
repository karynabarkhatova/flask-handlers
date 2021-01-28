### **1.** First of all you need to clone this repository
```python3
git clone https://github.com/karynabarkhatova/flask-handlers.git
```
### **2.** Now you need to install a virtual environment
```python3
python3 -m venv virtual_env
```
### **3.** Then you need to activate your virtual environment
```python3
source virtual_env/bin/activate
```
### **4.** Install the pack of files from requirements.txt
```python3
pip install -r requirements.txt
```
### Now you can use flake8 to fix problems if they are 
```python3
flake8 main.py
```
### If there're no problems you can run a program 
```python3
python3 app.py
```
### To see the results you will need to open local host in your browser ###
```
http://127.0.0.1:5000
```
### and indicate a path which is written in parenthesses, for example: ###
```python3
@app.route('/requirements/')
```
### That's what you will have: ###
```
http://127.0.0.1:5000/requirements/
```
### NOTE: There's a part in some paths which serves as an argument for a function, for example: ###
```python3
@app.route('/generate-users/<int:XX>')
def generate_users(XX)
```
### When you are indicating a path, you will need to use any number instead of "XX" and this number will serve you as an argument to the function. ###
