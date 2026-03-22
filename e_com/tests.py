from django.test import TestCase
from .models import *
# Create your tests here.

class MyTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="zoden", password="admin")
        service = Service.objects.create(name="Interior", max_days=2)
        sample = Sample.objects.create(sample_name="test_sample", price_on_offer=100, customer_rating=3)
        comment = Comment.objects.create(username_id=1, comment="Test_Comment")
        cart = Cart.objects.create(user_id=1)
        cart.item.add(service)
        worker = Worker.objects.create(first_name="Denz", last_name="Oti", )
        service_bought = ServiceBought.objects.create(customer=user, service=service, deposit=900000, balance=0)

    def test_returns(self):
        user = User.objects.get(id=1)
        sample = Sample.objects.get(id=1)
        comment = Comment.objects.get(id=1)
        service = Service.objects.get(id=1)
        order = ServiceBought.objects.get(id=1)
        cart = Cart.objects.get(id=1)
        worker = Worker.objects.get(id=1)

    
        
        self.assertEqual(str(service), 'Interior')
        self.assertEqual(str(sample), 'test_sample')
        self.assertEqual(str(comment), 'Test_Comment')
        self.assertEqual(str(user), 'zoden')
        self.assertEqual(str(worker), 'Denz')
        self.assertEqual(str(cart), 'zoden')
        self.assertEqual(str(), 'Interior')