#!/bin/sh

# requires py.test to be installed
py.test --cov ./cci --doctest-module ./cci
