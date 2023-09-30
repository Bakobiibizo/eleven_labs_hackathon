from ingestion.loaders.pypdf_loader import PyPdfLoader


class LoaderSelector:
    def __init__(self, loader_name: str = None):
        self.loader = loader_name

    def pdf_loader(self):
        self.loader = PyPdfLoader()
        return self.loader

