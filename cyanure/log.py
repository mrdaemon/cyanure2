#   ____
#  / ___|   _  __ _ _ __  _   _ _ __ ___
# | |  | | | |/ _` | '_ \| | | | '__/ _ \
# | |__| |_| | (_| | | | | |_| | | |  __/
#  \____\__, |\__,_|_| |_|\__,_|_|  \___|
#       |___/
#
# Multi Purpose Artificial Inelegance Program
# Copyright (c) Alexandre Gauthier 2010-2011
# All Rights Reserved
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

""" Logging module, provides logger initialization and related utils """

import logging
import logging.handlers
import os

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL,
    }

_DEFAULTLEVEL = 'warning'

baselogger = logging.getLogger("cyanure")

class LoggerInitError(Exception):
    """ Error thrown when the logging system fails to initialize """
    def __init__(self, message="Unknown Logger Error. Please file a bug."):
        super(LoggerInitError, self).__init__()
        self.message = message

    def __str__(self):
        """ Textual representation of exception, with message """
        return repr("Logger Init Error: %s " % self.message)


def init_log(logfp, level=_DEFAULTLEVEL, conecho=True):
    """ Initialize the logging handlers and return a configured logger """
    if level.lower() not in LEVELS:
        print "*** LOGGING SYSTEM INIT: WARNING ***"
        print "Loglevel %s is invalid. %s was used instead." % (level,
            _DEFAULTLEVEL)
        level = _DEFAULTLEVEL


    # Not using default value in get() so the above warning can be
    # displayed.
    log_level = LEVELS.get(level.lower())

    if os.path.isfile(logfp):
        if not os.access(logfp, os.W_OK):
            raise LoggerInitError("Logfile %s is not writable!" % logfp)

    lhandler = logging.handlers.RotatingFileHandler(
        logfp, maxBytes=1048576, backupCount=5)
    lformatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    lhandler.setFormatter(lformatter)

    baselogger.addHandler(lhandler)

    if conecho:
        chandler = logging.StreamHandler()
        cformatter = logging.Formatter("%(levelname)-8s %(message)s")

        chandler.setFormatter(cformatter)

        baselogger.addHandler(chandler)

    baselogger.setLevel(log_level)

    baselogger.info("Logging system initialized.")
