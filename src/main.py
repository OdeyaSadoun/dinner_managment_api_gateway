from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
import uvicorn

from infrastructures.factory import Factory

# יצירת אפליקציית FastAPI
app = FastAPI()

# חיבור כל הרואטרים
routes = Factory.create_all()
print("ROUTES:")
for router in routes:
    print(" -", router.prefix)
    app.include_router(router.get_router(), prefix=router.prefix)

# הגשת הקליינט מתוך dist
dist_path = os.path.join(os.path.dirname(__file__), "dist")
print(f"dist_path = {dist_path}")
if os.path.exists(dist_path):
    print("dist folder found")
    app.mount("/", StaticFiles(directory=dist_path, html=True), name="static")
else:
    print("dist folder NOT found")

# הרצת השרת
if __name__ == "__main__":
    print("Running FastAPI on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
