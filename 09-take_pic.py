import time
import picamera
import helper


in_humid, in_temp = helper.sensor_reading()
annotation_txt = f' Temp: {in_temp}C Hum: {in_humid}% '
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.annotate_background = picamera.Color('black')
    camera.annotate_text = annotation_txt
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    print('taking pic')
    camera.capture('SendPic.jpg')
