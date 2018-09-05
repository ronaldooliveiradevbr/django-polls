from datetime import datetime

from django.shortcuts import resolve_url as r
from django.test import TestCase
from django.utils import timezone

from .models import Question


class IndexTest(TestCase):
    def setUp(self):
        Question.objects.create(
            text='What is your favorite color?', pub_date=timezone.now())
        Question.objects.create(
            text='Who is going to win the election?', pub_date=timezone.now())
        Question.objects.create(
            text='Do you believe in aliens?', pub_date=timezone.now())

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
        Question.objects.create(
            text='What is your favorite color?', pub_date=timezone.now()
        )
        self.resp = self.client.get(r('detail', 1))

    def test_get(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/detail.html')

    def test_html(self):
        expected = [
            (1, '<h1>What is your favorite color?'),
            (1, '<ul'),
            #(1, '<li>Red</li>'),
            #(1, '<li>Blue</li>'),
            #(1, '<li>None</li>'),
        ]

        for count, tag in expected:
            with self.subTest():
                self.assertContains(self.resp, tag, count)


class QuestionModelTest(TestCase):
    def setUp(self):
        self.question = Question.objects.create(
            text="What's my favorite color?",
            pub_date=timezone.now()
        )

    def test_create(self):
        self.assertTrue(Question.objects.exists())

    def test_pub_date(self):
        self.assertIsInstance(self.question.pub_date, datetime)

    def test_str(self):
        self.assertEqual("What's my favorite color?", str(self.question))
