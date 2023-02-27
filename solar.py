import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
    "sun",
    (100,100),
    cv2.FONT_HERSHEY_COMPLEX,
    2,
    (200,200,134)
)

cv2.putText(img,
    "mercury",
    (100,180),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (200,200,134)
)

cv2.putText(img,
    "venus",
    (200,250),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (200,200,134)
)

cv2.putText(img,
    "Earth",
    (300,280),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (200,200,134)
)

cv2.putText(img,
    "Mars",
    (400,280),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (200,200,134)
)

cv2.putText(img,
    "Jupiter",
    (550,350),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (200,200,134)
)

cv2.putText(img,
    "saturn",
    (680,250),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (200,200,134)
)

cv2.putText(img,
    "Uranus",
    (1000,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (200,200,134)
)

cv2.putText(img,
    "Neptune",
    (1100,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (200,200,134)
)
cv2.imshow("output",img)
cv2.waitKey(0)

