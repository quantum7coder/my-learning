import cv2
import mediapipe as mp

# Initialize mediapipe
mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Configure Face Mesh and Hands
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=10, refine_landmarks=True)
hands = mp_hands.Hands(max_num_hands=2)
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.flip(frame, 1)  # Mirror image
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process detections
    face_results = face_mesh.process(rgb_frame)
    hand_results = hands.process(rgb_frame)

    # Check for any human detection
    human_detected = False

    # Draw face landmarks if found
    if face_results.multi_face_landmarks:
        human_detected = True
        for face_landmarks in face_results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=drawing_spec
            )

    # Draw hand landmarks if found
    if hand_results.multi_hand_landmarks:
        human_detected = True
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image=frame,
                landmark_list=hand_landmarks,
                connections=mp_hands.HAND_CONNECTIONS,
                landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=drawing_spec
            )

    # Display "Human detected" label
    if human_detected:
        cv2.putText(frame, "Human detected", (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2, cv2.LINE_AA)

    # Show the result
    cv2.imshow("Face & Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
