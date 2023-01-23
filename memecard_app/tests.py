""" Tests for the memecard application.

(c) 2023 He-Arc Cyrille Polier
"""

from django.test import TestCase

from .routers import MemecardRouter


class Model():
    _meta = None
    app_label = None


# Create your tests here.

class RouterTests(TestCase):
    def test_db_for_read(self):
        router = MemecardRouter()
        model = Model()
        model._meta = Model()
        model._meta.app_label = "memecard_app"
        self.assertEqual(router.db_for_read(model), "memecard")
        
        model._meta.app_label = "other_app"
        self.assertEqual(router.db_for_read(model), "default")
        
    def test_db_for_write(self):
        router = MemecardRouter()
        model = Model()
        model._meta = Model()
        model._meta.app_label = "memecard_app"
        self.assertEqual(router.db_for_write(model), "memecard")
        
        model._meta.app_label = "other_app"
        self.assertEqual(router.db_for_write(model), "default")
        
