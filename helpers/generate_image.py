'''generate_image.py

This file takes a dictionary of filename and caption values,
combines known paths to generate the html / JS for the image library

Testing:
    Ensure the generated html is correct given an existing image
    Ensure the Thumbnail, image url and ID are correct
    Ensure the Caption is correct
    Test Image creation page passes the right values when generating the page
Possible Enhancements:
    Dictionary is generated from storage content and meta values
'''

# ToDo: Bug: Escape the { in the f string correctly
# To use: add pairs to the dictionary, run in the terminal and copy html
# Format: "caption":"filename"


_images = {"Unknown, Paris 2018": "paris_img_1", "caption2": "filename2"}


def gen_images():

    for caption, filename in _images.items():
        print((f'''<div class="col-md-4">
                        <div class="card mb-4 shadow-sm">
                            <img src="{{ url_for('static', filename='images/thumbnails/t_{filename}.jpg') }}"
                            width="100%" height="100%" />
                            <title>{caption}</title>
                            <div class="card-body">
                                <p class="card-text">{caption}</p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <a href="image/?image={filename}&caption={caption}">
                                        <button type="button" class="btn btn-sm btn-outline-secondary" id="{filename}">
                                        View Full Size</button></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

    '''))


gen_images()
