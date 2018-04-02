# 1. dev.json
# 2. settings.dev
#   set_config() <- 이거 쓰세요
# 3. wsgi.dev
# 4. .config/dev/ 파일들
#   4.1. nginx-app.conf
#   4.2. uwsgi.ini
#   4.3. supervisord.conf
# 5. Dockerfile.dev
#   5.1. ENV를 사용해 환경변수 설정
#   5.2. docker build에서 migrate 및 createsu제외
# 6. docker build eb-docker:dev

# Bucket생성
# storage.py에 적절히 스토리지 생성
# 사용설정
# collectstatic
# 완-성
from .base import *

secrets = json.loads(open(SECRETS_DEV, 'rt').read())
set_config(secrets, module_name=__name__, start=True)

DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com',
    '.chan428.kr',
    '172.31.6.244',
]


def is_ec2_linux():
    """Detect if we are running on an EC2 Linux Instance
       See http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify_ec2_instances.html
    """
    if os.path.isfile("/sys/hypervisor/uuid"):
        with open("/sys/hypervisor/uuid") as f:
            uuid = f.read()
            return uuid.startswith("ec2")
    return False


def get_linux_ec2_private_ip():
    """Get the private IP Address of the machine if running on an EC2 linux server"""
    from urllib.request import urlopen
    if not is_ec2_linux():
        return None
    try:
        response = urlopen('http://172.31.6.244/latest/meta-data/local-ipv4')
        ec2_ip = response.read().decode('utf-8')
        if response:
            response.close()
        return ec2_ip
    except Exception as e:
        print(e)
        return None


private_ip = get_linux_ec2_private_ip()
if private_ip:
    ALLOWED_HOSTS.append(private_ip)

WSGI_APPLICATION = 'config.wsgi.dev.application'
INSTALLED_APPS += [
    'django_extensions',
    'storages',
]
# S3대신 EC2에서 정적파일을 제공 (프리티어의 Put사용량 절감)
# STATICFILES_STORAGE = 'config.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'config.storage.DefaultFileStorage'
