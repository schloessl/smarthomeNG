#!/usr/bin/env python3
# vim: set encoding=utf-8 tabstop=4 softtabstop=4 shiftwidth=4 expandtab
#########################################################################
#  Copyright 2019-      Martin Sinn                       m.sinn@gmx.de
#########################################################################
#  This file is part of SmartHomeNG
#
#  SmartHomeNG is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SmartHomeNG is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SmartHomeNG  If not, see <http://www.gnu.org/licenses/>.
#########################################################################

from lib.model.smartobject import SmartObject

from lib.shtime import Shtime
from lib.module import Modules
from lib.utils import Utils
from lib.translation import translate as lib_translate
import logging
import os


class Module(SmartObject, Utils):
    """
    The class Module implements the base class of call modules.
    The implemented methods are described below.

    In adition the methods implemented in lib.utils.Utils are inhereted.
    """

    _shortname = ''     #: Short name of the module; is initialized during loading of the module; :Warning: Don't change it
    _longname = ''      #: Long name of the module; is initialized during loading of the module


    def get_parameter_value(self, parameter_name):
        """
        Returns the configured value for the given parameter name

        If the parameter is not defined, None is returned

        :param parameter_name: Name of the parameter for which the value should be retrieved
        :type parameter_name: str

        :return: Configured value
        :rtype: depends on the type of the parameter definition
        """
        return self._parameters.get(parameter_name, None)


    def translate(self, txt, vars=None):
        """
        Returns translated text
        """
        txt = str(txt)

        return lib_translate(txt, vars, additional_translations='module/'+self._shortname)


