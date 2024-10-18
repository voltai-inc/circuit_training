Run the docker (with GPU):  

``` docker build --pull --no-cache --tag circuit_training_gpu:core --build-arg tf_agents_version=tf-agents[reverb] --build-arg dreamplace_version=dreamplace_20231214_c5a83e5_python3.9.tar.gz --build-arg placement_cost_binary=plc_wrapper_main_0.0.4 -f tools/docker/ubuntu_circuit_training_gpu tools/docker/ ``` 

``` docker build --pull --no-cache --tag circuit_training_gpu:core --build-arg tf_agents_version=tf-agents[reverb] --build-arg dreamplace_version=dreamplace_20231214_c5a83e5_python3.9.tar.gz --build-arg placement_cost_binary=plc_wrapper_main_0.0.4 --build-arg base_image=nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04 -f tools/docker/ubuntu_circuit_training tools/docker/ ```  

``` docker run --gpus all --rm -it -v "$(pwd)":/app -w /app circuit_training_gpu:core /bin/bash ```  

Run the docker (without GPU):  
``` docker build --pull --no-cache --tag circuit_training:core --build-arg tf_agents_version=tf-agents[reverb] --build-arg dreamplace_version=dreamplace_20231214_c5a83e5_python3.9.tar.gz --build-arg placement_cost_binary=plc_wrapper_main_0.0.4 -f tools/docker/ubuntu_circuit_training tools/docker/ ```  
``` docker run --rm -it -v "$(pwd)":/app -w /app circuit_training:core /bin/bash ```  

Run test and activate env:  
``` tox -e py39-stable -- circuit_training/grouping/grouping_test.py ```
``` source .tox/py39-stable/bin/activate ```  

Run the test:  
``` bash tools/e2e_smoke_test.sh --root_dir /app/logs ```  

Remove redundant elements from the netlist:  
``` python fix_netlist.py ```  

Run grouping code:  
``` python circuit_training/grouping/grouper_main.py --output_dir=output/ --block_name=adaptec --netlist_file=data/adaptec1_new.pb.txt --hmetis_dir=data/hmetis/ --plc_wrapper_main=data/plc_wrapper_main ```  
