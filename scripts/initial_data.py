from cgitb import text
import sys

from py import code

sys.path.insert(0, "")

from src.domain.regists import RegistsRepository, Regists
from src.domain.categories import CategoriesRepository, Categories
from src.domain.category_services import CategoryServicesRepository, Category_services
from src.domain.users_services import ServicesRepository, Services
from src.domain.data import cuidados, limpiezas, mudanzas, mantemientos
from src.domain.userDataPictures import( 
    pictures_cuidados_1,
    pictures_cuidados_2,
    pictures_cuidados_3,
    pictures_mantenimientos_1,
    pictures_mantenimientos_2,
    pictures_mantenimientos_3,
    pictures_limpiezas_1,
    pictures_limpiezas_2,
    pictures_limpiezas_3,
    pictures_mudanzas_1,
    pictures_mudanzas_2,
    pictures_mudanzas_3
)

database_path = "data/database.db"


regist_1= Regists(
    id= "service_1",
    email= "reinabo@vince.com",
    password= "password1",
)
regist_repository= RegistsRepository(database_path)
regist_repository.save(regist_1)


category_1 = Categories(
        cat_id= "category_1",
        text= "Servicios de Mudanzas",
        text_pictures= mudanzas,
       
    )
category_2 = Categories(
    cat_id= "category_2",
    text= "Servicios de Limpiezas",
    text_pictures= limpiezas,
    
    )
category_3 = Categories(
        cat_id= "category_3",
        text= "Servicios de Cuidados",
        text_pictures= cuidados,
       
    )
category_4 = Categories(
        cat_id= "category_4",
        text= "Servicios de Mantenimientos",
        text_pictures= mantemientos,
       
    )
categories_repository = CategoriesRepository(database_path)
categories_repository.save(category_1)
categories_repository.save(category_2)
categories_repository.save(category_3)
categories_repository.save(category_4)

services_repository = CategoryServicesRepository(database_path)
services_repository.save(
    Category_services(
        id= "service_1",
        cat_id= "category_1",
        user_name= "vince",
        text= "Mudanzas",
        intro= "Realizamos mudanzas",
        price= "por 7$ la hora",
        text_pictures= pictures_mudanzas_1,
        textarea= "Mudanzas",
        phone= "024-639-2574",
        email= "reinabo@vince.com",
        city= "Bilbao",
    )
)
services_repository.save(
    Category_services(
        id= "service_23",
        cat_id= "category_1",
        user_name= "oouygj",
        text= "Mudanzas",
        intro= "Realizamos mudanzas",
        price= "por 6$ la hora",
        text_pictures= pictures_mudanzas_2,
        textarea= "Mudanzas",
        phone= "024-639-2574",
        email= "aqsdo@voiuce.com",
        city= "xdghbao",
    )
)
services_repository.save(
    Category_services(
        id= "service_12",
        cat_id= "category_1",
        user_name= "rfedbj",
        text= "Mudanzas",
        intro= "Realizamos mudanzas",
        price= "por 6.5$ la hora",
        text_pictures= pictures_mudanzas_3,
        textarea= "Mudanzas",
        phone= "024-768-26544",
        email= "vhjbo@dsadce.com",
        city= "erhjkj",
    )
)

services_repository.save(
    Category_services(
        id= "service_9",
        cat_id= "category_2",
        user_name= "oshulem0",
        text= "Limpiezas",
        intro= "disponible para todo tipos de limpiezas",
        price= "por 8$ la hora",
        text_pictures= pictures_limpiezas_1,
        textarea= "Limpiezas",
        phone= "424-639-9574",
        email= "fbadland0@bizjournals.com",
        city= "Tayirove",
    )
)
services_repository.save(
    Category_services(
        id= "service_74",
        cat_id= "category_2",
        user_name= "teerarem0",
        text= "Limpiezas",
        intro= "disponible para todo tipos de limpiezas",
        price= "por 7$ la hora",
        text_pictures= pictures_limpiezas_2,
        textarea= "foto",
        phone= "124-234-9574",
        email= "efmland0@bizjournals.com",
        city= "sdjnkjrove",
    )
)
services_repository.save(
    Category_services(
        id= "service_45",
        cat_id= "category_2",
        user_name= "oshhgkhhj",
        text= "Limpiezas",
        intro= "todo tipos de limpiezas",
        price= "por 8$ la hora",
        text_pictures= pictures_limpiezas_3,
        textarea= "Limpiezas",
        phone= "008-639-94374",
        email= "jnk@bizjouals.com",
        city= "nkmncfe",
    )
)

