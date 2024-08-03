#!/bin/bash
docker build -t letswift-server .
docker stop letswift-server
docker rm letswift-server
docker run --name letswift-server --network letswift -p 8000:8000 letswift-server
