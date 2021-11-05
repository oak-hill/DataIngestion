import pandas as pd
import yaml
import os
import subprocess
import gc
import re
import datetime
import logging
import testutility as util 

def read_config_file(filepath):
    with open(filepath, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(exc)

