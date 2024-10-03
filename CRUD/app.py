from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample in-memory database using a list of dictionaries
students = [
    {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
    {'id': 2, 'name': 'Jane Doe', 'email': 'jane@example.com'}
]

# Helper function to find student by ID
def get_student_by_id(student_id):
    return next((student for student in students if student['id'] == student_id), None)

# Home page (Read/Display)
@app.route('/')
def index():
    return render_template('index.html', students=students)

# Create new student (Create)
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        new_id = len(students) + 1
        name = request.form['name']
        email = request.form['email']
        students.append({'id': new_id, 'name': name, 'email': email})
        return redirect(url_for('index'))
    return render_template('create.html')

# Update student (Update)
@app.route('/update/<int:student_id>', methods=['GET', 'POST'])
def update(student_id):
    student = get_student_by_id(student_id)
    if not student:
        return 'Student not found!', 404

    if request.method == 'POST':
        student['name'] = request.form['name']
        student['email'] = request.form['email']
        return redirect(url_for('index'))

    return render_template('update.html', student=student)

# Delete student (Delete)
@app.route('/delete/<int:student_id>', methods=['GET', 'POST'])
def delete(student_id):
    student = get_student_by_id(student_id)
    if not student:
        return 'Student not found!', 404

    if request.method == 'POST':
        students.remove(student)
        return redirect(url_for('index'))

    return render_template('delete.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
