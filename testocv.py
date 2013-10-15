import cv
 
cv.NamedWindow("camera", 1)
capture = cv.CaptureFromCAM(0)

while True:
    img = cv.QueryFrame(capture)
    cv.ShowImage("camera", img)
    if cv.WaitKey(10) == 27:
        break
cv.DestroyWindow("camera")



# import cv

# capture = cv.CaptureFromCAM(0)
# frame = cv.QueryFrame(capture)
# cv.SaveImage("c:/Programming/test/capture.jpg", frame)


# import cv

# capture = cv.CaptureFromCAM(-1)
# cv.NamedWindow("capture", cv.CV_WINDOW_AUTOSIZE)

# i = 0
# while True:
#     frame = cv.QueryFrame(capture)
#     cv.ShowImage("capture", frame)
#     cv.WaitKey(10)
#     path = "capture%.4d.jpg" % i 
#     cv.SaveImage(path, frame)
#     i += 1