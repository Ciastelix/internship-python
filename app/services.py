from typing import Iterator
from .repositories import AllocationRepository, DepartmentRepository, LanguageRepository, LicenseRepository, LocationRepository, ManagerRepository, PowerRepository, ProjectRepository, RoleRepository, TalkRepository, VacanciesRepository, WorkerRepository
from app.models import Allocation, Department, Language, License, Location, Power, Project, Role, Talk, Team, Vacancy, Worker, Workshop
from app.schemas import AllocationSchema, DepartmentSchema, LanguageSchema, LicenseSchema, LocationSchema, ManagerSchema, PowerSchema, ProjectSchemaIn, RoleSchema, TalkSchema, VacancySchema, WorkshopSchema, WorkerSchema

class RoleService:
    def __init__(self, role_repository: RoleRepository) -> None:

        self._repository: RoleRepository = role_repository

    def get_roles(self) -> Iterator[Role]:

        return self._repository.get_all()

    def get_role_by_id(self, role_id: int) -> Role:

        return self._repository.get_by_id(role_id)

    def create_role(self, role:RoleSchema) -> Role:

        return self._repository.add(role)

    def delete_location_by_id(self, role_id: int) -> None:
        
        return self._repository.delete_by_id(role_id)
    
    def get_worker_with_role(self, role_id:int):
        return self._repository.get_with_role(role_id)

class LocationService:

    def __init__(self, location_repository: LocationRepository) -> None:

        self._repository: LocationRepository = location_repository

    def get_locations(self) -> Iterator[Location]:

        return self._repository.get_all()

    def get_location_by_id(self, location_id: int) -> Location:

        return self._repository.get_by_id(location_id)

    def create_location(self, location:LocationSchema) -> Location:

        return self._repository.add(location)

    def delete_location_by_id(self, location_id: int) -> None:
        
        return self._repository.delete_by_id(location_id)

    def get_workers_with_location(self, location_id: int):

        return self._repository.get_location(location_id)

class PowerService:
    def __init__(self, power_repository: PowerRepository) -> None:

        self._repository: PowerRepository = power_repository

    def get_powers(self) -> Iterator[Power]:

        return self._repository.get_all()

    def get_power_by_id(self, power_id: int) -> Power:

        return self._repository.get_by_id(power_id)

    def create_power(self, power:PowerSchema) -> Power:

        return self._repository.add(power)

    def delete_power_by_id(self, power_id: int) -> None:
        
        return self._repository.delete_by_id(power_id)

    def get_worker_with_power(self, power_id:int):
        
        return self._repository.get_with_power(power_id)

class TalkService:
    def __init__(self, talk_repository: TalkRepository) -> None:

        self._repository: TalkRepository = talk_repository

    def get_talks(self) -> Iterator[Talk]:

        return self._repository.get_all()

    def get_talk_by_id(self, talk_id: int) -> Talk:

        return self._repository.get_by_id(talk_id)

    def create_talk(self, talk:TalkSchema) -> Team:

        return self._repository.add(talk)

    def delete_team_by_id(self, team_id: int) -> None:
        
        return self._repository.delete_by_id(team_id)

class WorkshopService:
    def __init__(self, workshop_repository: WorkerRepository) -> None:

        self._repository: WorkerRepository = workshop_repository

    def get_workshops(self) -> Iterator[Workshop]:

        return self._repository.get_all()

    def get_workshop_by_id(self, workshop_id: int) -> Workshop:

        return self._repository.get_by_id(workshop_id)

    def create_workshop(self, workshop:WorkshopSchema) -> Workshop:

        return self._repository.add(workshop)

    def delete_workshop_by_id(self, workshop_id: int) -> None:
        
        return self._repository.delete_by_id(workshop_id)

class LicenseService:
    def __init__(self, license_repository: LicenseRepository) -> None:

        self._repository: LicenseRepository = license_repository

    def get_licenses(self) -> Iterator[License]:

        return self._repository.get_all()

    def get_license_by_id(self, license_id: int) -> License:

        return self._repository.get_by_id(license_id)

    def create_license(self, licensee:LicenseSchema) -> License:

        return self._repository.add(licensee)

    def delete_license_by_id(self, license_id: int) -> None:
        
        return self._repository.delete_by_id(license_id)

class LanguageService:
    def __init__(self, language_repository: LanguageRepository) -> None:

        self._repository: LanguageRepository = language_repository

    def get_languages(self) -> Iterator[Language]:

        return self._repository.get_all()

    def get_language_by_id(self, language_id: int) -> Language:

        return self._repository.get_by_id(language_id)

    def create_language(self, language:LanguageSchema) -> Language:

        return self._repository.add(language)

    def delete_language_by_id(self, language_id: int) -> None:
        
        return self._repository.delete_by_id(language_id)

class WorkerService:

    def __init__(self, worker_repository: WorkerRepository) -> None:

        self._repository: WorkerRepository = worker_repository

    def get_workers(self) -> Iterator[Worker]:

        return self._repository.get_all()

    def get_worker_by_id(self, worker_id: int) -> Worker:

        return self._repository.get_by_id(worker_id)

    def get_worekr_by_name(self, worker_name: str):

        return self.get_by_name(worker_name)

    def create_worker(self, worker:WorkerSchema) -> Worker:

        return self._repository.add(worker)

    def get_worker_roles(self, worker_id):

        return self._repository.get_roles(worker_id)    

    def delete_worker_by_id(self, worker_id: int) -> None:
        
        return self._repository.delete_by_id(worker_id)
    
    def get_worker_with_perm(self, perm:str):

        return self._repository.get_with_perm(perm)

    def get_with_python(self):

        return self._repository.get_workers_with_python()

class AllocationService:

    def __init__(self, allocation_repository: AllocationRepository) -> None:

        self._repository: AllocationRepository = allocation_repository

    def create_allocation(self, allocation: AllocationSchema) -> Allocation:
        
        return self._repository.add(allocation)


class VacancyService:

    def __init__(self, vacancy_repository: VacanciesRepository) -> None:

        self._repository: VacanciesRepository = vacancy_repository

    def create_vacancy(self, vacancy: VacancySchema) -> Vacancy:
        
        return self._repository.add(vacancy)

    def get_all_vacancies(self):
        return self._repository.get_all()


class ProjectService:

    def __init__(self, project_repository: ProjectRepository) -> None:

        self._repository: ProjectRepository = project_repository

    def create_project(self, project: ProjectSchemaIn) -> Project:

        return self._repository.add(project)

    def get_all_projects(self) -> Iterator[Project]:

        return self._repository.get_all()


class DepartmentService:

    def __init__(self, department_repository: DepartmentRepository) -> None:

        self._repository: DepartmentRepository = department_repository

    def create_department(self, depertment: DepartmentSchema) -> Department:

        return self._repository.add(depertment)

    def get_all_departments(self) -> Iterator[Department]:

        return self._repository.get_all()


class ManagerService:

    def __init__(self, manager_repository: ManagerRepository) -> None:

        self._repository: ManagerRepository = manager_repository


    def add_manager(self, manager:ManagerSchema):
        return self._repository.add(manager)

    def get_all_managers(self):
        return self._repository.get_all()