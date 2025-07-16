from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

async def test():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client.school_activities
    cursor = db.activities.find({})
    docs = await cursor.to_list(length=None)
    print(f"Found {len(docs)} activities")
    for doc in docs:
        print(f"- {doc["_id"]}")

asyncio.run(test())
