from webbrowser import open_new
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from logger import *

operation = 0
operands = []

def help_command(update: Update, context: CallbackContext):
    global operation
    operation = 0

    res_str = ""
    res_str +="Calculator Programm\n"
    res_str +="Choose action and input operands\n"
    res_str +="Summation /sum\n"
    res_str +="Subtraction /sub\n"
    res_str +="Miltiplication /mul\n"
    res_str +="Divisin /div\n"
    res_str +="Complex number need to input by space"
    update.message.reply_text(res_str)

def sum_command(update: Update, context: CallbackContext):
    global operation
    operation = 1

def sub_command(update: Update, context: CallbackContext):
    global operation
    operation = 2

def mul_command(update: Update, context: CallbackContext):
    global operation
    operation = 3

def div_command(update: Update, context: CallbackContext):
    global operation
    operation = 4 

def analize_command(update: Update, context: CallbackContext):
    global operation, operands
    res_str = ""

    if operation:
        if len(operands)<2:
            msg = update.message.text

            if " " in msg and msg.split(" ")[0].isdigit() and msg.split(" ")[1].isdigit():
                operands.append(complex(float(msg.split(" ")[0]), float(msg.split(" ")[1])))
                update.message.reply_text(f"Complex number {operands[-1]}")
            elif msg.isdigit():
                operands.append(float(msg))
            else:
                update.message.reply_text("Inserted data not a digit. Repeat input")
        if len(operands) == 2:
            match operation:
                case 1:
                    res_str = f"{operands[0]} + {operands[1]} = {operands[0]+operands[1]}"
                case 2:
                    res_str = f"{operands[0]} - {operands[1]} = {operands[0]-operands[1]}"
                case 3:
                    res_str = f"{operands[0]} * {operands[1]} = {operands[0]*operands[1]}"
                case 4:
                    res_str = f"{operands[0]} / {operands[1]} = {operands[0]/operands[1]}"
            log(update,context,res_str)
            res_str += "\n\n Do you want another calculation? \help"
            update.message.reply_text(res_str)
            operands = []
            operation = 0