services_repository.save(
    Category_services(
        id= "service_97",
        cat_id= "category_3",
        user_name= "Roanne",
        text= "Cuidados",
        intro= "disponible para todo tipos de cuidados",
        price= "por 7$ la hora",
        text_pictures= pictures_cuidados_1,
        textarea= "cuidados",
        phone= "810-629-1584",
        email= "msisson2@disqus.com",
        city= "awaldron2",
    )
)
services_repository.save(
    Category_services(
        id= "service_80",
        cat_id= "category_3",
        user_name= "eewols3",
        text= "Cuidados",
        intro= "disponible para todo tipos de cuidados",
        price= "por 7$ la hora",
        text_pictures= pictures_cuidados_2,
        textarea= "cuidados",
        phone= "481-201-6380",
        email= "ecardoo3@wufoo.com",
        city= "Tanahmerah",
    )
)
services_repository.save(
    Category_services(
        id= "service_71",
        cat_id= "category_3",
        user_name= "Roanne",
        text= "Cuidados",
        intro= "disponible para todo tipos de cuidados",
        price= "por 7$ la hora",
        text_pictures= pictures_cuidados_3,
        textarea= "cuidados",
        phone= "382-214-1560",
        email= "msisson2@disqus.com",
        city= "awaldron2",
    )
)

services_repository.save(
    Category_services(
        id= "service_32",
        cat_id= "category_4",
        user_name= "rnisen5",
        text= "Mantenimientos",
        intro= "disponible para todo tipos de Mantenimientos",
        price= "por 5$ la hora",
        text_pictures= pictures_mantenimientos_3,
        textarea= "Mantenimientos",
        phone= "562-575-0936",
        email= "dillsley5@shareasale.com",
        city= "Olival Basto",
    )
)
services_repository.save(
    Category_services(
        id= "service_56",
        cat_id= "category_4",
        user_name= "mdowle6",
        text= "Mantenimientos",
        intro= "disponible para todo tipos de Mantenimientos",
        price= "por 5$ la hora",
        text_pictures= pictures_mantenimientos_1,
        textarea= "Mantenimientos",
        phone= "939-267-4173",
        email= "kreisen6@earthlink.net",
        city= "Tubli",
    )
)
services_repository.save(
    Category_services(
        id= "service_64",
        cat_id= "category_4",
        user_name= "atunniclisse7",
        text= "Mantenimientos",
        intro= "disponible para todo tipos de Mantenimientos",
        price= "por 5$ la hora",
        text_pictures= pictures_mantenimientos_2,
        textarea= "Mantenimientos",
        phone= "843-625-9927",
        email= "grickerd7@dion.ne.jp",
        city= "Zielona Góra",
    )
)

services_repository = ServicesRepository(database_path)
services_repository.save(
    Services(
        id= "service_1",
        cat_id= "category_1",
        user_name= "vince",
        text= "Mudanzas",
        intro= "Realizamos mudanzas",
        price= "por 7$ la hora",
        text_pictures= pictures_mudanzas_1,
        textarea= "Mudanzas",
        phone= "024-639-2574",
        email= "reinabo@vince.com",
        city= "Bilbao",
    )
)
services_repository.save(
    Services(
        id= "service_23",
        cat_id= "category_1",
        user_name= "oouygj",
        text= "Mudanzas",
        intro= "Realizamos mudanzas",
        price= "por 6$ la hora",
        text_pictures= pictures_mudanzas_2,
        textarea= "Mudanzas",
        phone= "024-639-2574",
        email= "aqsdo@voiuce.com",
        city= "xdghbao",
    )
)
services_repository.save(
    Services(
        id= "service_12",
        cat_id= "category_1",
        user_name= "rfedbj",
        text= "Mudanzas",
        intro= "Realizamos mudanzas",
        price= "por 6.5$ la hora",
        text_pictures= pictures_mudanzas_3,
        textarea= "Mudanzas",
        phone= "024-768-26544",
        email= "vhjbo@dsadce.com",
        city= "erhjkj",
    )
)

