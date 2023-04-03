# AIRBOARD

A project made using Python and OpenCV by which we can draw lines and shapes on the screen by moving a red object on the screen.

**How it works**:

- A red(used for drawing) object is detected by creating a color mask using an HSV range and seperating the objects which fall in that range. A bounding rectangle is created around the red object.
- The coordinates of the upper left and lower right corners of the bounding rectangle is sent to the `get_mid_box` method to calculate the middle coordinates of that rectangle.
- The mid coordinates are appened to a list which gets converted into a numpy array. This numpy array is provided to the `drawContours` method which draws the lines on the webcam video frames.
- The red colored object is tracked by using an object tracking algorithm provided by the OpenCV library

*So far the [CSRT](https://arxiv.org/pdf/1611.08461.pdf) algorithm provides the best accuracy*

### Demo

<img src="assets/screencast.gif" alt="demo" width="600px" height="400px">