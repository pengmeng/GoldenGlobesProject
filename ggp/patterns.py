__author__ = 'mengpeng'
import re

"""
Put all keywords and regex here
"""

# keywords
host_kw = ["host", "hosting", "hosts", "hosted", "hosted by"]
presenter_kw = ["presented by", "presenter", "presenting"]

# regex
name_re = re.compile("([A-Z][a-z]+\s[A-Z][-'a-zA-Z]+)")  # 'Golden Globes', 'Lea Michele' .etc
winner_re = []
host_re = []