import os

from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    #data_info_path : str = os.path.join(('artifact','data_info.csv'))
    #data_links_path : str = os.path.join(('artifact','data_links.csv'))
    data_path : str = os.path.join('artifact',"data.csv")