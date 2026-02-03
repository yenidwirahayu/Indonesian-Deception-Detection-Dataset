# landmark_annotations.py
"""
MediaPipe Landmark Annotations
Compliant with MediaPipe FaceMesh v0.8+ specification

FaceMesh: 468 landmarks (0-467)
Iris: 10 landmarks (468-477) - requires refine_landmarks=True
Pose: 33 landmarks (0-32)
"""

# ============================================================================
# FACEMESH LANDMARKS (0-467) - 468 LANDMARKS
# ============================================================================
# NOTE: Landmarks 271-280 are NOT iris! They are part of face mesh.
# Real iris landmarks are 468-477 (separate, requires refine_landmarks=True)

FACEMESH_LANDMARKS = {
    # Silhouette & Jawline (0-32)
    "Contour_Chin": 0,
    "Contour_Left_Jawline": list(range(1, 17)),
    "Contour_Right_Jawline": list(range(17, 33)),
    
    # Eyebrows (33-50)
    "Contour_Left_Eyebrow": list(range(33, 42)),
    "Contour_Right_Eyebrow": list(range(42, 51)),
    
    # Nose (51-59)
    "Nose_Bridge": list(range(51, 55)),
    "Nose_Bottom": list(range(55, 60)),
    
    # Eyes (60-91)
    "Left_Eye_Upper": list(range(60, 68)),
    "Left_Eye_Lower": list(range(68, 76)),
    "Right_Eye_Upper": list(range(76, 84)),
    "Right_Eye_Lower": list(range(84, 92)),
    
    # Lips (92-128)
    "Lips_Upper_Outer": list(range(92, 103)),
    "Lips_Upper_Inner": list(range(103, 111)),
    "Lips_Lower_Inner": list(range(111, 119)),
    "Lips_Lower_Outer": list(range(119, 129)),
    
    # Eyebrow Details (129-160)
    "Left_Eyebrow_Upper": list(range(129, 137)),
    "Left_Eyebrow_Lower": list(range(137, 145)),
    "Right_Eyebrow_Upper": list(range(145, 153)),
    "Right_Eyebrow_Lower": list(range(153, 161)),
    
    # Eye Contours (161-184)
    "Left_Eye_Contour": list(range(161, 173)),
    "Right_Eye_Contour": list(range(173, 185)),
    
    # Nose Contours (185-217)
    "Nose_Left_Contour": list(range(185, 197)),
    "Nose_Right_Contour": list(range(197, 209)),
    "Nose_Tip": list(range(209, 218)),
    
    # Lips Details (218-239)
    "Lips_Upper_Outer_Detail": list(range(218, 228)),
    "Lips_Lower_Outer_Detail": list(range(228, 238)),
    "Lips_Corner": [238, 239],
    
    # Face Oval (240-270)
    "Face_Oval": list(range(240, 271)),
    
    # ✅ IMPORTANT: Landmarks 271-280 are NOT iris!
    # They are part of face mesh (possibly eye region details)
    "Left_Eye_Region": list(range(271, 276)),    # NOT iris!
    "Right_Eye_Region": list(range(276, 281)),   # NOT iris!
    
    # Forehead (281-309)
    "Forehead_Center": list(range(281, 290)),
    "Forehead_Left": list(range(290, 300)),
    "Forehead_Right": list(range(300, 310)),
    
    # Cheeks (310-339)
    "Left_Cheek": list(range(310, 325)),
    "Right_Cheek": list(range(325, 340)),
    
    # Nose Details (340-364)
    "Nose_Bridge_Detail": list(range(340, 350)),
    "Nose_Tip_Detail": list(range(350, 365)),
    
    # Chin Details (365-379)
    "Chin_Detail": list(range(365, 380)),
    
    # Eye Details (380-413)
    "Left_Eye_Detail": list(range(380, 397)),
    "Right_Eye_Detail": list(range(397, 414)),
    
    # Mouth Details (414-437)
    "Mouth_Detail": list(range(414, 438)),
    
    # Eyebrow Details (438-467)
    "Eyebrow_Detail": list(range(438, 468))
}

# ============================================================================
# IRIS LANDMARKS (468-477) - 10 LANDMARKS
# ============================================================================
# These are SEPARATE from FaceMesh 468 landmarks
# Requires: mp_face_mesh.FaceMesh(refine_landmarks=True)
# MediaPipe Iris Model: 5 landmarks per eye
#   - Center (pupil center)
#   - Left, Top, Right, Bottom (iris boundary)

IRIS_LANDMARKS = {
    # Left Iris (468-472)
    'Left_Iris_Center': 468,
    'Left_Iris_Right': 469,    # Right side of left iris (from camera view)
    'Left_Iris_Top': 470,
    'Left_Iris_Left': 471,     # Left side of left iris (from camera view)
    'Left_Iris_Bottom': 472,
    
    # Right Iris (473-477)
    'Right_Iris_Center': 473,
    'Right_Iris_Right': 474,   # Right side of right iris (from camera view)
    'Right_Iris_Top': 475,
    'Right_Iris_Left': 476,    # Left side of right iris (from camera view)
    'Right_Iris_Bottom': 477
}

