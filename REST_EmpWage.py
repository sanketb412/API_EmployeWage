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

@app.route("/employee/<string:name>", methods=['POST'])
def create_employee_details(name):
    """
        Description:
            function create_employee_details creates one new entry of employee in an object
        Parameter:
            request is call to get the json data. new_item to ge the employee details and them append into into Emp_details
        Return:
            returning the Json object.
    """
    for emp_details in Emp_details:
        if(emp_details['Employee_Name'] != name):
            req_data = request.get_json()
            new_item = {
                'ID':req_data['ID'],
                'Employee_Name':req_data['Employee_Name'],
                'Employee_ID': req_data['Employee_ID'],
                'Employee_Daily_Wage': req_data['Employee_Daily_Wage']
            }
            Emp_details.append(new_item)
            return jsonify(new_item)
        return jsonify({'messgae': "Employee Already exists "})

@app.route("/employee/<int:emp_id>", methods = ['PUT'])
def update_employee_details(emp_id):
    for emp_update in Emp_details:
        if(emp_update['ID'] == emp_id):
            req_data = request.get_json()
            emp_update['Employee_Name'] = req_data['Employee_Name']
            return jsonify(emp_update)
    return jsonify({'messgae': "Employee didnt find"})

@app.route("/employee/<int:id>", methods=['DELETE'])
def delete_employee(id):
    """
        Description:
            function delete_employee is define as to delete the entries from the json list
        Parameter:
            parameter ID is define to get the entries from user and .remove function is used
        Return:
            returning the Json object.
    """
    try:
        Emp_details.remove(Emp_details[id-1])
        return jsonify({'result': True})
    except:
        return jsonify({'messgae': "Employee didnt find"})

if __name__ == '__main__':
    # calling main function to run the app while debug is to be True
    app.run(port=8000, debug=True)