import subprocess

from behave import *

@given('I add the help flag')
def step_impl(context):
    context.command = ["../host.py", "--help"]

@when('I run the host')
def step_impl(context):
    context.program_result = subprocess.run(context.command, shell = False, capture_output=True, text=True)

@then('it should display help')
def step_impl(context):
    assert "usage:" in context.program_result.stdout
