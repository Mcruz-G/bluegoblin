from .update_db import update_db

def update_data():
    update_db("1h")
    update_db("1m")
if __name__ == "__main__":
    update_data()