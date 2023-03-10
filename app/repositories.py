from contextlib import AbstractContextManager
from json import load
from typing import Callable, Iterator
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from app.models import Allocation, Comment, Department, Language, License, Location, Manager, Power, Project, Role, Talk, Team, Vacancy, Worker, WorkerPowers, WorkerRoles, Workshop, Education
from app.schemas import AllocationSchema, CommentSchema, DepartmentSchema, LanguageSchema, LicenseSchema, LocationSchema, ManagerSchema, PowerSchema, ProjectSchemaIn, RoleSchema, VacancySchema, WorkshopSchema, WorkerSchema
from elasticsearch import Elasticsearch
from random import choice
def add_to_db(session, obj):
    session.add(obj)
    session.commit()
    session.refresh(obj)

def add_role(session, obj, worker):
    role = session.query(Role).filter_by(id=obj["id"]).first()
    if not role:
        role = Role(**obj)
        add_to_db(session, role)
    worker.roles_json.append(role)

def add_team(session, obj, worker):
    team = session.query(Team).filter_by(id=obj["id"]).first()
    if not team:
        team = Team(**obj)
        add_to_db(session, team)
    worker.teams_json.append(team)

def add_power(session, obj, worker):
    power = session.query(Power).filter_by(id=obj["id"]).first()
    if not power:
        power = Power(**obj)
        add_to_db(session, power)
    worker.powers.append(power)

def add_workshop(session, obj, worker):
    workshop = session.query(Workshop).filter_by(id=obj["id"]).first()
    if not workshop:
        workshop = Workshop(**obj)
        add_to_db(session, workshop)
    worker.workshops.append(workshop)

def add_education(session, obj, worker):
    education = session.query(Education).filter_by(id=obj["id"]).first()
    if not education:
        education = Education(**obj)
        add_to_db(session, education)
    worker.educations.append(education)

def add_talk(session, obj, worker):
    talk = session.query(Talk).filter_by(id=obj["id"]).first()
    if not talk:
        talk = Talk(**obj)
        add_to_db(session, talk)
    worker.talks.append(talk)

def add_language(session, obj, worker):
    language = session.query(Language).filter_by(id=obj["id"]).first()
    if not language:
        language = Language(**obj)
        add_to_db(session, language)
    worker.languages.append(language)

def add_license(session, obj, worker):
    licenses = session.query(License).filter_by(id=obj["id"]).first()
    if not licenses:
        licenses = License(**obj)
        add_to_db(session, licenses)
    worker.licenses.append(licenses)

def object_as_dict(obj):
        return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

class RoleRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Role]:
        with self.session_factory() as session:
            return session.query(Role).all()

    def get_by_id(self, role_id: int) -> Role:
        with self.session_factory() as session:
            role = session.query(Role).filter(Role.id == role_id).first()
            if not role:
                raise NoResultFound
            return role

    def add(self, role:RoleSchema) -> Role:
        with self.session_factory() as session:
            role = Role(**role.dict(exclude_unset=True))
            session.add(role)
            session.commit()
            session.refresh(role)
            return role

    def delete_by_id(self, role_id: int) -> None:
        with self.session_factory() as session:
            entity: Role = session.query(Role).filter(Role.id == role_id).first()
            if not entity:
                raise NoResultFound
            session.delete(entity)
            session.commit()

    def get_with_role(self, role_id:int):
        with self.session_factory() as session:
            return [session.query(Worker).filter(Worker.id==i.worker_id).first() for i in session.query(WorkerRoles).filter_by(role_id=role_id).all()]

class LocationRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Location]:
        with self.session_factory() as session:
            return session.query(Location).all()

    def get_by_id(self, location_id: int) -> Location:
        with self.session_factory() as session:
            location = session.query(Location).filter(Location.id == location_id).first()
            if not location:
                raise NoResultFound
            return location

    def add(self, location:LocationSchema) -> Location:
        with self.session_factory() as session:
            location = Location(**location.dict(exclude_unset=True))
            session.add(location)
            session.commit()
            session.refresh(location)
            return location

    def delete_by_id(self, location_id: int) -> None:
        with self.session_factory() as session:
            entity: Location = session.query(Location).filter(Location.id == location_id).first()
            if not entity:
                raise NoResultFound
            session.delete(entity)
            session.commit()

    def get_location(self, location_id:int):
        with self.session_factory() as session:
            return session.query(Worker).filter_by(location = location_id).all()

class PowerRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Power]:
        with self.session_factory() as session:
            return session.query(Power).all()

    def get_by_id(self, power_id: int) -> Power:
        with self.session_factory() as session:
            location = session.query(Power).filter(Power.id == power_id).first()
            if not location:
                raise NoResultFound
            return location

    def add(self, power:PowerSchema) -> Power:
        with self.session_factory() as session:
            power = Power(**power.dict(exclude_unset=True))
            session.add(power)
            session.commit()
            session.refresh(power)
            return power


    def delete_by_id(self, power_id: int) -> None:
        with self.session_factory() as session:
            entity: Location = session.query(Power).filter(Power.id == power_id).first()
            if not entity:
                raise NoResultFound
            session.delete(entity)
            session.commit()

    def get_with_power(self, power_id:int):
        with self.session_factory() as session:
            return [session.query(Worker).filter(Worker.id==i.worker_id).first() for i in session.query(WorkerPowers).filter_by(power_id=power_id).all()]

class TalkRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Talk]:
        with self.session_factory() as session:
            return session.query(Talk).all()

    def get_by_id(self, talk_id: int) -> Talk:
        with self.session_factory() as session:
            talk = session.query(Talk).filter(Talk.id == talk_id).first()
            if not talk:
                raise NoResultFound
            return talk

    def add(self, talk:LocationSchema) -> Talk:
        with self.session_factory() as session:
            talk = Talk(**talk.dict(exclude_unset=True))
            session.add(talk)
            session.commit()
            session.refresh(talk)
            return talk


    def delete_by_id(self, talk_id: int) -> None:
        with self.session_factory() as session:
            entity: Talk = session.query(Talk).filter(Talk.id == talk_id).first()
            if not entity:
                raise NoResultFound
            session.delete(entity)
            session.commit()

class WorkshopRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Workshop]:
        with self.session_factory() as session:
            return session.query(Workshop).all()

    def get_by_id(self, workshop_id: int) -> Workshop:
        with self.session_factory() as session:
            workshop = session.query(Workshop).filter(Workshop.id == workshop_id).first()
            if not workshop:
                raise NoResultFound
            return workshop

    def get_by_name(self, workshop_name:str)->Workshop:
        with self.session_factory() as session:
            workshop = session.query(Workshop).filter(Workshop.name == workshop_name).first()
            if not workshop:
                raise NoResultFound
            return workshop

    def add(self, workshop:WorkshopSchema) -> Workshop:
        with self.session_factory() as session:
            workshop = Workshop(**workshop.dict(exclude_unset=True))
            session.add(workshop)
            session.commit()
            session.refresh(workshop)
            return workshop


    def delete_by_id(self, workshop_id: int) -> None:
        with self.session_factory() as session:
            entity: Workshop = session.query(Workshop).filter(Workshop.id == workshop_id).first()
            if not entity:
                raise NoResultFound
            session.delete(entity)
            session.commit()

class LicenseRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[License]:
        with self.session_factory() as session:
            return session.query(License).all()

    def get_by_id(self, license_id: int) -> License:
        with self.session_factory() as session:
            licensee = session.query(License).filter(License.id == license_id).first()
            if not licensee:
                raise NoResultFound
            return licensee

    def get_by_name(self, license_name:str)->License:
        with self.session_factory() as session:
            licensee = session.query(License).filter(License.name == license_name).first()
            if not licensee:
                raise NoResultFound

    def add(self, licensee:LicenseSchema) -> License:
        with self.session_factory() as session:
            licensee = License(**licensee.dict(exclude_unset=True))
            session.add(licensee)
            session.commit()
            session.refresh(licensee)
            return licensee


    def delete_by_id(self, license_id: int) -> None:
        with self.session_factory() as session:
            entity: License = session.query(License).filter(License.id == license_id).first()
            if not entity:
                raise NoResultFound
            session.delete(entity)
            session.commit()

class LanguageRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Language]:
        with self.session_factory() as session:
            return session.query(Language).all()

    def get_by_id(self, language_id: int) -> Language:
        with self.session_factory() as session:
            language = session.query(Language).filter(Language.id == language_id).first()
            if not language:
                raise NoResultFound
            return language

    def get_by_name(self, language_name:str)->Language:
        with self.session_factory() as session:
            language = session.query(Language).filter(Language.name == language_name).first()
            if not language:
                raise NoResultFound
            return language

    def add(self, language:LanguageSchema) -> Language:
        with self.session_factory() as session:
            language = Language(**language.dict(exclude_unset=True))
            session.add(language)
            session.commit()
            session.refresh(language)
            return language


    def delete_by_id(self, language_id: int) -> None:
        with self.session_factory() as session:
            entity: Language = session.query(Language).filter(Language.id == language_id).first()
            if not entity:
                raise NoResultFound
            session.delete(entity)
            session.commit()

class WorkerRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]], es: Callable[..., AbstractContextManager[Elasticsearch]]) -> None:
        self.session_factory = session_factory
        self.es = es


    def get_all(self) -> Iterator[Worker]:
        with self.es() as es:
            return es.search(index="id", query={"match_all": {}})["hits"]["hits"]

    def get_by_id(self, worker_id: int) -> Worker:
        with self.session_factory() as session:
            return session.query(Worker).filter_by(id=worker_id).first()

    def get_by_name(self, worker_name:str) -> Worker:
        with self.es() as es:
            return es.search(index="id", query={"match":{"name": worker_name}})["hits"]["hits"]

    def add(self, worker:WorkerSchema) -> Worker:
        with self.session_factory() as session:
            location = worker.location
            _worker = worker.dict(exclude_unset=True, exclude={"location", "roles_json", "teams_json", "powers", "workshops", "educations", "talks", "languages", "licenses", "groups", "teams", "roles", "all_perms"})
            lists = worker.dict(include={"groups", "teams", "roles", "all_perms"})
            lists["teams"] = [str(i) for i in lists["teams"]]
            _worker = Worker(**_worker)
            _worker.groups=", ".join(lists["groups"])
            _worker.teams=", ".join(lists["teams"])
            _worker.roles=", ".join(lists["roles"])
            _worker.all_perms=", ".join(lists["all_perms"])
            workerAttribs = worker.dict(include={"roles_json", "teams_json", "powers", "workshops", "educations", "talks", "languages", "licenses"})
            if _worker.location:
                location = Location(id=location[0], name=location[1], tag=location[2])
                if not session.query(Location).filter_by(id=location.id):
                    add_to_db(session, location)
                _worker.location = location.id
            f = {"roles_json":add_role, "teams_json":add_team, "powers":add_power, "workshops":add_workshop, "educations":add_education, "talks":add_talk, "languages":add_language, "licenses":add_license}
            for attrib in workerAttribs:
                for i in workerAttribs[attrib]:
                    f[attrib](session, i, _worker)
            project = choice(session.query(Project).all())
            vacancy = choice(project.vacancies)
            allocation = Allocation(project_id=project.id,project_name=project.name,vacancy_id=vacancy.id, vacancy_role=vacancy.role)
            _worker.projects_allocated = [allocation]
            add_to_db(session, _worker)
            with self.es() as es:
                worker= worker.dict()
                worker["intranet_id"] = worker["id"]
                es.index(index="id", id=worker["intranet_id"], document=worker)
            return _worker


    def delete_by_id(self, worker_id: int) -> None:
        with self.session_factory() as session:
            entity: Worker = session.query(Worker).filter(Worker.id == worker_id).first()
            if not entity:
                raise NoResultFound
            session.delete(entity)
            session.commit()
    
    def get_with_perm(self, perm:str) ->  Iterator[Worker]:
        with self.es() as es:
            return es.search(index="id", query={"terms":{"all_perms": [perm]}})

    def get_workers_with_python(self):
        with self.es() as es:
            elements  = es.search(index="id", query=load(open("query.json")))["hits"]["hits"]
            with self.session_factory() as  session:
                return [session.query(Worker).filter_by(id=i["_source"]["intranet_id"]).first() for i in elements]

class CommentRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]], es: Callable[..., AbstractContextManager[Elasticsearch]]) -> None:
        self.session_factory = session_factory
        self.es = es

    def add(self, comment:CommentSchema) -> Comment:
        with self.session_factory() as session:
            project_id = comment.project 
            comment = Comment(**comment.dict(exclude_unset=True, exclude_none=True, exclude={"project"}))
            comment.author_name=session.query(Worker).filter_by(id = comment.employee).first().name
            comment.vacancy = comment.vacancy.id
            session.add(comment)
            session.commit()
            session.refresh(comment)
            project = session.query(Project).filter_by(id=project_id).fitst()
            project.vacancies = [comment]
            session.commit()
            session.refresh(project)
        return comment

    def get_all(self) -> Iterator[Comment]:
        with self.session_factory() as session:
            return session.query(Comment).all()

    
    def get_by_id(self, comment_id:int) -> Comment:
        with self.session_factory() as session:
            return session.query(Comment).filter_by(id=comment_id).first()

    def update(self, comment_id:int, to_update: dict) -> Comment:
        with self.session_factory() as session:
            comment = session.query(Comment).filter_by(id=comment_id).first()
            for k, v in to_update.items():
                setattr(comment, k, v)

            session.commit()
            session.refresh(comment)

    def delete(self, comment_id:int) -> None:
        with self.session_factory() as session:
            comment = session.query(Comment).filter_by(id=comment_id).first()
            session.delete(comment)
            session.commit()

class ManagerRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]], es: Callable[..., AbstractContextManager[Elasticsearch]]) -> None:
        self.session_factory = session_factory
        self.es = es

    def get_all(self) -> Iterator[Manager]:
        with self.session_factory() as session:
            return session.query(Manager).all()

    def add(self, manager:ManagerSchema):
        with self.session_factory() as session:
            manager = Manager(**manager.dict())
            session.add(manager)
            session.commit()
            session.refresh(manager)
        return manager

class ProjectRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]], es: Callable[..., AbstractContextManager[Elasticsearch]]) -> None:
        self.session_factory = session_factory
        self.es = es

    def get_all(self) -> Iterator[Project]:
        with self.session_factory() as session:
            return session.query(Project).all()
    
    def get_by_id(self, project_id:int) -> Project:
        with self.session_factory() as session:
            return session.query(Project).filter_by(id=project_id).first()
    
    def add(self, project: ProjectSchemaIn) -> Project:
        with self.session_factory() as session:
            project = Project(**project.dict(exclude_none=True, exclude_unset=True, exclude={"contract_status"}))
            session.add(project)
            session.commit()
            session.refresh(project)
            return project

    def update(self, project_id:int, to_update: dict) -> Project:
        with self.session_factory() as session:
            project = session.query(Project).filter_by(id=project_id).first()
            for k, v in to_update.items():
                setattr(project, k, v)

            session.commit()
            session.refresh(project)

    def delete(self, project_id:int) -> None:
        with self.session_factory() as session:
            project = session.query(Project).filter_by(id=project_id).first()
            session.delete(project)
            session.commit()

class VacanciesRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]], es: Callable[..., AbstractContextManager[Elasticsearch]]) -> None:
        self.session_factory = session_factory
        self.es = es

    def get_all(self) -> Iterator[Vacancy]:
        with self.session_factory() as session:
            return session.query(Vacancy).all()
    
    def get_by_id(self, vacancy_id:int) -> Vacancy:
        with self.session_factory() as session:
            return session.query(Vacancy).filter_by(id=vacancy_id).first()
    
    def add(self, vacancy: VacancySchema) -> Project:
        with self.session_factory() as session:
            status = vacancy.status
            vacancy = Vacancy(**vacancy.dict(exclude_none=True, exclude_unset=True, exclude={"status"}))
            session.add(vacancy)
            session.commit()
            session.refresh(vacancy)
            return vacancy

            #! status jest do vacancies i tam ustawiasz sobie normalnie patologicznie bo tam są od tego pola

    def update(self, vacancy_id:int, to_update: dict) -> Vacancy:
        with self.session_factory() as session:
            vacancy = session.query(Project).filter_by(id=vacancy_id).first()
            for k, v in to_update.items():
                setattr(vacancy, k, v)

            session.commit()
            session.refresh(vacancy)

    def delete(self, vacancy_id:int) -> None:
        with self.session_factory() as session:
            vacancy = session.query(Vacancy).filter_by(id=vacancy_id).first()
            session.delete(vacancy)
            session.commit()

class AllocationRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]], es: Callable[..., AbstractContextManager[Elasticsearch]]) -> None:
        self.session_factory = session_factory
        self.es = es

    def add(self, allocation:AllocationSchema) -> Allocation:
        with self.session_factory() as session:
            status = allocation.status
            priority = allocation.priority
            allocation = allocation.dict(exclude={"status", "priority"})
            allocation["vacancy_id"] = allocation.pop("vacancy")
            employee = allocation.pop("employee")
            alloc = allocation
            allocation = Allocation(**allocation)
            vacancy = session.query(Vacancy).filter_by(id=allocation.vacancy_id).first()
            vacancy.status = status
            project = session.query(Project).filter_by(id=vacancy.project).first()
            project.priority = priority
            allocation.vacancy_status = status
            allocation.vacancy_role = vacancy.role
            allocation.project_id = project.id
            allocation.project_name = project.name
            allocation.employees.append(session.query(Worker).filter_by(intranet_id=employee).first())
            session.add(allocation)
            session.commit()
            session.refresh(allocation)
            with self.es() as es:
                es.update(index="id", id=employee, body={"doc":{"projects_allocated":alloc}})
        return allocation

class DepartmentRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]], es: Callable[..., AbstractContextManager[Elasticsearch]]) -> None:
        self.session_factory = session_factory
        self.es = es

    def add(self, department:DepartmentSchema) -> Department:
        with self.session_factory() as session:
            department = Department(**department.dict())
            session.add(department)
            session.commit()
            session.refresh(department)
        return department

    def get_all(self) -> Iterator[Department]:
        with self.session_factory() as session:
            return session.query(Department).all()