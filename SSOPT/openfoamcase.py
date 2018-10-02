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

from ssopt import load_input_file
from os import getcwd

class CaseSetup():
    def __init__(self):
        self._name = "unknown"
        self._workdir = getcwd()
        self._ncpus = 1
        self._runtime = 20
        self._project = "jara0185"

    def set_from_params(self, params):
        self._name = params['general']['name']
        self._workdir = params['general']['workdir']
        self._ncpus = params['case']['ncpus']
        self._runtime = params['case']['runtime']
        self._project = params['case']['project']

    @property
    def workdir(self):
        return self._workdir

    @workdir.setter
    def workdir(self, wkdir):
        self._workdir = wkdir

    @property
    def ncpus(self):
        return self._ncpus

    @ncpus.setter
    def ncpus(self, n):
        self._ncpus = n

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def runtime(self):
        return self._runtime

    @runtime.setter
    def runtime(self, r):
        self._runtime = r

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, p):
        self._project = p


class OpenFOAMCase():
    def __init__(self, setup):
        self._workdir = setup.workdir
        self._shebang = "#!/usr/bin/env zsh\n\n"
        self._modules = ["DEVELOP", "gcc/8"]
        self._ofbasrcpath = "$HOME/OpenFOAM/OpenFOAM-v1806/etc/bashrc"
        self._ncpus = setup.ncpus
        self._name = setup.name
        self._runtime = setup.runtime
        self._project = setup.project

    def create(self):
        self.generate_job_script()

    def generate_job_script(self):
        with open(self._workdir + '/run.j', 'w+') as f:
            f.write(self._shebang)
            f.write("#BSUB -J " + self._name + "\n")
            f.write("#BSUB -o " + self._name + ".log\n")
            f.write("#BSUB -n " + str(self._ncpus) + "\n")
            f.write("#BSUB -W " + str(self._runtime) + "\n")
            f.write("#BSUB -a openmpi\n")
            f.write("#BSUB -M 2048\n")
            f.write("#BSUB -P " + self._project + "\n\n")
            self.write_modules(f)
            f.write(". " + self._ofbasrcpath + "\n\n")
            f.write("blockMesh >> blockMesh.log\n")
            f.write("mkdir -p 0/polyMesh\n")
            f.write("cp constant/polyMesh/points.gz 0/polyMesh\n\n")
            f.write("cp 0/alpha.aluminum.orig 0/alpha.aluminum\n")
            f.write("setFields >> setFields.log\n\n")
            f.write("decomposePar >> decomposePar.log\n\n")
            f.write("mpiexec -np " + str(self._ncpus) + " foamExec interFoam -parallel\n\n")

    def write_modules(self, f):
        f.writelines("module load ")
        for module in self._modules:
            f.writelines([module, " "])
        f.writelines("\n\n")



def main(parameter_file):
    params = load_input_file(parameter_file)
    case_setup = CaseSetup()
    case_setup.set_from_params(params)
    case = OpenFOAMCase(case_setup)
    case.create()