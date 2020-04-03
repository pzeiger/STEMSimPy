from ._projdefaults import _ProjDefaults


class _Project(_ProjDefaults):
    """
    """
    
    def __init__(self, projzarr=None, inputyaml=None):
        super().__init__()
        self._open_
        if projzarr:
            self._load_from_projzarr()
        if inityaml:
            self._load_from_inputyaml()
        
        
