""" Game fix for Pes 2021
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ 
    """

    # Replace launcher with game exe in proton arguments
    util.protontricks('vcrun2019_ge')
    util.protontricks('allfonts')
    util.protontricks('dotnet462')
    util.protontricks('dotnet471')
    util.use_seccomp()
