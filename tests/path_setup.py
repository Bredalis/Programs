
# Library to navigate to the path
# where the files are located
import os
import sys


# Insert the main directory of the current file
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../src",
        )
    ),
)
