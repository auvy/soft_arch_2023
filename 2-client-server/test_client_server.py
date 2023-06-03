import pytest
import threading
import time
import subprocess

# from server import run_server
from client import run_client


@pytest.fixture(scope="session", autouse=True)
def run():
  server_process = subprocess.Popen(["python", "server.py"])
  time.sleep(1)

  yield

  server_process.terminate()


def test_client_server_interaction():
  res = run_client('helo')
  assert res == 'wym "helo" lol'


def test_multiple_client_server_interactions():
  reqs = ["hii", "helo hii", "what"]
  ress = []
  for req in reqs:
    res = run_client(req)
    ress.append(res)

  assert ress == [f'wym "{req}" lol' for req in reqs]
  
  