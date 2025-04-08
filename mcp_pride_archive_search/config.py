"""
Configuration settings for PRIDE Archive Search.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Default server settings
DEFAULT_PORT = 3001
DEFAULT_CONNECTION_TYPE = "http"  # Alternative: "stdio" 