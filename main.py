from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

openssl_config = "/home/sensorid/apps/certs_factory/openssl.cnf"

class Item(BaseModel):
    cert_id: str


@app.delete("/")
async def delete_cert(cert_id: Item):
    cert = cert_id.cert_id
    temp = subprocess.call(["openssl", "ca", "-config", openssl_config, "-revoke", cert ])
    temp = subprocess.call(["openssl", "ca", "-config", openssl_config, "-gencrl", "-out", cert ])
    # openssl ca -config /path -revoke nome_certificato.crt
    # openssl ca -config /path -gencrl -out /path
    return cert_id


@app.post("/")
async def create_cert(cert_id: Item):
    """
    :param cert_id:
    :return:
    """
    print(cert_id.cert_id)
    return cert_id



"""
openssl genrsa -out $outkey.key 2048
openssl req -new -out $outkey.csr -key $outkey.key -subj "/CN=sensorid/C=IT/ST=Campobasso/L=Campochiaro/O=Sensor ID"
openssl ca -config /home/sensorid/apps/certs_factory/openssl.cnf -notext -batch -in $outkey.csr -out $outkey.crt
"""