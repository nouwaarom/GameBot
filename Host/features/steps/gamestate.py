from behave import *
from host.board import Board

# Moves available
@given('a forced move is available')
def step_impl(context):
    context.board = Board(10) 
    context.board.setStartBoard()

@given('a legal move is available')
def step_impl(context):
    context.board = Board(10) 
    context.board.setStartBoard()

@given('no forced move is available')
def step_impl(context):
    context.board = Board(10) 
    context.board.setStartBoard()
