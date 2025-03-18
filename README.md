<h1 style="display: flex; align-items: center;  gap: 10px;">
    <img src="documents/submaroo_v3.webp"  alt="Submar-roo Logo" width="100">
    Submar-roo Workspace
</h1>


This is a *template* workspace for students. We development in *containers* to allow for reproduciable development and deployment. This is achieved by using docker, VsCode with the `Dev Container extension` and `NVIDIA Container Toolkit`. In essence, the workspace and your source code will be mounted in a running container, where you change and modify the source code. You also dont need to worry about the correct CUDA version on your host machine, matching or exceeding the host CUDA version required for your machine.

Your developed pgk's go into the `src ` directory, either as submodules,as git packages.Add installation instructions somewhere. 


# Quickstart:

1. Clone the workspace to your desired directory on your local machine
   1. Remove the .git from the workspace and initialize your own git repo
   2. Create and push it to your own project or repository
  
2. Install all the dependencies as shown in the installation 

3. Add/clone your code in the in the src directory, i.e `src/my_awsome_pkg`
   1. If you clone it, make sure to add it to the .gitignore so you don`t track it with the workspace git

4. Update or modfiy docker file to include all dependencies. 
5. Build and launch the container through `vscode`. Use `Ctr+Shft+P` to open the command window and type `Dev Container: Rebuild and Reopen Devcontainer`, will autocomplete if the extension is installed.
6. Start developing

# Worskpace Overview:
``` bash
worskpace_root
├── .vscode
├── .devcontainer
├── .git
├── data
├── documents
├── .gitignore
├── README.md
└── src
    └── awsome_pkg
```
- "Workspace Root" or "workspacee directory" refers to the root or origin of this workspace
- `.devcontainer`: Used for devcontainer[here](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) configuration and Docker file
- `src` this is where you pkgs should go. 


# Installation:

## Installing Docker
To install docker, follow the instructuions [here](https://docs.docker.com/engine/install/ubuntu/) or the commands below. Refer to the website for any issues.

For Ubuntu 2X.04 LTS use the following 
``` bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

```

```bash
# Install docker
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Docker Post Install Instructions, adds the you (the user) to the docker user group. 
The latest instructions can always be found on [here](https://docs.docker.com/engine/install/linux-postinstall/).

``` bash
# Creat the docker group and add user
sudo groupadd docker

sudo usermod -aG docker $USER
```
Log in an out to of your account.

```bash
docker run hello-world
```

## Installing VsCode:
Downaload the latest version [here](https://code.visualstudio.com/download)
Open Vscode and install the `Dev Container` extension [here](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)


## Installing CUDA dependencies
The expectation is that CUDA is needed for deep learning. W
- Install the CUDA toolkit from [here](https://developer.nvidia.com/cuda-downloads).
  - Make sure you GPU is compatible with the CUDA version.
  - Try to install the latest version possible, the container development environment will should make any version prior work. 

- Install the NVIDIA Container Toolkit from [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
``` bash 
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

```bash
sudo dnf install -y nvidia-container-toolkit
```

Addtional Links without any promis of relevance:
- https://a-nau.github.io/blog/2024-03-17-VS_Code_Devcontainer/


## Where to get good base docker images from:
Most of the time, a good base image is availbe from ROS, Nvidia or another organisition that will make life easier. 

ROS [Link](https://hub.docker.com/r/osrf/ros/tags)
Nvidia [Link](https://hub.docker.com/r/nvidia/cuda)

Dusty is developer that allows to build jetson container for a varity of examples [Link](https://github.com/dusty-nv/jetson-containers)

Commonly, many open source project or pkgs will have docker containers with their source code. So build them and use it as base container. 


## FAQ

I want to use my own devcontainer?
- Modify the 

Is my GPU working in the container?
- Run `nvidia-smi` and you should see your GPU

I can't see my GPU
- Most likely something is wrong with either the `Nvidia Container Toolkit` or docker user groups. Otherwise, good googling.
