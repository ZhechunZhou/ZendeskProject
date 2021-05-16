# Readme

This is a Django project displaying Zendesk tickets. Due to this week is my exam week, I barely have time to work on this project, hence the resulting webpage is not polished. While, I think it still fulfills the function required and demonstrates my understanding in MVC pattern and restful Api.

### How to use

>#### Run in local
>
>1. install Django. Assume you have python3 in your machine. use **pip install django** to install it.
>2. use command **python manage.py runserver** in termianl to start the project
>3.  Open http://127.0.0.1:8000/ticket_visualization/ in your browser
>
>#### Run in server
>
>welcome to https://zhechundemo.com/ticket_visualization/ to have a look at the deployed project
>
>(I may use the domain name or other purpose or shut down the instance to save money. Please let me know if the page doesn't show what you want :) )

#### Data transformation process

>The ticket from Zendesk is store in the database. The data model is defined in models.py. The Webpage send an ajex request in every 5 seconds to the backend to. When handling such request, the backend firstly make a Api call to collect the newest ticket and update the database, then send a complex list of tickets in Json form to the front end. 

#### Technologies used

>- Ajax
>- jQuery
>- Echarts









