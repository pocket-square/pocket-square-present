#!/usr/bin/env sh

##############################################################################
##
##  Perform SSH connection to deployment host and run update_to_latest_image
##  script there
##
##############################################################################

warn ( ) {
    echo "$*"
}

warn "Preparing ssh agent..."
eval "$(ssh-agent -s)"
chmod 600 .travis/id_rsa
ssh-add .travis/id_rsa

warn "Starting SSH connection..."
ssh "$DEPLOY_USER"@"$DEPLOY_HOST" update_to_latest_image.sh
