import aiohttp
import asyncio
import json
import sys
import os

headers = {"accept": "application/json"}
params = {
    "format": "json",
}
default_ip = "172.28.5.240"
default_staging_ip = "172.28.6.30"
default_port = 5005

def get_default_ip():
    if os.getenv('STAGING'):
        return default_staging_ip
    else:
        return default_ip

def get_endpoint_host():
    return os.getenv('ENDPOINT_IP', get_default_ip())

def get_endpoint_port():
    return os.getenv('ENDPOINT_PORT', default_port)

def get_default_serial():
    return os.getenv('SERIAL', '100000000204e8e1')

def getserial():
  # Extract serial from cpuinfo file
  cpuserial = None
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = None
 
  return cpuserial

def get_device():
    try:
        serial = getserial()
        if serial is not None:
            return serial
    except:
        return get_default_serial()
    return get_default_serial()

def urlbuilder(url, params):
    r = f"{url}"
    for i, kv in enumerate(params.items()):
        k, v = kv
        if i == 0:
            r = f"{r}?{k}={v}"
        else:
            r = f"{r}&{k}={v}"
    return r


async def fetch(session, url, params):
    """
        Fetch data from url
    """
    u = urlbuilder(url, params)
    async with session.get(u) as response:
        return await response.json()

async def get_config(session):
    """
    Get config
    """
    req_url = f'http://{get_endpoint_host()}:{get_endpoint_port()}/device/{get_device()}/config'
    print(req_url)
    return await fetch(session, req_url, {})

async def process():
    async with aiohttp.ClientSession(trust_env=True) as session:
        output = await get_config(session)
        # print(output)
        return output

def mock_response():
    response = None
    path = os.getenv('API_MOCK_PATH')
    if path:
        try:
            f = open(path,'r')
            response = json.loads(f.read())
            f.close()
        except:
            response = None        
    return response

def sync():
    mock = mock_response()
    if mock:
        return mock
    else:    
        assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(loop.create_task(process()))
    
if __name__ == "__main__":
    sync()