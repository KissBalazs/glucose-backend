from django.test import TestCase
from levels.models import Level
from django.utils import timezone
import datetime


class LevelModelTests(TestCase):
    def start_date_should_be_earlier_than_end_date(self):
        """
        Should not be able to create a new entry if the end date is earlier than the start date.
        """
        current_time = timezone.now()
        earlier_time = current_time - datetime.timedelta(days=1)
        try:
            bad_level = Level(start=current_time, end=earlier_time)
            self.fail("Was able to create a badly formatted entry")
        except Exception:
            pass

    def should_create_correctly_ordered_date_level(self):
        """
        Should not be able to create a new entry if the end date is earlier than the start date.
        """
        current_time = timezone.now()
        earlier_time = current_time + datetime.timedelta(days=1)
        good_level = Level(start=current_time, end=earlier_time)
        self.assertTrue("Was able to create a badly formatted entry")
