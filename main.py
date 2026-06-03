import json
from pathlib import Path
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(
    title="Course Records API",
    description="JSON 파일 기반 수강기록 관리 FastAPI 서버",
    version="1.0.0"
)

DATA_FILE = Path("courses.json")


class Course(BaseModel):
    course_name: str = Field(..., min_length=1, description="과목명")
    year: str = Field(..., min_length=4, max_length=4, description="이수연도")
    semester: str = Field(..., min_length=1, max_length=1, description="이수학기")
    grade: str = Field(..., min_length=1, description="성적")


def load_courses() -> List[dict]:
    """
    courses.json 파일에서 전체 수강기록을 읽어오는 함수입니다.
    """
    try:
        if not DATA_FILE.exists():
            return []

        with open(DATA_FILE, "r", encoding="utf-8-sig") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise HTTPException(
                status_code=500,
                detail="courses.json 파일의 최상위 구조는 list여야 합니다."
            )

        return data

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="courses.json 파일의 JSON 형식이 올바르지 않습니다."
        )


def save_courses(courses: List[dict]) -> None:
    """
    수강기록 리스트를 courses.json 파일에 저장하는 함수입니다.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(courses, file, ensure_ascii=False, indent=2)


@app.get("/")
def read_root():
    return {
        "message": "Course Records API 서버가 실행 중입니다.",
        "endpoints": {
            "GET /courses": "전체 수강기록 조회",
            "POST /courses": "새 수강기록 추가"
        }
    }


@app.get("/courses")
def get_courses():
    """
    GET /courses

    courses.json 파일에 저장된 전체 수강기록 리스트를 반환합니다.
    """
    courses = load_courses()
    return courses


@app.post("/courses")
def create_course(course: Course):
    """
    POST /courses

    요청 body로 전달된 새 수강기록을 기존 JSON list에 추가한 뒤,
    courses.json 파일에 다시 저장합니다.
    """
    courses = load_courses()

    new_course = course.model_dump()
    courses.append(new_course)

    save_courses(courses)

    return {
        "message": "수강기록이 추가되었습니다.",
        "added_course": new_course,
        "total_count": len(courses)
    }