# ============================================================================
# POSE LANDMARKS (0-32) - 33 LANDMARKS
# ============================================================================
# MediaPipe Pose BlazePose model

POSE_LANDMARKS = {
    # Face (0-10)
    'NOSE': 0,
    'LEFT_EYE_INNER': 1,
    'LEFT_EYE': 2,
    'LEFT_EYE_OUTER': 3,
    'RIGHT_EYE_INNER': 4,
    'RIGHT_EYE': 5,
    'RIGHT_EYE_OUTER': 6,
    'LEFT_EAR': 7,
    'RIGHT_EAR': 8,
    'MOUTH_LEFT': 9,
    'MOUTH_RIGHT': 10,
    
    # Upper Body (11-22)
    'LEFT_SHOULDER': 11,
    'RIGHT_SHOULDER': 12,
    'LEFT_ELBOW': 13,
    'RIGHT_ELBOW': 14,
    'LEFT_WRIST': 15,
    'RIGHT_WRIST': 16,
    'LEFT_PINKY': 17,
    'RIGHT_PINKY': 18,
    'LEFT_INDEX': 19,
    'RIGHT_INDEX': 20,
    'LEFT_THUMB': 21,
    'RIGHT_THUMB': 22,
    
    # Lower Body (23-32)
    'LEFT_HIP': 23,
    'RIGHT_HIP': 24,
    'LEFT_KNEE': 25,
    'RIGHT_KNEE': 26,
    'LEFT_ANKLE': 27,
    'RIGHT_ANKLE': 28,
    'LEFT_HEEL': 29,
    'RIGHT_HEEL': 30,
    'LEFT_FOOT_INDEX': 31,
    'RIGHT_FOOT_INDEX': 32
}

# ============================================================================
# COMBINE ALL LANDMARKS
# ============================================================================

ALL_LANDMARKS = {}

# Add FaceMesh landmarks (0-467)
for region, landmarks in FACEMESH_LANDMARKS.items():
    if isinstance(landmarks, list):
        for i, landmark in enumerate(landmarks):
            ALL_LANDMARKS[f"{region}_{i}"] = landmark
    else:
        ALL_LANDMARKS[region] = landmarks

# Add Pose landmarks (0-32)
ALL_LANDMARKS.update(POSE_LANDMARKS)

# Add Iris landmarks (468-477)
ALL_LANDMARKS.update(IRIS_LANDMARKS)

# ============================================================================
# VERIFICATION
# ============================================================================

def verify_landmarks():
    """Verify landmark counts match MediaPipe specification"""
    
    # Count FaceMesh landmarks
    facemesh_indices = set()
    for region, landmarks in FACEMESH_LANDMARKS.items():
        if isinstance(landmarks, list):
            facemesh_indices.update(landmarks)
        else:
            facemesh_indices.add(landmarks)
    
    # Count Iris landmarks
    iris_indices = set(IRIS_LANDMARKS.values())
    
    # Count Pose landmarks
    pose_indices = set(POSE_LANDMARKS.values())
    
    print("="*70)
    print("LANDMARK VERIFICATION")
    print("="*70)
    print(f"FaceMesh landmarks: {len(facemesh_indices)} (expected: 468)")
    print(f"  Range: {min(facemesh_indices)}-{max(facemesh_indices)}")
    print(f"  Expected: 0-467")
    print(f"  Match: {'✅' if len(facemesh_indices) == 468 and min(facemesh_indices) == 0 and max(facemesh_indices) == 467 else '❌'}")
    
    print(f"\nIris landmarks: {len(iris_indices)} (expected: 10)")
    print(f"  Range: {min(iris_indices)}-{max(iris_indices)}")
    print(f"  Expected: 468-477")
    print(f"  Match: {'✅' if len(iris_indices) == 10 and min(iris_indices) == 468 and max(iris_indices) == 477 else '❌'}")
    
    print(f"\nPose landmarks: {len(pose_indices)} (expected: 33)")
    print(f"  Range: {min(pose_indices)}-{max(pose_indices)}")
    print(f"  Expected: 0-32")
    print(f"  Match: {'✅' if len(pose_indices) == 33 and min(pose_indices) == 0 and max(pose_indices) == 32 else '❌'}")
    
    print(f"\nTotal landmarks: {len(facemesh_indices) + len(iris_indices) + len(pose_indices)}")
    print(f"Expected: 511 (468 face + 10 iris + 33 pose)")
    print("="*70)
    
    return len(facemesh_indices) == 468 and len(iris_indices) == 10 and len(pose_indices) == 33


if __name__ == "__main__":
    verify_landmarks()
