import torch
import cv2
import numpy as np

# Auto downloads model on first run (~90MB)
model = torch.hub.load(
    "bryandlee/animegan2-pytorch:main",
    "generator",
    pretrained=True
).eval()


def cartoonize_image(input_path, output_path):
    img = cv2.imread(input_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    h, w = img.shape[:2]
    img = cv2.resize(img, (512, 512))

    img = img.astype(np.float32) / 255.0
    img = torch.from_numpy(img.transpose(2,0,1)).unsqueeze(0)

    with torch.no_grad():
        out = model(img)[0].cpu().numpy()

    out = np.clip(out.transpose(1,2,0), 0, 1)
    out = (out * 255).astype(np.uint8)
    out = cv2.cvtColor(out, cv2.COLOR_RGB2BGR)

    cv2.imwrite(output_path, out)
