#!/bin/bash

export PGUSER='postgres'

psql -c 'CREATE DATABASE sa'

psql sa -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"