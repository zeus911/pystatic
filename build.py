#        ██████╗ ██╗   ██╗███████╗████████╗ █████╗ ████████╗██╗ ██████╗
#        ██╔══██╗╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔════╝
#        ██████╔╝ ╚████╔╝ ███████╗   ██║   ███████║   ██║   ██║██║     
#        ██╔═══╝   ╚██╔╝  ╚════██║   ██║   ██╔══██║   ██║   ██║██║     
#        ██║        ██║   ███████║   ██║   ██║  ██║   ██║   ██║╚██████╗
#        ╚═╝        ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝
#
#┌─┐┌┬┐┌─┐┌┬┐┬┌─┐  ┌┐ ┬  ┌─┐┌─┐┌─┐┬┌┐┌┌─┐  ┌┬┐┬ ┬┌─┐  ┌─┐┬ ┬┌┬┐┬ ┬┌─┐┌┐┌  ┬ ┬┌─┐┬ ┬
#└─┐ │ ├─┤ │ ││    ├┴┐│  │ ││ ┬│ ┬│││││ ┬   │ ├─┤├┤   ├─┘└┬┘ │ ├─┤│ ││││  │││├─┤└┬┘
#└─┘ ┴ ┴ ┴ ┴ ┴└─┘  └─┘┴─┘└─┘└─┘└─┘┴┘└┘└─┘   ┴ ┴ ┴└─┘  ┴   ┴  ┴ ┴ ┴└─┘┘└┘  └┴┘┴ ┴ ┴ 
#
##################################################################################
##################################################################################
###                         This is the build file for                         ###
###                                                                            ###
###                              Pystatic, v 1.1                               ###
###                                                                            ###
###                            as of July 23, 2018                             ###
###                  https://github.com/Zedelghem/pystatic/                    ###
###                                                                            ###
###                                      by                                    ###
###                                                                            ###
###                              Borys Jastrzębski                             ###
###                                                                            ### 
###                          Licensed under GNU GPL 3.0                        ###
###                                                                            ###
###     For easy configuration head straight to the CONFIG file in the main    ###
###     directory. Make any changes in this file only if you know well what    ###
###     you are doing.                                                         ###
###                                                                            ###
##################################################################################
##################################################################################

from pystatic import *

build_website(parse_config("pystatic.cfg")[0], **parse_config("pystatic.cfg")[1])