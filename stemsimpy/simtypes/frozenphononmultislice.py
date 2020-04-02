from stemsimpy.simstorage import SimStorage

class FrozenPhononMultislice(SimStorage):
    """ 
    """
    def __init__(self, filelist):
        """
        """
        self._assemble_data(filelist)
    
    
    def _assemble_data(self):
        """ Method to read data.
        """
        self._data = FrozenPhononData()
    
    def process(self):
        """ Method to process data.
        """
        self._data.average_diffpatts()
    
    def analyze(self):
        """
        """

#class StemSimPy(zarr.hierarchy.Group):
#    """
#    """
#    
#    def __init__(self, simtype=None, projfile='project.zarr'):
#        
#        store = zarr.DirectoryStore(projfile)
#        if store.getsize() == 0:
#            self._init_stemsimpy = True
#        super().__init__(store=store, read_only=False, chunk_store=None,
#                         cache_attrs=None, synchronizer=None, path=None)
#        
#        if self._init_stemsimpy:
#            self.stemsimpy_proj = True
#            self._create_subgroup(path='/rawdata')
#            self._create_subgroup(path='/procdata')
#            self._create_subgroup(path='/visualize')
#            self._simtype = simtype
#        else:       
#            assert self._simtype is simtype.lower(), 'Simulation types do not match'
#            assert self._stemsimpy_proj, 'Not a StemSimPy project.'
#        
#        return self._run_simtype()
#
#        
#    def _create_subgroup(self, path):
#        """
#        """
#        try:
#            newgroup = self.create_group(path)
#        except ValueError:
#            pass
#        return newgroup
#    
#    
#    def _run_simtype(simtype):
#        """Dispatch method
#        """
#        method_name = '_instantiate_' + str(simtype).lower()
#        method = getattr(self, method_name, lambda: "Invalid method")
#        return method() 
#    
#    
#    def _instantiate_fpms(self):
#        """
#        """
#        return 
