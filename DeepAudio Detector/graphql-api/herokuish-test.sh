#!/usr/bin/env bash
set -x
# Syntax sugar.
BIN_DIR=$(cd "$(dirname "$0")" || return; pwd) # absolute path

# shellcheck source=bin/utils
source "$BIN_DIR/utils"

# Locale support for Pipenv.
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

DISABLE_COLLECTSTATIC=1 INSTALL_TEST=1 "$(dirname "${0:-}")/compile" "$1" "$2" "$3"

# Location of 'manage.py', if it exists.
MANAGE_FILE=$(find . -maxdepth 3 -type f -name 'manage.py' -printf '%d\t%P\n' | sort -nk1 | cut -f2 | head -1)
MANAGE_FILE=${MANAGE_FILE:-fakepath}

# Ensure that Django is explicitly specified in requirements.txt
#sp-grep -s django && DJANGO_INSTALLED=1
DJANGO_INSTALLED=1


if [ -f "$MANAGE_FILE" ] && [ "$DJANGO_INSTALLED" ]; then
    set +e

    puts-step "$ python $MANAGE_FILE test"

    # Run collectstatic, cleanup some of the noisy output.
    PYTHONPATH=${PYTHONPATH:-.}
    export PYTHONPATH

    # Create a temporary file for collecting the collectstaic logs.
    TEST_LOG=$(mktemp)

    python "$MANAGE_FILE" test 2>&1 | tee "$TEST_LOG"
    TEST_STATUS="${PIPESTATUS[0]}"

    set -e

    # Display a warning if test failed.
    [ "$TEST_STATUS" -ne 0 ] && {
        echo
        echo " !     Error while running '$ python $MANAGE_FILE test'."
        echo "       See traceback above for details."
        echo

	exit 1
    }

    echo

fi
