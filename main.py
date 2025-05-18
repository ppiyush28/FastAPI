from fastapi import FastAPI, Path, HTTPException, Query
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
def dydata(id:str = Path(..., description="id of patient in file")):
    with open("data.json","r") as file:
        data = json.load(file)

    if id in data:
        return data[id]
    raise HTTPException("data not present")


@app.get("/sort")
def sort_data(sort_by :str = Query(..., description="sort on basis of height,weight,bmi"), order : str= Query('asc', description="sort in asc or desc")):

    valid_fields = [ 'heaight', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, details = 'invalid field selected from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, details = ' invalid order seletected')
    
    with open("data.json","r") as file:
        data = json.load(file)

    sort_order = True if order == 'desc' else False 

    sort_data = sorted(data.values(), key=lambda x : x.get(sort_by,0), reverse= sort_order)

    return sort_data



# if __name__ == "__main__":
#     uvicorn.run(app=app)




