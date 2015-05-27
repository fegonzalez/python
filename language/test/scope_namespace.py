
# ==============================================================================
# scope & namespace test
# ==============================================================================

# bash-3.2$ python3 -m scope_namespace

# EXPECTED RESULT

# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam


# ==============================================================================


def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


# ------------------------------------------------------------------------------


scope_test()

print("In global scope:", spam) # spam defined inside do_global()


# ------------------------------------------------------------------------------
