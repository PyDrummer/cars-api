from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Car

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_car = Car.objects.create(
            driver = testuser1,
            make = 'Mazda',
            model = 'Miata'
        )
        test_car.save()

    def test_blog_content(self):
        car = Car.objects.get(id=1)
        actual_driver = str(car.driver)
        actual_make = str(car.make)
        actual_model = str(car.model)
        self.assertEqual(actual_driver, 'testuser1')
        self.assertEqual(actual_make, 'Mazda')
        self.assertEqual(actual_model, 'Miata')