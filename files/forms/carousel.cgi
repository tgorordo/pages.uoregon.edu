#!/usr/bin/env -S uv run python

import cgi, cgitb
import sys, os
import html

cgitb.enable()

form = cgi.FieldStorage()

if 'spreadsheet' in form:
    message = """
    <h1>Matching:</h1>
    <p><a href="../carousel.html">Go Back</a></p>
    """
else:
    message = """
    <h1>Error</h1>
    <p>No file field found in the form.</p>
    <p><a href="../carousel.html">Go Back</a></p>
    """

response = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Carousel - Stable Matching </title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 40px auto;
            padding: 20px;
        }
        h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
   {message}
</body>
<footer>
  <hr>
  <p>Author: <a href="https://pages.uoregon.edu/tgorordo">Thomas (Tom) C. Gorordo</a>
     Source: <a href="https://github.com/tgorordo/pages.uoregon.edu">pages.uoregon.edu/tgorordo</a>,
             <a href="https://github.com/tgorordo/carousel">carousel</a></p>
</footer> 
"""

print(response)