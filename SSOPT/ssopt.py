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

import yaml
from SSOPT.study import Study


def main(parameter_file):
    params = load_input_file(parameter_file)
    study = Study(params)
    study.run()


def load_input_file(parameter_file):
    with open(parameter_file, 'r') as f:
        parameters = yaml.load(f)
    return parameters
