from flask import render_template as render, flash, url_for, redirect
from flask_login import login_required, current_user
from .form import UpdateImageProfileForm
from app.services import update_profile_picture
from werkzeug.utils import secure_filename
from app.utils import random_name
from . import users

@users.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    username = current_user.id
    profile_form = UpdateImageProfileForm()
    context = {
        'username': username,
        'profile_form': profile_form
    }

    if profile_form.validate_on_submit():
        ext = profile_form.upload.data.filename.split(".")[-1]

        filename = secure_filename(
            random_name(username) + "." + ext
        )
        profile_form.upload.data.save("app/uploads/profile_pictures/" + filename)
        update_profile_picture(username, filename)
        flash("Foto de perfil cargada exitosamente !!", category="success")

        return redirect(url_for("users.profile"))

    return render('users/profile.html', **context) 