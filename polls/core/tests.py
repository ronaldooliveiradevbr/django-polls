from django.shortcuts import resolve_url as r
from django.test import TestCase


class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('index'))

    def test_get(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/index.html')

    def test_html(self):
        expected = [
            (1, '<ul'),
            (3, '<li>'),
            (1, 'href="{}">{}'.format('/polls/1/', 'What is your favorite color?')),
            (1, 'href="{}">{}'.format('/polls/2/', 'Who is going to win the election?')),
            (1, 'href="{}">{}'.format('/polls/3/', 'Do you believe in aliens?')),
        ]

        for count, tag in expected:
            with self.subTest():
                self.assertContains(self.resp, tag, count)


class DetailTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('detail', 1))

    def test_get(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/detail.html')

    def test_html(self):
        expected = [
            (1, '<h1>What is your favorite color?'),
            (1, '<ul'),
            (1, '<li>Red</li>'),
            (1, '<li>Blue</li>'),
            (1, '<li>None</li>'),
        ]

        for count, tag in expected:
            with self.subTest():
                self.assertContains(self.resp, tag, count)
