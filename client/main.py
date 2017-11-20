from client.gui.control import MainController
from client.model.dbConnect import connection_to_db
from client.model.user_action import User

conn = connection_to_db()

#user = User(conn, "banifest", "123")

if __name__ == "__main__":
    controller = MainController.MainController()
else:
    exit(0)