import subprocess
import sys

def install_databricks_sql_connector():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-dotenv"])

if __name__ == "__main__":
    install_databricks_sql_connector()