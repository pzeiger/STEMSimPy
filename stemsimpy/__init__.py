from .simstorage import SimStorage
from . import simtypes
#from . import  stemdata



class _SimSelect():
    """
    """
    
    def __init__(self):
        pass 
    
    def _run_simtype(self, simtype, projfile):
        """Dispatch method
        """
        method_name = '_instantiate_' + str(simtype).lower()
        method = getattr(self, method_name, lambda: "Invalid method")
        return method(projfile=projfile) 
    
    
    def _instantiate_fpms(self, projfile):
        """ 
        """
        print('Instantiating FrozenPhononMultislice')
#        return FrozenPhononMultislice(projfile)


def open_project(projfile='project.zarr', simtype=None):
    """
    """
    selector = _SimSelect()
    return selector._run_simtype(simtype=simtype, projfile=projfile)


