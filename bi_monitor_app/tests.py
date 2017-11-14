# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse


# Create your tests here.


class TestViewDetail(TestCase):
    """
    测试detail这个view
    """
    def test_no_report(self):
        """
        If no questions exist, an appropriate message is displayed.
        :return:
        """
        response = self.client.get(reverse('detail', kwargs={'report_id': 100}))
        self.assertEqual(response.status_code, 404)
