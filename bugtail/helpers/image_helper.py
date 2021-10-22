from datetime import datetime

def get_upload_path(instance, filename):
    date = datetime.date(datetime.now())
    return f'{instance._meta.model_name}/{date}/{filename}'