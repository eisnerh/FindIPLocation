import unittest
from unittest.mock import patch
from main import get_public_ip

class TestGetPublicIP(unittest.TestCase):
    @patch('main.urlopen')
    def test_get_public_ip(self, mock_urlopen):
        mock_response = {'ip': '192.168.0.1'}
        mock_urlopen.return_value = mock_response

        result = get_public_ip()

        self.assertEqual(result, '192.168.0.1')

if __name__ == '__main__':
    unittest.main()