# YouVersionHTTPService
This is a small http API service, which gives a caller the verse of the day, that the api requests

Setup and Run Instructions:
This program is built to be run in a bash terminal and all commands will refelct this. If using a powershell terminal these commands may not work.

This program uses several python libraries. 
Command to install dependencies: 'pip install fastapi uvicorn requests pytest'

Run from main folder: YouversionHTTPService/

Command: 'uvicorn src.app:app --reload'

API available at: http://127.0.0.1:8000 or
http://localhost:8000

To Test Manually with Active API runs alter path: 

http://127.0.0.1:8000/votd?day=195&version=206

To Test: 
Run: 'pytest -q'

Decisions and Assumptions: 
- I chose the defualt verison to be the BSB. This is because of the 11 versions that are available, the Berean Standard Bible is the most popular modernized verions. ASV is the most recognized of versions avaible, but I opted not to use it as the defualt, beacause of the Elizabethian English used in it. 
- For the defualt day, I chose to use the system that runs the code as the defualt. When the file votdRouter.py is run it creates a variable that is accessible to the functions in the file, which stores the systems day of the year. The reson I chose the system's day of the year, is becasue the person running more than likey wants their verson of the day. There are problems with this, approch such is a person travels they could get the same verse of the day as defualt two days in a row. However, this way of doing the defualt verse of the day keeps a person from having the verse of the day changing at a weird time. 

Next Steps: 
- One of the first things I would want to do, is sanitize any input from a user. 

- Obvously, I would have loved to include a way to get versions.

- Rudimentury Interface, so GETs can be displayed. 

