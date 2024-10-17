
from decouple import config

def main():

    # Acessando as variáveis de ambiente
    db_engine = config('DB_ENGINE', default='nome')
    db_name = config('DB_NAME', default='nome')
    db_user = config('DB_USER', default='nome')
    db_password = config('DB_PASSWORD', default='nome')
    db_host = config('DB_HOST', default='nome')
    db_port = config('DB_PORT', default='nome')
    db_options = config('DB_OPTIONS', default='nome')
 
    print(f"DB_ENGINE {db_engine}")
    print(f"B_NAME {db_name}")
    print(f"DB_USER {db_user}")
    print(f"DB_PASSWORD {db_password}")
    print(f"DB_HOST {db_host}")
    print(f"DB_PORT {db_port}")
    print(f"DB_OPTIONS {db_options}")

if __name__ == "__main__":
    main()