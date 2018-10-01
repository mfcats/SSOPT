# Copyright 2018 Markus Frings (frings@cats.rwth-aachen.de)
#
# This file is part of SSOPT.
#
# SSOPT is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation version 3 of the License.
#
# SSOPT is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along with SSOPT.  If not, see
# <http://www.gnu.org/licenses/>.
#

from SSOPT.case import Case
from SSOPT.dakota import Dakota


class Study():
    def __init__(self, params):
        self.dakota = Dakota(params)

    def run(self):
        self.dakota.run()
        self.postprocess()

    def postprocess(self):
        pass
