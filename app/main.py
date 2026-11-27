from fastapi import FastAPI 

app = FastAPI(title = "Hi-app")

@app.get("/")
def root ():
    return{"hello world welcome"}

#health
@app.get("/health")
def health ():
    return {"status":"ok"}

