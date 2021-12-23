try:
    from PIL import Image
except ImportError:
    import Image
    
image = Image.open('../Apple/Data/img/apple1.png')