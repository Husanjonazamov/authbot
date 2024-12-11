from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')
ADMIN = env('ADMIN')
BASE_URL = env('BASE_URL')
REGISTER_URL = 'https://d2d1-188-113-237-187.ngrok-free.app'

