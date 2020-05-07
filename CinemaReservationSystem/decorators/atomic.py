from CinemaReservationSystem.database.db import Database


def atomic(method):
    def inner_method(instance, *args, **kwargs):
        db = Database()
        cursor = db.connection.cursor()
        value = method(instance, cursor, *args, **kwargs)
        db.connection.commit()
        db.connection.close()
        return value
    return inner_method
