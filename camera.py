import cv2
import os
import torch

model = torch.hub.load('./', 'custom', path='D:\code\RUAS-main\ckpt\dark.pt',source='local')
# model.iou=0.7
model.device=0

def detect():
    cap = cv2.VideoCapture(0)

    while True:
        ret,frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame= cv2.flip(frame,1)

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        cv2.imshow('M', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()

if __name__ == '__main__':
    detect()


