
#Error handling
class exceptionError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class ConnectionError(ConnectionRefusedError):
    pass