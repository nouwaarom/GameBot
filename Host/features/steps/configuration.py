import subprocess

from behave import *

@given('I provide no arguments')
def step_impl(context):
    context.command = ["./config", ""]

@when('I run the configuration program')
def step_impl(context):
    context.program = subprocess.Popen(context.command, shell = False)

@then('it should display help')
def step_impl(context):
    (stdout, stderr) = context.program.communicate()

    assert "usage:" in stdout
