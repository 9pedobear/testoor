from pathlib import Path
import os


# Создавайте пути внутри проекта следующим образом: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#  секретный ключ, используемый в производстве!
SECRET_KEY = 'django-insecure-7tkr_%vghf+cwl-c46j&!23+0zotflx%856-c-0d45*8gdf5+-'

#  включенная отладка для подсказок проблем
DEBUG = True

# перечисляем хосты к которым можем подключиться
ALLOWED_HOSTS = []


# приложения
INSTALLED_APPS = [
    # встроенные приложения
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Наши приложения
    'employer.apps.EmployerConfig', # Подключаем наше приложение c сотрудниками
    'feedback.apps.FeedbackConfig', # Подключаем наше приложение с отзывами
    'debug_toolbar', # Подключаем штучку которая будет показавать ошибки
]
# безопасность
MIDDLEWARE = [
    # встроенная
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # наша
    'debug_toolbar.middleware.DebugToolbarMiddleware', # Настройка для debug_toolbar
]

# константа определяет что корень маршрутов будет в main
ROOT_URLCONF = 'main.urls'

# шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Все шаблоны проекта
        # будут храниться здесь
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# надстройка для wsgi сервера
WSGI_APPLICATION = 'main.wsgi.application'


# настройка база данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # База данных sqlite3
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Проверка пароля
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Интернационализация
LANGUAGE_CODE = 'ru' # Устанавливаем русский язык

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Статические файлы (CSS, JavaScript, Images)
STATIC_URL = '/static/' # Константа для хранения стилей

STATIC_ROOT = os.path.join(BASE_DIR, 'static') # Константа для поиска стилей
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main/static'), # Константа для установки стилей
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Константа для поиска медия
# файлов
MEDIA_URL = '/media/' # Константа для хранения медия файлов

INTERNAL_IPS = ["127.0.0.1",] # Панель инструментов отладки отображается только в том случае, если ваш IP-адрес указан в параметре Django INTERNAL_IPS. Это означает, что для локальной разработки необходимо добавить «127.0.0.1» в INTERNAL_IPS. Вам нужно будет создать этот параметр, если он еще не существует в вашем модуле настроек:

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
