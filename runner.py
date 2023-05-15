import subprocess
import json

# login = ["gcloud", "auth", "login", "--no-launch-browser"]
# login= subprocess.check_output(login)
# print(login)
# define the gcloud command to list existing TPUs
def list_tpu():
    list_cmd = ["gcloud", "compute", "tpus","tpu-vm", "list", "--zone=us-central1-f","--format=json"]


# execute the gcloud command and get the output as a JSON string
    output = subprocess.check_output(list_cmd)
    tpus = json.loads(output)
    return tpus


# check if there are any TPUs available
def create_tpu_if_required(tpus):
    if not tpus:
      create_tpu_vm_cmd = ["gcloud", "compute", "tpus","tpu-vm", "create", "tpu-7", "--zone=us-central1-f","--accelerator-type=v2-8", "--version=tpu-vm-pt-2.0", "--format=json"]
    # create a new TPU
      created = subprocess.check_output(create_tpu_vm_cmd)
      print(f"createed : {created}")
      print("Created a new TPU!")
    else:
        print("Found an existing TPU:", tpus[0]["name"])

def install_requirements():
  install_command = ["pip3", "install", "-r", "requirement/requirements.txt"]
  response = subprocess.check_output(install_command)
  return response

def connect_machine():
  try:
    ssh_cmd = ["gcloud", "compute",  "tpus","tpu-vm", "ssh", "tpu-7", "--zone=us-central1-f", "--format=json"]
    connected = subprocess.check_output(ssh_cmd)
    print(f"Connected to machine: {connected}")
  except subprocess.CalledProcessError as e:
    print(f"Error connecting to machine with code: {e.returncode} and output: {e.output}")
  

def main():
  tpus = list_tpu()
  create_tpu_if_required(tpus=tpus)
  connect_machine()
  install_requirements() # create method with command to install requirements 

if __name__ == "__main__":
    main()
    
