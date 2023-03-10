from dependency_injector import containers, providers
from app.db import Database
from app.repositories import AllocationRepository, DepartmentRepository, LanguageRepository, LicenseRepository, LocationRepository, ManagerRepository, PowerRepository, ProjectRepository, RoleRepository, TalkRepository, VacanciesRepository, WorkerRepository, WorkshopRepository
from app.services import AllocationService, DepartmentService, LanguageService, LicenseService, LocationService, ManagerService, PowerService, ProjectService, RoleService, TalkService, VacancyService, WorkerService, WorkshopService
from app.elasticsearch import Elastic
class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["app.endpoints"])
    config = providers.Configuration()
    config.db.url.from_env("DATABASE_URL")  
    db = providers.Singleton(Database, db_url=config.db.url)
    config.es.url.from_env("ES_URL")    
    config.es.index_name.from_env("INDEX_NAME")    
    config.es.mapping_url.from_env("MAPPING_URL")    
    es = providers.Singleton(Elastic, es_url = config.es.url, index_name = config.es.index_name , mapping_url = config.es.mapping_url)

    worker_repository = providers.Factory(
        WorkerRepository,
        session_factory=db.provided.session,
        es = es.provided.es_inst
    )

    worker_service = providers.Factory(
        WorkerService,
        worker_repository=worker_repository,
    )
    location_repository = providers.Factory(
        LocationRepository,
        session_factory=db.provided.session,
    )

    location_service = providers.Factory(
        LocationService,
        location_repository=location_repository,
    )
    power_repository = providers.Factory(
        PowerRepository,
        session_factory=db.provided.session,
    )

    power_service = providers.Factory(
        PowerService,
        power_repository=power_repository,
    )
    talk_repository = providers.Factory(
        TalkRepository,
        session_factory=db.provided.session,
    )

    talk_service = providers.Factory(
        TalkService,
        talk_repository=talk_repository,
    )    
    workshop_repository = providers.Factory(
        WorkshopRepository,
        session_factory=db.provided.session,
    )

    workshop_service = providers.Factory(
        WorkshopService,
        workshop_repository=workshop_repository,
    )   
    license_repository = providers.Factory(
        LicenseRepository,
        session_factory=db.provided.session,
    )

    license_service = providers.Factory(
        LicenseService,
        license_repository=license_repository,
    )   
    language_repository = providers.Factory(
        LanguageRepository,
        session_factory=db.provided.session,
    )

    language_service = providers.Factory(
        LanguageService,
        language_repository=language_repository,
    )   

    role_repository = providers.Factory(
        RoleRepository,
        session_factory=db.provided.session,
    )

    role_service = providers.Factory(
        RoleService,
        role_repository=role_repository,
    )   

    allocation_repository = providers.Factory(
        AllocationRepository,
        session_factory=db.provided.session,
        es = es.provided.es_inst
    )

    allocation_service = providers.Factory(
        AllocationService,
        allocation_repository=allocation_repository,
    )   

    vacancy_repository = providers.Factory(
        VacanciesRepository,
        session_factory=db.provided.session,
        es = es.provided.es_inst
    )

    vacancy_service = providers.Factory(
        VacancyService,
        vacancy_repository=vacancy_repository,
    )   

    project_repository = providers.Factory(
        ProjectRepository,
        session_factory=db.provided.session,
        es = es.provided.es_inst
    )

    project_service = providers.Factory(
        ProjectService,
        project_repository=project_repository,
    )   

    department_repository = providers.Factory(
        DepartmentRepository,
        session_factory=db.provided.session,
        es = es.provided.es_inst
    )

    department_service = providers.Factory(
        DepartmentService,
        department_repository=department_repository,
    )   

    manager_repository = providers.Factory(
        ManagerRepository,
        session_factory=db.provided.session,
        es = es.provided.es_inst
    )

    manager_service = providers.Factory(
        ManagerService,
        manager_repository=manager_repository,
    )   
