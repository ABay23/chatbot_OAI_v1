import os
from dotenv import load_dotenv

load_dotenv()


jwt_s_key = os.getenv('JWT_SECRET_KEY')
algo = os.getenv('JWT_ALGORITHM')

print(jwt_s_key, algo)