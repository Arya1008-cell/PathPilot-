from fastapi import FastAPI
from pydantic import BaseModel
from langgraph_flow import build_graph
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Fix frontend-backend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

graph = build_graph()


class UserProfile(BaseModel):
    profile: str


@app.post("/analyze")
async def analyze(data: UserProfile):

    if not data.profile:
        return {"error": "Profile cannot be empty"}

    try:
        result = graph.invoke({"profile": data.profile})
        return result

    except Exception as e:
        return {"error": str(e)}
