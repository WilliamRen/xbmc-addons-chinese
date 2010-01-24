# -*- coding: cp936 -*-
#"""
#    Plugin for showing Shanghai/shengzheng stocks from sina.com.cn
#"""

# main imports
import sys
import xbmc

# plugin constants
__plugin__ = "MyStocks"
__author__ = "Rabbitgg"
__version__ = "0.1.0"
__date__ = "$Date: 2009-11-19 05:47:47 +0800  $"
__XBMC_Revision__ = "19001"

def _check_compatible():
    try:
        # spam plugin statistics to log
        xbmc.log( "[PLUGIN] '%s: Version - %s' initialized!" % ( __plugin__, __version__), xbmc.LOGNOTICE )
        # get xbmc revision
        xbmc_rev = int( xbmc.getInfoLabel( "System.BuildVersion" ).split( " r" )[ -1 ] )
        # compatible?
        ok = xbmc_rev >= int( __XBMC_Revision__ )
    except:
        # error, so unknown, allow to run
        xbmc_rev = 0
        ok = 2
    # spam revision info
    xbmc.log( "     ** Required XBMC Revision: r%s **" % ( __XBMC_Revision__, ), xbmc.LOGNOTICE )
    xbmc.log( "     ** Found XBMC Revision: r%d [%s] **" % ( xbmc_rev, ( "Not Compatible", "Compatible", "Unknown", )[ ok ], ), xbmc.LOGNOTICE )
    return ok


if ( __name__ == "__main__" ):
    if ( not sys.argv[ 2 ] ):
            from MystocksAPI import mystocks_list as plugin
    elif ( "mode=show_info" in sys.argv[ 2 ] ):
        from MystocksAPI import mystocks_custom as plugin
    elif ( "mode=show_graph" in sys.argv[ 2 ] ):
        from MystocksAPI import mystocks_graph as plugin
    elif ( "mode=show_dp" in sys.argv[ 2 ] ):
        from MystocksAPI import mystocks_dp as plugin
    elif ( "mode=show_detail" in sys.argv[ 2 ] ):
        from MystocksAPI import mystocks_detail as plugin
    elif ( "mode=show_search" in sys.argv[ 2 ] ):
        from MystocksAPI import mystocks_search as plugin
    elif ( "mode=op_zx" in sys.argv[ 2 ]  ):
        from MystocksAPI import mystocks_zx as plugin
    elif ( "mode=show_ph" in sys.argv[ 2 ]  ):
        from MystocksAPI import mystocks_ph as plugin
    elif ( "mode=show_co_detail" in sys.argv[ 2 ]  ):
        from MystocksAPI import mystocks_phdetail as plugin
    else:
        from MystocksAPI import mystocks_list as plugin

    try:
        plugin.Main()
    except:
        import traceback
        traceback.print_exc()
#        pass
