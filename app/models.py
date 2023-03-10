from datetime import datetime
from app.db import Base
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, Date, DateTime
from sqlalchemy.orm import relationship

class Role(Base):
    __tablename__ = "roles_json"
    id = Column(Integer, primary_key=True)
    name= Column(String)
    shortcut=Column(String, default=None)
    workers = relationship('Worker', secondary="worker_roles", back_populates='roles_json', cascade="all, delete")

class Team(Base):
    __tablename__ = "teams_json"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    workers = relationship('Worker', secondary="worker_teams", back_populates='teams_json', cascade="all, delete")

class Power(Base):
    __tablename__ = "powers"
    id = Column(Integer, primary_key=True)
    name= Column(String, index=True)
    level = Column(Integer)
    add_date = Column(Date, default=None, nullable=True)
    edit_date = Column(Date, default=None, nullable=True)
    category_id = Column(Integer)
    category_name = Column(String)
    workers = relationship("Worker", secondary="worker_powers", back_populates='powers', cascade="all, delete")

class Talk(Base):
    __tablename__="talks"
    id = Column(Integer, primary_key=True)
    talk_name = Column(String)
    presentation_name = Column(String)
    event_date = Column(Date, nullable=True)
    workers = relationship("Worker", secondary="worker_talks", back_populates='talks', cascade="all, delete")

class Workshop(Base):
    __tablename__="workshops"
    id = Column(Integer, primary_key=True)
    workshop_name = Column(String)
    city = Column(String)
    event_date = Column(Date, default=None, nullable=True)
    workers = relationship("Worker", secondary="worker_workshops", back_populates='workshops', cascade="all, delete")

class Language(Base):
    __tablename__="worker_languages"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    language_level = Column(String)
    language_id = Column(Integer)
    language_name = Column(String)
    user_id = Column(Integer, ForeignKey("workers.id"))

class License(Base):
    __tablename__="licenses"
    id = Column(Integer, primary_key=True)
    license_name = Column(String)
    issuing_organization = Column(String)
    issue_date = Column(Date, default=None, nullable=True)
    user_id = Column(Integer, ForeignKey("workers.id"), default=None)

def default_id(context):
    return context.get_current_parameters()['id']

class Worker(Base):
    __tablename__= "workers"
    id = Column(Integer, primary_key=True)
    name= Column(String, index=True)
    img = Column(String, default="/static/img/anonymous.png")
    email = Column(String, default=None)
    is_active = Column(Boolean, default=True)
    partner = Column(Boolean, default=True)
    is_client = Column(Boolean, default=False)
    is_freelancer = Column(Boolean, default=False)
    is_uop = Column(Boolean, default=False)
    skype = Column(String, default=None)
    github =Column(String, default=None)
    employee_location= Column(String, default=None)
    phone = Column(String(31), default=None)
    phone_on_desk =Column(String, default=None)
    zulip = Column(String, default=None)
    start_work = Column(Date, default=None, nullable=True)
    start_full_time_work = Column(Date, default=None)
    start_work_experience = Column(Date, default=None)
    stop_work = Column(Date, default=None, nullable=True)
    date_of_birth = Column(Date, default=None, nullable=True)
    avatar_url = Column(String, default="/static/img/anonymous.png")
    room = Column(String, default=None)
    department = Column(Integer, default=None)
    department_name = Column(String, default=None)
    removal = Column(String, default=None)
    seniority = Column(String, default=None)
    seniority_name = Column(String, default=None)
    versatility = Column(String, default=None)
    versatility_name = Column(String, default=None)
    location = Column(Integer, ForeignKey("locations.id"), default=None)
    roles = Column(String, default=None)
    roles_json = relationship('Role', secondary="worker_roles", back_populates='workers', cascade="all, delete", lazy="joined")
    all_perms = Column(String)
    teams_json = relationship('Team', secondary="worker_teams", back_populates='workers', cascade="all, delete", lazy="joined")
    teams = Column(String, default=None)
    groups = Column(String, default=None)
    powers = relationship('Power', secondary="worker_powers", back_populates='workers', cascade="all, delete", lazy="joined")
    talks = relationship('Talk', secondary="worker_talks", back_populates='workers', cascade="all, delete", lazy="joined")
    workshops = relationship('Workshop', secondary="worker_workshops", back_populates='workers', cascade="all, delete", lazy="joined")
    languages = relationship('Language', cascade="all, delete", lazy="joined")
    licenses = relationship("License", cascade="all, delete", lazy="joined")
    educations = relationship("Education", cascade="all, delete", lazy="joined")
    object = Column(String, default=None)
    projects_count = Column(String, default=None)
    initials = Column(String, default=None)
    projects_allocated = relationship('Allocation', secondary="worker_allocations", back_populates='workers', cascade="all, delete", lazy="joined")
    intranet_id = Column(Integer, default=default_id)
    link_to_cv = Column(String, default=None)
    availability = Column(String, default=None)
    is_available = Column(Boolean, default=None)
    
