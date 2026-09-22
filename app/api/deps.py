from fastapi import Depends

# Mock dependency for db, auth, etc. if needed later
async def get_current_user():
    return {"user_id": "test_user"}
