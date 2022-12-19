

#images not taken at cruising altitude should be discarded
import cv2
from google.colab.patches import cv2_imshow
input_video = cv2.VideoCapture('/content/drive/My Drive/P1rural/droneFootage1.mp4')

# Metadata from the input video
frames_per_second = int(input_video.get(cv2.CAP_PROP_FPS))
frame_width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

num_frames = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))



print('Metadata from input video:',
      '\nFrames per second:', frames_per_second,
      '\nFrame width:', frame_width, 
      '\nFrame height:', frame_height)
codec = cv2.VideoWriter.fourcc(*'XVID')
video_writer = cv2.VideoWriter('output_video.mp4', 
                               codec, 
                               frames_per_second, 
                               (frame_width, frame_height))
# An array to hold the locations of faces that are detected on individual frames
face_locations = []

# A counter to keep track of the number of frames processed
count = 0
one_photo = []

# Loop through all the frames in the video
while (count != 3000):
  # Read the video to retrieve individual frames. 'frame' will reference the inidivdual frames read from the video.
  ret, frame = input_video.read()

  # Check the 'ret' (return value) to see if we have read all the frames in the video to exit the loop
  if not ret:
    print('Processed all frames')
    break

  # Convert the image (frame) to RGB format as by default Open CV uses BGR format. 
  # This conversion is done as face_recognition and other libraries usually use RGB format.
  rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

  
  # Loop through the face locations array and draw a rectangle around each face that is detected in the frame
  for top, right, bottom, left in face_locations:
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

  # Write the frame to the output vide0
  #video_writer.write(frame)
  x = 680 #30 frames per second, about 22 seconds captures frame for each new area
  # Print for every x frames processed
  if(count % x == 0):
    frame = cv2.resize(frame, (256, 256), interpolation=cv2.INTER_AREA)
    cv2_imshow(frame)
    img = frame
    img = cv2.resize(img, (256, 256), interpolation=cv2.INTER_AREA)
    one_photo.append(img)

    print('Processed', count, 'frames')

  count += 1

one_photo = np.array(one_photo)

predictions2 = model.predict(one_photo,verbose=1)

# Release to close all the resources that we have opened for reading and writing video
#input_video.release()
#video_writer.release() 

#cv2.destroyAllWindows()