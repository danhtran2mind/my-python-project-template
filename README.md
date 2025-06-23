# This is a template of Python Project
## Introduction

This Python project template is designed to promote clean, readable, and maintainable code, fostering a peaceful coding experience. By following best practices like clear naming, modular design, and consistent formatting, this template aims to make development enjoyable and stress-free. I’ve done my best to create a structure that’s easy to understand, maintain, and scale, ensuring coding feels calm and approachable for everyone involved.

## How to create `pyproject.toml` and set it can use for `pip install`

```bash
cd my-python-project-template
pip install poetry
poetry install       # Install dependencies
# pip install .       # Install local package if needed
cd ..
```

## 


## 6 Ways to run Python Project
### 1. Using `Args`
```bash
python <python_file.py> --args_` value --args_2 value
```
### 2. Using library through `pip install git+https://git-service` or `pip install <your_lib>`
```bash
pip install git+https://git-service
```
or
```bash
pip install <your_lib>
```
```python
from <your_lib> import something
...
```
### 3. Using Availabel Deploy Apps such as: Flask, FastAPI, Gradio, Streamlit


### 4. Using directly through Python code
```bash
git clone https://git-service/username/repo_name
cd repo_name
```
```python
from ... import ...
...
```
### 5. Using `Dockerfile`
```bash
docker run -p <host_port:container_port> <Dockerfile>
# For example
# host_port:container_port: 5000:5000
# <Dockerfile>: Dockerfile
```
### 6. Using bash file such as `*.sh`
