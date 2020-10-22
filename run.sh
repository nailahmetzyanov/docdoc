#!/bin/bash

rm -rf allure-results-local

mkdir -p allure-results-local

rm -rf allure-report

pytest tests

allure_generic/bin/allure generate allure-results-local