"""Initialize published package."""

from filpy.filters import Filter, OverlapedFilter, TiledFilter, EmpFilter

############## EDIT THESE INFORMATION ###############
AUTHOR = "Tamon Mikawa"
EMAIL = "mtamon.engineering@gmail.com"
YEAR = "2023"
GIT_URL = "https://github.com/MTamon/Filpy.git"
#####################################################

__copyright__ = f"Copyright (C) {YEAR} {AUTHOR}"
__version__ = "0.0.0"
__license__ = "MIT License"
__author__ = AUTHOR
__author_email__ = EMAIL
__url__ = GIT_URL

__all__ = ["Filter", "OverlapedFilter", "TiledFilter", "EmpFilter"]
