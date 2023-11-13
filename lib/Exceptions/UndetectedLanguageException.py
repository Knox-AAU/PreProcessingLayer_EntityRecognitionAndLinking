class UndetectedLanguageException(Exception):
    def __init__(self, message = "Undetected language. Supported: da, en"):
        super().__init__(message)