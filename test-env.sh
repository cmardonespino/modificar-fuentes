#!/usr/bin/env bash

NORMAL=$(tput sgr0)
GREEN=$(tput setaf 2; tput bold)
YELLOW=$(tput setaf 3)
RED=$(tput setaf 1)

function red() {
  echo -e "$RED$*$NORMAL"
}

function green() {
  echo -e "$GREEN$*$NORMAL"
}

function yellow() {
  echo -e "$YELLOW$*$NORMAL"
}

case "$1" in
  go)
    rm -rf output/
    cd src
    green "IDENTIFICANDO FUENTES .PARAMETROS CON EL AMBIENTE INGRESADO"
    python identificar_archivos.py
    green "MODIFICANDO FUENTES DE ACUERDO AL AMBIENTE INGRESADO"
    python modificar_fuentes.py
    ;;
esac