class Case():
    def __init__(self, params):
        case_params = params['case']
        self.gcheight = case_params['gcheight']
        self.gclength = case_params['gclength']
        self.outputlength = case_params['outputlength']
        self.outputheight = case_params['outputheight']
        self.deltax = case_params['deltax']
        self.ncpus = case_params['ncpus']
        runtime = case_params['runtime']

    def initialize(self):
        pass