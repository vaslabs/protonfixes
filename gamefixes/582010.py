""" Monster Hunter World
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Requires media foundation dlls
    """
    util.winedll_override('nvapi','')
    util.winedll_override('nvapi64','')
    util.protontricks('mf_install')
 
