from dataclasses import dataclass

#Data ingestion artifacts
@dataclass
class DataIngestionArtifacs:
    imbalance_data_file: str
    raw_data_file_path: str