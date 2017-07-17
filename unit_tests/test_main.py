""" Unit tests for the main entry point for the open ods api service. """
import unittest
from mock import patch, MagicMock
import main
import logging


class TestMain(unittest.TestCase):

    @patch('main.DefaultStreamHandler')
    @patch('main.ServiceManager')
    @patch('logging.getLogger')
    def test__main__do_setup__WillInstantiateCustomStreamHandler_WhenCalled(self,
                                                                        mock_default_stream_handler,
                                                                        mock_service_manager,
                                                                        mock_get_logger):
        main.do_setup()
        mock_default_stream_handler.assert_called_with()
