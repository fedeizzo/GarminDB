"""Test summary db."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import unittest
import logging

from test_summary_db_base import TestSummaryDBBase
import HealthDB
import garmin_db_config_manager as GarminDBConfigManager


root_logger = logging.getLogger()
handler = logging.FileHandler('summary_db.log', 'w')
root_logger.addHandler(handler)
root_logger.setLevel(logging.INFO)

logger = logging.getLogger(__name__)


class TestSummaryDB(TestSummaryDBBase, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        db_params_dict = GarminDBConfigManager.get_db_params()
        db = HealthDB.SummaryDB(db_params_dict)
        table_dict = {
            'summary_table' : HealthDB.Summary,
            'months_table' : HealthDB.MonthsSummary,
            'weeks_table' : HealthDB.WeeksSummary,
            'days_table' : HealthDB.DaysSummary
        }
        super(TestSummaryDB, cls).setUpClass(db, table_dict)


if __name__ == '__main__':
    unittest.main(verbosity=2)
