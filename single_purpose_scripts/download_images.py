import requests
from PIL import Image
from io import BytesIO


def download(url, fname):
    '''
    Download images from the web given its URL and
    the name to use for the file. The extension for
    the saved image will be the same as the original.

    
    Parameters
    ----------
    url : str
        The URL for the image to download.
    fname : str
        The name to use for the saved image.

    Returns
    -------
    None
    '''
    
    # Make a GET request for the image's URL
    img_request = requests.get(url)
    # Get the file extension of the image to be downloaded
    img_ext = url.split('.')[-1]
    # Create an image from the binary data returned by the request
    img = Image.open(BytesIO(img_request.content))
    # Now save the image
    img.save(f'{fname}.{img_ext}')
    
    return None


if __name__ == "__main__":
    ask_url = True

    while ask_url:
        ask_url = input('URL of the desired image: ')
        ask_fname = input('Name to use for downloaded image (without extension): ')

        try:
            download(ask_url, ask_fname)
            print('Image downloaded with success.')
        except:
            print('Unable to download the requested image.')

        print()

    else:
        print('The script has been terminated.')