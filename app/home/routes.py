from flask import render_template, request
from app.models.video import Video
from flask import jsonify
from flask import Blueprint

home_bp = Blueprint(
    "home",
    __name__,
)


@home_bp.route("/")
def home():

    videos = (
        Video.query
        .order_by(Video.created_at.desc())
        .all()
    )

    return render_template(
        "home/home.html",
        videos=videos,
    )

@home_bp.route("/search")
def search():

    query = request.args.get("q","")

    if query:

        videos = Video.query.filter(
            Video.title.ilike(f"%{query}%")
        ).all()

    else:

        videos = []

    return render_template(
    "home/home.html",
    videos=videos,
    search_query=query
)

@home_bp.route("/api/search")
def api_search():

    query = request.args.get("q","")


    if len(query) < 2:

        return jsonify([])


    videos = Video.query.filter(
        Video.title.ilike(f"%{query}%")
    ).limit(5).all()


    results=[]


    for video in videos:

        results.append({

            "id":video.id,

            "title":video.title,

            "category":video.category,

            "views":video.views

        })


    return jsonify(results)


@home_bp.route("/api/command-search")
def command_search():

    query=request.args.get("q","")


    videos=[]


    if query:

        videos = Video.query.filter(
            Video.title.ilike(f"%{query}%")
        ).limit(8).all()


    data=[]


    for video in videos:

        data.append({

            "id":video.id,

            "title":video.title,

            "category":video.category,

            "views":video.views,

            "thumbnail":
            video.thumbnail_filename

        })


    return jsonify(data)

