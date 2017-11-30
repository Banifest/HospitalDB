from datetime import date

from client.model.QueryMessage import QueryMessage


class Drag:
    _id: int
    _name: str
    _price: str
    _shelf_life: date
    _description: str
    _mass: float
    _is_need_recipe: bool

    def __init__(self, conn, id_: int = None, name: str = None):
        cursor = conn.cursor()
        if id_ is not None:
            cursor.execute("EXEC get_drag_by_id {0}".format(id_))
        elif name is not None:
            cursor.execute("EXEC get_drag_by_name '{0}'".format(name))
        else:
            QueryMessage(303)
        row = cursor.fetchone()

        if row is not None:
            self._id = row[0]
            self._name = row[1]
            self._price = row[2]
            self._shelf_life = row[3]
            self._description = row[4]
            self._mass = row[5]
            self._is_need_recipe = row[6]
