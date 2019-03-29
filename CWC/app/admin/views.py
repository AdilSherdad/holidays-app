from flask import flash, redirect, render_template, url_for
# from flask_login import login_required

from . import admin
from .forms import HolidayForm

#base_url = 'http://localhost:8080'

@admin.route('/')
def dashboard():
    """
    Render the dashboard template on the / route
    """
    # holidays = requests.get(url).json()
    holidays = [{'id' : 1, 'name': 'Quaid-e-azam', 'description': 'Founder of Pakistan', 'date': '2019-2-11'},{'id' : 2, 'name': 'Eid-Ul-Azha', 'description': 'Muslim Celebration', 'date': '2019-6-07'},{'id' : 3, 'name': 'Kashmir Day', 'description': 'Solidarity with people of Kashmir', 'date': '2019-5-01'}]
    return render_template('admin/dashboard.html', holidays = holidays, title="Dashboard")

@admin.route('/add')
def add_holiday():
    """
    Add a department to the database
    """

    add_holiday = True

    form = HolidayForm()
    if form.validate_on_submit():
        # department = Department(name=form.name.data,
        #                         description=form.description.data)

        holiday = {'name': form.name.data, 'description': form.description.data}

        try:
            # add holiday to the database
            # db.session.add(department)
            # db.session.commit()
            # requests.post(url, data = holiday)
            flash('You have successfully added a new department.')
        except:
            # in case holiday name already exists
            flash('Error: holiday name already exists.')

        # redirect to holidays page
        return redirect(url_for('admin.dashboard'))

    # load holiday template
    return render_template('admin/holiday.html', action="Add",
                           add_holiday=add_holiday, form=form,
                           title="Add Holiday")

@admin.route('/edit/<int:id>', methods=['GET', 'POST'])
#@login_required
def edit_holiday(id):
    """
    Edit a holiday
    """

    add_holiday = False

    # Get holiday from database based on id
    # holiday = Department.query.get_or_404(id)
    # holiday = requests.get(url)
    holiday = {'id' : 1, 'name': 'Husnain', 'description': 'something', 'date': '2019-2-11'}
    form = HolidayForm(obj=holiday)
    if form.validate_on_submit():
        holiday.name = form.name.data
        holiday.description = form.description.data
        # db.session.commit()
        # Store the holiday in database
        # requests.put(url, data = holiday)
        flash('You have successfully edited the holiday.')

        # redirect to the departments page
        return redirect(url_for('admin.dashboard'))

    # form.description.data = holiday.description
    # form.name.data = holiday.name
    form.description.data = holiday['description']
    form.name.data = holiday['name']
    return render_template('admin/holiday.html', action="Edit",
                           add_holiday=add_holiday, form=form,
                           holiday=holiday, title="Edit Holiday")

@admin.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_holiday(id):
    """
    Delete a holiday from the database
    """

    # Delete holiday from database based on id
    # resp = requests.delete(url/id)

    flash('You have successfully deleted the department.')

    # redirect to the departments page
    return redirect(url_for('admin.dashboard'))
