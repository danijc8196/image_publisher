#!/usr/bin/env python

import rospy, time
import AirSimClient as airsim
from std_msgs.msg import String


if __name__ == '__main__':

    rospy.init_node("image_publisher", anonymous=False)
    
    pub_img_depth = rospy.Publisher('camera/images/depth', String, queue_size=1)
    pub_img_segmentation = rospy.Publisher('camera/images/segmentation', String, queue_size=1)
    pub_img_scene = rospy.Publisher('camera/images/scene', String, queue_size=1)

    client = airsim.MultirotorClient("127.0.0.1")
    client.confirmConnection()
    time.sleep(1)
    
    while True:
        img_depth = client.simGetImage(0, airsim.AirSimImageType.DepthVis)
        img_segmentation = client.simGetImage(0, airsim.AirSimImageType.Segmentation)
        img_scene = client.simGetImage(0, airsim.AirSimImageType.Scene)    
    
        if img_depth != None:
            pub_img_depth.publish(String(img_depth))
        
        if img_segmentation != None:
            pub_img_segmentation.publish(String(img_segmentation))

        if img_depth != None:
            pub_img_scene.publish(String(img_scene))

        time.sleep(1)