from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request,
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user,
)

from app.auth.forms import RegisterForm, LoginForm
from app.auth.service import AuthService

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    # Redirect authenticated users
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard"))

    form = RegisterForm()

    if form.validate_on_submit():

        # Username already exists
        if AuthService.username_exists(form.username.data):
            flash("Username already exists.", "danger")
            return render_template("auth/register.html", form=form)

        # Email already exists
        if AuthService.email_exists(form.email.data):
            flash("Email is already registered.", "danger")
            return render_template("auth/register.html", form=form)

        # Create user
        AuthService.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        flash("Account created successfully! Please login.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # Redirect authenticated users
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard"))

    form = LoginForm()

    if form.validate_on_submit():

        user = AuthService.authenticate(
            email=form.email.data,
            password=form.password.data,
        )

        if user is None:
            flash("Invalid email or password.", "danger")
            return render_template("auth/login.html", form=form)

        # Login user
        login_user(
            user,
            remember=form.remember.data,
        )

        flash(f"Welcome back, {user.username}!", "success")

        # Redirect to the page the user originally requested
        next_page = request.args.get("next")

        return redirect(next_page or url_for("dashboard.dashboard"))

    return render_template("auth/login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()

    flash("You have been logged out successfully.", "info")

    return redirect(url_for("auth.login"))