from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import uuid, os
from animegan import cartoonize_image

app = FastAPI(title="AI Cartoonizer")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/cartoonize")
async def cartoonize(file: UploadFile = File(...)):
    uid = str(uuid.uuid4())
    input_path = f"{UPLOAD_DIR}/{uid}_input.jpg"
    output_path = f"{UPLOAD_DIR}/{uid}_cartoon.jpg"

    with open(input_path, "wb") as buffer:
        buffer.write(await file.read())

    cartoonize_image(input_path, output_path)

    return FileResponse(output_path, media_type="image/jpeg", filename="cartoon.jpg")
