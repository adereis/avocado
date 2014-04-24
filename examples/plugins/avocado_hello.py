# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Copyright: RedHat 2013-2014
# Author: Ruda Moura <rmoura@redhat.com>

from avocado.plugins import plugin


class HelloWorld(plugin.Plugin):

    """
    The classical Hello World! plugin example.
    """

    name = 'hello_world'
    enabled = True

    def configure(self, app_parser, cmd_parser):
        myparser = cmd_parser.add_parser('hello',
                                         help='Hello World! plugin example')
        myparser.set_defaults(func=self.hello)
        self.configured = True

    def hello(self, args):
        print self.__doc__