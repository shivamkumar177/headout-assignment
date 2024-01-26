from fastapi import APIRouter, HTTPException
from pathlib import Path
router = APIRouter()

BASE_PATH = Path("/tmp/data/")
# BASE_PATH = Path("files/")
@router.get('/data', status_code=200)
def get_line(n: int, m:int | None = None):
    file_path = BASE_PATH / f"{n}.txt"
    if file_path.exists():
        with open(file_path, 'r') as file:
            if m:
                lines = file.readlines()
                if 1 <= m <= len(lines):
                    return {"data": lines[m-1]}
                else:
                    raise HTTPException(status_code=400, detail="Invalid line number (m)")
            else:
                return {"data":str(file.readlines())}
    else:
        raise HTTPException(status_code=400, detail="File Not Found")