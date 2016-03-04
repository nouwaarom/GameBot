from behave import *

# Player choices
@when('the player doesnt do the forced move')
def step_impl(context):
    return False

@when('the player does a legal move')
def step_impl(context):
    return False

@when('the player does an illegal move')
def step_impl(context):
    return False
