from django.test import TestCase
from items.models import Item
from user.models import UserProfile
from django.contrib.auth.models import User
from django.db.models import Model
from django.core.serializers import serialize

from utils.query_utils import query_to_json, get_field_names
# Create your tests here.

# Query to JSON test
class JSONTestCase(TestCase):
    # Create users and 2 listings per user
    def setUp(self):
        item_id = 1
        for i in range(1, 2):
            index = str(i)
            user = User.objects.create_user('testusername'+index, 'testemail'+index, 'testpassword'+index)
            profile = UserProfile.objects.create(user=user, phone='testphone'+index, address='testaddress'+index)
            item = Item.objects.create(
                item_id = item_id,
                name = 'Item'+str(item_id),
                seller = profile,
                description ='Description'+str(item_id),
                price=item_id,
                quantity=item_id,
                sold = False
            )
            item_id += 1
            item2 = Item.objects.create(
                item_id=item_id,
                name='Item' + str(item_id),
                seller=profile,
                description='Description' + str(item_id),
                price=item_id,
                quantity=item_id,
                sold=False
            )
            item_id += 1



    def test_query_to_json(self):
        items = Item.objects.all()
        # print(serialize('json', items))
        # for item in items:
        #     print(type(serialize('json', [item])))

        item_json = query_to_json(items, exclude_fields="password")
        print(item_json)
        self.assertTrue(1+1==2)
    #TODO: Finish test case

