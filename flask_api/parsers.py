from flask_restful import reqparse

# Putting data
videos_parser = reqparse.RequestParser()

videos_parser.add_argument("id", type=int, help="Id of the video.")
videos_parser.add_argument("name", type=str, help="Name of the video.", required=True)
videos_parser.add_argument("likes", type=int, help="Likes on the video.", required=True)
videos_parser.add_argument("views", type=int, help="views of the video.", required=True)

videos_update_parser = reqparse.RequestParser()

videos_update_parser.add_argument("id", type=int, help="Id of the video.")
videos_update_parser.add_argument("name", type=str, help="Name of the video.")
videos_update_parser.add_argument("likes", type=int, help="Likes on the video.")
videos_update_parser.add_argument("views", type=int, help="views of the video.")