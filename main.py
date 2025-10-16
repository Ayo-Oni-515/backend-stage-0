from datetime import datetime, timezone

import requests
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware



# main application entry point
app = FastAPI(
    title="HNG 13",
    description="stage 0 backend track"
)

# CORS Management
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"]
)

# personal details
EMAIL = "ayodejioni1505@gmail.com"
NAME = "Oni Ayodeji Mahmuud"
STACK = "Python/FastAPI"
CAT_FACT_API = "https://catfact.ninja/fact"


# /me endpoint
@app.get("/me")
async def profile_information():
    """a public endpoint that returns my personal
    profile information alongside a dynamic cat fact.
    """
    try:

        response = requests.get(
            CAT_FACT_API,
            timeout=20.0
        )

        FACT = (response.json())['fact']

    except requests.exceptions.Timeout:

        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="Cat fact API timed out!"
        )
    except Exception:

        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Cat fact API is unresponsive!")

    TIMESTAMP: str = datetime.now(
        timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "success",
            "user": {
                "email": EMAIL,
                "name": NAME,
                "stack": STACK
            },
            "timestamp": TIMESTAMP,
            "fact": FACT
        }
    )
