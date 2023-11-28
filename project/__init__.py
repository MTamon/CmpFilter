"""Initialize published package."""

from .src import module1, module2, module3

############## EDIT THESE INFORMATION ###############
AUTHOR = "John Smith"
EMAIL = "john.smith@email.com"
YEAR = "2023"
GIT_URL = "https://github.com/john-smith/project.git"
#####################################################

__copyright__ = f"Copyright (C) {YEAR} {AUTHOR}"
__version__ = "0.0.0"
__license__ = "MIT License"
__author__ = AUTHOR
__author_email__ = EMAIL
__url__ = GIT_URL

__all__ = ["module1", "module2", "module3"]
