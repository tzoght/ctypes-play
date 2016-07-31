#!/bin/bash
MINPARAMS=1
echo "running script  \"`basename $0`\" with \"$*\"  "


print_help ()
{
  echo
  echo "This script needs at least $MINPARAMS command-line arguments!"
  echo "$0 [-c|--clean] [-t|--target target]"
  echo "where:"
  echo "      [-t|--target target] where target is one of the following "
  echo "      build : the default"
  echo "      test : runs the tests"
  exit -1
}

if [ $# -lt "$MINPARAMS" ]
then
  print_help
fi

# Initialize our own variables:
_print_help="no"
_clean="no"
_target="all"

while true; do
  case "$1" in
    -h | --help ) _print_help="yes"; shift ;;
    -c | --clean ) _clean="yes"; shift ;;
    -t | --target ) _target="$2"; shift; shift ;;
    -- ) shift; break ;;
    * ) break ;;
  esac
done

if [ $_print_help = "yes" ]; then
  print_help
  exit 0
fi

# Check if cmake is installed
hash cmake 2>/dev/null || { echo >&2 "I require cmake but it's not installed.  Aborting."; exit 1; }

echo "Excecuting: "
if [ $_clean = "yes" ]; then
   echo "cleaning ..."
   rm -rf build
   mkdir build
fi
mkdir build
cd build
cmake ..
make
cd ..
pwd
if [ $_target = "test" ]; then
   pwd
   cd build
   pwd
   cd output
   pwd
   ./native_test --no-exec
   cd ../../
fi
exit 0
