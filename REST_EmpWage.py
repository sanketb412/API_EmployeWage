# ''""
# @Author: Sanket Bagde
# @Date: 2021-19-08
# @Last Modified by:
# @Last Modified time:
# @Title :Write a program of EmployeeWagee using and get the Employee Details REST API.
# '''

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/",methods=['GET'])
def get_emp_ID():
    return jsonify({'Message': 'Welcome to Employee-Wage'})

if __name__ == '__main__':
    # calling main function to run the app while debug is to be True
    app.run(port=8000, debug=True)