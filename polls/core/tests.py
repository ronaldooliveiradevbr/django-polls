from datetime import date

from django.shortcuts import resolve_url as r
from django.test import TestCase

from polls.core.models import Choice, Question


class IndexTest(TestCase):
    def setUp(self):
        Question.objects.create(text='What is your favorite color?')
        Question.objects.create(text='Who is going to win the election?')
        Question.objects.create(text='Do you believe in aliens?')

        self.resp = self.client.get(r('index'))

    def test_get(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/index.html')

    def test_html(self):
        expected = [
            (1, '<ul'),
            (3, '<li>'),
            (1, 'href="{}">{}'.format(r('detail', 1), 'What is your favorite color?')),
            (1, 'href="{}">{}'.format(r('detail', 2), 'Who is going to win the election?')),
            (1, 'href="{}">{}'.format(r('detail', 3), 'Do you believe in aliens?')),
        ]

        for count, tag in expected:
            with self.subTest():
                self.assertContains(self.resp, tag, count)


class DetailTest(TestCase):
    def setUp(self):
        q = Question.objects.create(text='What is your favorite color?')

        q.choices.create(text='Red')
        q.choices.create(text='Blue')
        q.choices.create(text='None')

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
            (1, '</ul>')
        ]

        for count, tag in expected:
            with self.subTest():
                self.assertContains(self.resp, tag, count)


class NotFoundDetailGet(TestCase):
    def test_not_found(self):
        response = self.client.get(r('detail', 1))
        self.assertEqual(response.status_code, 404)


class QuestionModelTest(TestCase):
    def setUp(self):
        self.obj = Question.objects.create(text="What's my favorite color?")

    def test_create(self):
        self.assertTrue(Question.objects.exists())

    def test_str(self):
        self.assertEqual("What's my favorite color?", str(self.obj))

    def test_pub_date(self):
        self.assertIsInstance(self.obj.pub_date, date)

    def test_pub_date_auto_now(self):
        field = Question._meta.get_field('pub_date')
        self.assertTrue(field.auto_now)


class ChoiceModelTest(TestCase):
    def setUp(self):
        self.question = Question.objects.create(
            text='What is your favorite color?')
        self.choice = Choice.objects.create(
            text='Red', question=self.question)

    def test_create(self):
        self.assertTrue(Choice.objects.exists())

    def test_question(self):
        self.assertIsInstance(self.choice.question, Question)

    def test_str(self):
        self.assertEqual('Red', str(self.choice))


class ResultsGetTest(TestCase):
    def test_get(self):
        response = self.client.get(r('results', 1))
        self.assertEqual(response.status_code, 200)


class VoteGetTest(TestCase):
    def test_get(self):
        response = self.client.get(r('vote', 1))
        self.assertEqual(response.status_code, 200)
