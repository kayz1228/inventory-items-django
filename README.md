# Inventory-items-django <br />

This is a web application for **Shopify Backend Developer Intern Challenge - Summer 2022**. <br />
I use **Django** to complete CRUD functionality. Additional functionality I choose is - Pushing a button export product data to a CSV. <br />
<br />
## How to Run? <br />
I use macOS, so the instructions will be UNIX based. <br />
1. Activate virtual environment. After pulling the repo, <br />
```
source venv/bin/activate
```
2. Go to webapps: 
```
cd webapps
```
3.
```
python manage.py makemigrations inventory 
python manage.py migrate
python manage.py rumserver
```
4. Open browser (prefer chrome or FireFox) and enter the address: <br />
http://localhost:8000 <br />
<br />
You could browse this webapp now. <br />
<br />
**Note:** It could be possible that the given virtual environment is not working. You could create a new virtual environment(or run locally, the you would change every 'python' to 'python3' when prompting). <br />
1.1 Install python3 from https://python.org <br />
1.2 Choose a location in which to create the virtual environment. Let's call it "venv".
```
python3 -m venv my_env <br />
```
1.3 On MAC/Unix: <br />
```
source my_env/bin/activate <br />
```
On Windows: <br />
```
my_env\Scripts\activate.bat <br />
```
1.4 Upgrade pip to the most current versions <br />
```
pip install –-upgrade pip <br />
```
Install Django <br />
```
pip install django <br />
```
1.5 Do steps from 2 - 4. <br />
