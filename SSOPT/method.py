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

def get_method(params):
    if params['study']['type'] == 'parameter':
        return ParameterStudy(params)
    elif params['study']['type'] == 'optimizaiton':
        return OptimizationStudy(params)
    else:
        raise RuntimeError('Only parameter study and optimization study are implemented!')


class ParameterStudy():
    def __init__(self, params):
        self.nsswitch = params['study']['partitions'][0]
        self.nvfinal = params['study']['partitions'][1]

    def print_method(self, inputfile):
        inputfile.writelines(['method\n  multidim_parameter_study\n    partitions = ', str(self.nsswitch), ' ',
                              str(self.nvfinal), '\n\n'])

    @property
    def number_of_responses(self):
        return 7

    @staticmethod
    def print_responses(inputfile):
        inputfile.writelines(["responses\n",
                              "  descriptors 'a' 't' 'ea19' 'ea37' 'ea46' 'no' 'act'\n",
                              "  response_functions = 7\n"
                              "  no_gradients\n",
                              "  no_hessians\n\n"])


class OptimizationStudy():
    def __init__(self, params):
        raise RuntimeError('Optimization is not yet implemented.')