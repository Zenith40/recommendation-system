import os

from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    #data_info_path : str = os.path.join(('artifact','data_info.csv'))
    #data_links_path : str = os.path.join(('artifact','data_links.csv'))
    data_path : str = os.path.join('artifact',"data.csv")

@dataclass
class DataTransformationConfig:
    transformed_data_path =os.path.join('artifact',"transformed_data.csv")
    similarity_obj_path = os.path.join('artifact',"similarity.pkl")