#!/usr/bin/env sh

##############################################################################
##
##  Stop and kill currently running docker image, pull newest version and
##  run it.
##
##############################################################################

warn ( ) {
    echo "$*"
}

warn "Currently running docker images"
docker ps -a

warn "Killing currently running docker image..."
docker kill pocket-square-present; docker rm pocket-square-present

warn "Pulling latest docker image..."
docker pull pocketsquare/pocket-square-present:latest

warn "Starting docker image..."
docker run -dit --name pocket-square-present --link pocket-square-sort-shuffle --link pocket-square-users --link pocket-square-similar-by-text -e SERVICE_ENVIRONMENT=production -p 8080:5000 pocketsquare/pocket-square-present:latest

warn "Currently running docker images"
docker ps -a
