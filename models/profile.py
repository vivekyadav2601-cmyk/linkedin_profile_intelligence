from typing import List
from pydantic import BaseModel, Field
class Experience(BaseModel):
    company: str = ''; role: str = ''; duration: str = ''; description: str = ''
class Education(BaseModel):
    institution: str = ''; degree: str = ''; field: str = ''; year: str = ''
class Profile(BaseModel):
    name: str = ''; headline: str = ''; location: str = ''; about: str = ''
    current_role: str = ''; current_company: str = ''
    experience: List[Experience] = Field(default_factory=list)
    education: List[Education] = Field(default_factory=list)
    skills: List[str] = Field(default_factory=list)
    certifications: List[str] = Field(default_factory=list)
    projects: List[str] = Field(default_factory=list)
    achievements: List[str] = Field(default_factory=list)
    languages: List[str] = Field(default_factory=list)
    profile_url: str = ''
