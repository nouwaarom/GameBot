from behave import *

# Moves available
@given('a forced move is available')
def step_impl(context):
    context.board =  "FIXME"

@given('a legal move is available')
def step_impl(context):
    return False

@given('no forced move is available')
def step_impl(context):
    return False
