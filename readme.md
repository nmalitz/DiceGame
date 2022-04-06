# Nathan Malitz's Dice Game
## Contents
1. Download/Install VS Code
2. Download/Install Python 3.6+
3. Clone Repository
4. Create/Enter Virtual Environment
5. Download Dependencies
6. Create/Populate Database
7. Run Application
8. Working Demo Link
9. How to Play **Dice Game**

## Download/Install VSCode
Goto this [link](https://code.visualstudio.com) and follow the instructions for your machine.

## Download/Install Python 3.6+
Goto this [link](https://www.python.org/downloads/) and follow the instructions for your machine.

## Clone Repository
Clone the repository to your machine using this url https://github.com/nmalitz/DiceGame.git

## Create/Enter Virtual Environment
1. In an instance of VS Code, pointed at the project file cloned from the repository, open up a new session of Terminal.
2. Input the following command `pip3 install virtualenv`
3. Input the following command `virtualenv env`
4. Input the following command `source env/bin/activate`

## Download Dependencies
While in the virtual environment setup in the previous section, enter the following command `pip3 install flask flask-sqlalchemy`

## Create/Populate Database
1. From the project folder open an instance of Terminal in VS Code.
2. Input the following command `python3`
3. Input the following command and hit enter/return `from app import db`
4. Input the following command and hit enter/return `from app import User`
5. Input the following command and hit enter/return `db.create_all()`
6. Input the following command and hit enter/return `user1 = User(username='Nathan', score=4, previous_score=2, high_score =5)`
7. Input the following command and hit enter/return `user2 = User(username='Katelynn', score=5, previous_score=4, high_score =6)`
8. Input the following command and hit enter/return `db.session.add(user1)`
9. Input the following command and hit enter/return `db.session.add(user2)`
10. Input the following command and hit enter/return `db.session.commit()`
11. Input the following command and hit enter/return `exit()`

## Running the App
1. From the project folder open an instance of Terminal in VS Code.
2. Input the following command `python3 app.py`
3. Command-Click the url given on the line which begins 'Running on'
4. To quit the application enter the following Hotkey combination into Terminal `control-c`

## Working Demo Link
- Deployed on the free tier of Heroku.
- [Nathan Malitz's Dice Game](https://dicegame-nathanmalitz.herokuapp.com)

## How to Play **Dice Game**
1. Enter your name into the field labeled '**Name**'. All Names are case-sensitive.
2. Click the '**Roll**' button to see your score, previous score as well as highest score.
3. All of a player's scores are updated for each turn they take.
4. All players and their high scores are displayed at the bottom of the page, and update dynamically.
5. Have **fun**!