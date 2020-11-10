import abc
import os


class Configuration(abc.ABC):
    SITE_NAME = os.environ.get('APP_NAME', 'Flask Bones')
    UPLOAD_FOLDER = 'D:\\_temp_python\\blob_uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


class DevelopmentConfiguration(Configuration):
    pass


class ProductionConfiguration(Configuration):
    pass


configuration = DevelopmentConfiguration()
