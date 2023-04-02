import tracking
import cv2


def main():
    track = tracking.Tracker()      # instantiate tracker class
    cap = cv2.VideoCapture(0)       # capture webcam video
    tracker = cv2.legacy.TrackerTLD_create()    # initialise the tracker
    ret, first = cap.read()                          # read first frame
    bbox = track.make_box(first)                # make box around red color object
    tracker.init(first, bbox)                   # initialise the tracker on the first frame

    while True:
        ok, frame = cap.read()
        track.track_object(ok, frame, tracker)


if __name__ == '__main__':
    main()

