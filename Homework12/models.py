from app import db

class Locations(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    zip_code = db.Column(db.String(50), index=True, unique=True)
    latitude = db.Column(db.String(50))
    longitude = db.Column(db.String(50))
    address = db.Column(db.String(50))

    def __init__(self, zip_code, latitude, longitude, address):
        self.zip_code = zip_code
        self.latitude = latitude
        self.longitude = longitude
        self.address = address