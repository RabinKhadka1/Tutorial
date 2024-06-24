import pytest
from flask_testing import TestCase
from app import app, db, Product

class TestFlaskBase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()
        sample_product = Product(name="Test Product", price=50)
        db.session.add(sample_product)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestFlaskRoutes(TestFlaskBase):
    def test_products(self):
        response = self.client.get("/products")
        self.assert200(response)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0]['name'], "Test Product")
