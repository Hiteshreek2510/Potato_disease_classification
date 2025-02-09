from django.shortcuts import render
from .form import Imageform
from .models import Image
from django import forms
import numpy as np
from io import BytesIO
from PIL import Image as PILImage
import tensorflow as tf

# Create your views here.
MODEL=tf.keras.models.load_model("C:/Users/Hiteshree/models/2.h5")
class_names=["Early_blight",'Late_blight',"Healthy"]
def index(request):
    if request.method=='POST':
        form=Imageform(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            image_1 = read_file_as_img(obj.image)  # Make sure to read the image file correctly
            image_batch = np.expand_dims(image_1, 0)
            prediction = MODEL.predict(image_batch)
            predicted_class_idx = np.argmax(prediction, axis=-1)[0]
            predicted_class = class_names[predicted_class_idx]
            confidence = float(np.max(prediction))
            return render(request,'index.html',{'obj':obj,'predicted_class':predicted_class,'confidence':confidence})
    else:
        form=Imageform()
    img=Image.objects.all()

# Pass the predictions to the template
    return render(request, 'index.html', {'img': img, 'form': form})
def read_file_as_img(data)->np.ndarray:
    image_file = data.file  # Use the `file` attribute of the `ImageField`
    
    # Read the file content as bytes
    image_bytes = image_file.read()
    image_1=np.array(PILImage.open(BytesIO(image_bytes)))
    return image_1