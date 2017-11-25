from client.gui.control import MainController
from client.model.dbConnect import connection_to_db
from client.model.User import User

conn = connection_to_db()

if __name__ == "__main__":
    controller = MainController.MainController()
else:
    exit(0)