services_repository.save(
    Services(
        id= "service_9",
        cat_id= "category_2",
        user_name= "oshulem0",
        text= "Limpiezas",
        intro= "disponible para todo tipos de limpiezas",
        price= "por 8$ la hora",
        text_pictures= pictures_limpiezas_1,
        textarea= "Limpiezas",
        phone= "424-639-9574",
        email= "fbadland0@bizjournals.com",
        city= "Tayirove",
    )
)
services_repository.save(
    Services(
        id= "service_74",
        cat_id= "category_2",
        user_name= "teerarem0",
        text= "Limpiezas",
        intro= "disponible para todo tipos de limpiezas",
        price= "por 7$ la hora",
        text_pictures= pictures_limpiezas_2,
        textarea= "foto",
        phone= "124-234-9574",
        email= "efmland0@bizjournals.com",
        city= "sdjnkjrove",
    )
)
services_repository.save(
    Services(
        id= "service_45",
        cat_id= "category_2",
        user_name= "oshhgkhhj",
        text= "Limpiezas",
        intro= "todo tipos de limpiezas",
        price= "por 8$ la hora",
        text_pictures= pictures_limpiezas_3,
        textarea= "Limpiezas",
        phone= "008-639-94374",
        email= "jnk@bizjouals.com",
        city= "nkmncfe",
    )
)

services_repository.save(
    Services(
        id= "service_97",
        cat_id= "category_3",
        user_name= "Roanne",
        text= "Cuidados",
        intro= "disponible para todo tipos de cuidados",
        price= "por 7$ la hora",
        text_pictures= pictures_cuidados_1,
        textarea= "cuidados",
        phone= "810-629-1584",
        email= "msisson2@disqus.com",
        city= "awaldron2",
    )
)
services_repository.save(
    Services(
        id= "service_80",
        cat_id= "category_3",
        user_name= "eewols3",
        text= "Cuidados",
        intro= "disponible para todo tipos de cuidados",
        price= "por 7$ la hora",
        text_pictures= pictures_cuidados_2,
        textarea= "cuidados",
        phone= "481-201-6380",
        email= "ecardoo3@wufoo.com",
        city= "Tanahmerah",
    )
)
services_repository.save(
    Services(
        id= "service_71",
        cat_id= "category_3",
        user_name= "Roanne",
        text= "Cuidados",
        intro= "disponible para todo tipos de cuidados",
        price= "por 7$ la hora",
        text_pictures= pictures_cuidados_3,
        textarea= "cuidados",
        phone= "382-214-1560",
        email= "msisson2@disqus.com",
        city= "awaldron2",
    )
)

services_repository.save(
    Services(
        id= "service_32",
        cat_id= "category_4",
        user_name= "rnisen5",
        text= "Mantenimientos",
        intro= "disponible para todo tipos de Mantenimientos",
        price= "por 5$ la hora",
        text_pictures= pictures_mantenimientos_3,
        textarea= "Mantenimientos",
        phone= "562-575-0936",
        email= "dillsley5@shareasale.com",
        city= "Olival Basto",
    )
)
services_repository.save(
    Services(
        id= "service_56",
        cat_id= "category_4",
        user_name= "mdowle6",
        text= "Mantenimientos",
        intro= "disponible para todo tipos de Mantenimientos",
        price= "por 5$ la hora",
        text_pictures= pictures_mantenimientos_1,
        textarea= "Mantenimientos",
        phone= "939-267-4173",
        email= "kreisen6@earthlink.net",
        city= "Tubli",
    )
)
services_repository.save(
    Services(
        id= "service_64",
        cat_id= "category_4",
        user_name= "atunniclisse7",
        text= "Mantenimientos",
        intro= "disponible para todo tipos de Mantenimientos",
        price= "por 5$ la hora",
        text_pictures= pictures_mantenimientos_2,
        textarea= "Mantenimientos",
        phone= "843-625-9927",
        email= "grickerd7@dion.ne.jp",
        city= "Zielona Góra",
    )
)