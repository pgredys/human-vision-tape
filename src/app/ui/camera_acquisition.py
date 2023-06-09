import time

import pyrealsense2 as rs
import numpy as np
import cv2
import PIL


def distance_segmentation_from_515(min_dist: float, max_dist: float) -> object:
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
    profile = pipeline.start(config)

    depth_sensor = profile.get_device().first_depth_sensor()
    depth_scale = depth_sensor.get_depth_scale()

    min_distance = min_dist / depth_scale
    max_distance = max_dist / depth_scale

    align_to = rs.stream.color
    align = rs.align(align_to)

    frames = pipeline.wait_for_frames()
    aligned_frames = align.process(frames)

    aligned_depth_frame = aligned_frames.get_depth_frame()
    color_frame = aligned_frames.get_color_frame()

    depth_image = np.asanyarray(aligned_depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())

    filler_color = 255
    depth_image_3d = np.dstack((depth_image, depth_image, depth_image))
    bg_removed = np.where((depth_image_3d > max_distance) | (depth_image_3d <= min_distance), filler_color, color_image)

    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
    pipeline.stop()
    return np.hstack((bg_removed, depth_colormap))


if __name__ == "__main__":
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
    profile = pipeline.start(config)

    # start_time = time.time()
    images = distance_segmentation_from_515(min_dist=0.1, max_dist=3)
    # print("--- %s seconds ---" % (time.time() - start_time))
    # pipeline.stop()

    images = cv2.cvtColor(images, cv2.COLOR_BGR2RGB)
    output_images = PIL.Image.fromarray(images)
    output_images.show()
