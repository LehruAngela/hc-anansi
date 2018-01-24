from hc.api.models import Check
from hc.test import BaseTestCase


class UpdateTimeoutTestCase(BaseTestCase):
    """ tests grace and check periods can be set to more than a month"""
    def setUp(self):
        super(UpdateTimeoutTestCase, self).setUp()
        self.check = Check(user=self.alice)
        self.check.save()

    def test_it_works(self):
        """ test that the new extended timeouts actually resgister """
        
        period = 5184000
        url = "/checks/%s/timeout/" % self.check.code
<<<<<<< HEAD
<<<<<<< HEAD
        payload = {"timeout": period , "grace": period, "nag": period }
=======
        payload = {"timeout": period , "grace": period}
>>>>>>> Ft increase timeouts and grace periods #153727847 (#20)
=======
        payload = {"timeout": period , "grace": period, "nag": period }
>>>>>>> Nag interval Build Error Fix #153727845 (#19)

        self.client.login(username="alice@example.org", password="password")
        test = self.client.post(url, data=payload)
        self.assertRedirects(test, "/checks/")

        check = Check.objects.get(code=self.check.code)
        assert check.timeout.total_seconds() == period
        assert check.grace.total_seconds() == period
