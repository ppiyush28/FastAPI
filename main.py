from fastapi import FastAPI, Path, HTTPException
import uvicorn,json

app = FastAPI()


@app.get("/")
def hello():
    return "welcome to fastapi learning"

@app.post("/view")
def view():
    return "welcome in view"

@app.post("/dataview")
def dataview():
    with open("data.json","r") as file:
        data = json.load(file)
    return data
    
@app.get("/dydata/{id}")
def dydata(id:str = Path(description="id of patient in file")):
    with open("data.json","r") as file:
        data = json.load(file)

    if id in data:
        return data[id]
    raise HTTPException("data not present")



# if __name__ == "__main__":
#     uvicorn.run(app=app)




