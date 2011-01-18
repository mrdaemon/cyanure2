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

''' Configuration Paser '''

from __future__ import with_statement
import ConfigParser

class ConfigFile(object):
    ''' Configuration Parser Class '''
    def __init__(self, configfp):
        self._config = ConfigParser.SafeConfigParser()
        self.configfp = configfp
        try:
            self._cfhandle = open(self.configfp, 'r')
        except IOError, e:
            print "Unable to read config file %s: %s" % (
                                        self.configfp, e,
                                        )
            print "WARNING: Using defaults"
        else:
            with self._cfhandle as cfhandle:
                self._config.read(cfhandle)


