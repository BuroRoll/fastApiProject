from database.initialise import ZeepClient


def get_db():
    try:
        db = ZeepClient()
        yield db
    finally:
        db.close()
