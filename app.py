
from flask import Flask, render_template, request, jsonify
from database import db
from bson import json_util
import json

app = Flask(__name__)

# Supported collections
ALLOWED_COLLECTIONS = {
    "users",
    "students",
    "address"
}

# Supported aggregation stages
ALLOWED_STAGES = {
    "$match",
    "$group",
    "$unwind",
    "$project",
    "$sort",
    "$limit",
    "$sample",
    "$lookup"
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/collections", methods=["GET"])
def get_collections():

    return jsonify({
        "collections": sorted(ALLOWED_COLLECTIONS)
    })


@app.route("/execute", methods=["POST"])
def execute_pipeline():

    try:
        data = request.get_json(silent=True) or {}

        collection_name = data.get("collection")
        pipeline = data.get("pipeline")

        if collection_name not in ALLOWED_COLLECTIONS:
            return jsonify({
                "error": "Invalid collection selected."
            }), 400

        if not isinstance(pipeline, list) or not pipeline:
            return jsonify({
                "error": "Please provide at least one pipeline stage."
            }), 400

        if len(pipeline) > 10:
            return jsonify({
                "error": "Maximum 10 stages are allowed."
            }), 400

        for stage in pipeline:

            if not isinstance(stage, dict) or len(stage) != 1:
                return jsonify({
                    "error": "Each stage must contain exactly one operator."
                }), 400

            operator = next(iter(stage))

            if operator not in ALLOWED_STAGES:
                return jsonify({
                    "error": f"Unsupported stage: {operator}"
                }), 400

        collection = db[collection_name]

        result = list(
            collection.aggregate(
                pipeline,
                maxTimeMS=10000
            )
        )

        return app.response_class(
            response=json_util.dumps({
                "success": True,
                "collection": collection_name,
                "pipeline": pipeline,
                "result_count": len(result),
                "results": result
            }),
            mimetype="application/json"
        )

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)
