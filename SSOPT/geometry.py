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

class Geometry():
    def __init__(self, params):
        self.gclength = params['case']['gclength']
        self.gcheight = params['case']['gcheight']
        self.filling_ratio = params['case']['fillingratio']

    @property
    def initial_volume(self):
        return self.gclength * self.gcheight

    @property
    def send(self):
        return self.gclength * (1.0 - self.filling_ratio)