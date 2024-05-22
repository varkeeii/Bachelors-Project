from flask import *
from database import *
from public import public
from admin import admin
from staff import staff
from customer import customer
from courier import courier


app=Flask(__name__)
app.secret_key="pryulla"

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(staff)
app.register_blueprint(customer)
app.register_blueprint(courier)

app.run(debug=True,port=5002)