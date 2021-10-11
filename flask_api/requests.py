from flask_restful import fields, marshal_with, abort, Resource
from flask_api.models import VideoModel
from flask_api.parsers import videos_parser, videos_update_parser 
from flask_api import db, api

resource_field = {
    'id': fields.Integer,
    'name': fields.String,
    'likes': fields.Integer,
    'views': fields.Integer
}

# API methods
class Data(Resource):
    # Get method
    @marshal_with(resource_field)
    def get(self, video_id):
        video = VideoModel.query.filter_by(id=video_id).first()
        if not video:
            abort(404, message="Could not find video with the id...")
        return video, 200

    # Post method
    @marshal_with(resource_field)
    def put(self, video_id):
        args = videos_parser.parse_args()
        video = VideoModel(id=args['id'], name=args['name'], likes=args['likes'], views=args['views'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_field)
    def patch(self, video_id):
        args = videos_update_parser.parse_args()
        video = VideoModel.query.filter_by(id=video_id).first()
        if not video:
            abort(404, "Video does not exist, cannot update...")

        if args['name']:
            video.name = args['name']
        if args['views']:
            video.views = args['views']
        if args['likes']:
            video.likes = args['likes']

        db.session.commit()

        return video
        
    # Delete method
    def delete(self, video_id):
        return 'Deleted...', 409

api.add_resource(Data, '/home/<int:video_id>')

