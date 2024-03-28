from Hate_speech_detection.logger import logging
from Hate_speech_detection.exception import CustomException
import sys
from Hate_speech_detection.configuration.Gcloud_syncer import GCloudSync

obj = GCloudSync()
obj.sync_folder_from_gcloud("hate-speech-detection-data", "dataset.zip", "dowload/dataset.zip")