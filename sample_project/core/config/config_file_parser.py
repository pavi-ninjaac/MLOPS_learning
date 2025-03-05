"""
This file contains the methods to parsh the config files and read it.
"""
import os
from configparser import ConfigParser

from constants import config


class ConfigParserHelper:
    """
    Helper class to make job easier for config parser methods.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.config = ConfigParser()

    def load(self):
        """
        Load the config file into the config parsher object.
        """
        self.config.read(self.file_path)

    def has_section(self, section: str):
        """
        Check the config file has the given section or not.
        """
        if section in self.config.sections():
            return True
        return False


class ConfigSelector:
    """
    Decides which config class to return depending on deployment mode.
    """

    def __new__(cls):
        obj = ConfigParserHelper.__new__(ConfigParserHelper)
        obj.__init__(cls.FILE_PATH)
        return obj


class SparkConfig(ConfigSelector):
    """
    Config parser for the spark config file.
    """
    FILE_PATH = os.path.join(config.CONFIG_FILE_DIRECTORY, config.SPARK_CONFIG_NAME)
