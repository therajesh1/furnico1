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
#mainnnnnnnnnn
from django.apps import AppConfig
import threading
import time
from django.db import connection

# def keep_db_alive():
#     """Function to keep the database connection alive."""
#     while True:
#         try:
#             with connection.cursor() as cursor:
#                 cursor.execute("SELECT 1;")  # Ping the database
#             print("Database is alive!")  # Optional for debugging
#         except Exception as e:
#             print(f"Database connection failed: {e}")
#         time.sleep(300)  # Ping every 5 minutes

# class EcoConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'eco'

#     def ready(self):
#         """Starts a background thread when Django starts."""
#         thread = threading.Thread(target=keep_db_alive, daemon=True)
#         thread.start()


import time
from django.conf import settings
from django.db import connection

def keep_db_alive():
    """Pings the DB every 5 minutes to avoid timeouts (safe, quiet)."""
    time.sleep(10)  # Allow DB to start
    while True:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1;")
            if settings.DEBUG:
                print("Database is alive!")  # Debug only
        except Exception as e:
            if settings.DEBUG:
                print(f"[DB keep-alive error]: {e}")
        time.sleep(300)  # every 5 minutes


class EcoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eco'

    def ready(self):
        import threading
        thread = threading.Thread(target=keep_db_alive, daemon=True)
        thread.start()




# delay the first ping  
# Let the database fully load before pinging.
# def keep_db_alive():
#     """Function to keep the database connection alive."""
#     time.sleep(10)  # Delay before the first ping
#     while True:
#         try:
#             with connection.cursor() as cursor:
#                 cursor.execute("SELECT 1;")  # Ping the database
#             print("Database is alive!")  # Optional
#         except Exception as e:
#             print(f"[DB keep-alive error]: {e}")
#         time.sleep(300)


#  Option 2: Suppress error output
# If the ping is non-critical (just to avoid timeouts), don't print the error unless in debug mode:
# import django.conf

# def keep_db_alive():
#     time.sleep(10)
#     while True:
#         try:
#             with connection.cursor() as cursor:
#                 cursor.execute("SELECT 1;")
#             print("Database is alive!")
#         except Exception as e:
#             if django.conf.settings.DEBUG:
#                 print(f"[DB keep-alive error]: {e}")
#         time.sleep(300)


# Option 3: Remove the whole thread (if unnecessary)
# Unless you really need to keep DB connections alive persistently (like for pooled queries), this thread isn’t mandatory. Django handles DB connections well on its own.

# Just comment out:

# python
# Copy
# Edit
# def ready(self):
#     pass  # disable keep-alive thread for now
