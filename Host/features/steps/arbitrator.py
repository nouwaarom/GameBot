from behave import *

# Arbitrator descisions
@then('the arbitrator should refuse the move')
def step_impl(context):
    assert True is False

@then('the arbitrator should allow the move')
def step_impl(context):
    assert True is False
