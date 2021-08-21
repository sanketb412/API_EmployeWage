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
def get_message():
    return jsonify({'Message': 'Welcome to Employee-Wage'})


'''
Defining the data for referance purpose.
Having 3 Employee Data in JSON format.
'''
Emp_details = [
    {
        'ID': 1,
        'Employee_Name': 'Sanket',
        'Employee_ID': 345,
        'Employee_Daily_Wage': 400
    },
    {
        'ID': 2,
        'Employee_Name': 'Nikita',
        'Employee_ID': 322,
        'Employee_Daily_Wage': 500
    },
    {
        'ID': 3,
        'Employee_Name': 'Anusha',
        'Employee_ID': 3452,
        'Employee_Daily_Wage': 600
    }
]

@app.route("/employee", methods=['GET'])
def get():
    """
        Description:
            function get call the data to fet all the entries
        Parameter:
            just to difne the object Employee Parameter is define.
        Return:
            returning the Json object.
    """    
    return jsonify({'Employee':Emp_details})

@app.route("/employee/<int:emp_id>", methods=['GET'])
def get_emp_ID(emp_id):
    """
        Description:
            function get_emp_id call the data by refering ID
        Parameter:
            just to difne the object Emp_ID Parameter is define.
        Return:
            returning the Json object.
    """
    return jsonify({'Emp_Id': Emp_details[emp_id-1]})

if __name__ == '__main__':
    # calling main function to run the app while debug is to be True
    app.run(port=8000, debug=True)