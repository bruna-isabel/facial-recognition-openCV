import face_recognition

image = face_recognition.load_image_file('./img/groups/team1.jpg')
face_locations = face_recognition.face_locations(image)

# Outputs array of coordinates of each face
print(f'There are {len(face_locations)} people in this image')