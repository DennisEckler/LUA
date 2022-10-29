from django.test import TestCase
from django.urls import reverse
from .models import Article
# Create your tests here.

class ArticleModelTests(TestCase):

    def test_article_update(self):
        """
        tests if the update works properly
        """
        article = Article(anzahl=2)
        article.setAmount(2),
        
        self.assertIs(article.anzahl == 4, True)


class LagerAppIndexViewTests(TestCase):
    def test_no_articles(self):
        """
        If no Articles here, we should see an appropriate message 
        """
        response = self.client.get(reverse('LagerApp:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Articles here.")
