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

from shot import ShotCurve
from math import sqrt

class Variables():
    def __init__(self, params):
        self.shot_curve = ShotCurve(params)
        self.amax = params['study']['constraints']['amax']
        self.vmax = params['study']['bounds']['vmax']
        self.tmax = params['study']['constraints']['tmax']
        p_half = self.shot_curve.send - self.tmax**2 * self.amax
        self.sswitchmin = - p_half - sqrt(p_half**2 - self.shot_curve.send**2)
        self.vfinalmin = (self.shot_curve.send + self.sswitchmin) / self.tmax
        self.sswitchmax = min(self.shot_curve.send, self.tmax * self.vmax - self.shot_curve.send)
        self.vfinalmax = min(self.vmax, self.tmax * self.vmax - self.shot_curve.send)

    def print_variables(self, inputfile):
        inputfile.writelines(["variables\n",
                              "  continuous_design = 2\n",
                              "    lower_bounds ", str(self.sswitchmin), " ", str(self.vfinalmin), "\n"])
        inputfile.writelines(["    upper_bounds ", str(self.sswitchmax), " ", str(self.vfinalmax), "\n"])
        inputfile.writelines(["    descriptors 'sswitch' 'vfinal'\n\n"])