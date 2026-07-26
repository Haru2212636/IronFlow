"""Test cases for FirstApp."""

from django.test import TestCase


class SimpleTest(TestCase):
    """Basic health check test."""

    def test_basic_addition(self):
        """Test basic math."""
        self.assertEqual(1 + 1, 2)
