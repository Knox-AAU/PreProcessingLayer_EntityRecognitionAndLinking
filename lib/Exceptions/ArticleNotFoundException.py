class ArticleNotFoundException(Exception):
    def __init__(self, articleName, message = "Article: NAME not found in database"):
        super().__init__(message.replace("NAME", articleName))