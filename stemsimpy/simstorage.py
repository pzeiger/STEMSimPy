import zarr


class SimStorage(zarr.hierarchy.Group):
    """
    """
    
    def __init__(self, projfile='project.zarr'):
       
        store = zarr.DirectoryStore(projfile)
        print(store.getsize())
        self._init_storage = store.getsize() == 0
        print(self._init_storage)
        root = zarr.group(store=store, overwrite=False)
        
        super().__init__(store=root.store, read_only=False, chunk_store=None,
                         cache_attrs=None, synchronizer=None, path=root.path)
        
        if self._init_storage:
            self.attrs['simstorage'] = True
            self._create_subgroup(path='/rawdata')
            self._create_subgroup(path='/procdata')
            self._create_subgroup(path='/visualize')
            self._init_storage = False
        else:       
            assert self.attrs['simstorage'], 'Not a SimStorage project.'
        

        
    def _create_subgroup(self, path):
        """
        """
        try:
            newgroup = self.create_group(path)
        except ValueError:
            pass
        return newgroup





