# Procurement System using Django Rest Framework

A procurement system has been developed for a purchasing department. The intended use
of the system is to allow staff in any department to easily search for a component and view a
list of approved suppliers for that component. Purchasing staff, as administrators of the
system, maintain the list of components, and suppliers.

Currently the system allows us to store a representative name, and representative email for
each supplier - however some suppliers have multiple representatives. It handles multiple representatives and their contact information for a supplier.

## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/Paromita-Sengupta/Procurement_System.git
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd procurement_system
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/admin
    ```




