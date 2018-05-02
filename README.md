# Census+

Main repository for Census+ Project. Census+ is basically obtaining all census information about an address. 'plus' means we will try to gather more open data on top of census data to gain further insights. We just focus on NSW open data at this stage. Possible use cases are market segmentation, property research, risk rating, government resource allocation and others.

## How to download and run censusplus-django.
I assume that git, pip and virtualenv have been installed in local computer.<br>
(1) Clone the repository <br>
```>git clone https://github.com/codesydney/censusplus-django.git <br>```
(2) Create virtual environment  <br>
```>cd project_directory```<br>
```>virtualenv venv```<br>
(3) Activate virtual environment <br>
```>venv\scripts\activate``` <br>
(4) Install all need package according to requirements.txt <br>
```>pip install -r requirements.txt``` <br>
(5) Run Django server <br>
```>python manage.py runserver``` <br>
(6) Quit the virtual environment after it has finished runing <br>
```>deactivate``` <br>