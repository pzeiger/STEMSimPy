import zarr


class SimStorage(zarr.hierarchy.Group):
    """
    """
    
    def __init__(self, projfile='project.zarr'):
        
        store = zarr.DirectoryStore(projfile)
        if store.getsize() == 0:
            self._init_storage = True
        super().__init__(store=store, read_only=False, chunk_store=None,
                         cache_attrs=None, synchronizer=None, path=None)
        
        if self._init_storage:
            self._simstorage = True
            self._create_subgroup(path='/rawdata')
            self._create_subgroup(path='/procdata')
            self._create_subgroup(path='/visualize')
            self._init_storage = False
        else:       
            assert self._simstorage, 'Not a SimStorage project.'
        

        
    def _create_subgroup(self, path):
        """
        """
        try:
            newgroup = self.create_group(path)
        except ValueError:
            pass
        return newgroup





