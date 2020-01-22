import face_recognition

image_bill_gates = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
bill_face_encoding = face_recognition.face_encodings(image_bill_gates)[0]

unknown = face_recognition.load_image_file('./img/unknown/gates_lookalike.jpg')
unknown_encoding = face_recognition.face_encodings(unknown)[0]

# Compare faces 
results = face_recognition.compare_faces([bill_face_encoding], unknown_encoding)

if results[0]:
    print('This is Bill Gates')
else:
    print('Not Bill Gates')
