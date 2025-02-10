from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional, List
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str

class WorkoutType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class MuscleGroup(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class WorkoutName(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    workout_type_id: int = Field(foreign_key="workouttype.id")

class WorkoutLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    workout_name_id: int = Field(foreign_key="workoutname.id")
    workout_date: datetime
    sets: int
    reps: int
    weight: float

class PerformanceStats(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    workout_name_id: int = Field(foreign_key="workoutname.id")
    personal_record: float
    frequency: int

# Database setup
sqlite_file_name = "workout_tracking.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)