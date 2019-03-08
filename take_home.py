'''
                     .                          
                     M                          
                    dM                          
                    MMr                         
                   4MMML                  .     
                   MMMMM.                xf     
   .              "MMMMM               .MM-     
    Mh..          +MMMMMM            .MMMM      
    .MMM.         .MMMMML.          MMMMMh      
     )MMMh.        MMMMMM         MMMMMMM       
      3MMMMx.     'MMMMMMf      xnMMMMMM"       
      '*MMMMM      MMMMMM.     nMMMMMMP"        
        *MMMMMx    "MMMMM\    .MMMMMMM=         
         *MMMMMh   "MMMMM"   JMMMMMMP           
           MMMMMM   3MMMM.  dMMMMMM            .
            MMMMMM  "MMMM  .MMMMM(        .nnMP"
=..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*  
  "MMn...     'MMMMr 'MM   MMM"   .nMMMMMMM*"   
   "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""     
     ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"        
        *PMMMMMMhn. *x > M  .MMMM**""           
           ""**MMMMhx/.h/ .=*"                  
                    .3P"%....                   
                  nP"     "*MMnx      


 /$$                      /$$$$$$  /$$ /$$           /$$            
| $$                     /$$__  $$| $$|__/          | $$            
| $$  /$$$$$$   /$$$$$$ | $$  \__/| $$ /$$ /$$$$$$$ | $$   /$$      
| $$ /$$__  $$ |____  $$| $$$$    | $$| $$| $$__  $$| $$  /$$/      
| $$| $$$$$$$$  /$$$$$$$| $$_/    | $$| $$| $$  \ $$| $$$$$$/       
| $$| $$_____/ /$$__  $$| $$      | $$| $$| $$  | $$| $$_  $$       
| $$|  $$$$$$$|  $$$$$$$| $$      | $$| $$| $$  | $$| $$ \  $$      
|__/ \_/$$___/ \_______/|__/      |__/|__/|__/  |__/|__/  \__/      
      | $$                                                          
  /$$$$$$$  /$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$   /$$$$$$$        
 /$$__  $$ /$$__  $$|  $$  /$$//$$__  $$ /$$__  $$ /$$_____/        
| $$  | $$| $$$$$$$$ \  $$/$$/| $$  \ $$| $$  \ $$|  $$$$$$         
| $$  | $$| $$_____/  \  $$$/ | $$  | $$| $$  | $$ \____  $$        
|  $$$$$$$|  $$$$$$$   \  $/  |  $$$$$$/| $$$$$$$/ /$$$$$$$/        
 \_/$$___/ \_______/    \_/    \_/$$__/ | $$____/ |_______/         
  | $$                          | $$    | $$                        
 /$$$$$$    /$$$$$$   /$$$$$$$ /$$$$$$  | $$                        
|_  $$_/   /$$__  $$ /$$_____/|_  $$_/  |__/                        
  | $$    | $$$$$$$$|  $$$$$$   | $$                                
  | $$ /$$| $$_____/ \____  $$  | $$ /$$                            
  |  $$$$/|  $$$$$$$ /$$$$$$$/  |  $$$$/                            
   \___/   \_______/|_______/    \___/                              
                                                                    

This application won't work! Your challenge is to fix that.

Please connect this application to a database
and encapsulate it in such a way that you can send me a 
zip of the dir and I can have this up and running if I have

* Docker + docker-compose
* Python with the following packages:
    * Flask
    * SqlAlchemy
* VirtualEnv

installed.

How you do so is entirely up to you. I just need to be able to 
easily run it on my machine! 

You can install additional python packages (if, say, you use virtalenv) 
but I shouldn't  need to install any additional system level packages.


HINT: Here at LeafLink we use docker-compose 

Deliverable: a zip or otherwise compressed file. This file
MUST include take_home.py and it MUST include a README.MD
that will explain how to run this app so it works. It can
include as many or as little other files as you wish so long
as they do not destroy my computer.

HINT: The less I need to type to see that it works, the better

                                                                                                                                                                                                     
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  "postgresql://myuser:mypassword@db/mydb"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def hello():
    admin = User(username='admin', email='admin@example.com')
    db.session.add(admin)
    db.session.commit()
    return "It works"

db.create_all()
app.run()
