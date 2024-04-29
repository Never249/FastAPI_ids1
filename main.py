from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_name():
    return {
        "first_name": "Шмидт",
        "last_name": "Артур",
        "sur_name": "Александрович",
    }


@app.get("/users")
def get_contact_info():
    return {
        "phone": "+7-800-555-35-35",
    }


@app.get("/tools")
def get_info():
    return {
        "Labs": {
            "python": [
                "3.12",
                "FastAPI",
            ],
            "backend": [
                "lab1"
            ]
        },
    }