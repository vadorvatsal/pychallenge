# This document contains how to work with regular expressions and few of examples to try
# You need to use some regular expression engine to work with
# Here we are using python engine and read the documentation if you need to know how to start with it

# There are different flags which indicates modes of our regular expression
# Possible modes are,
#
# Standard          :   /re/
# Global            :   /re/g
# Case insensitive  :   /re/i
# Multi line        :   /re/m

# Keep in mind that searches are case-sensitive by default
# famous UNIX based regex program is called grep which stands for g/re/p - global regular expression print



# ------------------------------------------------------------------------------------------------------------------------- #
#                                                   Program starts here
# ------------------------------------------------------------------------------------------------------------------------- #

import re

txt = "This is demo text on which over the time we will be performing different regular expression examples and try to grab or grep the matching pattern. Keep in mind that this is single line without any new line character."
<<<<<<< HEAD
result = re.findall("l?d",txt)
=======
result = re.findall("t|x",txt)
>>>>>>> 4e6501a96cf618d3f7318b1d1f1ee07346c41c78

if result:
    print("\n It's match !\n Total matche(s): {} \n\n {}\n".format(len(result),result))
else:
    print("\nNo match\n")
