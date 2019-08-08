from tests.courses.register_courses import RegisterCoursesCSVDataTests
from tests.home.login_tests import LoginTests
import unittest
import pytest

t1=unittest.TestLoader().loadTestsFromTestCase(LoginTests)
t2=unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)
suit=unittest.TestSuite([t1,t2])
unittest.TextTestRunner().run(suit)
