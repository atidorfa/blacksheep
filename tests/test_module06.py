# module 6: cmd line options

# help of the list of commands:
#   pytest --help


# test filtering run tests by test-name:
#   pytest -v -k "module" --tb=no
#   pytest -v -k "case" --tb=no
#   pytest -v -k "case or str" --tb=no
#   pytest -v -k "module and not case" --tb=no


# -x flag stop after first failed test:
#   pytest -v -k "module and not case" --tb=no -x
#   pytest -v --maxfail=2 --tb=no


# -q flag is quiet execution:
#   pytest -v --maxfail=2 --tb=no


# --collect-only do not run test instead show the group of tests:
#   pytest -v -k "module" --tb=no --collect-only


# --lf run only the last:
#   pytest -v -k "module" --tb=no --lf


# --ff run the failed tests first and after all the others
#   pytest -v -k "module" --tb=no --ff