class WorkerRoles(Base):
    __tablename__ = "worker_roles"
    worker_id = Column(Integer, ForeignKey('workers.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('roles_json.id'), primary_key=True)

class WorkerTeams(Base):
    __tablename__ = "worker_teams"
    worker_id = Column(Integer, ForeignKey('workers.id'), primary_key=True)
    team_id = Column(Integer, ForeignKey('teams_json.id'), primary_key=True)

class WorkerPowers(Base):
    __tablename__ = "worker_powers"
    worker_id = Column(Integer, ForeignKey('workers.id'), primary_key=True)
    power_id = Column(Integer, ForeignKey('powers.id'), primary_key=True)

class WorkerTalks(Base):
    __tablename__ = "worker_talks"
    worker_id = Column(Integer, ForeignKey('workers.id'), primary_key=True)
    talk_id = Column(Integer, ForeignKey('talks.id'), primary_key=True)

class WorkerWorkshops(Base):
    __tablename__ = "worker_workshops"
    worker_id = Column(Integer, ForeignKey('workers.id'), primary_key=True)
    workshop_id = Column(Integer, ForeignKey('workshops.id'), primary_key=True)

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True)
    name= Column(String)
    tag = Column(String(3))
    worker= relationship("Worker", cascade="all, delete")

class Education(Base):
    __tablename__="educations"
    id = Column(Integer, primary_key=True)
    facility_name = Column(String)
    education_field = Column(String)
    graduation_date = Column(Date, default=None, nullable=True)
    still_enrolled = Column(Boolean)
    education_level = Column(String)
    user_id = Column(ForeignKey("workers.id"), default=None)

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    object = Column(String)
    name = Column(String)
    short_name = Column(String)
    managers = relationship('Manager', cascade="all, delete", lazy="joined")
    
class Vacancy(Base):
    __tablename__ = "vacancies"
    id =  Column(Integer, primary_key=True)
    description = Column(String)
    needed = Column(Integer)
    role = Column(String)
    project = Column(Integer)
    offered = Column(String)
    selected = Column(String)
    introduced = Column(String)
    accepted = Column(String)
    rejected = Column(String)
    created_at = Column(DateTime)
    closed_at = Column(DateTime)
    projects= relationship("Project", secondary="project_vacancies", cascade="all, delete", lazy="joined")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    create_date = Column(Date, default=datetime.now())
    content = Column(String , default=None)
    author_name = Column(String, default=None)
    employee = Column(Integer, ForeignKey("workers.id"), default=None)
    vacancy = Column(Integer, ForeignKey("vacancies.id"), default=None)
    type = Column(String, default="comment")
    projects = relationship('Project', secondary="project_comments", back_populates='comments', cascade="all, delete", lazy="joined")

class Manager(Base):
    __tablename__ = "managers"
    id = Column(Integer, primary_key=True)
    object = Column(String)
    name = Column(String)
    type = Column(String)
    department = Column(Integer, ForeignKey("departments.id"), default=None)
    user = Column(Integer, ForeignKey("workers.id"), default=None)
    username = Column(String)

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    object = Column(String)
    name = Column(String)
    description = Column(String)
    status = Column(String)
    ready_to_start = Column(Boolean)
    partners = Column(Boolean)
    concract_status = Column(Integer)
    length = Column(String)
    start_date = Column(Date)
    account = Column(Integer, ForeignKey("managers.id"), default=None)
    allocation_lead = Column(Integer, ForeignKey("workers.id"), default=None)
    vacancies = relationship('Vacancy', secondary="project_vacancies", back_populates='projects', cascade="all, delete")
    priority = Column(Integer)
    comments = relationship('Comment', secondary="project_comments", back_populates='projects', cascade="all, delete", lazy="joined")
    category = Column(Integer)
    currency = Column(String)
    monthly_rate = Column(Integer)
    monthly_rate_pln = Column(Integer)
    allocations = relationship("Allocation", cascade="all, delete", lazy="joined")

class ProjectVacancies(Base):
    __tablename__ = "project_vacancies"
    project_id = Column(Integer, ForeignKey('projects.id'), primary_key=True)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'), primary_key=True)

class ProjectComments(Base):
    __tablename__ = "project_comments"
    project_id = Column(Integer, ForeignKey('projects.id'), primary_key=True)
    comment_id = Column(Integer, ForeignKey('comments.id'), primary_key=True)

class Allocation(Base):
    __tablename__ = "allocations"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    project_name = Column(String)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    vacancy_role = Column(String)
    vacancy_status = Column(String, default=None)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    employees = relationship("Worker", secondary='worker_allocations', cascade="all, delete", lazy="joined")

class EmployeeAllocations(Base):
    __tablename__ = "worker_allocations"
    allocation_id = Column(Integer, ForeignKey('allocations.id'), primary_key=True)
    comment_id = Column(Integer, ForeignKey('workers.id'), primary_key=True)

