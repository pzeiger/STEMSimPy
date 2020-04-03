from .simstorage import SimStorage
from . import fileio


def _compare_dicts(dict1, dict2, mode=''):
    """
    Return the 
    
    Parameter
    ---------
    dict1:       dict
    dict2:       dict
    """
    if mode is 'shared_diff_val':
        result = {k: d1[k] for k in d1 if k in d2 and d1[k] != d2[k]}
    if mode is 'shared_same_val':
        result = {k: d1[k] for k in d1 if k in d2 and d1[k] == d2[k]}
    if mode is 'unique_dict1':
        result = {k: d1[k] for k in d1 if k not in d2}
    if mode is 'unique_dict2':
        result = {k: d2[k] for k in d2 if k not in d1}
    return result 



class _ProjDefaults():
    """ Class for specifying the defaults settings of projects
    """

    def __init__(self, init_projstorage=False, init_settings=False):
        """
        """
        self.projzarr = 'project.zarr'
        self.projyaml = 'project.yaml'
        self.settings = {}
        
        if init_projstorage:
            self.projstorage = self._open_projstorage()
        else:
            self.projstorage = None
        
        if init_settings:
            self._init_settings()
    

    def update_settings
        
    def _init_settings(self, projzarr, ):
        """
        """
        
    
    
    def _open_projstorage(self, projzarr=None):
        """
        """
        if not projzarr:
            projzarr = self._projzarr
        return SimStorage(projzarr)
    
    
    def _settings_from_projyaml(self, projyaml=None):
        """
        """
        if not projyaml:
            projyaml = self._projyaml
        yamldata = fileio.open_yaml(projyaml)
        shared_it_diff_val = _compare_dicts(yamldata, self.settings, mode='shared_diff_val')
        
        self.settings = SimStorage(projzarr)
        
    
    def _settings_from_projstorage(self, projzarr=None):
        """

        """
        if not projzarr:
            projzarr = self._projzarr
        root = zarr.open(projzarr, 'r')
        
    
    
    def _store_in_proj(proj):
        """
        Parameters
        ----------
        proj:       stemsimpy.SimStore
                    stemsimpy project
        """

