import json

class AppConfig:
    def __init__(self, config_path='config/config.json'):
        with open(config_path) as config_file:
            config = json.load(config_file)
        
        self.geofence_api_url = config['GEOFENCE_API_URL']
        self.bearer_token = config['BEARER_TOKEN']
        self.allow_webhook_host = config['ALLOW_WEBHOOK_HOST']
        self.receiver_port = int(config['RECEIVER_PORT'])
        self.db_host = config['DATABASE_HOST']
        self.db_port = int(config['DATABASE_PORT'])
        self.db_name = config['DATABASE_NAME']
        self.db_user = config['DATABASE_USER']
        self.db_password = config['DATABASE_PASSWORD']
        self.celery_broker_url = config['CELERY_BROKER_URL']
        self.celery_result_backend = config['CELERY_RESULT_BACKEND']
        self.max_queue_size = int(config['MAX_QUEUE_SIZE'])
        self.extra_flush_threshold = int(config['EXTRA_FLUSH_THRESHOLD'])
        self.flush_interval = int(config['FLUSH_INTERVAL'])
        self.max_retries = int(config['MAX_RETRIES'])
        self.retry_delay = int(config['RETRY_DELAY'])
        self.celery_log_level = config['CELERY_LOG_LEVEL']
        self.celery_log_file = config['CELERY_LOG_FILE']
        self.celery_log_max_bytes = int(config['CELERY_LOG_MAX_BYTES'])
        self.celery_max_log_files = int(config['CELERY_MAX_LOG_FILES'])
        self.flask_log_level = config['FLASK_LOG_LEVEL']
        self.flask_log_file = config['FLASK_LOG_FILE']
        self.flask_log_max_bytes = int(config['FLASK_LOG_MAX_BYTES'])
        self.flask_max_log_files = int(config['FLASK_MAX_LOG_FILES'])
        self.redis_host = config['REDIS_HOST']
        self.redis_port = int(config['REDIS_PORT'])
        self.redis_db = config['REDIS_DB']
        self.redis_url = config['REDIS_URL']
        self.api_log_level = config['API_LOG_LEVEL']
        self.api_log_file = config['API_LOG_FILE']
        self.api_log_max_bytes = int(config['API_LOG_MAX_BYTES'])
        self.api_max_log_files = int(config['API_MAX_LOG_FILES'])
        self.api_port = int(config['API_PORT'])
        self.api_secret_key = config['API_SECRET_KEY']
        self.api_secret_header_key = config['API_SECRET_HEADER_KEY']
        self.api_daily_cache = int(config['API_DAILY_CACHE'])
        self.api_weekly_cache = int(config['API_WEEKLY_CACHE'])
        self.api_monthly_cache = int(config['API_MONTHLY_CACHE'])
        self.api_ip_restriction = config['API_IP_RESTRICTION'].lower() == 'true'
        self.api_allowed_ips = config['API_ALLOWED_IPS'].split(", ")
        self.api_header_name = config['API_HEADER_NAME']
# Create a global instance of AppConfig to use throughout the application
app_config = AppConfig()