from fastapi import APIRouter, Depends, Response, status
from app.schemas import AllocationSchema, DepartmentSchema, ManagerSchema, PowerSchema, ProjectSchemaIn, VacancySchema, WorkerSchema
from dependency_injector.wiring import inject, Provide
from app.containers import Container
from sqlalchemy.orm.exc import NoResultFound
from app.services import AllocationService, DepartmentService, ManagerService, PowerService, ProjectService, RoleService, VacancyService, WorkerService, LocationService
router = APIRouter()

@router.get("/users", tags=["worker"])
@inject
def get_list(
        worker_service: WorkerService = Depends(Provide[Container.worker_service]),
):
    return worker_service.get_workers()

@router.get("/users/{user_id}", tags=["worker"])
@inject
def get_by_id(
        worker_id: int,
        worker_service: WorkerService = Depends(Provide[Container.worker_service])
):
    try:
        return worker_service.get_worker_by_id(worker_id)
    except NoResultFound:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.get("/usersn/{worker_name}", tags=["worker"])
@inject
def get_by_name(
        worker_name: str,
        worker_service: WorkerService = Depends(Provide[Container.worker_service])
):
    try:
        return worker_service.get_worekr_by_name(worker_name)
    except NoResultFound:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@router.get("/perm/{perm_name}", tags=["worker"])
@inject
def get_by_name(
        perm_name: str,
        worker_service: WorkerService = Depends(Provide[Container.worker_service])
):
    try:
        return worker_service.get_worker_with_perm(perm_name)
    except NoResultFound:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@router.post("/users", status_code=status.HTTP_201_CREATED, tags=["worker"])
@inject
def add(
        worker: WorkerSchema,
        worker_service: WorkerService = Depends(Provide[Container.worker_service])
):
    _worker = worker_service.create_worker(worker)
    return _worker

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["worker"])
@inject
def remove(
        worker_id: int,
        worker_service: WorkerService = Depends(Provide[Container.worker_service]),
):
    try:
        worker_service.delete_worker_by_id(worker_id)
    except NoResultFound:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get("/locations", tags=["location"])
@inject
def get_list(
        location_service: LocationService = Depends(Provide[Container.location_service]),
):
    return location_service.get_locations()


@router.get("/locations/{location_id}", tags=["location"])
@inject
def get_user_location(
        location_id:int,
        location_service: LocationService = Depends(Provide[Container.location_service]),
):
    return location_service.get_location_users(location_id)

@router.get("/location/{location_id}", tags=["location"])
@inject
def get_location_by_id(
        location_id:int,
        location_service: LocationService = Depends(Provide[Container.location_service]),
):
    return location_service.get_location_by_id(location_id)

@router.get("/roles/", tags=["roles"])
@inject
def get_roles(
    role_service: RoleService = Depends(Provide[Container.role_service])
):
    return role_service.get_roles()

@router.get("/roles/{role_id}", tags=["roles"])
@inject
def get_role_by_id(
    role_id:int,
    role_service: RoleService = Depends(Provide[Container.role_service])
):
    return role_service.get_role_by_id(role_id)

@router.get("/roles/{role_id}", tags=["roles"])
@inject
def get_workers_role(
    role_id: int,
    role_service: RoleService = Depends(Provide[Container.role_service])
):
    return role_service.get_worker_with_role(role_id)

@router.get("/powers", tags=["power"])
@inject
def get_power_list(
        power_service: PowerService = Depends(Provide[Container.power_service]),
):
    return power_service.get_powers()

@router.get("/powers/{power_id}", tags=["power"])
@inject
def get_power_by_id(
        power_id: int,
        power_service: PowerService = Depends(Provide[Container.power_service])
):
    try:
        return power_service.get_power_by_id(power_id)
    except NoResultFound:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@router.get("/power/{power_id}", tags=["power"])
@inject
def get_workers_with_powers(
        power_id: str,
        power_service: PowerService = Depends(Provide[Container.power_service])
):
    return power_service.get_worker_with_powers(power_id)

@router.post("/powers", status_code=status.HTTP_201_CREATED, tags=["power"])
@inject
def add(
        power: PowerSchema,
        power_service: PowerService = Depends(Provide[Container.power_service])
):
    power = power_service.create_power(power)
    return power

@router.delete("/powers/{power_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["power"])
@inject
def remove(
        power_id: int,
        power_service: PowerService = Depends(Provide[Container.power_service]),
):
    try:
        power_service.delete_power_by_id(power_id)
    except NoResultFound:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post("/department")
@inject
def add_department(
    department: DepartmentSchema,
    department_service: DepartmentService = Depends(Provide[Container.department_service])
):
    return department_service.create_department(department)

@router.get("/department")
@inject
def get_all_departments(
    department_service: DepartmentService = Depends(Provide[Container.department_service])
):
    return department_service.get_all_departments()

@router.post("/manager")
@inject
def add_manager(
    manager: ManagerSchema, 
    manager_service: ManagerService = Depends(Provide[Container.manager_service])
):
    return manager_service.add_manager(manager)

@router.get("/manager")
@inject
def get_managers(
    manager_service: ManagerService = Depends(Provide[Container.manager_service])
):
    return manager_service.get_all_managers()


@router.post("/project")
@inject
def add_project(
    project: ProjectSchemaIn, 
    project_service: ProjectService = Depends(Provide[Container.project_service])
):
    return project_service.create_project(project)

@router.get("/project")
@inject
def get_projects(
    project_service: ProjectService = Depends(Provide[Container.project_service])
):
    return project_service.get_all_projects()


@router.post("/allocation")
@inject
def allocate(
    allocation: AllocationSchema,
    allocation_service: AllocationService = Depends(Provide[Container.allocation_service])
):
    return allocation_service.create_allocation(allocation)

@router.post("/vaccancy")
@inject
def vacancies(
    vacancy: VacancySchema,
    vacancy_service: VacancyService = Depends(Provide[Container.vacancy_service])
):
    return vacancy_service.create_vacancy(vacancy)

@router.get("/python")
@inject
def python(
    worker_service: WorkerService = Depends(Provide[Container.worker_service])
):
    return worker_service.get_with_python()