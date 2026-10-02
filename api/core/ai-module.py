“””
Personal AI Learning Service
This is YOUR private AI tutor/learning companion - NOT a shared backend
Runs locally on your machine for development and personal use
Integrates: SignSpeak API, Anthropic Claude, and your personal learning data
Deploy to: Your local machine, or your personal cloud instance when ready
“””

from fastapi import FastAPI, HTTPException, Depends, Header, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
import httpx
import jwt
import os
from datetime import datetime
import logging
from google.cloud import storage
from anthropic import Anthropic
import redis
import json

# Initialize FastAPI

app = FastAPI(
title=“MBTQ Personal AI Learning Service”,
description=“Your private AI tutor - runs locally for personal use only”
)

# CORS - Allow connections from your local frontend

app.add_middleware(
CORSMiddleware,
allow_origins=[
“http://localhost:3000”,  # Your local frontend
“http://localhost:5173”,  # Vite dev server
“https://mbtquniverse.com”,  # Your production frontend
],
allow_credentials=True,
allow_methods=[”*”],
allow_headers=[”*”],
)

# Logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(**name**)

# Clients

storage_client = storage.Client()
anthropic_client = Anthropic(api_key=os.getenv(“ANTHROPIC_API_KEY”))

# Redis - Optional for local development

try:
redis_client = redis.Redis(
host=os.getenv(“REDIS_HOST”, “localhost”),
port=int(os.getenv(“REDIS_PORT”, 6379)),
decode_responses=True
)
redis_client.ping()
REDIS_AVAILABLE = True
except:
logger.warning(“Redis not available - using in-memory storage”)
REDIS_AVAILABLE = False
# In-memory fallback for local dev
_memory_cache = {}

# Configuration

