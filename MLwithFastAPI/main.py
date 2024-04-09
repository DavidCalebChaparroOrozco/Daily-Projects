<<<<<<< HEAD
import io
import pickle
import numpy as np
import PIL.Image, PIL.ImageOps
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

with open('mnist_model.pkl',"rb") as file:
    model = pickle.load(file)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_header=["*"],
)

@app.post("/predict-image/")
async def predict_image(file:UploadFile = File(...)):
    contents = await file.read()
    pil_image = PIL.Image.open(io.BytesIO(contents)).conert('L')
    pil_image = PIL.ImageOps.invert(pil_image)
    pil_image = pil_image.resize((28,28), PIL.Image.ANTIALIAS)
    img_array = np.array(pil_image).reshape(1,-1)
    prediction = model.predict(img_array)
    return {"prediction": int(prediction[0])}


=======
import io
import pickle
import numpy as np
import PIL.Image, PIL.ImageOps
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

with open('mnist_model.pkl',"rb") as file:
    model = pickle.load(file)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_header=["*"],
)

@app.post("/predict-image/")
async def predict_image(file:UploadFile = File(...)):
    contents = await file.read()
    pil_image = PIL.Image.open(io.BytesIO(contents)).conert('L')
    pil_image = PIL.ImageOps.invert(pil_image)
    pil_image = pil_image.resize((28,28), PIL.Image.ANTIALIAS)
    img_array = np.array(pil_image).reshape(1,-1)
    prediction = model.predict(img_array)
    return {"prediction": int(prediction[0])}


>>>>>>> df0de19 (Day 27)
