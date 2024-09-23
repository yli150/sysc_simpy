# sysc_simpy
System C over Simpy

## Overview 
SystemC/TLM is a well known framework for hardware modelling. It is written in C/C++.  This repo tries to build SystemC interface over Simpy , so the your hardware modelling framework can leverage the power of python to achieve better productivity and less code. 

[Simpy](https://simpy.readthedocs.io/en/latest/) is a process-based discrete-event simulation framework based on standard Python. It provides concepts like process, thread, store, resource, event which has equivant components of SystemC. 

There are 30+ examaples from [learnsystemc](https://github.com/learnwithexamples/learnsystemc/). I tried to rewrite them by using this library to show the usage of SysCsim. You can check [examples](./examples/) for all details. 

## Get Started 

- Create conda env 
```
conda create -n sysc python=3.9
```
- Install requirements 
```
source activate sysc 
pip install -r requirements.txt
```
- Run example 
```
python examples/01_thread/module_with_thread.py
```

## Remaining Issues 

## FAQ 
1. What's the difference with [PySysC](https://github.com/accellera-official/PySysC.git)
    - `PySysC` is a simple python wrapper of systemc. You can't build a real model with it. You have to have majority of code implemented on systemc c++ domain. 
    - `SysCsim` provides building block to write your own hardware model. 