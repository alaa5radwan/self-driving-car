#######################prepare Your dataset##################################
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="4kPEAeQIuuSxjFLQXHFx")
project = rf.workspace("object-detection-onsq3").project("more-speedbump")
dataset = project.version(1).download("yolov8")

#########################install YOLOv8####################################
!pip install ultralytics==8.0.196
from ultralytics import YOLO

#########################start training####################################
!yolo task=detect mode=train model=yolov8n.pt data=/content/drive/MyDrive/more-speedbump-1/data.yaml epochs=100 imgsz=800 plots=True
