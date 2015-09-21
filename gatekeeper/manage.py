#!/usr/bin/env python
import os
import sys
import yaml

if __name__ == "__main__":
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
        print(cfg)

