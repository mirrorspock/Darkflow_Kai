kai_video:
  recognise saved video
  
kai_resample_video:
  used to resample video

kai_camera:
  uses yolo weights to detect camera images


new_model_data:
  kai_get_images:
    gets images via google
  kai_generate_xml:
    used to generate xml

command to train with new data:
flow --model cfg/kai-tiny-yolo-voc-1c.cfg --load bin/yolov2.weights --train --annotation train/Annotations --dataset train/Images

kai_camera-learned:
  uses new learned weights