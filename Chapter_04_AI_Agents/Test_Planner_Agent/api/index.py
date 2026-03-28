import sys
import os

# Allow Vercel Serverless runtime to import from root directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import app
