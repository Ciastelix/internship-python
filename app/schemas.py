from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, BaseConfig, conlist, validator

class LocationSchema(BaseModel):
    id: int
    name: str
    tag: str

    class Config(BaseConfig):
        arbitrary_types_allowed = True

class RoleSchema(BaseModel):
    id: int
    name: str
    shortcut: str

    class Config(BaseConfig):
        arbitrary_types_allowed = True
        orm_mode =  True

class TeamSchema(BaseModel):
    id: int
    name: str

    class Config(BaseConfig):
        arbitrary_types_allowed = True
        orm_mode =  True

class PermSchema(BaseModel):
    id: int
    name: str

    class Config(BaseConfig):
        arbitrary_types_allowed = True
        orm_mode =  True

class PowerSchema(BaseModel):
    id: int
    name: str
    level: int
    add_date: date
    edit_date: Optional[date] = None
    category_id: int
    category_name: str

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

class TalkSchema(BaseModel):
    id: int
    talk_name: str
    presentation_name: str
    event_date: date

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

    @validator("event_date", pre=True)
    def parse_date(cls, value):
        return datetime.strptime(
            value,
            "%d/%m/%Y"
        ).date()

class WorkshopSchema(BaseModel):
    id: int
    workshop_name: str
    city: str
    event_date: date

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
    
    @validator("event_date", pre=True)
    def parse_date(cls, value):
        return datetime.strptime(
            value,
            "%d/%m/%Y"
        ).date()

class LanguageSchema(BaseModel):
    id: int
    language_name: str
    language_level: str
    language_id: int

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

class LicenseSchema(BaseModel):
    id: int
    license_name: str
    issuing_organization: str
    issue_date: date

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

    @validator("issue_date", pre=True)
    def parse_date(cls, value):
        return datetime.strptime(
            value,
            "%d/%m/%Y"
        ).date()

class EducationSchema(BaseModel):
    id: int
    user_id: int
    facility_name: str
    education_field: str
    graduation_date: date
    still_enrolled: bool 
    education_level: str

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

    @validator("graduation_date", pre=True)
    def parse_date(cls, value):
        return datetime.strptime(
            value,
            "%d/%m/%Y"
        ).date()

class WorkerSchema(BaseModel):
    id: int 
    name: str
    img: Optional[str] = "/static/img/anonymous.png"
    email: Optional[str] = None
    is_active: Optional[bool] = True
    partner: Optional[bool] = True
    is_client: Optional[bool] = False
    is_freelancer: Optional[bool] = False
    is_uop: Optional[bool] = False
    skype: Optional[str] = None
    github: Optional[str] = None
    employee_location: Optional[str] = None
    phone: Optional[str] = None
    phone_on_desk: Optional[str] = None
    zulip: Optional[str] = None
    start_work: Optional[date] = None
    start_full_time_work: Optional[date] = None
    start_work_experience: Optional[date] = None
    stop_work: Optional[date] = None
    date_of_birth: Optional[date] = None
    avatar_url: Optional[str] = None
    room: Optional[str] = None
    department: Optional[int] = None
    department_name: Optional[str] = None
    removal: Optional[str] = None
    seniority: Optional[int] = None
    seniority_name: Optional[str] = None
    versatility: Optional[int] = None
    versatility_name: Optional[str] = None
    location: Optional[conlist(item_type=str, max_items=3, min_items=3)] = []
    roles_json: Optional[conlist(item_type=RoleSchema)] = []
    roles: Optional[conlist(item_type=str)] = []
    all_perms: Optional[conlist(item_type=str)] = []
    teams_json: Optional[conlist(item_type=TeamSchema)] = []
    groups: Optional[conlist(item_type=str)] = []
    teams: Optional[conlist(item_type=int)] = []
    powers: Optional[conlist(item_type=PowerSchema)] = []
    workshops: Optional[conlist(item_type=WorkshopSchema)] = []
    educations: Optional[conlist(item_type=EducationSchema)] = []
    talks: Optional[conlist(item_type=TalkSchema)] = []
    languages: Optional[conlist(item_type=LanguageSchema)] = []
    licenses: Optional[conlist(item_type=LicenseSchema)] = []
    intranet_id: Optional[int]
    english_skills: Optional[str]
    link_to_cv: Optional[str]
    availability: Optional[str]
    is_available: Optional[bool]


    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

class DepartmentSchema(BaseModel):
    id: int
    object: str
    name: str
    short_name: str

class VacancySchema(BaseModel):
    id: Optional[int] = None
    description: str
    needed: int
    role: str
    project: int
    status: Optional[str] =  None
    offered: Optional[str] = None
    selected: Optional[str] = None
    introduced: Optional[str] = None
    accepted: Optional[str] = None
    rejected: Optional[str] = None
    created_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None

class CommentSchema(BaseModel):
    id: Optional[int]
    create_date: Optional[date]
    content: str
    author_name: Optional[str]
    employee: int
    vacancy: int
    type: Optional[str] = "comment"

class ManagerSchema(BaseModel):
    object: str
    name: str
    type: str
    department: int
    user: int
    username: str

    class Config(BaseConfig):
        arbitrary_types_allowed = True
        orm_mode =  True

class ProjectSchema(BaseModel):
    id: Optional[int]
    object: Optional[str]
    name: str
    description: str
    status: str
    ready_to_start: bool
    partners: bool
    concract_status: int
    length: str
    start_date: date
    account: ManagerSchema
    allocation_lead: ManagerSchema  
    vacancies: Optional[conlist(item_type=VacancySchema)]
    priority: int
    comments: Optional[conlist(item_type=CommentSchema)]
    category: str
    currency: str
    monthly_rate: int
    monthly_rate_pln: Optional[int]

class AvailabilitySchema(BaseModel):
    additionalProp1: str
    additionalProp2: str
    additionalProp3: str

class AllocationSchema(BaseModel):
    vacancy: int
    employee: int
    priority: int
    status: str

class ProjectSchemaIn(BaseModel):
  name: str
  description: str
  status: str
  ready_to_start: bool
  partners: bool
  contract_status: int
  length: str
  start_date: date
  account: int
  allocation_lead: int
  priority: int
  category: int
  currency: str
  monthly_rate: int