from fastapi import FastAPI, File, UploadFile
import src.predict as predict

app = FastAPI()

@app.get('/')
def hello():
    return 'Hello!'

@app.get('/predict')
def predict_from_url(url):
    return predict.predict(url)

@app.post('/predict')
def predict_from_file(file: UploadFile = File(...)):
    return predict.predict(file.file)
