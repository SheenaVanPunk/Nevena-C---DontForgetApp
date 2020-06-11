# Don't Forget App

[Testoper Codeathon](https://testoper.com/portfolio/testoper_codeathon/) - Beginner Track final project
by Nevena C.

This is a console application with 2 courses of action:
1. User is asked to authenticate through logging in or registering a new account.
   - local MySql database is queried for confirming the existing account or for recording a new one.
2. After authentication, user can choose to either see previously saved tasks or create new tasks.
   - previosly saved tasks are printed to the console
   - new tasks are recorded in database
   
   
## Login flow 
- While logging in user can repeat incorrectly entered password.
- If account doesn't exist in the database, user will be offered to register account (TODO)

## Registration flow
- After user enters the username, the program checks if it is unique. If not, user is offered to pick another username until the unique username is entered.
- After entering a password, a new account is recorded in db.

## Program Flow
![FlowChat Image](https://github.com/SheenaVanPunk/DontForgetApp/blob/master/flow%20chart/DontForgetApp%20ProgramFlow.jpg)
