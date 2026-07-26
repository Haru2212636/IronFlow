"""Test cases for FirstApp views."""

from django.test import TestCase


class SimpleTest(TestCase):
    """Basic health check test."""

    def test_basic_math(self):
        """Test standard arithmetic."""
        self.assertEqual(1 + 1, 2)
