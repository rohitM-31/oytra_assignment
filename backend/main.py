
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from llm_validator import validate_order_details

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"]
)


class CustomerDetails(BaseModel):
    customer_name: str
    address: str
    city: str
    state: str
    pincode: str


@app.post("/validate-address")
def validate_address(data: CustomerDetails):

    # Call your Gemini Python function
    result = validate_order_details(
        data.customer_name,
        data.address,
        data.city,
        data.state,
        data.pincode
    )

    return result
