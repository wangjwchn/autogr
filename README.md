# AutoGR
Automated Geo-Replication with Fast System Performance and Preserved Application Semantics



### Directory structure

```bash
├── applications              # input --collector--> z3pyir --rigi--> result
│   ├── input                     # original code of applications
│   │   ├── HealthPlus                # git repo of HealthPlus as a submodule
│   │   └── oltpbench                 # git repo of Smallbank, RUBiS, and Seats as a submodule
│   ├── z3pyir                    # z3py representation of applications
│   └── result                    # restrications idencified by Rigi
├── collector                 # git repo of the collector as a submodule
├── olisipo                   # git repo of olisipo as a submodule
└── rigi                      # source code of Rigi
```



### Dependencies

##### Rigi:

[Python](https://www.python.org/) 3.6.6

[Z3](https://github.com/Z3Prover/z3) 4.8.10 and Z3Py





##### Collector:

See the maven dependency file [here](https://github.com/ksqsf/AutoGR-Translator).



##### Olisipo:

See the maven dependency file [here](https://github.com/pandaworrior/VascoRepo/tree/master/vasco).



