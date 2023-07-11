class Config:
    def __init__(self, id, name, query, db_host, db_username, db_password, db_name, db_port, api_type, api_host,
                 api_method, api_headers, api_body, event_name, created_at, updated_at, deleted_at):
        self.id = id
        self.name = name
        self.query = query
        self.db_host = db_host
        self.db_username = db_username
        self.db_password = db_password
        self.db_name = db_name
        self.db_port = db_port
        self.api_type = api_type
        self.api_host = api_host
        self.api_method = api_method
        self.api_headers = api_headers
        self.api_body = api_body
        self.event_name = event_name
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    def __repr__(self):
        return f"Config(id={self.id}, name={self.name}, query={self.query}, db_host={self.db_host}, " \
               f"db_username={self.db_username}, db_password={self.db_password}, db_name={self.db_name}, " \
               f"db_port={self.db_port}, api_type={self.api_type}, api_host={self.api_host}, " \
               f"api_method={self.api_method}, api_headers={self.api_headers}, api_body={self.api_body}, " \
               f"event_name={self.event_name}, created_at={self.created_at}, updated_at={self.updated_at}, " \
               f"deleted_at={self.deleted_at})"
