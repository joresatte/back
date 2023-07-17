from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.users_services import ServicesRepository, Services
from src.domain.category_services import CategoryServicesRepository, Category_services
from src.domain.categories import CategoriesRepository, Categories
from src.domain.regists import RegistsRepository, Regists

def setupForGeneralServices():
    services_repository = ServicesRepository(temp_file())
    app = create_app(repositories={"services": services_repository})
    client = app.test_client()

    user_1= Services(
       id= "service_1",
        cat_id= "category_1",
        user_name= "vince",
        text= "Mudanzas",
        intro= "Realizamos mudanzas",
        price= "por 7$ la hora",
        text_pictures= "foto",
        textarea= "Mudanzas",
        phone= "024-639-2574",
        email= "reinabo@vince.com",
        city= "Bilbao",
    )
    services_repository.save(user_1)
    
    user_2= Services(
        id= "service_2",
        cat_id= "category_2",
        user_name= "oshulem0",
        text= "Limpiezas",
        intro= "disponible para todo tipos de limpiezas",
        price= "por 8$ la hora",
        text_pictures= "foto",
        textarea= "Limpiezas",
        phone= "424-639-9574",
        email= "fbadland0@bizjournals.com",
        city= "Tayirove",
    )
    user_3= Services(
        id= "service_50",
        cat_id= "category_2",
        user_name= "zegerton1",
        text= "Limpiezas",
        intro= "todo tipos de limpiezas",
        price= "por 6$ la hora",
        text_pictures= "foto",
        textarea= "Limpiezas",
        phone= "382-214-1560",
        email= "wglenister1@latimes.com",
        city= "Al Burayqah",
    )
    services_repository.save(user_2)
    services_repository.save(user_3)

    return client

def setupForGeneralCategoryServices():
    services_repository = CategoryServicesRepository(temp_file())
    app = create_app(repositories={"categories_services": services_repository})
    client = app.test_client()

    user_1= Category_services(
       id= "service_1",
        cat_id= "category_1",
        user_name= "vince",
        text= "Mudanzas",
        intro= "Realizamos mudanzas",
        price= "por 7$ la hora",
        text_pictures= "foto",
        textarea= "Mudanzas",
        phone= "024-639-2574",
        email= "reinabo@vince.com",
        city= "Bilbao",
    )
    services_repository.save(user_1)
    
    user_2= Category_services(
        id= "service_2",
        cat_id= "category_2",
        user_name= "oshulem0",
        text= "Limpiezas",
        intro= "disponible para todo tipos de limpiezas",
        price= "por 8$ la hora",
        text_pictures= "foto",
        textarea= "Limpiezas",
        phone= "424-639-9574",
        email= "fbadland0@bizjournals.com",
        city= "Tayirove",
    )
    user_3= Category_services(
        id= "service_50",
        cat_id= "category_2",
        user_name= "zegerton1",
        text= "Limpiezas",
        intro= "todo tipos de limpiezas",
        price= "por 6$ la hora",
        text_pictures= "foto",
        textarea= "Limpiezas",
        phone= "382-214-1560",
        email= "wglenister1@latimes.com",
        city= "Al Burayqah",
    )
    services_repository.save(user_2)
    services_repository.save(user_3)

    return client

def setupForCategoryServices():
    services_repository = CategoryServicesRepository(temp_file())
    app = create_app(repositories={"categories_services": services_repository})
    client = app.test_client()
    return client

def setup():
    Categories_Repository = CategoriesRepository(temp_file())
    app = create_app(repositories={"categories": Categories_Repository})
    client = app.test_client()
    return client

def setupForCategory():
    categories_repository = CategoriesRepository(temp_file())
    app = create_app(repositories={"categories": categories_repository})
    client = app.test_client()
    
    category_1 = Categories(
        cat_id= "category_1",
        text= "Mudanzas",
        text_pictures= "text_pictures",
       
    )
    categories_repository.save(category_1)

    category_2 = Categories(
        cat_id= "category_2",
        text= "Limpiezas",
        text_pictures= "text_pictures",
    )
    categories_repository.save(category_2)

    return client

def setupForAuthentication():
    regists_repository = RegistsRepository(temp_file())
    app = create_app(repositories={"regists": regists_repository})
    client = app.test_client()

    user1= Regists(
       id= "service_1",
        email= "reinabo@vince.com",
        password= "password1",
    )
    regists_repository.save(user1)
    return client

def setupForPostedRequest():
    services_repository = ServicesRepository(temp_file())
    app = create_app(repositories={"services": services_repository})
    client = app.test_client()
    return client

def setupForPostedCategoryServices():
    services_repository = CategoryServicesRepository(temp_file())
    app = create_app(repositories={"categories_services": services_repository})
    client = app.test_client()
    return client

def setupForUpdatedCategoryServices():
    services_repository = CategoryServicesRepository(temp_file())
    app = create_app(repositories={"categories_services": services_repository})
    client = app.test_client()

    user_1= Category_services(
       id= "service_1",
        cat_id= "category_1",
        user_name= "vince",
        text= "Mudanzas",
        intro= "Realizamos mudanzas",
        price= "por 7$ la hora",
        text_pictures= "foto",
        textarea= "Mudanzas",
        phone= "024-639-2574",
        email= "reinabo@vince.com",
        city= "Bilbao",
    )
    services_repository.save(user_1)
    return client

def setupForUpDatedRequest():
    services_repository = ServicesRepository(temp_file())
    app = create_app(repositories={"services": services_repository})
    client = app.test_client()

    user_1= Services(
       id= "service_1",
        cat_id= "category_1",
        user_name= "vince",
        text= "Mudanzas",
        intro= "Realizamos mudanzas",
        price= "por 7$ la hora",
        text_pictures= "foto",
        textarea= "Mudanzas",
        phone= "024-639-2574",
        email= "reinabo@vince.com",
        city= "Bilbao",
    )
    services_repository.save(user_1)
    return client

