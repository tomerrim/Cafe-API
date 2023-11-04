from flask import Flask, jsonify, render_template, request
from database import db, Cafe

app = Flask(__name__)

