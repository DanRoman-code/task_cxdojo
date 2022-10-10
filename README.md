## Installation

Python must be already installed

```shell
git clone https://github.com/DanRoman-code/taxi-service
python3 -m venv venv
source venv/bin/activate (on Linux and macOS) or venv\Scripts\activate (on Windows)
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python manage.py runserver
```
## Demo

![Website Interface](demo1.PNG)

![Website Interface](demo2.PNG)