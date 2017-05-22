from flask_frozen import Freezer
from app import app
freezer = Freezer(app)

@freezer.register_generator
def detail():
	for row in csv_list:
		yield {'number': row['IDPIF']}

if __name__ == '__main__':
     pfreezer.freeze()
							