# from django.apps import AppConfig


# class EcoConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'eco'

# from django.apps import AppConfig
# import threading
# import time
# from django.db import connection

# def keep_db_alive():
#     """Function to keep the database connection alive."""
#     while True:
#         try:
#             with connection.cursor() as cursor:
#                 cursor.execute("SELECT 1;")  # Ping the database
#             print("Database is alive!")  # Optional for debugging
#         except Exception as e:
#             print(f"Database connection failed: {e}")
#         time.sleep(300)  # Wait 5 minutes before the next ping

# class EcoConfig(AppConfig):
#     name = 'eco'

#     def ready(self):
#         """Starts a background thread when Django starts."""
#         thread = threading.Thread(target=keep_db_alive, daemon=True)
#         thread.start()
from django.apps import AppConfig
import threading
import time
from django.db import connection

def keep_db_alive():
    """Function to keep the database connection alive."""
    while True:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1;")  # Ping the database
            print("Database is alive!")  # Optional for debugging
        except Exception as e:
            print(f"Database connection failed: {e}")
        time.sleep(300)  # Ping every 5 minutes

class EcoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eco'

    def ready(self):
        """Starts a background thread when Django starts."""
        thread = threading.Thread(target=keep_db_alive, daemon=True)
        thread.start()
