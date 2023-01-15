"""Router for the correct database connection depending on django DB or specific memecard DB

(c) 2023 He-Arc Cyrille Polier
"""


class MemecardRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == "memecard_app":
            return "memecard"
        return "default"

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "memecard_app":
            return "memecard"
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label == "memecard_app"
            or obj2._meta.app_label == "memecard_app"
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "memecard_app":
            return db == "memecard"
        return None