BUCKET_NAME = os.getenv(“GCP_BUCKET_NAME”, “mbtq-personal-learning”)
SIGN_SPEAK_API = os.getenv(“SIGN_SPEAK_API_URL”, “https://api.signspeak.ai”)
SIGN_SPEAK_KEY = os.getenv(“SIGN_SPEAK_API_KEY”)

# Your personal user ID (hardcoded for local dev)

MY_USER_ID = os.getenv(“MY_USER_ID”, “your-deafauth-user-id”)

# Models

class ASLRecognitionRequest(BaseModel):
video_base64: Optional[str] = None
video_url: Optional[str] = None
context: Optional[str] = “personal”  # Personal learning context

class ASLTranslationRequest(BaseModel):
text: str
target_language: str = “ASL”
include_animation: bool = True

class LearningAnswerRequest(BaseModel):
question_id: str
question_type: str  # “equation”, “comprehension”, “asl_practice”
user_answer: Any
context: Dict[str, Any] = {}

class AITutorRequest(BaseModel):
message: str
subject: Optional[str] = None
difficulty_level: Optional[str] = “adaptive”

class BundlePersonalizationRequest(BaseModel):
learning_style: Optional[str] = None
preferred_sign_language: Optional[str] = “ASL”
accessibility_needs: Dict[str, Any] = {}

# Simple auth - just for local development security

async def verify_local_token(authorization: str = Header(None)):
“”“Simple token verification for local development”””
if not authorization:
# In local dev, allow no auth
return {“sub”: MY_USER_ID}

```
# If production, verify JWT
if authorization.startswith("Bearer "):
    token = authorization.replace("Bearer ", "")
    try:
        payload = jwt.decode(
            token, 
            os.getenv("JWT_SECRET", "dev-secret"),
            algorithms=["HS256"]
        )
        return payload
    except:
        # Fallback to local user
        return {"sub": MY_USER_ID}

return {"sub": MY_USER_ID}
```

# Helper: Get/save your personal learning bundle

async def get_my_bundle() -> Dict[str, Any]:
“”“Load YOUR personal learning bundle”””

```
# Try cache first
if REDIS_AVAILABLE:
    cached = redis_client.get(f"my_bundle")
    if cached:
        return json.loads(cached)
else:
    if "my_bundle" in _memory_cache:
        return _memory_cache["my_bundle"]

# Load from GCP or local file
try:
    # Try GCP first
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(f"my_personal_bundle.json")
    
    if blob.exists():
        bundle_data = json.loads(blob.download_as_string())
    else:
        # Load from local file if exists
        local_bundle_path = "./my_learning_bundle.json"
        if os.path.exists(local_bundle_path):
            with open(local_bundle_path, 'r') as f:
                bundle_data = json.load(f)
        else:
            # Create new bundle
            bundle_data = {
                "user_id": MY_USER_ID,
                "learning_style": "visual",
                "preferred_sign_language": "ASL",
                "gamification_points": 0,
                "learning_progress": {},
                "accessibility_settings": {},
                "created_at": datetime.utcnow().isoformat()
            }
    
    # Cache it
    if REDIS_AVAILABLE:
        redis_client.setex(f"my_bundle", 3600, json.dumps(bundle_data))
    else:
        _memory_cache["my_bundle"] = bundle_data
    
    return bundle_data
except Exception as e:
    logger.error(f"Error loading bundle: {str(e)}")
    # Return default
    return {
        "user_id": MY_USER_ID,
        "learning_style": "visual",
        "preferred_sign_language": "ASL",
        "gamification_points": 0,
        "learning_progress": {},
        "accessibility_settings": {},
    }
```

async def save_my_bundle(bundle_data: Dict[str, Any]):
“”“Save YOUR personal bundle”””
try:
# Save to local file first (always)
with open(”./my_learning_bundle.json”, ‘w’) as f:
json.dump(bundle_data, f, indent=2)

```
    # Try to save to GCP
    try:
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(f"my_personal_bundle.json")
        blob.upload_from_string(json.dumps(bundle_data, indent=2))
    except:
        logger.warning("GCP save failed - using local file only")
    
    # Update cache
    if REDIS_AVAILABLE:
        redis_client.setex(f"my_bundle", 3600, json.dumps(bundle_data))
    else:
        _memory_cache["my_bundle"] = bundle_data
        
except Exception as e:
    logger.error(f"Error saving bundle: {str(e)}")
```

# Health check

@app.get(”/health”)
async def health_check():
return {
“status”: “healthy”,
“service”: “mbtq-personal-ai-learning”,
“mode”: “local_development”,
“user”: MY_USER_ID,
“integrations”: {
“signspeak”: SIGN_SPEAK_KEY is not None,
“anthropic”: anthropic_client is not None,
“redis”: REDIS_AVAILABLE,
“gcp”: True
}
}

# ASL Recognition (SignSpeak API)

@app.post(”/asl/recognize”)
async def recognize_asl(
request: ASLRecognitionRequest,
user_data: dict = Depends(verify_local_token)
):
“””
Recognize ASL from video using SignSpeak API
For YOUR personal learning
“””
try:
bundle = await get_my_bundle()

```
    # Call SignSpeak API
    async with httpx.AsyncClient(timeout=30.0) as client:
        payload = {
            "video": request.video_base64 or request.video_url,
            "language": bundle.get("preferred_sign_language", "ASL"),
            "context": request.context
        }
        
        response = await client.post(
            f"{SIGN_SPEAK_API}/v1/recognize",
            json=payload,
            headers={"Authorization": f"Bearer {SIGN_SPEAK_KEY}"}
        )
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="SignSpeak API error")
    
    result = response.json()
    
    # Log your learning progress
    await log_my_progress(
        "asl_recognition",
        result.get("recognized_signs", []),
        result.get("confidence", 0)
    )
    
    logger.info(f"ASL recognized: {result.get('recognized_signs')}")
    
    return {
        "success": True,
        "recognized_signs": result.get("recognized_signs", []),
        "confidence": result.get("confidence", 0),
        "suggestions": result.get("suggestions", []),
        "my_progress": bundle.get("learning_progress", {})
    }

except Exception as e:
    logger.error(f"ASL recognition error: {str(e)}")
    raise HTTPException(status_code=500, detail=str(e))
```

# ASL Translation

@app.post(”/asl/translate”)
async def translate_to_asl(
request: ASLTranslationRequest,
user_data: dict = Depends(verify_local_token)
):
“”“Translate text to ASL for YOUR learning”””
try:
bundle = await get_my_bundle()

```
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            f"{SIGN_SPEAK_API}/v1/translate",
            json={
                "text": request.text,
                "target_language": request.target_language,
                "include_animation": request.include_animation
            },
            headers={"Authorization": f"Bearer {SIGN_SPEAK_KEY}"}
        )
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Translation failed")
    
    result = response.json()
    
    return {
        "success": True,
        "original_text": request.text,
        "sign_sequence": result.get("signs", []),
        "animation_url": result.get("animation_url") if request.include_animation else None,
        "learning_tips": result.get("tips", [])
    }

except Exception as e:
    logger.error(f"Translation error: {str(e)}")
    raise HTTPException(status_code=500, detail=str(e))
```

# AI Tutor - YOUR personal AI tutor

@app.post(”/tutor/ask”)
async def my_ai_tutor(
request: AITutorRequest,
user_data: dict = Depends(verify_local_token)
):
“””
YOUR personal AI tutor powered by Claude
Knows YOUR learning history and preferences
“””
try:
bundle = await get_my_bundle()
learning_progress = bundle.get(“learning_progress”, {})

```
    # Build personalized prompt based on YOUR data
    system_prompt = f"""You are my personal AI tutor. You know my learning style and history.
```

My learning profile:

- Preferred sign language: {bundle.get(‘preferred_sign_language’, ‘ASL’)}
- Learning style: {bundle.get(‘learning_style’, ‘visual’)}
- Points earned so far: {bundle.get(‘gamification_points’, 0)}
- Recent progress: {json.dumps(learning_progress, indent=2)[:500]}

Guidelines for teaching me:

1. Use clear, visual metaphors (I’m a visual learner)
1. Avoid audio-centric language (I’m deaf)
1. Structure explanations spatially
1. Include ASL-compatible phrasing
1. Remember our previous conversations
1. Be encouraging and celebrate my progress
   “””
   
   ```
    # Get recent tutor history for context
    tutor_history = bundle.get("tutor_history", [])[-5:]  # Last 5 interactions
    
    messages = []
    for interaction in tutor_history:
        messages.append({"role": "user", "content": interaction["question"]})
        messages.append({"role": "assistant", "content": interaction["response"]})
    
    messages.append({"role": "user", "content": request.message})
    
    # Call Claude
    message = anthropic_client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=system_prompt,
        messages=messages
    )
    
    response_text = message.content[0].text
    
    # Store in YOUR tutor history
    await store_my_tutor_interaction(request.message, response_text)
    
    return {
        "success": True,
        "tutor_response": response_text,
        "subject": request.subject,
        "my_points": bundle.get("gamification_points", 0),
        "follow_up_suggestions": [
            "Can you show me a visual example?",
            "How would I sign this concept?",
            "Give me a practice problem"
        ]
    }
   ```
   
   except Exception as e:
   logger.error(f”AI tutor error: {str(e)}”)
   raise HTTPException(status_code=500, detail=str(e))

# Check YOUR answers

@app.post(”/learning/check-answer”)
async def check_my_answer(
request: LearningAnswerRequest,
user_data: dict = Depends(verify_local_token)
):
“”“Check YOUR learning answers with personalized AI feedback”””
try:
bundle = await get_my_bundle()

```
    prompt = f"""I'm a deaf student working on {request.question_type}.
```

Context: {json.dumps(request.context, indent=2)}
My answer: {request.user_answer}

Check if my answer is correct and give me visual, ASL-friendly feedback.
If I’m wrong, show me the correct approach step-by-step.
Be encouraging - I’m trying my best!

Respond as JSON:
{{
“correct”: true/false,
“feedback”: “your visual explanation”,
“correct_answer”: “if I got it wrong”,
“learning_tip”: “helpful tip for me”,
“points_earned”: number
}}
“””

```
    message = anthropic_client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    
    try:
        result = json.loads(message.content[0].text)
    except:
        result = {
            "correct": False,
            "feedback": message.content[0].text,
            "points_earned": 5
        }
    
    # Update MY points if correct
    if result.get("correct"):
        await update_my_points(
            "answer_correct",
            result.get("points_earned", 10)
        )
    
    return {
        "success": True,
        **result,
        "my_total_points": bundle.get("gamification_points", 0)
    }

except Exception as e:
    logger.error(f"Check answer error: {str(e)}")
    raise HTTPException(status_code=500, detail=str(e))
```

# Update YOUR personalization

@app.post(”/bundle/personalize”)
async def personalize_my_bundle(
request: BundlePersonalizationRequest,
user_data: dict = Depends(verify_local_token)
):
“”“Update YOUR personal AI tutor settings”””
try:
bundle = await get_my_bundle()

```
    if request.learning_style:
        bundle["learning_style"] = request.learning_style
    if request.preferred_sign_language:
        bundle["preferred_sign_language"] = request.preferred_sign_language
    if request.accessibility_needs:
        bundle["accessibility_settings"].update(request.accessibility_needs)
    
    bundle["updated_at"] = datetime.utcnow().isoformat()
    await save_my_bundle(bundle)
    
    return {
        "success": True,
        "message": "Your personal AI tutor has been updated!",
        "your_settings": {
            "learning_style": bundle["learning_style"],
            "preferred_sign_language": bundle["preferred_sign_language"],
            "total_points": bundle.get("gamification_points", 0)
        }
    }

except Exception as e:
    logger.error(f"Personalization error: {str(e)}")
    raise HTTPException(status_code=500, detail=str(e))
```

# Helper functions for YOUR personal data

async def log_my_progress(activity_type: str, data: Any, confidence: float):
“”“Log YOUR learning progress”””
try:
bundle = await get_my_bundle()

```
    if "learning_progress" not in bundle:
        bundle["learning_progress"] = {}
    
    if activity_type not in bundle["learning_progress"]:
        bundle["learning_progress"][activity_type] = []
    
    bundle["learning_progress"][activity_type].append({
        "timestamp": datetime.utcnow().isoformat(),
        "data": data,
        "confidence": confidence
    })
    
    await save_my_bundle(bundle)
except Exception as e:
    logger.error(f"Error logging progress: {str(e)}")
```

async def store_my_tutor_interaction(question: str, response: str):
“”“Store YOUR tutor conversation history”””
try:
bundle = await get_my_bundle()

```
    if "tutor_history" not in bundle:
        bundle["tutor_history"] = []
    
    bundle["tutor_history"] = bundle["tutor_history"][-19:] + [{
        "timestamp": datetime.utcnow().isoformat(),
        "question": question,
        "response": response
    }]
    
    await save_my_bundle(bundle)
except Exception as e:
    logger.error(f"Error storing interaction: {str(e)}")
```

async def update_my_points(event_type: str, points: int):
“”“Update YOUR gamification points”””
try:
bundle = await get_my_bundle()
bundle[“gamification_points”] = bundle.get(“gamification_points”, 0) + points
await save_my_bundle(bundle)

```
    logger.info(f"🎉 You earned {points} points! Total: {bundle['gamification_points']}")
    
    return bundle["gamification_points"]
except Exception as e:
    logger.error(f"Points update error: {str(e)}")
    return 0
```

if **name** == “**main**”:
import uvicorn
print(“🚀 Starting YOUR personal AI learning service…”)
print(f”👤 User: {MY_USER_ID}”)
print(f”📚 Your learning data will be saved to: ./my_learning_bundle.json”)
print(f”🌐 API running at: http://localhost:8000”)
print(f”📖 API docs at: http://localhost:8000/docs”)
uvicorn.run(app, host=“0.0.0.0”, port=8000)