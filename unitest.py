import unittest

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_landing_aliases(self):
        landing = self.client.post('/')
        assert landing.status_code == 405

    def test_home(self):
        landing = self.client.get("/")
        html = landing.data.decode()
        assert "<h1 style=\"padding:10px\">Stock News Sentiment Analyzer</h1>" in html
        landing.status_code == 200

    def test_textfiled_correct(self):
            response = self.client.get('/', data=dict(text_field='AMZN'))
            self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()