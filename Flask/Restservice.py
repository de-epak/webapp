from flask import Flask, jsonify
import Database
from Database import Session
from Database import Car
from dataclasses import dataclass

app = Flask(__name__)

@app.route("/",methods=['GET',"POST"])
def home():
    ses = Session()    
    ses.add_all(
      [Car(Id=1, Name='Audi', Price=52642), 
        Car(Id=2, Name='Mercedes', Price=57127),
        Car(Id=3, Name='Skoda', Price=9000),
        Car(Id=4, Name='Volvo', Price=29000),
        Car(Id=5, Name='Bentley', Price=350000),
        Car(Id=6, Name='Citroen', Price=21000),
        Car(Id=7, Name='Hummer', Price=41400),
        Car(Id=8, Name='Volkswagen', Price=21600)])
    ses.commit()

    rs = ses.query(Car).all()
    for Car in rs:
        print (Car.Name, Car.Price)
    return rs
    
    
@app.route("/get_data",methods=['GET',"POST"])
def get_data():
    ses = Session()
    rs = ses.query(Car).all()
    # you have to serialize the data from data object to serail data here
    #rs is the data output in data object format, 
    global data
    data = [ {"car":Car.Name,"price":Car.Price} for Car in rs]
    #json.dump(rs)
    return jsonify([data])

if __name__=="__main__":
    app.run(debug = True)